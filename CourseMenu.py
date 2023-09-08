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
        total_height = 10 * 300
        super().__init__(root, "Courses Menu", height=total_height)

        self.interior_backbutton = BackButton(
            self.interior, None
        )  # Add to interior frame
        self.interior_backbutton.pack()

        self.interior_mmuleft = MMULeft(self.interior)
        self.interior_mmuleft.pack()

        self.interior_heading_1 = Heading(self.interior, "Foundation In IT", 1)
        self.interior_heading_1.place(x=48, y=149)

        self.interior_heading_2 = Heading(self.interior, "Semester 3", 2)
        self.interior_heading_2.place(x=48, y=210)

        self.interior.update_idletasks()

class CourseBox(tk.Frame):
    def __init__(
        self,
        root: tk.Tk,
        course_name: str,
        course_code: str,
        course_description: str,
    ):
        super().__init__(root)

        # Create label for course name
        self.course_name = course_name
        self.course_name_label = Heading(self, course_name, 3)
        self.course_name_label.grid(row=0, column=0, columnspan=1, sticky="w")

        # Create label for course code
        self.course_code = course_code
        self.course_code_label = Heading(self, course_code, 3)
        self.course_code_label.grid(row=0, column=2, columnspan=1, sticky="w", padx=0)

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
        self.like_button.grid(
            row=1, column=0, columnspan=1, sticky="W", padx=5, pady=10
        )

        # Create dislike button
        self.dislike_button = tk.Button(
            self,
            image=self.dislike_button_image,
            command=self.increment_dislike,  # Call increment_dislike when the button is clicked
            borderwidth=0,
            relief="flat",
        )
        self.dislike_button.grid(
            row=1, column=0, columnspan=1, sticky="W", padx=60, pady=10
        )

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
        self.like_count_label.grid(row=1, column=0, columnspan=1, sticky="W", padx=30)

        # Create dislike counter label
        self.dislike_count_label = Heading(
            self,
            "",
            6,
            "#EC1A2F",
            textvariable=self.dislike_count,  # automatically update the dislike label
        )
        self.dislike_count_label.grid(
            row=1, column=0, columnspan=1, sticky="W", padx=90
        )

        # Create Course Description
        self.course_description = course_description
        self.course_description_text = tk.Message(
            self,
            text=course_description,
            font=("inter", 13),
            aspect=360,
            justify="left",
        )
        self.course_description_text.grid(
            row=2, column=0, columnspan=50, sticky="W", padx=0, pady=0
        )

         # Create Apply for Class button
        self.apply_button = WhiteButton(
            self,
            text="Apply for Class",
            command= lambda: self.open_apply_window(course_name, course_code),
            width=15,
        )
        self.apply_button.grid(
            row=3, column=0, columnspan=1, sticky="W", padx=5, pady=10
        )

    # Like & dislike counter method
    def increment_likes(self):
        self.like_count.set(
            self.like_count.get() + 1
        )  # Increment the like count

    def increment_dislike(self):
        self.dislike_count.set(
            self.dislike_count.get() + 1
        )  # Increment the dislike count

    def open_apply_window(self, course_name, course_code):
        self.apply_window = ApplyCourse(course_name, course_code)
        

