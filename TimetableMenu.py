import tkinter as tk
from modules import Heading, MMULeft, BackButton


class TimetableMenu(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self._back_button = BackButton(self, None)
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

        # Create the rest of the cells
        for i in range(1, 6):
            for j in range(1, 6):
                cell = Heading(
                    self._content_frame,
                    text="",
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
