# Laura Maree

import tkinter as tk
from tkinter import ttk

class Popup(tk.Frame):
    def __init__(self, root):
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        win_x = root_x + 300
        win_y = root_y + 100
        self.top = tk.Toplevel(root)
        self.top.geometry(f'+{win_x}+{win_y}')
        self.top.geometry("225x100")
        self.drop_down = ttk.Combobox(self.top, width=20, textvariable=tk.StringVar())
        self.top.title("Error!")
        self.new_key = ""

    def key_err(self):
        title = tk.Label(self.top, text="Invalid Keywords!\n Try Again!")
        title.pack()
        button = tk.Button(self.top, text="Try Again!", command=self.top.destroy)
        button.pack()

    def not_found(self):
        title = tk.Label(self.top, text="Article Not Found!")
        title.pack()
        button = tk.Button(self.top, text="Try Again!", command=self.top.destroy)
        button.pack()

    def para_not_found(self):
        title = tk.Label(self.top, text="Paragraph with Keyword 1\n and Keyword2 not Found!")
        title.pack()
        button = tk.Button(self.top, text="Try Again!", command=self.top.destroy)
        button.pack()

    def key_disambig(self, results):
        title = tk.Label(self.top, text="Disambiguation Error:\n Choose an Article to \n Redirect to: ")
        title.pack()
        self.drop_down['values'] = results
        self.drop_down.pack()
        var = tk.StringVar()
        button = tk.Button(self.top, text="Search!", command=lambda: var.set(self.combo_val()))
        button.pack()
        button.wait_variable(var)
        self.close()
        return var.get()

    def combo_val(self):
        self.new_key = self.drop_down.get()
        return self.new_key

    def close(self):
        self.top.destroy()
        return
