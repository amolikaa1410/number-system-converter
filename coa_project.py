import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Conversion Functions ---------- #
def to_binary(n): return bin(n)[2:]
def to_octal(n): return oct(n)[2:]
def to_hex(n): return hex(n)[2:].upper()
def to_bcd(n): return " ".join(format(int(d), "04b") for d in str(n))
def to_excess3(n): return " ".join(format(int(d) + 3, "04b") for d in str(n))
def to_gray(n): return bin(n ^ (n >> 1))[2:]

def convert_number(n, system):
    if system == "Decimal": return str(n)
    elif system == "Binary": return to_binary(n)
    elif system == "Octal": return to_octal(n)
    elif system == "Hexadecimal": return to_hex(n)
    elif system == "BCD": return to_bcd(n)
    elif system == "Excess-3": return to_excess3(n)
    elif system == "Gray": return to_gray(n)
    else: return str(n)

# ---------- Calculator Logic ---------- #
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # evaluate math expression safely
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

def convert():
    try:
        value = int(entry.get())  # only integer conversion supported
        system = combo.get()
        converted = convert_number(value, system)
        result_label.config(text=f"{system}: {converted}")
    except Exception:
        messagebox.showerror("Error", "Please enter a valid integer for conversion")

# ---------- GUI Setup ---------- #
root = tk.Tk()
root.title("Conversion Assisted Calculator")

# Entry Display
entry = tk.Entry(root, width=25, font=("Helvetica", 16), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda val=text: button_click(val)

    tk.Button(root, text=text, width=5, height=2, font=("Helvetica", 14), command=action).grid(row=row, column=col, padx=5, pady=5)

# Conversion Dropdown
combo = ttk.Combobox(root, values=["Decimal", "Binary", "Octal", "Hexadecimal", "BCD", "Excess-3", "Gray"])
combo.current(0)
combo.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Convert Button
tk.Button(root, text="Convert" , width=15 , font=("Helvetica",13) , command=convert).grid(row=5, column=2, columnspan=2,padx = 5, pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=6, column=0, columnspan=4, pady=10)

root.mainloop()
