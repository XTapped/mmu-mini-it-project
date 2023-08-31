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
        total_height = 10 * 100
        super().__init__(root, "Courses Menu", height=total_height)

        self.interior_backbutton = BackButton(
            self.interior, None
        )  # Add to interior frame
        self.interior_backbutton.pack()

        self.interior_mmuleft = MMULeft(self.interior)  # Add to interior frame
        self.interior_mmuleft.pack()

        self.interior_heading_1 = Heading(
            self.interior, "Foundation In IT", 1
        )  # Add to interior frame
        self.interior_heading_1.place(x=48, y=149)

        self.interior_heading_2 = Heading(
            self.interior, "Semester 3", 2
        )  # Add to interior frame
        self.interior_heading_2.place(x=48, y=210)

        self.interior.update_idletasks()

class CourseBox(tk.Frame):
    def __init__(
        self,
        root: tk.Tk,
        course_name: str,
        course_code: str,
    ):
        super().__init__(root)

        # Create label for course name
        self.course_name = course_name
        self.course_name_label = Heading(self, course_name, 3)
        self.course_name_label.grid(row=0, column=0, columnspan=1, sticky="w")

        # Create label for course code
        self.course_code = course_code
        self.course_code_label = Heading(self, course_code, 3)
        self.course_code_label.grid(row=0, column=2, columnspan=1, sticky="w")

        # Add like & Dislike img
        self.like_button_image = tk.PhotoImage(file="assets/like.png")
        self.dislike_button_image = tk.PhotoImage(file="assets/dislike.png")

        # Create like button
        self.like_button = tk.Button(
            self,
            image=self.like_button_image,
            command=self.increment_likes,  # Call increment_likes when the button is clicked
            borderwidth=0,
            relief="flat",
        )
        self.like_button.grid(row=1, column=0, columnspan=1, sticky="W")

        # Create dislike button
        self.dislike_button = tk.Button(
            self,
            image=self.dislike_button_image,
            command=self.increment_dislike,  # Call increment_dislike when the button is clicked
            borderwidth=0,
            relief="flat",
        )
        self.dislike_button.grid(row=1, column=0, columnspan=1, sticky="W", padx=60)

        self.like_count = tk.IntVar()  # Variable to store the like count
        self.like_count.set(0)  # Set like counter to begin from 0

        self.dislike_count = tk.IntVar()  # Variable to stroe the like count
        self.dislike_count.set(0)  # Set dislike counter to begin from 0

        # Create like counter label
        self.like_count_label = Heading(
            self,
            "",
            6,
            "#07A40D",
            textvariable=self.like_count,  # automatically update the like label
        )
        self.like_count_label.grid(row=1, column=0, columnspan=1, sticky="W", padx=25)

        # Create dislike counter label
        self.dislike_count_label = Heading(
            self,
            "",
            6,
            "#EC1A2F",
            textvariable=self.dislike_count,  # automatically update the dislike label
        )
        self.dislike_count_label.grid(row=1, column=0, columnspan=1, sticky="W", padx=90)



    def increment_likes(self):
        self.like_count.set(self.like_count.get() + 1)  # Increment the like count

    def increment_dislike(self):
        self.dislike_count.set(
            self.dislike_count.get() + 1
        )  # Increment the dislike count


courses_menu = CoursesMenu(root)
courses_menu.pack(fill="both", expand=True)


eng = CourseBox(courses_menu.interior, 
                "Acadamic English", 
                "(PEN0065)")
               
eng.place(x=48, y=280)

# Physics = CourseBox(courses_menu.interior, "Principles of Physics", "(PPP0101)")
# Physics.place(x=48, y=380)

courses_menu.interior.update_idletasks()
root.mainloop()
