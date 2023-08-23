from tkinter import *


class BackButton:
    def __init__(self, root):
        self.my_img = PhotoImage(file="backarrow.png")

        self.my_button = Button(
            root, image=self.my_img, command=self.clicker, borderwidth=0
        )

    def pack(self):
        self.my_button.pack()
        self.my_button.place(x=5, y=10)

    def clicker(self):
        pass
