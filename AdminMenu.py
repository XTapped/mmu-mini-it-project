import tkinter as tk

from modules.BackButton import BackButton
from modules.MMULeft import MMULeft
from modules.WhiteButton import WhiteButton
from modules.Heading import Heading


root = tk.Tk()


class AdminMenu(tk.Frame):
    def __init__(self, root: tk.Tk):
        root.geometry("800x500")
        root.title("Student Menu")
        root.resizable(False, False)
        super().__init__(root)

        self.backbutton = BackButton(root, None).pack()

        self.mmuleft = MMULeft(root).pack()

        self.admin_name_label = Heading(root, "Admin", 3, "#0650A4")
        self.admin_name_label.place(x=140, y=149)

        self.welcome_heading = Heading(root, "Hello,", 3)
        self.welcome_heading.place(x=44, y=149)

        self.description_heading = Heading(root, "What would you like to do today?", 3)
        self.description_heading.place(x=44, y=190)

        self.student_actions_button = WhiteButton(
            root, "Student Actions", None, 20, 2, "w"
        )
        self.student_actions_button.place(x=48, y=245)

        self.course_actions_button = WhiteButton(
            root, "Course Actions", None, 20, 2, "w"
        )
        self.course_actions_button.place(x=48, y=305)


student_menu = AdminMenu(root)
student_menu.pack()

root.mainloop()
