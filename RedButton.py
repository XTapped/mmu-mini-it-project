from tkinter import *

root = Tk()
#Create class for whitebutton
class RedButton:
    def __init__(self,root,label,size):
        self.myFrame = Frame(root)
        self.myFrame.pack()

        #Button Border Atribuites
        self.button_frame = Frame(root,  
                                 highlightbackground="black", 
                                 highlightcolor="black", 
                                 highlightthickness=1)
        
        self.button_frame.pack(padx=10, pady=10)


        #Atribuites of button
        self.red_button = Button(self.button_frame,
                                  text=label, 
                                  font="inter",
                                  bg="red",
                                  fg="white",
                                  width=size,
                                  borderwidth=0, 
                                  relief="flat",
                                  activebackground="red",
                                  activeforeground="white",
                                  command=self.clicker, )

        self.red_button.pack()
        
    def clicker(self): 
        pass

#Specifying what text and size should be the button
rb = RedButton(root,"TEXT","10")
root.mainloop()