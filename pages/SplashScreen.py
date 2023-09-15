import tkinter as tk
from modules import MMUCenter
from modules import Heading
from modules import TextEntry
from modules import PasswordEntry
from modules import WhiteButton


class SplashScreen(tk.Frame):
    def __init__(self, root, sign_in_cmd):
        super().__init__(root)
        mmu_logo = MMUCenter(self).pack()
        content_frame = tk.Frame(self)
        content_frame.pack()
        # content_frame.place(y=150, x=170)
        heading = Heading(content_frame, "Course Registration System", 3).pack(
            pady=(0, 23)
        )
        self._student_id = TextEntry(content_frame, "Student ID", width=35)
        self._student_id.pack(pady=(0, 23))
        self._password = PasswordEntry(content_frame, width=35)
        self._password.pack(pady=(0, 40))
        sign_in_button = WhiteButton(content_frame, "Sign In", sign_in_cmd).pack(
            pady=(0, 23)
        )

    def get(self):
        return {"student_id": self._student_id.get(), "password": self._password.get()}


if __name__ == "__main__":
    master = tk.Tk()
    master.geometry("800x500")
    master.resizable(False, False)
    SplashScreen(master).pack()
    master.mainloop()
