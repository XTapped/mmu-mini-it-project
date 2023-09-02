from modules import MMUCenter, Heading, TextEntry, PasswordEntry, WhiteButton
import tkinter as tk


class SplashScreen(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        mmu_logo = MMUCenter(self).pack()
        content_frame = tk.Frame(root)
        content_frame.pack()
        content_frame.place(y=150, x=170)
        heading = Heading(content_frame , "Course Registration System", 3).pack(pady=(0,23))
        student_id = TextEntry(content_frame, "Student ID", width=35).pack(pady=(0,23))
        password = PasswordEntry(content_frame, width=35).pack(pady=(0,40)) 
        sign_in_button = WhiteButton(content_frame, "Sign In", None).pack(pady=(0,23))


master = tk.Tk()
master.geometry("800x500")
master.resizable(False, False)
SplashScreen(master).pack()
master.mainloop()
