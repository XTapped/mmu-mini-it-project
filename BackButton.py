from tkinter import*
from PIL import ImageTk,Image

root=Tk()
root.title="BackButton"
root.geometry("200x300")

class BackButton:
    def __init__(self,back_button):
        myFrame = Frame(back_button)
        myFrame.pack()
        
        self.my_img = Image.open("backarrow.png")  
         
        self.my_img = ImageTk.PhotoImage(self.my_img)
        self.my_label = Label(image = self.my_img)

        self.my_button = Button(back_button, 
                                image=self.my_img, 
                                command=self.clicker, 
                                borderwidth=0)
        self.my_button.pack()
        self.my_button.place(x=5, y=10)

    def clicker(self):
        pass


back = BackButton(root)

root.mainloop()