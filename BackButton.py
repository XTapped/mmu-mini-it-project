from tkinter import *


class BackButton:
    def __init__(self, root, back_frame):
        self._back_frame = back_frame
        self._root = root
        self._img = PhotoImage(file="assets/backarrow.png")
        self._button = Button(root, image=self._img, command=self.back, borderwidth=0)

    def pack(self):
        self._button.pack()
        self._button.place(x=5, y=10)

    def back(self):
        self._button.pack_forget()
        self._root.pack_forget()
        self._back_frame.pack()
