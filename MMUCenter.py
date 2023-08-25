import tkinter as tk
from typing import *


class MMUCenter(tk.Canvas):
    """
    A picture of the MMU logo centered in the middle of the screen. This class inherits from tk.Canvas.

    Args:
        root (Tk): The root window.
    """

    def __init__(self, root: tk.Tk):
        self._image = tk.PhotoImage(file="assets/mmu.png")
        self._padding = 40
        super().__init__(root, width=self._image.width(), height=self._image.height())

        self.create_image(
            self._image.width() / 2, self._image.height() / 2, image=self._image
        )

    def pack(self):
        super().pack(pady=self._padding)
