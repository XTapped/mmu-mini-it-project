from typing import *
import tkinter as tk


class PasswordEntry(tk.Frame):
    """
    Default password entry field used in the program. You should use get() to fetch text typed into the entry. This class inherits from tk.Frame.

    Args:
        root (Tk): The root window of the program.
        width (int, optional): The width of the entry field. Defaults to 20.
    """

    def __init__(self, root: tk.Tk, width: int = 20):
        super().__init__(root)

        self._label = tk.Label(self, text="Password", font=("Inter", 16))
        self._entry = tk.Entry(
            self,
            bg="#D9D9D9",
            font=("Inter", 16),
            bd=1,
            highlightthickness=1,
            highlightbackground="black",
            relief=tk.FLAT,
            width=width,
            show="•",
        )

        self._label.pack(anchor=tk.W, side=tk.TOP)
        self._entry.pack()

    def get(self) -> str:
        """
        Get the password from the entry field.

        Returns:
            str: The password from the entry field.
        """
        return self._entry.get()


# test code
# if __name__ == "__main__":
#     root = Tk()
#     root.geometry("800x500")
#     root.title("PasswordEntry Test")
#     root.resizable(False, False)

#     frame = Frame(root, width=800, height=500)
#     frame.pack()

#     password_entry = PasswordEntry(frame)
#     password_entry.pack()

#     root.mainloop()
