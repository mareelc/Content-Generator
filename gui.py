# Laura Maree

import tkinter as tk
import tkinter.font as tkFont
from verify_search import *
from read_write import *
from popups import *

class Content_Generator(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.title_label = self.title(self.root)
        self.user_dir = self.directions(self.root)
        self.key1_input = tk.Entry(self.root)
        self.key2_input = tk.Entry(self.root)
        self.button = tk.Button(self.root, text="Generate", command=self.set_display)
        self.keyword_inputs = self.keyword_input(self.root, self.key1_input, self.key2_input, self.button)
        self.para_label = self.paragraph(self.root)
        self.textbox = tk.Text(root, height=13, width=47)
        self.textbox.grid(row=3, column=4, columnspan=4, rowspan=6)
        self.clear1 = tk.Button(self.root, text="Clear", command=self.clear_keywords)
        self.clear2 = tk.Button(self.root, text="Clear", command=self.clear_textbox)
        self.clear1.grid(row=4, column=3)
        self.clear2.grid(row=2, column=7)


    def title(self, root):
        fontStyle = tkFont.Font(size=40)
        labelExample = tk.Label(root, text="        Content Generator         ", font=fontStyle, fg="grey95", bg="grey")
        labelExample.grid(columnspan=9)
        tk.Label(root, text=" ").grid(row=1)

    def directions(self, root):
        fontStyle2 = tkFont.Font(size=20)
        directionsLabel = tk.Label(root, text=" Input: ", font=fontStyle2)
        directionsLabel.grid(row=2, columnspan=2)
        words = "Generate a paragraph of text from Wikipedia \n" \
                "by entering two keywords below and" \
                "\n clicking the Generate " \
                "button. Paragraph\n " \
                "will appear at the right of this \n" \
                "page and will include both keywords. \n" \
                "Results will be saved to output.csv."
        text = tk.Label(root, text=words)
        text.grid(columnspan=4)

    def keyword_input(self, root, keyword1, keyword2, button):
        tk.Label(root, text=" ").grid(row=4)
        tk.Label(root, text="Keyword 1").grid(row=5, column=1)
        keyword1.grid(row=5, column=2)
        tk.Label(root, text="Keyword 2").grid(row=6, column=1)
        keyword2.grid(row=6, column=2)
        tk.Label(root, text=" ").grid(row=7)
        button.grid(columnspan=4)

    def paragraph(self, root):
        fontStyle2 = tkFont.Font(size=20)
        tk.Label(root, text=" ").grid(column=4)
        paragraphLabel = tk.Label(root, text="Output: ", font=fontStyle2)
        paragraphLabel.grid(row=2, column=3, columnspan=2)

    def set_display(self):
        popup = Popup(self.root)
        self.clear_textbox()
        results = verify_keywords(self.key1_input.get(), self.key2_input.get())
        if results == "keywords invalid":
            popup.key_err()
            return
        if results == "not found":
            popup.not_found()
            return
        if results[0]:
            self.textbox.insert(tk.END, results[1])
        else:
            popup.key_disambig(results)
            # for x in range(1, len(results[1])):
            #     self.textbox.insert(tk.END, results[1][x])
            #     self.textbox.insert(tk.END, ", \n")
        keywords = [self.key1_input.get(), self.key2_input.get()]
        write_csv(keywords, results)

    def clear_keywords(self):
        self.key1_input.delete(0, tk.END)
        self.key2_input.delete(0, tk.END)

    def clear_textbox(self):
        self.textbox.delete(1.0, tk.END)

def main():
    """Main function for http_server.py."""
    root = tk.Tk()
    app = Content_Generator(root)
    root.title("Content Generator")
    root.geometry("685x360")
    root.configure(bg="grey95")
    root.grid_columnconfigure(4, minsize=90)
    app.mainloop()

if __name__ == '__main__':
    main()