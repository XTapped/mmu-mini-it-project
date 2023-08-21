# import tkinter
from tkinter import * 
class MMUCenter:
    def __init__(self):
        window = Tk()
        window.title("MMU Center")
        # create a canvas
        canvas = Canvas(window, width = 314, height = 98)
        canvas.pack(pady=40)
        # create a photoimage object
        image1 = PhotoImage(file = "mmu.png")
        # create a label in the canvas
        canvas.create_image(160, 49, image = image1)
        # run the mainloop
        window.mainloop()
# call the class
MMUCenter()
#


