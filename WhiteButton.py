from tkinter import *

root = Tk()


class WhiteButton:
    def __init__(self, root, text, width, x_pos, y_pos):
        self.button_frame = Frame(
            root,
            bg="black",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )

        self.white_button = Button(
            self.button_frame,
            text=text,
            font="inter",
            command=self.clicker,
            bg="white",
            fg="black",
            width=width,
            borderwidth=0,
            relief="flat",
        )

        self.white_button.pack()
        self.button_frame.place(x=x_pos, y=y_pos)

    def clicker(self):
        pass


wb = WhiteButton(root, "TEXT", "10", x_pos=3, y_pos=5)
root.mainloop()
