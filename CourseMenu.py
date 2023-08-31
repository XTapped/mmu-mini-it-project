import tkinter as tk
from typing import *

from modules import BackButton
from modules import MMULeft
from modules import Heading
from modules import ScrollableFrame
from modules import WhiteButton

root = tk.Tk()


class CoursesMenu(ScrollableFrame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, "Courses Menu")

        self.interior_backbutton=BackButton(self, None)
        self.interior_backbutton.pack()

        self.interior_mmuleft=MMULeft(self)
        self.interior_mmuleft.pack()

        self.interior_heading_1 = Heading(self, "Foundation In IT", 1)
        self.interior_heading_1.place(x=48, y=149)

        self.interior_heading_2 = Heading(self, "Semester 3", 2)
        self.interior_heading_2.place(x=48, y=210)


courses_menu = CoursesMenu(root)
courses_menu.pack()


class CourseBox(tk.Frame):
    def __init__( 
            self, 
            root: tk.Tk, 
            course_name: str, 
            course_code: str, 
            x_like_count_label:int, 
            x_dislike_count_label:int,
            ):
        
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
            command=self.increment_likes,  # Call increment_likes when the button is clicked
            borderwidth=0,
            relief="flat",
        )
        self.like_button.grid(row=2, column=0, sticky="w",padx=0,columnspan=2)

        #Create dislike button
        self.dislike_button = tk.Button(
            self,
            image=self.dislike_button_image,
            command=self.increment_dislike, # Call increment_dislike when the button is clicked
            borderwidth=0,
            relief="flat"
        )
        self.dislike_button.grid(row=2, column=1, sticky="w",padx=0)
        
        self.like_count = tk.IntVar()  # Variable to store the like count
        self.like_count.set(0) #Set like counter to begin from 0

        self.dislike_count = tk.IntVar() #Variable to stroe the like count
        self.dislike_count.set(0) #Set dislike counter to begin from 0

        
        self.x_like_count_label = x_like_count_label 
        self.like_count_label = Heading(
                                        self, 
                                        "",
                                        6,
                                        "#07A40D",
                                        textvariable=self.like_count, # automatically update the label                           
        )  
        
        self.like_count_label.place(x=x_like_count_label, y=44) #Specify x possition of like counter label


        self.x_dislike_count_label = x_dislike_count_label 
        self.dislike_count_label = Heading(
                                        self,
                                        "",
                                        6,
                                        "#EC1A2F",
                                        textvariable=self.dislike_count, # automatically update the label              
        )  
        
        self.dislike_count_label.place(x=x_dislike_count_label, y=44) #Specify y possition of dislike counter label


    def increment_likes(self):
        self.like_count.set(self.like_count.get() + 1)  #Increment the like count
        
        
    def increment_dislike(self):
        self.dislike_count.set(self.dislike_count.get() + 1) #Increment the dislike count
        

#course_box = CourseBox(root, "Accadamic English", "(PEN0065)", 26 ,104)
#course_box.place(x=48, y=300)

#root.mainloop()