import tkinter as tk
from modules.BackButton import BackButton
from modules.MMULeft import MMULeft
from modules.WhiteButton import WhiteButton
from modules.Heading import Heading
from modules.RedButton import RedButton


class UpdateStudent(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self._root = root
        self._root.geometry("800x500")

        self._mmu_left = MMULeft(self._root)
        self._mmu_left.pack()  # Use the custom pack() method

        self._back_button = BackButton(self._root, None)
        self._back_button.pack()
        self._back_button.place(x=50, y=30)

        # This is where we create the list of students and their update and delete buttons
        self._students_list = self._get_students_list()
        self._student_elements = (
            {}
        )  # Dictionary to store the labels and buttons for each student

        # Offset for vertical spacing between students
        vertical_offset = 170

        for i, student in enumerate(self._students_list):
            row = (i // 2) + 1  # Start from the second row
            column = (i % 2) * 3  # Alternate between the first and second column

            student_name_label = Heading(self, text=student, heading=4)
            student_name_label.place(
                x=column * 200 + 10,
                y=row * (student_name_label.winfo_reqheight() + vertical_offset) - 100,
            )

            update_button = WhiteButton(
                self, "Update", self._update_student_handler, width=14, height=2
            )
            update_button.place(
                x=column * 200 + 10,
                y=row * (update_button.winfo_reqheight() + vertical_offset) + 50,
            )

            delete_button = RedButton(
                self,
                "Delete",
                lambda student=student: self._delete_student_handler(student),
                width=14,
                height=2,
            )
            delete_button.place(
                x=column * 200 + 180,
                y=row * (delete_button.winfo_reqheight() + vertical_offset) + 50,
            )

            # Store the label and buttons associated with the student
            self._student_elements[student] = (
                student_name_label,
                update_button,
                delete_button,
            )

            # Store the label and buttons associated with the student
            self._student_elements[student] = (
                student_name_label,
                update_button,
                delete_button,
            )

    def _get_students_list(self):
        # You would fetch the actual students list from your data source
        # For now, let's just use a dummy list
        return [
            "Kubenthran Udeyar",
            "Hawash Abdullah",
            "Harris Majeed",
            "Laxman Pillai",
            "Vinesh Sivaneswaran",
            "Khiisen Nair",
        ]

    def _update_student_handler(self):
        # This is where you would handle student update
        print("Update student")

    def _delete_student_handler(self, student):
        # Remove the student from the list
        self._students_list.remove(student)

        # Destroy the label and buttons associated with the deleted student
        label, update_button, delete_button = self._student_elements[student]
        label.destroy()
        update_button.destroy()
        delete_button.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Update Student")
    update_student_page = UpdateStudent(root)
    update_student_page.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
