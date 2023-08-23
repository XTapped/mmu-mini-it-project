from tkinter import *

root = Tk()
root.title = "BackButton"
root.geometry("200x300")


class BackButton:
    def __init__(self, back_button):
        self.my_img = PhotoImage(file="backarrow.png")

        self.my_button = Button(
            back_button, image=self.my_img, command=self.clicker, borderwidth=0
        )

    def pack(self):
        self.my_button.pack()
        self.my_button.place(x=5, y=10)

    def clicker(self):
        pass


back = BackButton(root)

root.mainloop()
