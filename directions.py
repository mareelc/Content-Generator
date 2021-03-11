# Laura Maree
# directions.py
# 2.28.2021


class Directions(tk.Frame):
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