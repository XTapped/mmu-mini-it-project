# import tkinter
from tkinter import * 
# make a class for an png logo called MMULeft aligned to the left of the window with dimensions of 159.43 x 50 and fits perfectly in the window for a course registration system 
class MMULeft:
    def __init__(self):
        window = Tk()
        window.title("MMU Left")
        # create a canvas
        canvas = Canvas(window, width = 159.43, height = 50)
        canvas.pack(pady=40)
        # create a photoimage object
        image1 = PhotoImage(file = "mmu.png")
        # create a label in the canvas
        canvas.create_image(80, 25, image = image1)
        # run the mainloop
        window.mainloop()
# call the class
MMULeft()
