# heinl11
# error.py
# 3.10.2021

import tkinter as tk
from tkinter import ttk

class Popup(tk.Frame):
    """Class for Content Generator GUI Popups."""
    def __init__(self, root):
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        win_x = root_x + 300
        win_y = root_y + 100
        self.top = tk.Toplevel(root)
        self.top.geometry(f"+{win_x}+{win_y}")
        self.top.geometry("225x100")
        self.drop_down = ttk.Combobox(self.top, width=20, textvariable=tk.StringVar())
        self.top.title("Error!")

    def key_err(self, text):
        """Keywords invalid popup constructor."""
        if not text:
            text = "Paragraph with Keyword 1\n and Keyword2 not Found!"
        tk.Label(self.top, text=text).pack()
        tk.Button(self.top, text="Try Again!", command=self.top.destroy).pack()

    def key_disambig(self, results):
        """Disambiguation error popup constructor."""
        tk.Label(self.top, text="Disambiguation Error:\n Choose an Article to \n Redirect to: ").pack()

        # Create drop down box disambig values.
        self.drop_down["values"] = results
        self.drop_down.pack()

        # On click, button call to combo_val to save new article.
        var = tk.StringVar()
        button = tk.Button(self.top, text="Search!", command=lambda: var.set(self.combo_val()))
        button.pack()
        button.wait_variable(var)
        self.close()
        return var.get()

    def combo_val(self):
        """Save selected new variable in drop down on button click."""
        return self.drop_down.get()

    def close(self):
        """Close popup."""
        return self.top.destroy()

