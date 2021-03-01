# Laura Maree
# gui.py
# 2.28.2021

import tkinter as tk
import tkinter.font as tkFont
from verify_search import *
from read_write import *
from popups import *

class GUI(tk.Frame):
    """Class for Content Generator GUI main window."""
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.title_label = self.title(self.root)
        self.user_dir = self.directions(self.root)
        self.key1_input = tk.Entry(self.root)
        self.key2_input = tk.Entry(self.root)
        self.button = tk.Button(self.root, text="Generate", command=self.set_display)
        self.keyword_inputs = self.keyword_input(self.root)
        self.para_label = self.paragraph(self.root)
        self.textbox = tk.Text(root, height=13, width=47)
        self.textbox.grid(row=3, column=4, columnspan=4, rowspan=6)
        self.clear1 = tk.Button(self.root, text="Clear", command=self.clear_keywords).grid(row=4, column=3)
        self.clear2 = tk.Button(self.root, text="Clear", command=self.clear_textbox).grid(row=2, column=7)

    def title(self, root):
        """Title constructor."""
        fontStyle = tkFont.Font(size=40)
        labelExample = tk.Label(root, text="        Content Generator         ",\
                font=fontStyle, fg="grey95", bg="grey")
        labelExample.grid(columnspan=9)
        tk.Label(root, text=" ").grid(row=1)

    def directions(self, root):
        """Directions constructor."""
        fontStyle2 = tkFont.Font(size=20)
        tk.Label(root, text=" Input: ", font=fontStyle2).grid(row=2, columnspan=2)
        words = "Generate a paragraph of text from Wikipedia \n" \
                "by entering two keywords below and" \
                "\n clicking the Generate " \
                "button. Paragraph\n " \
                "will appear at the right of this \n" \
                "page and will include both keywords. \n" \
                "Results will be saved to output.csv."
        tk.Label(root, text=words).grid(columnspan=4)

    def keyword_input(self, root):
        """Keyword input constructor."""
        tk.Label(root, text="Keyword 1").grid(row=5, column=1)
        self.key1_input.grid(row=5, column=2)
        tk.Label(root, text="Keyword 2").grid(row=6, column=1)
        self.key2_input.grid(row=6, column=2)
        self.button.grid(row=8, columnspan=4)

    def paragraph(self, root):
        """Paragraph output constructor."""
        fontStyle2 = tkFont.Font(size=20)
        tk.Label(root, text="Output: ", font=fontStyle2).grid(row=2, column=3, columnspan=2)

    def set_display(self):
        """Clear textbox and call to wiki for results."""
        self.clear_textbox()
        results = verify_keywords(self.key1_input.get(), self.key2_input.get())
        self.check_output(results)

    def check_output(self, results):
        """Determine output (popup error or text) from
        results of article/paragraph search."""
        # Instantiate Popup class for errors in results.
        popup = Popup(self.root)
        if results[0] == "err" or not results[1]:
            return popup.key_err(results[1])
        # Results valid, print paragraph in textbox.
        if results[0]:
            return self.valid_results(results, popup)
        return self.disambig_err(results, popup)

    def valid_results(self, results, popup):
        """Insert valid results into gui textbox and
        write to csv."""
        self.textbox.insert(tk.END, results[1])
        keywords = [self.key1_input.get(), self.key2_input.get()]
        write_csv(keywords, results)
        popup.close()

    def disambig_err(self, results, popup):
        """Handle disambiguation error with popup and
        verify new selection."""
        new = popup.key_disambig(results[1])
        new_results = find_article(new, self.key1_input.get(), self.key2_input.get())
        self.check_output(new_results)

    def clear_keywords(self):
        """Clear keyword inputs."""
        self.key1_input.delete(0, tk.END)
        self.key2_input.delete(0, tk.END)

    def clear_textbox(self):
        """Clear textbox."""
        self.textbox.delete(1.0, tk.END)

def main():
    """Main function for gui.py."""
    root = tk.Tk()
    app = GUI(root)
    root.title("Content Generator")
    root.geometry("685x360")
    root.configure(bg="grey95")
    root.grid_columnconfigure(4, minsize=90)
    app.mainloop()


if __name__ == '__main__':
    main()