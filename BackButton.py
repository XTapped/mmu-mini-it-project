from tkinter import *


class BackButton:
    def __init__(self, root):
        self.img = PhotoImage(file="backarrow.png")

        self.my_button = Button(root, image=self.img, command=self.back, borderwidth=0)

    def pack(self):
        self.my_button.pack()
        self.my_button.place(x=5, y=10)

    def back(self):
        pass
