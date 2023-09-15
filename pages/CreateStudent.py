import tkinter as tk
import os
import hashlib
from typing import *
from modules import BackButton
from modules import MMULeft
from modules import TextEntry
from modules import WhiteButton
from modules import ScrollableFrame
from modules import DropDown
from modules import execute_query


class CreateStudent(ScrollableFrame):

    """
    A page for creating a student.

    Args:
        root (tk.Tk): The root window.
    """

    def __init__(self, root, back_frame):
        super().__init__(root, height=700)

        self._mmu_left = MMULeft(self.interior)
        self._mmu_left.pack()  # Placing the MMULeft logo first

        self._back_button = BackButton(self.interior, back_frame, current_frame=self)
        self._back_button.pack()  # Placing the BackButton on top of MMULeft
        self._back_button.place(x=48, y=40)

        self._student_name_entry = TextEntry(self.interior, "Student Name", width=38)
        self._student_id_entry = TextEntry(
            self.interior, "Student ID", copy=True, width=38
        )
        self._student_password_entry = TextEntry(
            self.interior, "Student Password", copy=True, width=38, regen_password=True
        )
        # self._current_semester_entry = TextEntry(
        #     self.interior, "Current Semester", width=38
        # )
        self._current_semester_entry = DropDown(
            self.interior, [1], True, "Current Semester", 37
        )

        # self._current_program_entry = TextEntry(
        #     self.interior, "Current Program", width=38
        # )

        course_name_and_sem = execute_query("SELECT * FROM Courses")
        course_names = [x[0] for x in course_name_and_sem]

        self._current_program_entry = DropDown(
            self.interior, course_names, True, "Current Program", 37
        )

        def change_semester_dropdown(event):
            selected_index = self._current_program_entry.get()[1]
            max_sems = course_name_and_sem[selected_index][1]
            sem_list = [x for x in range(1, max_sems + 1)]
            self._current_semester_entry._combobox["values"] = sem_list

        self._current_program_entry.bind("<FocusIn>", change_semester_dropdown)

        self._create_button = WhiteButton(
            self.interior, "Create Student", self._create_student_handler, width=13
        )

        self._student_name_entry.pack()
        self._student_name_entry.place(x=48, y=160)
        self._student_id_entry.pack()
        self._student_id_entry.place(x=48, y=230)
        self._student_password_entry.pack()
        self._student_password_entry.place(x=48, y=320)
        self._current_semester_entry.pack()
        self._current_semester_entry.place(x=48, y=440)
        self._current_program_entry.pack()
        self._current_program_entry.place(x=48, y=520)
        self._create_button.pack()
        self._create_button.place(x=48, y=615)

    def _create_student_handler(self):
        student_name = self._student_name_entry.get()
        student_id = self._student_id_entry.get()
        student_password = self._student_password_entry.get()
        current_semester = self._current_semester_entry.get()[0]
        current_program = self._current_program_entry.get()[0]

        # Generate a salt and hash the password for storage
        salt = hashlib.sha256(os.urandom(10)).hexdigest().encode("ascii")
        hashed_password = hashlib.scrypt(
            student_password.encode("utf-8"), salt=salt, n=2**10, r=8, p=1
        )

        # Insert the hashed password into the Passwords table
        password_id = execute_query(
            "INSERT INTO Passwords (salt, hash) VALUES (?, ?)",
            (salt, hashed_password),
            insert=True,
        )[1]

        # Insert the student into the Students table
        execute_query(
            "INSERT INTO Students (id, name, current_semester, password_id, course_name) VALUES (?, ?, ?, ?, ?)",
            (student_id, student_name, current_semester, password_id, current_program),
        )

        self._back_button._back()

        # print(
        #     f"Creating student:\n"
        #     f"Name: {student_name}\n"
        #     f"ID: {student_id}\n"
        #     f"Password: {student_password}\n"
        #     f"Semester: {current_semester}\n"
        #     f"Program: {current_program}"
        # )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Create Student")
    create_student_page = CreateStudent(root, None).pack()
    root.mainloop()
