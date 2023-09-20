import tkinter as tk
from typing import *
from modules import switch_frames
from modules import MMULeft
from modules import BackButton
from modules import Heading
from modules import WhiteButton

from pages.CreateCourse import CreateCourse


class CourseAction(tk.Frame):
    def __init__(self, root: tk.Tk, back_frame):
        super().__init__(root, width=800, height=500)
        self.pack_propagate(0)
        root.title("Course Action")
        root.geometry("800x500")
        root.resizable(False, False)

        self.create_course = CreateCourse(root, self)

        back_button = BackButton(self, back_frame, current_frame=self)
        back_button.pack()
        back_button.place(x=48, y=40)

        MMULeft(self).pack()

        heading3 = Heading(self, "Course Actions", 3)
        heading3.pack()
        heading3.place(x=48, y=149)

        create_course = WhiteButton(
            self,
            "Create Course",
            lambda: switch_frames(self, self.create_course),
            19,
            "2",
            "w",
        )
        create_course.pack(anchor="w")
        create_course.place(x=48, y=200)

        Update_Delete_course = WhiteButton(
            self, "Update/Delete Course", None, 19, "2", "w"
        )
        Update_Delete_course.pack()
        Update_Delete_course.place(x=48, y=260)


# TEST CODE
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    root.title("CourseAction Test")
    root.resizable(False, False)

    frame = tk.Frame(root)
    frame.pack()

    course_action = CourseAction(root)
    course_action.pack()

    root.mainloop()
