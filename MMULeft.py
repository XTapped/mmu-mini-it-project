from tkinter import *


class MMULeft:
    def __init__(self, frame):
        self._frame = frame
        self._image = PhotoImage(file="assets/mmuleft.png")
        self._padding = 40

        self._canvas = Canvas(
            self._frame, width=self._image.width(), height=self._image.height()
        )
        self._canvas.create_image(
            self._image.width() / 2, self._image.height() / 2, image=self._image
        )

    def pack(self, **kwargs):
        self._canvas.pack(pady=self._padding, **kwargs)
        self._canvas.place(x=48, y=80)
