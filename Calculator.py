import tkinter as tk


def press(key):
    entry_var.set(entry_var.get() + str(key))


def calculate():
    try:
        expr = entry_var.get()
        result = str(eval(expr))
        entry_var.set(result)
    except Exception:
        entry_var.set("Erro")


def clear():
    entry_var.set("")


def backspace():
    entry_var.set(entry_var.get()[:-1])


root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

entry_var = tk.StringVar()


entry = tk.Entry(root, textvariable=entry_var, font=("Consolas", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("←", 5, 0), ("=", 5, 1, 3)  
]

for (text, row, col, *opt) in buttons:
    colspan = opt[0] if opt else 1
    if text == "C":
        action = clear
    elif text == "=":
        action = calculate
    elif text == "←":
        action = backspace
    else:
        action = lambda t=text: press(t)
    
    b = tk.Button(root, text=text, width=5, height=2,
                  font=("Consolas", 18), command=action)
    b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)


for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()
