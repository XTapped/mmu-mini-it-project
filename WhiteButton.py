from tkinter import *

root = Tk()
#Create class for whitebutton
class WhiteButton:
    def __init__(self,root,label,size):
        self.myFrame = Frame(root)
        self.myFrame.pack()

        #Button Border Atribuites
        self.button_frame = Frame(root, 
                                 bg="black", 
                                 highlightbackground="black", 
                                 highlightcolor="black", 
                                 highlightthickness=1)
        
        self.button_frame.pack(padx=10, pady=10)


        #Atribuites of button
        self.white_button = Button(self.button_frame,
                                  text=label, 
                                  font="inter",
                                  command=self.clicker, 
                                  bg="white",
                                  width=size,
                                  borderwidth=0,
                                  fg="black", 
                                  relief="flat")

        self.white_button.pack()
        
    def clicker(self): 
        pass


#Specifying what text and size should be the button
wb = WhiteButton(root,"TEXT","10")
root.mainloop()