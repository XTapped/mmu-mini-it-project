import tkinter as tk
from tkinter import ttk
from typing import *


class DropDown(tk.Frame):
    """
    Default dropdown menu used in the program. You should use get() to fetch the selected value. This class inherits from tk.Frame.

    Args:
        root (Tk): The root window of the program.
        values (List[str]): The values to be displayed in the dropdown menu.
        label (bool, optional): Whether the dropdown menu should have a label. Defaults to False.
        label_text (str, optional): The text to be displayed on the label. Defaults to "Label".
        width (int, optional): The width of the dropdown menu. Defaults to 20.
    """

    def __init__(
        self,
        root: tk.Tk,
        values: List[str],
        label: bool = False,
        label_text: str = "Label",
        width: int = 20,
    ):
        super().__init__(root)

        self._label = tk.Label(self, text=label_text, font=("Inter", 16))
        self._combobox = ttk.Combobox(
            self,
            background="#D9D9D9",
            font=("Inter", 16),
            width=width,
            values=values,
            state="readonly",
        )

        if label:
            self._label.pack(anchor=tk.W, side=tk.TOP)

        self._combobox.pack()
        self._combobox.current(0)

    def get(self) -> str:
        """
        Get the selected value from the dropdown menu.

        Returns:
            str: The selected value from the dropdown menu.
        """
        return self._combobox.get()


# # test code
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x500")
#     root.title("DropDown Test")
#     root.resizable(False, False)

#     frame = tk.Frame(root, width=800, height=500)
#     frame.pack()

#     drop_down = DropDown(frame, ["Option 1", "Option 2", "Option 3"], True)
#     drop_down.pack()

#     # test get()
#     button = tk.Button(
#         frame,
#         text="Get",
#         font=("Inter", 16),
#         command=lambda: print(drop_down.get()),
#     )
#     button.pack()

#     root.mainloop()
