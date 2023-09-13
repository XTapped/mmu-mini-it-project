import tkinter as tk
from typing import *
from modules import BackButton
from modules import MMULeft
from modules import TextEntry
from modules import WhiteButton
from modules import LongEntry
from modules import DateEntry
from modules import ScrollableFrame


class CreateCourse(ScrollableFrame):
    def __init__(self, root: tk.Tk):
        # TODO: We should probably turn title into a parameter
        super().__init__(root)

        # TODO: We need to figure out how to pass in back_frame later
        self._back_button = BackButton(self.interior, None, current_frame=self)
        self._back_button.pack()

        self._mmu_logo = MMULeft(self.interior)
        self._mmu_logo.pack()

        self._content_frame = tk.Frame(self.interior)
        self._content_frame.pack(side="left", padx=(48, 0), pady=(160, 0))

        self._course_name_entry = TextEntry(self._content_frame, "Course Name")
        self._course_name_entry.pack()

        self._semester_entry = TextEntry(self._content_frame, "Number of Semesters")
        self._semester_entry.pack()

        # TODO: We should add a command to go to the next page later on
        self._proceed_button = WhiteButton(self._content_frame, "Proceed")
        self._proceed_button.pack(side="left", pady=20)


class _CreateCourse2(ScrollableFrame):
    def __init__(self, root: tk.Tk):
        # TODO: We should probably turn title into a parameter
        super().__init__(root)

        # TODO: We need to figure out how to pass in back_frame later
        self._back_button = BackButton(self.interior, None, current_frame=self)
        self._back_button.pack()

        self._mmu_logo = MMULeft(self.interior)
        self._mmu_logo.pack()

        self._content_frame = tk.Frame(self.interior)
        self._content_frame.pack(anchor="w", padx=(48, 0), pady=(160, 0))

        self._class_factory()

        # TODO: Add a command here later
        self._create_course_button = WhiteButton(
            self._content_frame, "Create Course", None, width=15
        )
        self._create_course_button.pack(anchor="w", pady=(0, 100), side="bottom")

    def _class_factory(self):
        _Class(self._content_frame, self._class_factory).pack()


class _Class(tk.Frame):
    def __init__(self, root, button_command):
        super().__init__(root)

        self._group_counter = 1

        self._add_button_img = tk.PhotoImage(file="assets/add_button.png")
        self._add_button_subject = tk.Button(
            self, image=self._add_button_img, borderwidth=0, command=button_command
        )
        self._add_button_subject.pack(anchor="nw", pady=(0, 20))

        self._subject_name_entry = TextEntry(self, "Subject Name", width=35)
        self._subject_name_entry.pack(anchor="w", pady=(0, 15))

        self._subject_code_entry = TextEntry(self, "Subject Code", width=35)
        self._subject_code_entry.pack(anchor="w", pady=(0, 15))

        self._subject_description_entry = LongEntry(self, "Description", width=35)
        self._subject_description_entry.pack(anchor="w", pady=(0, 15))

        self._group_frame = tk.Frame(self)
        self._group_frame.pack(pady=(0, 30))

        self._group_factory()

    def _group_factory(self):
        widget = _Group(
            self._group_frame, self._group_factory, self._group_counter
        ).pack(pady=(0, 15))
        self._group_counter += 1
        return widget


class _Group(tk.Frame):
    def __init__(self, root, button_command, group_num):
        super().__init__(root)
        self._add_button_img = tk.PhotoImage(file="assets/add_button.png")

        self._group_text_frame = tk.Frame(self)
        self._group_text_frame.pack(anchor="w")

        self._group_num = tk.Label(
            self._group_text_frame,
            font="Inter 16 bold",
            text=f"Group {group_num}",
        )
        self._group_num.grid(row=0, column=0)

        self._add_button_group = tk.Button(
            self._group_text_frame,
            image=self._add_button_img,
            borderwidth=0,
            command=button_command,
        )
        self._add_button_group.grid(row=0, column=1, padx=(10, 0))

        self._capacity_entry = TextEntry(self, "Capacity", 10)
        self._capacity_entry.pack(anchor="w", pady=(0, 15))

        self._lecture_time_entry = DateEntry(self)
        self._lecture_time_entry.pack(pady=(0, 15))

        self._tutorial_time_entry = DateEntry(self)
        self._tutorial_time_entry.pack()


if __name__ == "__main__":
    root = tk.Tk()
    frame = _CreateCourse2(root)
    frame.pack()
    root.mainloop()
