import tkinter as tk
from typing import *

from modules import BackButton
from modules import MMULeft
from modules import TextEntry
from modules import WhiteButton
from modules import ScrollableFrame


class CreateStudent(ScrollableFrame):

    """
    A page for creating a student.

    Args:
        root (tk.Tk): The root window.
    """

    def __init__(self, root):
        super().__init__(root, height=800)

        self._mmu_left = MMULeft(self.interior)
        self._mmu_left.pack()  # Placing the MMULeft logo first

        self._back_button = BackButton(self.interior, None)
        self._back_button.pack()  # Placing the BackButton on top of MMULeft
        self._back_button.place(x=48, y=40)

        self._student_name_entry = TextEntry(self.interior, "Student Name", width=38)
        self._student_id_entry = TextEntry(
            self.interior, "Student ID", regen_student_id=False, copy=True, width=38
        )
        self._student_password_entry = TextEntry(
            self.interior, "Student Password", regen_password=True, copy=True, width=38
        )
        self._current_semester_entry = TextEntry(
            self.interior, "Current Semester", width=38
        )
        self._current_program_entry = TextEntry(
            self.interior, "Current Program", width=38
        )
        self._create_button = WhiteButton(
            self.interior,
            "Create Student",
            self._create_student_handler,
            width=14,
            height=2,
        )

        self._student_name_entry.pack()
        self._student_name_entry.place(x=48, y=160)
        self._student_id_entry.pack()
        self._student_id_entry.place(x=48, y=240)
        self._student_password_entry.pack()
        self._student_password_entry.place(x=48, y=330)
        self._current_semester_entry.pack()
        self._current_semester_entry.place(x=48, y=450)
        self._current_program_entry.pack()
        self._current_program_entry.place(x=48, y=530)
        self._create_button.pack()
        self._create_button.place(x=48, y=610)

    def _create_student_handler(self):
        student_name = self._student_name_entry.get()
        student_id = self._student_id_entry.get()
        student_password = self._student_password_entry.get()
        current_semester = self._current_semester_entry.get()
        current_program = self._current_program_entry.get()

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


# TEST CODE
if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    root.title("Create Student")
    create_student_page = CreateStudent(root)
    root.mainloop()
