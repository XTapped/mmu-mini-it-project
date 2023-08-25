from tkinter import *
from typing import *


class RedButton(Frame):
    """
    A red button with white text. This class extends tk.Frame()

    Args:
        root (Tk): The root window.
        text (str): The text to display on the button.
        command (Optional[Callable], optional): The function to call when the button is clicked. Defaults to None.
        width (int, optional): The width of the button. Defaults to 10.
    """

    def __init__(
        self, root: Tk, text: str, command: Optional[Callable] = None, width: int = 10
    ):
        super().__init__(
            root,
            bg="black",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )

        self.red_button = Button(
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
        )

        self.red_button.pack()
