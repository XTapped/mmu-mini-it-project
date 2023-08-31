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

        #Add like & Dislike img
        self.like_button_image = tk.PhotoImage(file="assets/like.png")
        self.dislike_button_image = tk.PhotoImage(file="assets/dislike.png")

        #Create like button 
        self.like_button = tk.Button(
            self,
            image=self.like_button_image,
            command=self.increment_likes,  
            borderwidth=0,
            relief="flat",
        )
        self.like_button.grid(row=2, column=0, sticky="w",padx=0,columnspan=2)

        #Create dislike button
        self.dislike_button = tk.Button(
            self,
            image=self.dislike_button_image,
            command=self.increment_dislike, 
            borderwidth=0,
            relief="flat"
        )
        self.dislike_button.grid(row=2, column=1, sticky="w",padx=0)

    def increment_likes(self):
        self.like_count.set(self.like_count.get() + 1)  #Increment the like count
        
        
    def increment_dislike(self):
        self.dislike_count.set(self.dislike_count.get() + 1) #Increment the dislike count








course_box = CourseBox(root, "Accadamic English", "(PEN0065)")
course_box.place(x=48, y=300)


root.mainloop()