import tkinter as tk
from typing import *


class Heading(tk.Label):
    """
    Default heading used in the program. This class inherits from tk.Label.

    Args:
        root (Tk): The root window of the program.
        text (str): The text to be displayed on the label.
        heading (Literal[1, 2, 3, 4, 5, 6, 7]): The heading level of the label.
        color (str, optional): The color of the text as a hex code. Defaults to "#000000" (black).
    """

    def __init__(
        self,
        root: tk.Tk,
        text: str,
        heading: Literal[1, 2, 3, 4, 5, 6, 7],
        color: str = "#000000",
    ):
        self._headings = {
            1: ("Inter 40 bold"),
            2: ("Inter 32 bold"),
            3: ("Inter 24 bold"),
            4: ("Inter 20 bold"),
            5: ("Inter 16"),
            6: ("Inter 14"),
            7: ("Inter 13 underline"),
        }

        super().__init__(
            root,
            text=text,
            font=self._headings[heading],
            fg=color,
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.config(bg="#FFFFFF")

    heading = Heading(root, "Heading", 5, "#4F4F4F")
    heading.pack()

    root.mainloop()
