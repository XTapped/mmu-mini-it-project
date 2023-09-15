import tkinter as tk
from typing import *
from modules import BackButton
from modules import MMULeft
from modules import WhiteButton
from modules import Heading


class AdminMenu(tk.Frame):
    def __init__(
        self, root: tk.Tk, back_frame, student_actions_btn_cmd, course_actions_btn_cmd
    ):
        root.geometry("800x500")
        root.title("Student Menu")
        root.resizable(False, False)
        super().__init__(root, width=800, height=500)
        self.pack_propagate(0)

        self.backbutton = BackButton(self, back_frame, current_frame=self).pack()

        self.mmuleft = MMULeft(self).pack()

        self.admin_name_label = Heading(self, "Admin", 3, "#0650A4")
        self.admin_name_label.place(x=140, y=149)

        self.welcome_heading = Heading(self, "Hello,", 3)
        self.welcome_heading.place(x=44, y=149)

        self.description_heading = Heading(self, "What would you like to do today?", 3)
        self.description_heading.place(x=44, y=190)

        self.student_actions_button = WhiteButton(
            self, "Student Actions", student_actions_btn_cmd, 20, 2, "w"
        )
        self.student_actions_button.place(x=48, y=245)

        self.course_actions_button = WhiteButton(
            self, "Course Actions", course_actions_btn_cmd, 20, 2, "w"
        )
        self.course_actions_button.place(x=48, y=305)


if __name__ == "__main__":
    root = tk.Tk()
    student_menu = AdminMenu(root)
    student_menu.pack()
    root.mainloop()
