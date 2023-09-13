import tkinter as tk
from modules import BackButton
from modules import MMULeft
from modules import WhiteButton
from modules import Heading


class StudentMenu(tk.Frame):
    def __init__(self, root: tk.Tk, student_name):
        root.geometry("800x500")
        root.title("Student Menu")
        root.resizable(False, False)
        super().__init__(root)

        self.backbutton = BackButton(root, None).pack()

        self.mmuleft = MMULeft(root).pack()

        self.student_name = student_name
        self.student_name_label = Heading(root, student_name, 3, "#0650A4")
        self.student_name_label.place(x=140, y=149)

        self.welcome_heading = Heading(root, "Hello,", 3)
        self.welcome_heading.place(x=44, y=149)

        self.description_heading = Heading(root, "What would you like to do today?", 3)
        self.description_heading.place(x=44, y=190)

        self.available_course_button = WhiteButton(
            root, "Browse Available Course", None, 20, 2, "w"
        )
        self.available_course_button.place(x=48, y=245)

        self.view_timetable_button = WhiteButton(
            root, "View Timetable", None, 20, 2, "w"
        )
        self.view_timetable_button.place(x=48, y=305)


if __name__ == "__main__":
    root = tk.Tk()
    student_menu = StudentMenu(root, "Kubenthran Udayar")
    student_menu.pack()
    root.mainloop()
