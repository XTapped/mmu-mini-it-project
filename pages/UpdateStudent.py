import tkinter as tk
from idlelib.tooltip import Hovertip
from modules import ScrollableFrame
from modules import BackButton
from modules import MMULeft
from modules import Heading
from modules import WhiteButton
from modules import RedButton


class UpdateStudent(ScrollableFrame):
    # TODO: Remove all the Nones from the params
    def __init__(self, root, back_frame):
        super().__init__(root)
        self._back_button = BackButton(self.interior, back_frame, current_frame=self)
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
        self._student_widget_list = []

        self._column_num = 1
        for index, student in enumerate(self._student_list):
            if index % 2 == 0:
                self._row_num = index // 2
            self._column_num = 0 if self._column_num == 1 else 1

            widget = _Student(self._student_container, student, index, self.regrid)
            widget.grid(
                row=self._row_num, column=self._column_num, padx=(0, 50), pady=(0, 50)
            )
            self._student_widget_list.append(widget)

    def regrid(self, list_pos):
        self._student_list.pop(list_pos)

        for widget in self._student_widget_list:
            widget.destroy()

        self._student_widget_list.clear()

        self._column_num = 1
        for index, student in enumerate(self._student_list):
            if index % 2 == 0:
                self._row_num = index // 2
            self._column_num = 0 if self._column_num == 1 else 1

            widget = _Student(self._student_container, student, index, self.regrid)
            widget.grid(
                row=self._row_num, column=self._column_num, padx=(0, 50), pady=(0, 50)
            )
            self._student_widget_list.append(widget)


class _Student(tk.Frame):
    def __init__(self, root, name, list_pos, delete_func):
        super().__init__(root)

        self.list_pos = list_pos
        self._delete_func = delete_func

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

        self._delete_button = RedButton(
            self._text_frame, "Delete", self._super_destroy, 8, 2
        )
        self._delete_button.pack(side="left", anchor="w", padx=5)

    def _truncate_string(self, string):
        if len(string) > 13:
            return string[:10] + "..."
        else:
            return string

    def _super_destroy(self):
        self._delete_func(self.list_pos)


if __name__ == "__main__":
    root = tk.Tk()
    UpdateStudent(root, None).pack()
    root.mainloop()
