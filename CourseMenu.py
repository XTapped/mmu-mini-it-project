import tkinter as tk
from typing import *

from modules import BackButton
from modules import MMULeft
from modules import Heading
from modules import Page
from modules import WhiteButton

root = tk.Tk()


class CoursesMenu(Page):
    def __init__(self, root: tk.Tk):
        super().__init__(root, "Courses Menu")

        back_button = BackButton(self, None)
        back_button.place(x=48, y=40)

        MMULeft(self).pack()

        heading_1 = Heading(self, "Foundation In IT", 1)
        heading_1.place(x=48, y=149)

        heading_2 = Heading(self, "Semester 3", 2)
        heading_2.place(x=48, y=210)


courses_menu = CoursesMenu(root)
courses_menu.pack()

class CourseBox(tk.Frame):
    def __init__( 
            self, 
            root: tk.Tk, 
            course_name: str, 
            course_code: str, ):

        super().__init__(root)

        #Create label for course name
        self.course_name = course_name   
        self.course_name_label = Heading(self, course_name, 3)
        self.course_name_label.grid(row=0, column=0, columnspan=4, sticky="w")

        #Create label for course code
        self.course_code = course_code
        self.course_code_label = Heading(self, course_code, 3)
        self.course_code_label.grid(row=0, column=4, columnspan=4, sticky="w")


# course_box = CourseBox(root, "Accadamic English", "(PEN0065)")
# course_box.place(x=48, y=300)


# root.mainloop()