import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from typing import *


class ScrollableFrame(ttk.Frame):
    """
    A frame that can be scrolled vertically. This class inherits from ttk.Frame.
    You should use this frame when your page has a lot of content that cannot fit in the window.

    You should inherit this class and use self.interior to add widgets to the frame.
    If you find that some stuff is being cut off, try increasing the height of the frame.

    Args:
        root (Tk): The root window.
        title (str, optional): The title of the window. Defaults to "MMU Mini IT Project".
        height (int, optional): The height of the frame. Defaults to 500.
    """

    def __init__(
        self,
        root: tk.Tk,
        title: str = "MMU Mini IT Project",
        height: int = 500,
        *args,
        **kwargs
    ):
        ttk.Frame.__init__(self, root, *args, **kwargs)
        root.title(title)
        root.geometry("800x500")
        root.resizable(False, False)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = tk.Canvas(
            self,
            bd=0,
            highlightthickness=0,
            width=200,
            height=300,
            yscrollcommand=vscrollbar.set,
        )
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=self.canvas.yview)

        # Reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = ttk.Frame(self.canvas, width=800, height=height)
        self.interior.bind("<Configure>", self._configure_interior)
        self.canvas.bind("<Configure>", self._configure_canvas)
        self.interior_id = self.canvas.create_window(
            0, 0, window=self.interior, anchor=NW
        )

        self.pack(fill=BOTH, expand=TRUE)

    def _configure_interior(self, event):
        # Update the scrollbars to match the size of the inner frame.
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion=(0, 0, size[0], size[1]))
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the canvas's width to fit the inner frame.
            self.canvas.config(width=self.interior.winfo_reqwidth())

    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())
