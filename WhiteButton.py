from tkinter import *

root = Tk()


class WhiteButton(Frame):
    def __init__(self, root, text, width=10):
        super().__init__(
            root,
            bg="black",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )

        self.white_button = Button(
            self,
            text=text,
            font="inter",
            command=self.command,
            bg="white",
            fg="black",
            width=width,
            borderwidth=0,
            relief="flat",
        )

        self.white_button.pack()

    def command(self):
        pass


wb = WhiteButton(root, "Hello World!")
wb.pack()
root.mainloop()
