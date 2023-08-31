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