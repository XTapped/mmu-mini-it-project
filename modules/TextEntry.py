from typing import *
import tkinter as tk
import random
import string


class TextEntry(tk.Frame):
    """
    Default text entry field used in the program. You should use get() to fetch text typed into the entry. This class inherits from tk.Frame.

    Args:
        root (Tk): The root window of the program.
        label_text (str): The text to be displayed on the label.
        width (int, optional): The width of the entry field. Defaults to 20.
        regen (bool, optional): Whether the entry field should have a button to regenerate the text. Defaults to False.
        copy (bool, optional): Whether the entry field should have a button to copy the text. Defaults to False.
        disabled (bool, optional): Whether the entry field should be greyed out and unclickable. Defaults to False.
    """

    def __init__(
        self,
        root: tk.Tk,
        label_text: str,
        width: int = 20,
        regen: bool = False,
        copy: bool = False,
        disabled: bool = False,
    ):
        super().__init__(root)

        self._disabled = disabled
        self._label = tk.Label(self, text=label_text, font=("Inter", 16))
        self._entry = tk.Entry(
            self,
            bg="#D9D9D9",
            font=("Inter", 16),
            bd=1,
            highlightthickness=1,
            highlightbackground="black",
            relief=tk.FLAT,
            width=width,
            state=tk.DISABLED if self._disabled else tk.NORMAL,
        )

        self._regenerate_icon = tk.PhotoImage(file="assets/regenerate_icon.png")
        self._regenerate = tk.Label(
            self,
            text="Regenerate",
            font=("Inter 13 underline"),
            fg="#363636",
            cursor="hand2",
            image=self._regenerate_icon,
            compound=tk.LEFT,
        )

        self._copy_icon = tk.PhotoImage(file="assets/copy_icon.png")
        self._copy = tk.Label(
            self,
            text="Copy",
            font=("Inter 13 underline"),
            fg="#363636",
            cursor="hand2",
            image=self._copy_icon,
            compound=tk.LEFT,
        )

        self._label.pack(anchor=tk.W, side=tk.TOP)
        self._entry.pack()

        if regen:
            self._display_regenerate_button()
        if copy:
            self._display_copy_button()

    def _put_password(self, event):
        if self._disabled:
            self._entry.config(state=tk.NORMAL)
            self._entry.delete(0, tk.END)
            self._entry.insert(0, self._generate_random_password())
            self._entry.config(state=tk.DISABLED)
        else:
            self._entry.delete(0, tk.END)
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
            self._entry.config(state=tk.NORMAL)
            self._entry.select_range(0, tk.END)
            self._entry.event_generate("<<Copy>>")
            self._entry.config(state=tk.DISABLED)
        else:
            self._entry.select_range(0, tk.END)
            self._entry.event_generate("<<Copy>>")

    def _display_regenerate_button(self):
        self._regenerate.pack(anchor=tk.W)
        self._regenerate.bind("<Button-1>", self._put_password)

    def _display_copy_button(self):
        self._copy.pack(anchor=tk.W)
        self._copy.bind("<Button-1>", self._copy_password)

    def get(self) -> str:
        """
        Get the text from the entry field.

        Returns:
            str: The text from the entry field.
        """
        return self._entry.get()


# test code
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    root.title("TextEntry Test")
    root.resizable(False, False)

    frame = tk.Frame(root, width=800, height=500)
    frame.pack()

    text_entry = TextEntry(frame, "TextEntry Test")
    text_entry.pack()

    root.mainloop()
