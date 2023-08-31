import tkinter as tk
from typing import *


class Page(tk.Frame):
    """
    When coding a page, you should always inherit from this class. This class inherits from tk.Frame.
    This class is used to create a scrollable page.
    Note: Make sure to call this class' construtor when inheriting. If not, the page will not be scrollable.

    Args:
        root (Tk): The root window of the program.
        title (str, optional): The title of the page. Defaults to "Mini IT Project".
    """

    def __init__(self, root: tk.Tk, title: str = "Mini IT Project", *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        root.title(title)
        root.geometry("800x500")
        root.resizable(False, False)

        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame.bind("<Configure>", self._on_frame_configure)

        self.pack(fill=tk.BOTH, expand=1)

    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    frame = Page(root)
    root.mainloop()
