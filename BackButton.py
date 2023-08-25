from tkinter import *
from typing import *


class BackButton(Button):
    """
    A back button that returns to the previous frame when clicked. This class inherits from tk.Button.

    Args:
        root (Tk): The root window.
        back_frame (Frame): The frame to return to when the button is clicked.
    """

    def __init__(self, root: Tk, back_frame: Frame) -> None:
        self._img = PhotoImage(file="assets/backarrow.png")
        self._back_frame = back_frame
        super().__init__(root, image=self._img, command=self._back, borderwidth=0)

    def _back(self):
        self.master.pack_forget()
        self._back_frame.pack()

    def pack(self):
        super().pack()
        self.place(x=5, y=10)


# if __name__ == "__main__":
#     root = Tk()
#     root.geometry("800x500")
#     root.title("BackButton Test")
#     root.resizable(False, False)

#     frame1 = Frame(root, width=800, height=500, bg="red")
#     frame1.pack()
#     front_button = Button(
#         frame1, text="Front", command=lambda: [frame1.pack_forget(), frame2.pack()]
#     )
#     front_button.pack()

#     frame2 = Frame(root, width=800, height=500, bg="blue")
#     back_button = BackButton(frame2, frame1)
#     back_button.pack()

#     root.mainloop()
