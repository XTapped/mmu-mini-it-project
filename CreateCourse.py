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


class CreateCourse2(ScrollableFrame):
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


if __name__ == "__main__":
    root = tk.Tk()
    frame = CreateCourse2(root)
    frame.pack()
    root.mainloop()
