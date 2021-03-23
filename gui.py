# heinl11
# gui.py
# 3.10.2021

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
        self.title_label = self.title()
        self.user_dir = tk.Label(self.root, text="Generate a paragraph from Wikipedia!")
        self.user_dir.grid(row=3, columnspan=4)
        self.dir_button = tk.Button(self.root, text="Show Directions", command=self.show_directions)
        self.dir_button.grid(row=4, column=1)
        self.key1_input = tk.Entry(self.root)
        self.key2_input = tk.Entry(self.root)
        self.gen_button = tk.Button(self.root, text="Generate", command=self.set_display)
        self.keyword_inputs = self.keyword_input()
        self.textbox = tk.Text(root, height=13, width=47)
        self.textbox.grid(row=3, column=4, columnspan=4, rowspan=6)
        self.clear1 = tk.Button(self.root, text="Clear", command=self.clear_keywords).grid(row=4, column=3)
        self.clear2 = tk.Button(self.root, text="Clear", command=self.clear_textbox).grid(row=2, column=7)

    def title(self):
        """Title and subtitle constructor."""
        labelExample = tk.Label(self.root, text="        Content Generator         ",\
                font=tkFont.Font(size=40), fg="grey95", bg="grey")
        labelExample.grid(columnspan=9)
        tk.Label(self.root, text=" ").grid(row=1)
        tk.Label(self.root, text=" Input: ", font=tkFont.Font(size=20)).grid(row=2, columnspan=2)
        tk.Label(self.root, text="Output: ", font=tkFont.Font(size=20)).grid(row=2, column=3, columnspan=2)

    def show_directions(self):
        """Show directions for user."""
        words = "Generate a paragraph of text from Wikipedia \n" \
                "by entering two keywords below and" \
                "\n clicking the Generate " \
                "button. Paragraph\n " \
                "will appear at the right of this \n" \
                "page and will include both keywords. \n" \
                "Results will be saved to output.csv."
        self.user_dir["text"] = words
        self.dir_button["text"] = "Hide Directions"
        self.dir_button["command"] = self.hide_directions

    def hide_directions(self):
        """Hide directions for user."""
        self.user_dir["text"] = "Generate a paragraph from Wikipedia!"
        self.dir_button["text"] = "Show Directions"
        self.dir_button["command"] = self.show_directions

    def keyword_input(self):
        """Keyword input constructor."""
        tk.Label(self.root, text="Keyword 1").grid(row=5, column=1)
        self.key1_input.grid(row=5, column=2)
        tk.Label(self.root, text="Keyword 2").grid(row=6, column=1)
        self.key2_input.grid(row=6, column=2)
        self.gen_button.grid(row=8, columnspan=4)

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
