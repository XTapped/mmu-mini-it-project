import tkinter as tk

from modules.BackButton import BackButton
from modules.WhiteButton import WhiteButton
from modules.MMULeft import MMULeft
from modules.Heading import Heading


root = tk.Tk()
root.title("Student Course Action")
root.geometry("800x500")
root.resizable(False, False)


back_button = BackButton(root, None)
back_button.pack()
back_button.place(x=48, y=40)

mmu_left = MMULeft(root)
mmu_left.pack()


heading3 = Heading(root, "Course Actions", 3)
heading3.pack()
heading3.place(x=40, y=149)

create_course = WhiteButton(root, "Create Course", None, 17)
create_course.pack(anchor="nw")
create_course.place(x=48, y=200)

Update_Delete_course = WhiteButton(root, "Update/Delete Course", None, 17)
Update_Delete_course.pack()
Update_Delete_course.place(x=48, y=250)


root.mainloop()