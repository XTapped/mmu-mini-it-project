
import tkinter as tk
from typing import *
from modules import BackButton, MMULeft, WhiteButton, Heading, RedButton
from modules import ScrollableFrame



class CoursesMenu(ScrollableFrame):
    def init(self, root: tk.Tk):
        total_height = 10 * 10
        super().init(root, "Courses Menu", height=total_height)
        

class UpdateStudent(tk.Frame):
    def __init__(self, root):   
        super().__init__(root)
        self.config(width=800, height=500)
        
        

        # Main frame
        main_frame = tk.Frame(self)
        main_frame.pack(pady=1)  # Added vertical padding

        # BackButton
        back_frame = tk.Frame(main_frame)  # Changed root to self
        self.back_button = BackButton(
            root=root, back_frame=back_frame
        )  # Corrected root=tk to root=root
        self.back_button.pack()
        back_frame.pack()  # Changed grid to pack

        # MMULeft logo
        mmu_frame = tk.Frame(main_frame)  # Add a frame for MMULeft
        self.mmu_logo = MMULeft(
            root=root
        )  # Corrected root to root and removed parent argument
        self.mmu_logo.pack()
        mmu_frame.pack()  # Changed grid to pack

        self._Avatar = tk.PhotoImage(file="assets/Avatar.png")
        self._AvatarLabel = tk.Label(main_frame, image=self._Avatar, compound=tk.LEFT)
        # Students
        self.students_frame = tk.Frame(main_frame)  # Changed root to self
        self.students_data = [
            ("Kubenthran Udayar", self.on_update, self.on_delete),
            ("Hawash Abdullah", self.on_update, self.on_delete),
            ("Student 3", self.on_update, self.on_delete),
            ("Student 4", self.on_update, self.on_delete),
            ("Student 5", self.on_update, self.on_delete),
            ("Student 6", self.on_update, self.on_delete),
        ]

        self.student_frames = []

        for i, student_data in enumerate(self.students_data):
            student_frame = tk.Frame(self.students_frame)
            self.student_frames.append(student_frame)
            student_name = student_data[0]
            update_button = WhiteButton(
                student_frame, "Update", student_data[1], width=12, height=2
            )

            delete_button = RedButton(
                student_frame,
                "Delete",
                lambda i=i: self.on_delete(i),
                width=12,
                height=2,
            )

            heading = Heading(student_frame, student_name, 4)
            heading.grid(
                row=0, column=1, columnspan=1
            )  # Added vertical padding
            heading.place(x=150, y=6)

            student_label = tk.Label(
                student_frame, image=self._Avatar, compound=tk.LEFT
            )

            update_button.grid(row=1, column=1, padx=8)  # Added horizontal padding
            delete_button.grid(
                row=1, column=2, padx=8, pady=45
             )  # Added horizontal padding
            student_label.grid(row=1, column=0, padx=0 )  # Added padding

            # Calculate new row and column values
            row = (i + 2) // 2  # Start from row 2 instead of row 0
            column = (i + 2) % 2  # Alternate between column 0 and column 1

            # Set different padx values for different columns
            if column == 0:
                padx = 25
            else:
                padx = 350

            student_frame.grid(
                row=row, column=column, padx=padx, pady=10
            )  # Increased padding

        self.students_frame.pack(
            side="left", pady=10
        )  # Kept pack to ensure it's below the MMULeft logo
        self.pack(side="left", padx=10, pady=120)

    def on_update(self):
        """Handle update logic here"""
        pass

    def on_delete(self, index):
        """Remove the student at the given index"""
        # Remove the student's data
        del self.students_data[index]
        # Remove the student's frame from the GUI
        self.student_frames[index].grid_forget()
        del self.student_frames[index]



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Update Student Page")
    update_student_page = UpdateStudent(root)

    # Added vertical padding to ensure it's below the MMULeft logo
    root.mainloop()
