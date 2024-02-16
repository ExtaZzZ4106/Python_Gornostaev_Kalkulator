import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Простой Калькулятор")

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self.master, textvariable=self.entry_var, font=('Arial', 14), justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, font=('Arial', 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        clear_button = tk.Button(self.master, text='C', font=('Arial', 14), command=self.clear_entry)
        clear_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        # Configure grid row and column weights
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        current_text = self.entry_var.get()

        if value == '=':
            try:
                result = str(eval(current_text))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set('Ошибка')
        else:
            self.entry_var.set(current_text + value)

    def clear_entry(self):
        self.entry_var.set('')


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
