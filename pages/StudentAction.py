import tkinter as tk
from typing import *
from modules import MMULeft
from modules import BackButton
from modules import Heading
from modules import WhiteButton
from modules import switch_frames

from pages import CreateStudent
from pages.UpdateStudent import UpdateStudent


class StudentAction(tk.Frame):
    def __init__(self, root: tk.Tk, back_frame):
        super().__init__(root, width=800, height=500)
        self.pack_propagate(0)
        root.title("Student Action")
        root.geometry("800x500")
        root.resizable(False, False)

        back_button = BackButton(self, back_frame, current_frame=self)
        back_button.pack()
        back_button.place(x=48, y=40)

        MMULeft(self).pack()

        heading3 = Heading(self, "Student Action", 3)
        heading3.pack()
        heading3.place(x=48, y=149)

        create_course = WhiteButton(
            self,
            "Create Student",
            lambda: switch_frames(self, CreateStudent(root, self)),
            19,
            "2",
            "w",
        )
        create_course.place(x=48, y=200)

        Update_Delete_course = WhiteButton(
            self,
            "Update/Delete Student",
            lambda: switch_frames(self, UpdateStudent(root, self)),
            19,
            "2",
            "w",
        )
        Update_Delete_course.pack()
        Update_Delete_course.place(x=48, y=260)


# TEST CODE
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Student Test")
    root.resizable(False, False)

    frame = tk.Frame(root)
    frame.pack()

    course_action = StudentAction(root, None)
    course_action.pack()

    root.mainloop()
