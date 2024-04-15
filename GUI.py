import tkinter as tk

class Gui:
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        # self.root.geometry("300x300")
        
        
    def app_title(self, title):
        self.root.title(title)

    def make_input_Field(self, row, col):
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=col, padx=15, pady=5)
        return entry

    def make_button(self, text, func, row, col):
        button = tk.Button(self.root, text=text, command=func)
        button.grid(row=row, column=col, padx=15, pady=5)
        return button

    def make_label(self, text, row, col):
        str_var = tk.StringVar(self.root, text)
        label = tk.Label(self.root, textvariable=str_var)
        label.grid(row=row, column=col)
        return [label, str_var]  # Return both label and its associated StringVar

    def run(self):
        self.root.mainloop()
