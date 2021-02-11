# Laura Maree

import tkinter as tk
import tkinter.font as tkFont
from gui import *

class Popup:
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root



def main():
    """Main function for http_server.py."""
    root = tk.Tk()
    app = Content_Generator(root)
    app.mainloop()

if __name__ == '__main__':
    main()