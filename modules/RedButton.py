import tkinter as tk
from typing import *


class RedButton(tk.Frame):
    """
    A red button with white text. This class extends tk.Frame()

    Args:
        root (Tk): The root window.
        text (str): The text to display on the button.
        command (Optional[Callable], optional): The function to call when the button is clicked. Defaults to None.
        width (int, optional): The width of the button. Defaults to 10.
        height (int, optional): The height of the button. Defaults to 1.
        anchor (Literal["n", "ne", "e", "se", "s", "sw", "w", "nw", "center"], optional): The alignment of the text in the button. Defaults to "center".
    """

    def __init__(
        self,
        root: tk.Tk,
        text: str,
        command: Optional[Callable] = None,
        width: int = 10,
        height: int = 1,
        anchor: Literal[
            "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"
        ] = "center",
    ):
        super().__init__(
            root,
            bg="black",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )

        self.red_button = tk.Button(
            self,
            text=text,
            font="inter",
            command=command,
            bg="red",
            fg="white",
            width=width,
            borderwidth=0,
            relief="flat",
            activebackground="red",
            activeforeground="black",
            height=height,
            anchor=anchor,
        )

        self.red_button.pack()
