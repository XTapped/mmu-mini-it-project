import tkinter as tk
import sqlite3
import hashlib
from tkinter.messagebox import showerror
from contextlib import closing

from pages import SplashScreen
from pages import StudentMenu
from pages import TimetableMenu
from pages import CourseMenu
from pages import AdminMenu
from pages import StudentAction
from pages import CourseAction
from pages import CreateStudent

# Database Schema:
# CREATE TABLE IF NOT EXISTS Passwords (
#         id INTEGER PRIMARY KEY,
#         salt TEXT,
#         hash TEXT
#     )

# CREATE TABLE IF NOT EXISTS Students (
#         id TEXT PRIMARY KEY,
#         name TEXT,
#         current_semester INTEGER,
#         password_id INTEGER,
#         course_name TEXT,
#         FOREIGN KEY(password_id) REFERENCES Passwords(id),
#         FOREIGN KEY(course_name) REFERENCES Courses(name)
#     )

# CREATE TABLE IF NOT EXISTS Courses (
#         name TEXT PRIMARY KEY,
#         total_semesters INTEGER
#     )

# CREATE TABLE IF NOT EXISTS Classes (
#         code TEXT PRIMARY KEY,
#         name TEXT,
#         description TEXT,
#         course_name TEXT,
#         FOREIGN KEY(course_name) REFERENCES Courses(name)
#     )

# CREATE TABLE IF NOT EXISTS ClassRating (
#             class_code TEXT,
#             student_id INTEGER,
#             liked INTEGER,
#             PRIMARY KEY(class_code, student_id),
#             FOREIGN KEY(class_code) REFERENCES Classes(code),
#             FOREIGN KEY(student_id) REFERENCES Students(id)
#             )

# CREATE TABLE IF NOT EXISTS Sections (
#         id INTEGER PRIMARY KEY,
#         class_code TEXT,
#         capacity INTEGER,
#         lecture_day TEXT,
#         tutorial_day TEXT,
#         lecture_start_time INTEGER,
#         lecture_end_time INTEGER,
#         tutorial_start_time INTEGER,
#         tutorial_end_time INTEGER,
#         lecture_venue TEXT,
#         tutorial_venue TEXT,
#         FOREIGN KEY(class_code) REFERENCES Classes(code)
#     )

# CREATE TABLE IF NOT EXISTS SectionEnrollment (
#         student_id INTEGER,
#         section_id INTEGER,
#         semester INTEGER,
#         failed INTEGER,
#         PRIMARY KEY(student_id, section_id, semester),
#         FOREIGN KEY(student_id) REFERENCES Students(id),
#         FOREIGN KEY(section_id) REFERENCES Sections(id)
#     )

root = tk.Tk()
root.geometry("800x500")
root.resizable(False, False)


def switch_frames(frame1, frame2):
    # Unpack the first frame
    frame1.pack_forget()
    # Pack the second frame
    frame2.pack()


def execute_query(query, params=()):
    # Connect to the database
    with closing(sqlite3.connect("database.db")) as db:
        with db:
            # Execute the query and fetch the result
            result = db.execute(query, params).fetchall()
    # Return the result
    return result


def main(student_id, password):
    if student_id == "admin" and password == "admin":
        admin_menu = AdminMenu(
            root,
            splash_screen,
            lambda: switch_frames(
                admin_menu,
                StudentAction(root, admin_menu),
            ),
            lambda: switch_frames(admin_menu, CourseAction(root, admin_menu)),
        )
        switch_frames(splash_screen, admin_menu)
    else:
        student = execute_query("SELECT * FROM Students WHERE id=?", (student_id,))
        if student == []:
            showerror(
                "Invalid Student ID/Password",
                "The student ID/password you entered is invalid.",
            )
            return
        else:
            student = student[0]
            student_password = execute_query(
                "SELECT * FROM Passwords WHERE id=?", (student[3],)
            )[0]

            student_salt = student_password[1]
            student_hash = student_password[2]
            hash = hashlib.scrypt(
                password.encode("utf-8"), salt=student_salt, n=2**10, r=8, p=1
            )
            if hash == student_hash:
                student_menu = StudentMenu(
                    root,
                    student[1],
                    splash_screen,
                    lambda: switch_frames(
                        student_menu,
                        CourseMenu(root, student_menu, student[4], student),
                    ),
                    lambda: switch_frames(
                        student_menu,
                        TimetableMenu(root, student_menu, student[0], student[2]),
                    ),
                )
                switch_frames(splash_screen, student_menu)
            else:
                showerror(
                    "Invalid Student ID/Password",
                    "The student ID/password you entered is invalid.",
                )


splash_screen = SplashScreen(
    root,
    lambda: main(splash_screen.get()["student_id"], splash_screen.get()["password"]),
)
splash_screen.pack()


root.mainloop()
