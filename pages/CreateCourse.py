import tkinter as tk
from typing import *
from modules import BackButton
from modules import MMULeft
from modules import TextEntry
from modules import WhiteButton
from modules import LongEntry
from modules import DateEntry
from modules import ScrollableFrame
from modules import switch_frames
from modules import execute_query


class _CreateCourse2(ScrollableFrame):
    def __init__(
        self,
        root: tk.Tk,
        course_name: str,
        semesters: str,
        course_actions_frame: tk.Frame,
    ):
        # TODO: We should probably turn title into a parameter
        super().__init__(root)

        self._classes = []
        self._course_name = course_name
        self._semesters = semesters

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
            self._content_frame,
            "Create Course",
            lambda: self.add_data_to_db(),
            width=15,
        )
        self._create_course_button.pack(anchor="w", pady=(0, 100), side="bottom")

    def _class_factory(self):
        class_instance = _Class(self._content_frame, self._class_factory)
        class_instance.pack()
        self._classes.append(class_instance)

    def get_data(self):
        """
        Returns a list containing the data from all the classes.

        Data from all the classes is in the following format: [subject name, subject code, subject description, [(capacity, venue, lecture time, tutorial time), ...]
        """
        return [class_.get_data() for class_ in self._classes]

    def add_data_to_db(self):
        """
        Adds the data from the CreateCourse2 page to the database.
        """
        # Add the course to the database
        execute_query(
            "INSERT INTO Courses (name, total_semesters) VALUES (?, ?)",
            (self._course_name, self._semesters),
        )

        # Get all data
        data = self.get_data()

        # Add the classes to the database
        for subject_name, subject_code, subject_description, groups in data:
            execute_query(
                "INSERT INTO Classes (name, code, description, course_name) VALUES (?, ?, ?, ?)",
                (subject_name, subject_code, subject_description, self._course_name),
            )

            # Get the class code
            class_code = execute_query(
                "SELECT code FROM Classes WHERE name = ?", (subject_name,)
            )[0][0]

            # Add the sections to the database
            for capacity, venue, lecture_time, tutorial_time in groups:
                lecture_day, lecture_start_time, lecture_end_time = lecture_time
                tutorial_day, tutorial_start_time, tutorial_end_time = tutorial_time

                execute_query(
                    "INSERT INTO Sections (class_code, capacity, lecture_day, tutorial_day, lecture_start_time, lecture_end_time, tutorial_start_time, tutorial_end_time, lecture_venue, tutorial_venue) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        class_code,
                        capacity,
                        lecture_day[0],
                        tutorial_day[0],
                        lecture_start_time[0].removesuffix("00"),
                        lecture_end_time[0].removesuffix("00"),
                        tutorial_start_time[0].removesuffix("00"),
                        tutorial_end_time[0].removesuffix("00"),
                        venue,
                        venue,
                    ),
                )

        # Go back to the course actions page
        switch_frames(self, self._course_actions_frame)


class _Class(tk.Frame):
    def __init__(self, root, button_command):
        super().__init__(root)

        self._group_counter = 1
        self._groups = []

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
        widget = _Group(self._group_frame, self._group_factory, self._group_counter)
        self._groups.append(widget)
        widget.pack(pady=(0, 15))
        self._group_counter += 1
        return widget

    def get_data(self):
        """
        Returns a tuple containing the subject name, subject code, subject description, and the data from all the groups.

        Data from all the groups is in the following format: (capacity, venue, lecture time, tutorial time)
        """
        return (
            self._subject_name_entry.get(),
            self._subject_code_entry.get(),
            self._subject_description_entry.get(),
            [group.get_data() for group in self._groups],
        )


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

        self.cap_venue_frame = tk.Frame(self)
        self.cap_venue_frame.pack(anchor="w", pady=(0, 15))

        self._capacity_entry = TextEntry(self.cap_venue_frame, "Capacity", 10)
        self._capacity_entry.pack(anchor="w", pady=(0, 15), padx=(0, 20), side="left")

        self._venue_entry = TextEntry(self.cap_venue_frame, "Venue", 10)
        self._venue_entry.pack(anchor="w", pady=(0, 15), side="right")

        self._lecture_time_entry = DateEntry(self, "Lecture")
        self._lecture_time_entry.pack(pady=(0, 15))

        self._tutorial_time_entry = DateEntry(self, "Tutorial")
        self._tutorial_time_entry.pack()

    def get_data(self):
        """
        Returns a tuple containing the capacity, venue, lecture time, and tutorial time entered by the user.
        """
        return (
            self._capacity_entry.get(),
            self._venue_entry.get(),
            self._lecture_time_entry.get(),
            self._tutorial_time_entry.get(),
        )


class CreateCourse(ScrollableFrame):
    def __init__(self, root: tk.Tk, course_actions_frame: tk.Frame):
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
        self._proceed_button = WhiteButton(
            self._content_frame,
            "Proceed",
            command=lambda: switch_frames(
                self,
                _CreateCourse2(
                    root,
                    self._course_name_entry.get(),
                    self._semester_entry.get(),
                    course_actions_frame,
                ),
            ),
        )
        self._proceed_button.pack(side="left", pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    frame = _CreateCourse2(root, "Computer Science", "8")
    frame.pack()
    root.mainloop()
