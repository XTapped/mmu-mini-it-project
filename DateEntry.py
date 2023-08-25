from typing import *
import tkinter as tk
import DropDown as lib


class DateEntry(tk.Frame):
    def __init__(
        self,
        root: tk.Tk,
    ):
        super().__init__(root)

        self._days_list = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ]

        self._hours_list = [f"{str(hour).zfill(2)}00" for hour in range(8, 19, 2)]

        self._label = tk.Label(
            self, text="Class Time (Day/Start Time/End Time)", font=("Inter", 16)
        )
        self._day = lib.DropDown(self, self._days_list, width=10)
        self._start_hour = lib.DropDown(self, self._hours_list, width=10)
        self._end_hour = lib.DropDown(self, self._hours_list, width=10)

        self._label.grid(sticky=tk.W, row=0, column=0)
        self._day.grid(sticky=tk.W, row=1, column=0)
        self._start_hour.grid(sticky=tk.W, row=2, column=0)
        self._end_hour.grid(sticky=tk.W, row=3, column=0)
        self.grid_rowconfigure(2, pad=20)

    def get(self) -> Tuple[str, str, str]:
        """
        Get the selected values from the dropdown menus.

        Returns:
            Tuple[str, str, str]: The selected values from the dropdown menus. The first value is the day, the second value is the start hour, and the third value is the end hour.
        """
        return self._day.get(), self._start_hour.get(), self._end_hour.get()


# test code
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x500")
#     root.title("DateEntry Test")
#     root.resizable(False, False)

#     date = DateEntry(root)
#     date.pack(anchor=tk.W, side=tk.TOP, padx=20, pady=20)

#     root.mainloop()
