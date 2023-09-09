import tkinter as tk
from typing import *

from modules import BackButton
from modules import MMULeft
from modules import Heading
from modules import Page
from modules import WhiteButton

root = tk.Tk()

class CoursesMenu (Page):
    def __init__(self,root: tk.Tk):
        super().__init__(root,"Courses Menu")
        
        back_button = BackButton(self,None)
        back_button.pack()
        back_button.place(x=48, y=40)

        MMULeft(self).pack()

        heading_1 = Heading(self,"Foundation In IT",1)
        heading_1.pack()
        heading_1.place(x=48, y=149)

        heading_2 = Heading(self,"Semester 3",2)
        heading_2.pack()
        heading_2.place(x=48, y=210)

courses_menu =CoursesMenu(root)
courses_menu.pack()

class CourseBox(tk.Frame):

        def __init__(self, parent, course_name, course_code, likes, dislikes, description):
            tk.Frame.__init__(self, parent)
            self.course_name = course_name
            self.course_code = course_code
            self.likes = likes
            self.dislikes = dislikes
            self.description = description

            # Create a label for the course name and code
            self.course_label = tk.Label(self, text=f"{self.course_name} ({self.course_code})")
            self.course_label.pack()

            # Create labels for the like and dislike counts
            self.like_label = tk.Label(self, text=f"Likes: {self.likes}")
            self.like_label.pack()
            self.dislike_label = tk.Label(self, text=f"Dislikes: {self.dislikes}")
            self.dislike_label.pack()

            # Create the like and dislike buttons
            self.like_button = tk.Button(self, text="Like", command=self.increment_likes)
            self.like_button.pack()
            self.dislike_button = tk.Button(self, text="Dislike", command=self.increment_dislikes)
            self.dislike_button.pack()

            # Create a label for the course description
            self.description_label = tk.Label(self, text=self.description, wraplength=200)
            self.description_label.pack()

            # Add the apply button
            self.apply_button = tk.Button(self, text="Apply for course", command=self.apply)
            self.apply_button.pack(side='bottom', padx=5, pady=5)

        def increment_likes(self):
            self.likes += 1
            self.like_label.config(text=f"Likes: {self.likes}")

        def increment_dislikes(self):
            self.dislikes += 1
            self.dislike_label.config(text=f"Dislikes: {self.dislikes}")

        def apply(self):
            # This method will be called when the apply button is clicked
            pass

english_course = CourseBox(root, "English", "PEN 002", 0, 0, "This is the course description...")
english_course.pack()

root.mainloop()

       
       














        
