import tkinter as tk
from typing import *


class LongEntry(tk.Frame):
    """
    Default long entry field used in the program. You should use get() to fetch text typed into the entry. This class inherits from tk.Frame.

    The difference between this and TextEntry is that you can have multiple lines of text in this entry field.

    Args:
        root (Tk): The root window of the program.
        label_text (str): The text to be displayed on the label.
        width (int, optional): The width of the entry field. Defaults to 20.
        height (int, optional): The height of the entry field. Defaults to 10.
    """

    def __init__(self, root: tk.Tk, label_text: str, width: int = 20, height: int = 10):
        super().__init__(root)

        self._label = tk.Label(self, text=label_text, font=("Inter", 16))
        self._entry = tk.Text(
            self,
            bg="#D9D9D9",
            font=("Inter", 16),
            bd=1,
            highlightthickness=1,
            highlightbackground="black",
            relief=tk.FLAT,
            width=width,
            height=height,
        )

        self._label.pack(anchor=tk.W, side=tk.TOP)
        self._entry.pack()

    def get(self) -> str:
        """
        Get the text from the entry field.

        Returns:
            str: The text from the entry field.
        """
        return self._entry.get("1.0", tk.END)


# test code
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x500")
#     root.title("LongEntry Test")
#     root.resizable(False, False)

#     frame = tk.Frame(root, width=800, height=500)
#     frame.pack()

#     long_entry = LongEntry(frame, "Long Entry")
#     long_entry.pack()

#     def test_get():
#         print(long_entry.get())

#     button = tk.Button(frame, text="Get", command=test_get)
#     button.pack()

#     root.mainloop()
