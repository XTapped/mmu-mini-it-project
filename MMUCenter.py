from tkinter import *


class MMUCenter:
    def __init__(self, frame):
        self.frame = frame
        self.image = PhotoImage(file="assets/mmu.png")
        self.padding = 40

        self.canvas = Canvas(
            self.frame, width=self.image.width(), height=self.image.height()
        )
        self.canvas.create_image(
            self.image.width() / 2, self.image.height() / 2, image=self.image
        )

    def pack(self, **kwargs):
        self.canvas.pack(pady=self.padding, **kwargs)
