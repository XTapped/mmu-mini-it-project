from tkinter import *


class BackButton:
    def __init__(self, root):
        self.img = PhotoImage(file="backarrow.png")
        self.button = Button(root, image=self.img, command=self.back, borderwidth=0)

    def pack(self):
        self.button.pack()
        self.button.place(x=5, y=10)

    def back(self):
        pass
