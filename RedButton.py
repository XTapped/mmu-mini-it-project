from tkinter import *

root = Tk()

#Create class for redbutton
class RedButton:
    def __init__(self,root,label,size,x_pos, y_pos):
       
        #Button Border Atribuites
        self.button_frame = Frame(
            root,  
            bg="black",
            highlightbackground="black", 
            highlightcolor="black", 
            highlightthickness=1
        )
        
        #Atribuites of button
        self.red_button = Button(
            self.button_frame,
            text=label, 
            font="inter",
            command=self.clicker,
            bg="red",
            fg="white",
            width=size,
            borderwidth=0, 
            relief="flat",
            activebackground="red",
            activeforeground="black")

        self.red_button.pack()
        self.button_frame.place(x=x_pos, y=y_pos)
        
    def clicker(self): 
        pass

#Specifying what text size and possition should the button be 
rb = RedButton(root,"TEXT","10", x_pos=3, y_pos=5)
root.mainloop()