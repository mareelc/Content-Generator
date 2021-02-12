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

    def key_disambig(self, results):
        title = tk.Label(self.top, text="Disambiguation Error:\n Choose an Article to \n Redirect to: ")
        title.pack()
        self.drop_down['values'] = results[1]
        self.drop_down.pack()
        button = tk.Button(self.top, text="Search!", command=self.top.destroy)
        button.pack()
        return
