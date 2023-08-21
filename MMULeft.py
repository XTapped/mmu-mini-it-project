# import tkinter
from tkinter import * 
class MMULeft:
    def __init__(self):
        window = Tk()
        window.title("MMU Center")
        # create a canvas
        canvas = Canvas(window, width = 800, height = 500)
        canvas.pack(padx=48 ,pady=80)
        canvas.place(x=-30, y=48)
        # create a photoimage object
        image1 = PhotoImage(file = "mmuleft.png")
        # create a label in the canvas
        canvas.create_image(160, 49, image = image1)
        # run the mainloop
        window.mainloop()
# call the class
MMULeft()