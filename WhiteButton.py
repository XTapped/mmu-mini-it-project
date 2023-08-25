from tkinter import *
from typing import *


class WhiteButton(Frame):
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

        self.white_button = Button(
            self,
            text=text,
            font="inter",
            command=command,
            bg="white",
            fg="black",
            width=width,
            borderwidth=0,
            relief="flat",
        )

        self.white_button.pack()
