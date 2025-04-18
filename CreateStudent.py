import tkinter as tk
from typing import *
from modules import BackButton
from modules import MMULeft
from modules import TextEntry
from modules import WhiteButton


class CreateStudent:

    """
    A page for creating a student.

    Args:
        root (tk.Tk): The root window.
    """

    def __init__(self, root):
        self.root = root

        self.root.geometry("800x617")  # Set window dimensions

        self._mmu_left = MMULeft(self.root)
        self._mmu_left.pack()  # Placing the MMULeft logo first

        self._back_button = BackButton(self.root, None)
        self._back_button.pack()  # Placing the BackButton on top of MMULeft
        self._back_button.place(x=48, y=40)

        self._student_name_entry = TextEntry(self.root, "Student Name", width=38)
        self._student_id_entry = TextEntry(self.root, "Student ID", copy=True, width=38)
        self._student_password_entry = TextEntry(
            self.root, "Student Password", copy=True, width=38, regen_password=True
        )
        self._current_semester_entry = TextEntry(
            self.root, "Current Semester", width=38
        )
        self._current_program_entry = TextEntry(self.root, "Current Program", width=38)
        self._create_button = WhiteButton(
            self.root, "Create Student", self._create_student_handler, width=13
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
        student_name = self._student_name_entry.get_text()
        student_id = self._student_id_entry.get_text()
        student_password = self._student_password_entry.get_password()
        current_semester = self._current_semester_entry.get_text()
        current_program = self._current_program_entry.get_text()

        # Here, you would perform the actual student creation logic
        # For now, let's just print the student details
        print(
            f"Creating student:\n"
            f"Name: {student_name}\n"
            f"ID: {student_id}\n"
            f"Password: {student_password}\n"
            f"Semester: {current_semester}\n"
            f"Program: {current_program}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Create Student")
    create_student_page = CreateStudent(root)
    root.mainloop()
