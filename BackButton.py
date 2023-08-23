from tkinter import *


class BackButton:
    def __init__(self, root, back_frame):
        self.back_frame = back_frame
        self.root = root

        self.img = PhotoImage(file="assets/backarrow.png")
        self.button = Button(root, image=self.img, command=self.back, borderwidth=0)

    def pack(self):
        self.button.pack()
        self.button.place(x=5, y=10)

    def back(self):
        self.button.pack_forget()
        self.root.pack_forget()
        self.back_frame.pack()
