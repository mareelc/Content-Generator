# Laura Maree

import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()

root.title(" Content Generator ")
root.geometry("440x600")
root.configure(bg="grey95")

fontStyle = tkFont.Font(size=40)
fontStyle2 = tkFont.Font(size=20)
labelExample = tk.Label(root, text="Content Generator", font=fontStyle, fg="white", bg="grey")
labelExample.grid(columnspan=4)
tk.Label(root, text=" ").grid(row=1)

instructionLabel = tk.Label(root, text="Directions: ", font=fontStyle2)
instructionLabel.grid(columnspan=2)
words = "Generate a paragraph of text from Wikipedia \n" \
        "by entering two keywords below and" \
        "\n clicking the Generate " \
        "button. Paragraph\n " \
        "will appear at the bottom of this \n" \
        "page and will include both keywords. \n" \
        "Results will be saved to paragraph.csv."
text = tk.Label(root, text=words)
text.grid(columnspan=4)

tk.Label(root, text=" ").grid(row=4)
tk.Label(root, text="Keyword 1").grid(row=5, column=1)
keyword1 = tk.Entry(root).grid(row=5, column=2)
tk.Label(root, text="Keyword 2").grid(row=6, column=1)
keyword2 = tk.Entry(root).grid(row=6, column=2)

tk.Label(root, text=" ").grid(row=7)
button = tk.Button(root, text="Generate")
button.grid(columnspan=4)

paragraphLabel = tk.Label(root, text="Paragraph: ", font=fontStyle2)
paragraphLabel.grid(columnspan=2)

textbox = tk.Text(root, height=13, width=50)
textbox.grid(columnspan=4)
root.mainloop()