class ApplyCourse(tk.Toplevel):
    def __init__(
            self, 
            course_name, 
            course_code,
        ):

        super().__init__(root)
        self.title(f"Apply for {course_name} {course_code}")
        self.geometry("700x500") 
        

        self.heading_3 = Heading(self,"Choose your preferred class times",4)
        self.heading_3.grid(row=0,column=0,columnspan=3,sticky="W")

         # Shared variable
        self.selected_time = tk.StringVar()

        # List of time options
        time_options = ["Monday (13:00-16:00) / Thursday (08:00-11:00)",
                        "Tuesday (16:00-19:00) / Wednesday (14:00-17:00)",
                        "Monday (08:00-11:00) / Wednesday (13:00-16:00)",
                        "Wednesday (16:00-19:00) / Friday (08:00-11:00)"]
        
        # List of class location
        class_location = ["CNMX1002","CQAR3001","CQCR2002","CMNX1005"]
        
        # List of class capacity
        capacity_numbers = ["53/120","30/120","61/120","101/120"] 
        
        
        # Images for radiobutton
        self.img1 = tk.PhotoImage(file="assets/radiobutton_non_select.png")
        self.img2 = tk.PhotoImage(file="assets/radiobutton_selected.png")

        self.profile_img = tk.PhotoImage(file="assets/capacity_blue.png")

        # Create RadioButton 
        for i, option in enumerate(time_options):
            rb = tk.Radiobutton(
                self,
                text=option,
                font=("inter",15),
                variable=self.selected_time,
                value=option,
                image=self.img1,
                selectimage=self.img2,
                compound='left',
                borderwidth=0,
                indicatoron=0,
                padx=10
            )
            rb.grid(row=i*3+1,column=1,columnspan=2,sticky="W")
        
            location = Heading(self,class_location[i],6)
            location.grid(row=i*3+2, column=1, columnspan=1, sticky="W",padx=42)

            #Capacity image
            profile = tk.Label(self, image=self.profile_img)
            profile.grid(row=i*3+3, column=1, sticky="W", padx=10)

            # Capacity number
            capacity = Heading(self,capacity_numbers[i],6,"#0750A4") # replace 20 with your actual capacity value
            capacity.grid(row=i*3+3, column=1, sticky="W", padx=30)

        # Apply button
        apply_button = WhiteButton(self,"Apply",command=self.apply)
        apply_button.grid(row=len(time_options)*3+1, column=0, columnspan=2,padx=5,sticky="W")

#Apply button method
    def apply(self):
        selected_time = self.selected_time.get()
        ApplyCourse.destroy(self)


courses_menu = CoursesMenu(root)
courses_menu.pack(fill="both", expand=True)

eng = CourseBox(
    courses_menu.interior,
    "Acadamic English",
    "(PEN0065)",
    "Academic English is a course that aims to help students develop their academic writing and communication skills. This course covers topics such as grammar, vocabulary, style, structure, argumentation, citation, and plagiarism. Students will learn how to write different types of academic texts, such as essays, reports, reviews, and research papers. Students will also practice their oral presentation and discussion skills in various academic contexts. This course is suitable for students who want to improve their academic performance and prepare for further studies or professional careers.",
)
eng.place(x=48, y=270)

principles_of_physics = CourseBox(
    courses_menu.interior,
    "Principles of Physics",
    "(PPP0101)",
    "Principles of Physics is a course that introduces the fundamental concepts and methods of physics. It covers topics such as mechanics, thermodynamics, electromagnetism, optics, and quantum physics. This course aims to develop the students’ analytical and problem-solving skills, as well as their understanding of the physical world and its phenomena. This course also prepares the students for more advanced courses in physics and related fields. This course is suitable for students who have a strong background in mathematics and science, and who are interested in pursuing a career or further studies in physics or engineering.",
)
principles_of_physics.place(x=48,y=640)

mathematics_3 = CourseBox(
    courses_menu.interior,
    "Mathematics III",
    "(PMT0301)",
    "Mathematics III is a subject that covers advanced topics in mathematics, such as differential equations, linear algebra, complex analysis, and abstract algebra. This course aims to develop students’ mathematical skills and knowledge, as well as their ability to apply them to various fields of science and engineering. Students who take this course are expected to have a solid background in calculus, geometry, and algebra, and be familiar with basic concepts of logic and proof. Mathematics III is a challenging but rewarding subject that will prepare students for further studies or careers in mathematics and related disciplines.",
)
mathematics_3.place(x=48,y=1010)


courses_menu.interior.update_idletasks()
root.mainloop()