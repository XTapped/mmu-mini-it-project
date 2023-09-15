import tkinter as tk
from modules import Heading
from modules import MMULeft
from modules import BackButton
from contextlib import closing
import sqlite3


def execute_query(query, params=()):
    # Connect to the database
    with closing(sqlite3.connect("database.db")) as db:
        with db:
            # Execute the query and fetch the result
            result = db.execute(query, params).fetchall()
    # Return the result
    return result


class TimetableMenu(tk.Frame):
    def __init__(self, root, back_frame, student_id, semester):
        super().__init__(root)

        self._back_button = BackButton(self, back_frame)
        self._back_button.pack()

        self._mmu_logo = MMULeft(self)
        self._mmu_logo.pack()

        self._content_frame = tk.Frame(self)
        self._content_frame.pack(pady=(150, 0), anchor="w", padx=(50, 0))

        days = ["", "Mon", "Tue", "Wed", "Thu", "Fri"]
        times = [
            "08:00-10:00",
            "10:00-12:00",
            "12:00-14:00",
            "14:00-16:00",
            "16:00-18:00",
        ]

        # Create the labels for the days of the week
        for i in range(6):
            cell = Heading(
                self._content_frame,
                text=days[i],
                width=9,
                height=2,
                heading=6,
                highlightbackground="black",
                highlightthickness=1,
            )
            cell.grid(row=0, column=i)

        # Create the labels for the time slots
        for i in range(5):
            cell = Heading(
                self._content_frame,
                text=times[i],
                width=9,
                height=2,
                heading=6,
                highlightbackground="black",
                highlightthickness=1,
            )
            cell.grid(row=i + 1, column=0)

        day_to_col = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
        }

        time_to_row = {
            8: 1,
            10: 2,
            12: 3,
            14: 4,
            16: 5,
        }

        query = """
        SELECT 
            Classes.code, 
            Sections.lecture_venue, 
            Sections.lecture_day, 
            Sections.lecture_start_time,
            Sections.tutorial_venue,
            Sections.tutorial_day,
            Sections.tutorial_start_time
        FROM 
            SectionEnrollment 
        JOIN 
            Sections ON SectionEnrollment.section_id = Sections.id 
        JOIN 
            Classes ON Sections.class_code = Classes.code 
        WHERE 
            SectionEnrollment.student_id = ? AND 
            SectionEnrollment.semester = ?
        """
        data = execute_query(query, (student_id, semester))
        result = []
        for row in data:
            lecture_tuple = (row[0], row[1], row[2], row[3])
            tutorial_tuple = (row[0], row[4], row[5], row[6])
            result.append(lecture_tuple)
            result.append(tutorial_tuple)

        # dummy_data = [
        #     ("PEN0065", "CMNX1005", "Wednesday", 10),
        #     ("PPP0101", "CQAR3002", "Monday", 16),
        # ]
        class_dict = {
            (day_to_col[day], time_to_row[time]): (code, venue)
            for code, venue, day, time in result
        }

        # Create the rest of the cells
        for i in range(1, 6):
            for j in range(1, 6):
                the_class = class_dict.get((j, i))
                if the_class is None:
                    text = ""
                else:
                    text = f"{the_class[0]}\n{the_class[1]}"

                cell = Heading(
                    self._content_frame,
                    text=text,
                    width=9,
                    height=2,
                    heading=6,
                    highlightbackground="black",
                    highlightthickness=1,
                )
                cell.grid(row=i, column=j)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    TimetableMenu(root).pack(fill="both")
    root.mainloop()
