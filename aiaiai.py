import tkinter as tk

def evaluate (event) :
    result_label.config(text=str(eval(entry.get())))

    root = tk.TK()
    root.title("calculadora")

    entry = tk.Entry(root)
    entry.bind("<return>", evaluate)
    entry.pack()

    result_label = tk.Label (root, text="")
    result_label.pack()

    root.geometry("250x100")
    root.mainloop()
