from typing import *
from tkinter import *
import random
import string


class TextEntry(Frame):
    """
    Default text entry field used in the program. You should use get() to fetch text typed into the entry. This class inherits from tk.Frame.

    Args:
        root (Tk): The root window of the program.
        label_text (str): The text to be displayed on the label.
        width (int, optional): The width of the entry field. Defaults to 20.
        regen_and_copy (bool, optional): Whether to display the regenerate and copy buttons. Useful for password fields. Defaults to False.
        disabled (bool, optional): Whether the entry field should be greyed out and unclickable. Defaults to False.
    """

    def __init__(
        self,
        root: Tk,
        label_text: str,
        width: int = 20,
        regen_and_copy: bool = False,
        disabled: bool = False,
    ):
        super().__init__(root)

        self._disabled = disabled
        self._label = Label(self, text=label_text, font=("Inter", 16))
        self._entry = Entry(
            self,
            bg="#D9D9D9",
            font=("Inter", 16),
            bd=1,
            highlightthickness=1,
            highlightbackground="black",
            relief=FLAT,
            width=width,
            state=DISABLED if self._disabled else NORMAL,
        )

        self._regenerate_icon = PhotoImage(file="assets/regenerate_icon.png")
        self._regenerate = Label(
            self,
            text="Regenerate",
            font=("Inter 13 underline"),
            fg="#363636",
            cursor="hand2",
            image=self._regenerate_icon,
            compound=LEFT,
        )

        self._copy_icon = PhotoImage(file="assets/copy_icon.png")
        self._copy = Label(
            self,
            text="Copy",
            font=("Inter 13 underline"),
            fg="#363636",
            cursor="hand2",
            image=self._copy_icon,
            compound=LEFT,
        )

        self._label.pack(anchor=W, side=TOP)
        self._entry.pack()

        if regen_and_copy:
            self._display_regenerate_and_copy()

    def _put_password(self, event):
        if self._disabled:
            self._entry.config(state=NORMAL)
            self._entry.delete(0, END)
            self._entry.insert(0, self._generate_random_password())
            self._entry.config(state=DISABLED)
        else:
            self._entry.delete(0, END)
            self._entry.insert(0, self._generate_random_password())

    def _generate_random_password(self):
        password = ""
        for _ in range(12):
            password += random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )
        return password

    def _copy_password(self, event):
        if self._disabled:
            self._entry.config(state=NORMAL)
            self._entry.select_range(0, END)
            self._entry.event_generate("<<Copy>>")
            self._entry.config(state=DISABLED)
        else:
            self._entry.select_range(0, END)
            self._entry.event_generate("<<Copy>>")

    def _display_regenerate_and_copy(self):
        self._regenerate.pack(anchor=W)
        self._regenerate.bind("<Button-1>", self._put_password)
        self._copy.pack(anchor=W)
        self._copy.bind("<Button-1>", self._copy_password)

    def get(self) -> str:
        """
        Get the text from the entry field.

        Returns:
            str: The text from the entry field.
        """
        return self._entry.get()


# test code
# if __name__ == "__main__":
#     root = Tk()
#     root.geometry("800x500")
#     root.title("TextEntry Test")
#     root.resizable(False, False)

#     frame = Frame(root, width=800, height=500)
#     frame.pack()

#     text_entry = TextEntry(frame, "TextEntry Test", regen_and_copy=True, disabled=True)
#     text_entry.pack()

#     root.mainloop()
