from contextlib import closing
import random
import sqlite3
import hashlib
import os

# Database Schema:
# Password
# 	- id (PK) 				[int]
# 	- salt 					[str]
# 	- hash 					[str]

# Student
# 	- id (PK)				[int]
# 	- name 					[str]
# 	- current_semester 		[int]
# 	- password_id (FK) 		[int]
# 	- course_name (FK) 		[str]

# Course
# 	- name (PK) 			[str]
# 	- total_semesters 		[int]

# Class
# 	- code (PK) 			[str]
# 	- name 					[str]
# 	- description 			[str]
# 	- course_name (FK) 		[str]

# ClassRating
# 	- class_code (FK)		[str]
# 	- student_id (FK)		[int]
#   - liked                 [bool]

# Section
# 	- id (PK) 				[int]
# 	- class_code (FK) 		[str]
# 	- capacity 				[int]
# 	- lecture_day 			[str]
# 	- lecture_start_time 	[int]
# 	- lecture_end_time 		[int]
# 	- tutorial_start_time 	[int]
# 	- tutorial_end_time 	[int]

# SectionEnrollment
# 	- student_id (FK) (CK) 	[int]
# 	- section_id (FK) (CK) 	[int]
# 	- semester (CK) 		[int]
# 	- failed 				[bool]


def init_database():
    # Initialize database
    db = sqlite3.connect("database.db")
    c = db.cursor()

    # Create tables
    c.execute(
        """CREATE TABLE IF NOT EXISTS Passwords (
        id INTEGER PRIMARY KEY,
        salt TEXT,
        hash TEXT
    )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS Students (
        id TEXT PRIMARY KEY,
        name TEXT,
        current_semester INTEGER,
        password_id INTEGER,
        course_name TEXT,
        FOREIGN KEY(password_id) REFERENCES Passwords(id),
        FOREIGN KEY(course_name) REFERENCES Courses(name)
    )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS Courses (
        name TEXT PRIMARY KEY,
        total_semesters INTEGER
    )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS Classes (
        code TEXT PRIMARY KEY,
        name TEXT,
        description TEXT,
        course_name TEXT,
        FOREIGN KEY(course_name) REFERENCES Courses(name)
    )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS ClassRating (
            class_code TEXT,
            student_id INTEGER,
            liked INTEGER,
            PRIMARY KEY(class_code, student_id),
            FOREIGN KEY(class_code) REFERENCES Classes(code),
            FOREIGN KEY(student_id) REFERENCES Students(id)
            )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS Sections (
        id INTEGER PRIMARY KEY,
        class_code TEXT,
        capacity INTEGER,
        lecture_day TEXT,
        tutorial_day TEXT,
        lecture_start_time INTEGER,
        lecture_end_time INTEGER,
        tutorial_start_time INTEGER,
        tutorial_end_time INTEGER,
        FOREIGN KEY(class_code) REFERENCES Classes(code)
    )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS SectionEnrollment (
        student_id INTEGER,
        section_id INTEGER,
        semester INTEGER,
        failed INTEGER,
        PRIMARY KEY(student_id, section_id, semester),
        FOREIGN KEY(student_id) REFERENCES Students(id),
        FOREIGN KEY(section_id) REFERENCES Sections(id)
    )"""
    )

    # Commit changes
    db.commit()
    db.close()


def insert_dummy_data():
    db = sqlite3.connect("database.db")
    c = db.cursor()

    c.execute(
        """INSERT INTO Passwords (salt, hash)
        VALUES ("$2y$04$wl9o72cPZHUmx3ufeFq6GuSV2nwXl7xyXFjKOzTl2oQEoKcGnA7Da", "$2y$10$Ud7ctKIRyp.e2AvB3jXqZuZdekxlDk/aBwJW40Eztbcky6SG.P.LC")"""
    )

    c.execute(
        """INSERT INTO Courses (name, total_semesters)
        VALUES ("Foundation in Information Technology", 3)"""
    )

    c.execute(
        """INSERT INTO Classes (code, name, description, course_name)
        VALUES ("PEN0065", "Academic English", "This course aims to develop students’ academic English language skills in reading, writing, listening and speaking. It also aims to develop students’ critical thinking skills and their ability to use English for academic purposes.", "Foundation in Information Technology")"""
    )

    c.execute(
        """INSERT INTO Students (name, current_semester, password_id, course_name)
        VALUES ("Harris Majeed", 3, 1, "Foundation in Information Technology")"""
    )

    c.execute(
        """INSERT INTO Sections (class_code, capacity, lecture_day, tutorial_day, lecture_start_time, lecture_end_time, tutorial_start_time, tutorial_end_time)
        VALUES ("PEN0065", 120, "Monday", "Wednesday", 8, 10, 10, 12)"""
    )

    db.commit()
    db.close()


def delete_passwords():
    db = sqlite3.connect("database.db")
    c = db.cursor()

    c.execute("""DELETE FROM Passwords""")

    db.commit()
    db.close()


# Generate one entry in Passwords using hashlib.scrypt
# def generate_password(password):
#     db = sqlite3.connect("database.db")
#     c = db.cursor()

#     salt = hashlib.sha256(os.urandom(10)).hexdigest().encode("ascii")
#     hash = hashlib.scrypt(password.encode("utf-8"), salt=salt, n=2**10, r=8, p=1)

#     c.execute(
#         """INSERT INTO Passwords (salt, hash)
#         VALUES (?, ?)""",
#         (salt, hash),
#     )

#     db.commit()
#     db.close()


# generate_password("123")

# generate a random 10 digit number
num = random.randint(1000000000, 9999999999)

with closing(sqlite3.connect("database.db")) as db:
    with db:
        student = db.execute("SELECT * FROM STUDENTS").fetchone()

print(student)
