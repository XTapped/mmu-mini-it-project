import tkinter as tk
from modules import ScrollableFrame
from modules import BackButton
from modules import MMULeft
from modules import Heading
from modules import WhiteButton
from modules import RedButton


class UpdateCourse(ScrollableFrame):
    def __init__(self, root):
        super().__init__(root)

        self.back_button = BackButton(self.interior, None)
        self.back_button.pack()

        self.mmu_logo = MMULeft(self.interior)
        self.mmu_logo.pack()

        self.main_content = tk.Frame(self.interior)
        self.main_content.pack(pady=(150, 0), padx=(45, 0), anchor="w")

        self.main_heading = Heading(self.main_content, "Update Course", 2)
        self.main_heading.pack(anchor="w", pady=(0, 30))

        self.Course(self.main_content).pack(pady=30)
        self.Course(self.main_content).pack(pady=30)
        self.Course(self.main_content).pack(pady=30)
        self.Course(self.main_content).pack(pady=30)
        self.Course(self.main_content).pack(pady=30)
        self.Course(self.main_content).pack(pady=30)
        self.Course(self.main_content).pack(pady=30)
        self.Course(self.main_content).pack(pady=30)

    class Course(tk.Frame):
        def __init__(self, root):
            super().__init__(root)

            self.name_heading = Heading(self, "Foundation in Information Technology", 3)
            self.name_heading.pack(anchor="w")

            self.buttons_container = tk.Frame(self)
            self.buttons_container.pack(anchor="w")

            self.update_button = WhiteButton(
                self.buttons_container, "Update Course", None, 13
            )
            self.update_button.pack(side="left", padx=(0, 15))

            self.delete_button = RedButton(
                self.buttons_container, "Delete Course", None, 13
            )
            self.delete_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    UpdateCourse(root).pack()
    root.mainloop()
