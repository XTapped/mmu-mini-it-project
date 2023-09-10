import tkinter as tk
from typing import *


class BackButton(tk.Button):
    """
    A back button that returns to the previous frame when clicked. This class inherits from tk.Button.

    Note: Sometimes, particularly when using ScrollableFrame, the back button may be
    packed into a canvas or internal frame. In this case, current_frame is not the same as root
    and must be specified. If current_frame is not specified, it is assumed to be root. Thus,
    pressing the back button will destory root but will not destroy the outer frame.
    This may not be the desired behaviour.

    Args:
        root (Tk): The root window.
        back_frame (Frame): The frame to return to when the button is clicked.
        current_frame (Frame, optional kwargs): The frame that the button is currently in. This may be the same as root. If it is, ignore this argument. Defaults to root.
    """

    def __init__(self, root: tk.Tk, back_frame: tk.Frame, **kwargs) -> None:
        self._img = tk.PhotoImage(file="assets/backarrow.png")
        self._back_frame = back_frame
        self._current_frame = kwargs.get("current_frame", root)

        super().__init__(root, image=self._img, command=self._back, borderwidth=0)

    def _back(self):
        self._current_frame.pack_forget()
        self._back_frame.pack()

    def pack(self, **kwargs):
        super().pack(**kwargs)
        self.place(x=48, y=30)

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.place(x=48, y=30)


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x500")
#     root.title("BackButton Test")
#     root.resizable(False, False)

#     frame1 = tk.Frame(root, width=800, height=500, bg="red")
#     frame1.pack()
#     front_button = tk.Button(
#         frame1, text="Front", command=lambda: [frame1.pack_forget(), frame2.pack()]
#     )
#     front_button.pack()

#     frame2 = tk.Frame(root, width=800, height=500, bg="blue")
#     back_button = BackButton(frame2, frame1)
#     back_button.pack()

#     root.mainloop()
