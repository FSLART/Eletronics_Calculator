import tkinter as tk
from tkinter import messagebox


def calculate_ohms_law(entry_voltage, entry_current, entry_resistance, label_result):
    try:
        voltage = float(entry_voltage.get()) if entry_voltage.get() else None
        current = float(entry_current.get()) if entry_current.get() else None
        resistance = float(entry_resistance.get()) if entry_resistance.get() else None

        if voltage is None:
            result = current * resistance
            label_result.config(text=f"Voltage: {result:.2f} V")
        elif current is None:
            result = voltage / resistance
            label_result.config(text=f"Current: {result:.2f} A")
        elif resistance is None:
            result = voltage / current
            label_result.config(text=f"Resistance: {result:.2f} Ω")
        else:
            label_result.config(text="Leave one field empty to calculate.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def create_ohms_window():
    # ohms_law_window = tk.Frame(notebook) #this creates a tab need to add 'notebook' as a parameter of this function
    # notebook.add(ohms_law_window, text="Ohm's Law")
    ohms_law_window = tk.Toplevel()
    ohms_law_window.title("Ohm's Law")
    ohms_law_window.geometry("400x300")

    tk.Label(ohms_law_window, text="Voltage (V):").grid(row=0, column=0, padx=10, pady=5)
    entry_voltage = tk.Entry(ohms_law_window)
    entry_voltage.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ohms_law_window, text="Current (A):").grid(row=1, column=0, padx=10, pady=5)
    entry_current = tk.Entry(ohms_law_window)
    entry_current.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ohms_law_window, text="Resistance (Ω):").grid(row=2, column=0, padx=10, pady=5)
    entry_resistance = tk.Entry(ohms_law_window)
    entry_resistance.grid(row=2, column=1, padx=10, pady=5)

    label_result = tk.Label(ohms_law_window, text="Result will appear here.")
    label_result.grid(row=4, column=0, columnspan=2, pady=10)

    btn_calculate = tk.Button(
        ohms_law_window,
        text="Calculate",
        command=lambda: calculate_ohms_law(
            entry_voltage, entry_current, entry_resistance, label_result
        ),
        bg="green",
        fg="white",
    )
    btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)
