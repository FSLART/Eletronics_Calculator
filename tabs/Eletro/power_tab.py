import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_power(
    combo_formula, entry_voltage, entry_current, entry_resistance, label_result
):
    try:

        formula = combo_formula.get()

        if formula == "P = V * I":
            voltage = float(entry_voltage.get())
            current = float(entry_current.get())

            result = voltage * current

            label_result.config(text=f"Power: {result:.2f} W")

        elif formula == "P = I^2 * R":
            current = float(entry_current.get())
            resistance = float(entry_resistance.get())

            result = current**2 * resistance

            label_result.config(text=f"Power: {result:.2f} W")
        elif formula == "P = V^2 / R":
            voltage = float(entry_voltage.get())
            resistance = float(entry_resistance.get())

            result = voltage**2 / resistance

            label_result.config(text=f"Power: {result:.2f} W")
        else:
            label_result.config(text="Please select a formula.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def clear_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)


def update_fields(event, combo_formula, entries):
    selected_formula = combo_formula.get()
    clear_entries(entries)

    if selected_formula == "P = V * I":
        entries[0].config(state="normal")
        entries[1].config(state="normal")
        entries[2].config(state="disabled")
    elif selected_formula == "P = I^2 * R":
        entries[0].config(state="disabled")
        entries[1].config(state="normal")
        entries[2].config(state="normal")
    elif selected_formula == "P = V^2 / R":
        entries[0].config(state="normal")
        entries[1].config(state="disabled")
        entries[2].config(state="normal")


def create_power_window():
    # power_window = tk.Frame(notebook) #this creates a tab need to add 'notebook' as a parameter of this function
    # notebook.add(power_window, text="Power")

    power_window= tk.Toplevel()
    power_window.title("Power Calculator")
    power_window.geometry("400x300")

    tk.Label(power_window, text="Select Formula:").grid(row=0, column=0, padx=10, pady=5)
    equations = ["P = V * I", "P = I^2 * R", "P = V^2 / R"]
    combo_formula = ttk.Combobox(power_window, values=equations)
    combo_formula.set("P = V * I")  # Set a default value from the list
    combo_formula.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(power_window, text="Voltage (V):").grid(row=1, column=0, padx=10, pady=5)
    entry_voltage = tk.Entry(power_window)
    entry_voltage.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(power_window, text="Current (A):").grid(row=2, column=0, padx=10, pady=5)
    entry_current = tk.Entry(power_window)
    entry_current.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(power_window, text="Resistance (Ω):").grid(row=3, column=0, padx=10, pady=5)
    entry_resistance = tk.Entry(power_window)
    entry_resistance.grid(row=3, column=1, padx=10, pady=5)

    label_result = tk.Label(power_window, text="Result will appear here.")
    label_result.grid(row=5, column=0, columnspan=2, pady=10)

    entries = [entry_voltage, entry_current, entry_resistance]
    combo_formula.bind(
        "<<ComboboxSelected>>",
        lambda event: update_fields(event, combo_formula, entries),
    )

    btn_calculate = tk.Button(
        power_window,
        text="Calculate",
        command=lambda: calculate_power(
            combo_formula, entry_voltage, entry_current, entry_resistance, label_result
        ),
        bg="green",
        fg="white",
    )
    btn_calculate.grid(row=4, column=0, columnspan=2, pady=10)

    clear_entries(entries)
