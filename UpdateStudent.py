import tkinter as tk
from idlelib.tooltip import Hovertip
from modules import (
    ScrollableFrame,
    BackButton,
    MMULeft,
    Heading,
    WhiteButton,
    RedButton,
)


class UpdateStudent(ScrollableFrame):
    # TODO: Remove all the Nones from the params
    def __init__(self, root, back_frame=None):
        super().__init__(root)
        self._back_button = BackButton(self.interior, back_frame)
        self._back_button.pack()

        self._mmu_logo = MMULeft(self.interior)
        self._mmu_logo.pack()

        self._student_container = tk.Frame(self.interior)
        self._student_container.pack(fill="x", pady=180, padx=50)

        self._student_list = [
            "Harris Majeed",
            "Vinesh Sivaneswaran",
            "Laxman Pillai",
            "Kubenthran Udayar",
            "Khiisyen Nair",
        ]

        self._column_num = 1
        for index, student in enumerate(self._student_list):
            if index % 2 == 0:
                self._row_num = index // 2
            self._column_num = 0 if self._column_num == 1 else 1

            _Student(self._student_container, student).grid(
                row=self._row_num, column=self._column_num, padx=(0, 50), pady=(0, 50)
            )


class _Student(tk.Frame):
    def __init__(self, root, name):
        super().__init__(root)

        self.list_pos = list_pos

        self._avatar_frame = tk.Frame(self)
        self._avatar_frame.pack(side="left")

        self._text_frame = tk.Frame(self)
        self._text_frame.pack(padx=10)

        self._avatar_img = tk.PhotoImage(file="assets/avatar.png")
        self._avatar = tk.Label(self._avatar_frame, image=self._avatar_img)
        self._avatar.pack()

        self._student_name = Heading(self._text_frame, self._truncate_string(name), 4)
        self._student_name.pack(anchor="w")

        self._name_tooltip = Hovertip(self._student_name, name, hover_delay=200)

        self._update_button = WhiteButton(self._text_frame, "Update", None, 8, 2)
        self._update_button.pack(side="left", anchor="w", padx=5)

        self._delete_button = RedButton(self._text_frame, "Delete", None, 8, 2)
        self._delete_button.pack(side="left", anchor="w", padx=5)

    def _truncate_string(self, string):
        if len(string) > 13:
            return string[:10] + "..."
        else:
            return string


if __name__ == "__main__":
    root = tk.Tk()
    UpdateStudent(root).pack()
    root.mainloop()
