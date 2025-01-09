import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate():
    try:
        capacitance = (
            float(entry_capacitance.get()) if entry_capacitance.get() else None
        )
        initial_voltage = (
            float(entry_initial_voltage.get()) if entry_initial_voltage.get() else None
        )
        final_voltage = (
            float(entry_final_voltage.get()) if entry_final_voltage.get() else None
        )
        energy_retrieved = (
            float(entry_energy_retrieved.get())
            if entry_energy_retrieved.get()
            else None
        )

        if selected_calculation.get() == "Energy Retrieved = 0.5 * C * (Vi^2 - Vf^2)":
            if capacitance is None or initial_voltage is None or final_voltage is None:
                raise ValueError(
                    "Please enter capacitance, initial voltage, and final voltage."
                )
            if capacitance <= 0 or initial_voltage < 0 or final_voltage < 0:
                raise ValueError(
                    "Capacitance must be positive, and voltages must be non-negative."
                )
            initial_energy = 0.5 * capacitance * (initial_voltage**2)
            final_energy = 0.5 * capacitance * (final_voltage**2)
            energy_retrieved = initial_energy - final_energy
            messagebox.showinfo(
                "Energy Retrieved",
                f"The energy retrieved from the capacitor is {energy_retrieved:.2f} joules",
            )

        elif selected_calculation.get() == "Initial Voltage = sqrt((2 * E / C) + Vf^2)":
            if capacitance is None or final_voltage is None or energy_retrieved is None:
                raise ValueError(
                    "Please enter capacitance, final voltage, and energy retrieved."
                )
            if capacitance <= 0 or final_voltage < 0 or energy_retrieved < 0:
                raise ValueError(
                    "Capacitance must be positive, and voltages and energy must be non-negative."
                )
            initial_voltage = (
                (2 * energy_retrieved / capacitance) + (final_voltage**2)
            ) ** 0.5
            messagebox.showinfo(
                "Initial Voltage", f"The initial voltage is {initial_voltage:.2f} volts"
            )

        elif selected_calculation.get() == "Final Voltage = sqrt(Vi^2 - (2 * E / C))":
            if (
                capacitance is None
                or initial_voltage is None
                or energy_retrieved is None
            ):
                raise ValueError(
                    "Please enter capacitance, initial voltage, and energy retrieved."
                )
            if capacitance <= 0 or initial_voltage < 0 or energy_retrieved < 0:
                raise ValueError(
                    "Capacitance must be positive, and voltages and energy must be non-negative."
                )
            final_voltage = (
                (initial_voltage**2) - (2 * energy_retrieved / capacitance)
            ) ** 0.5
            messagebox.showinfo(
                "Final Voltage", f"The final voltage is {final_voltage:.2f} volts"
            )

        elif selected_calculation.get() == "Capacitance = 2 * E / (Vi^2 - Vf^2)":
            if (
                initial_voltage is None
                or final_voltage is None
                or energy_retrieved is None
            ):
                raise ValueError(
                    "Please enter initial voltage, final voltage, and energy retrieved."
                )
            if initial_voltage < 0 or final_voltage < 0 or energy_retrieved < 0:
                raise ValueError("Voltages and energy must be non-negative.")
            capacitance = (2 * energy_retrieved) / (
                (initial_voltage**2) - (final_voltage**2)
            )
            messagebox.showinfo(
                "Capacitance", f"The capacitance is {capacitance:.2f} farads"
            )

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


def clear_fields():
    entry_capacitance.delete(0, tk.END)
    entry_initial_voltage.delete(0, tk.END)
    entry_final_voltage.delete(0, tk.END)
    entry_energy_retrieved.delete(0, tk.END)


def update_fields(event):
    clear_fields()
    for widget in frame_inputs.winfo_children():
        widget.grid_remove()

    calculation = selected_calculation.get()

    if calculation == "Energy Retrieved = 0.5 * C * (Vi^2 - Vf^2)":
        tk.Label(frame_inputs, text="Capacitance (F):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_capacitance.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Initial Voltage (V):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_initial_voltage.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Final Voltage (V):").grid(
            row=2, column=0, padx=10, pady=5
        )
        entry_final_voltage.grid(row=2, column=1, padx=10, pady=5)
    elif calculation == "Initial Voltage = sqrt((2 * E / C) + Vf^2)":
        tk.Label(frame_inputs, text="Capacitance (F):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_capacitance.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Final Voltage (V):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_final_voltage.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Energy Retrieved (J):").grid(
            row=2, column=0, padx=10, pady=5
        )
        entry_energy_retrieved.grid(row=2, column=1, padx=10, pady=5)
    elif calculation == "Final Voltage = sqrt(Vi^2 - (2 * E / C))":
        tk.Label(frame_inputs, text="Capacitance (F):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_capacitance.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Initial Voltage (V):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_initial_voltage.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Energy Retrieved (J):").grid(
            row=2, column=0, padx=10, pady=5
        )
        entry_energy_retrieved.grid(row=2, column=1, padx=10, pady=5)
    elif calculation == "Capacitance = 2 * E / (Vi^2 - Vf^2)":
        tk.Label(frame_inputs, text="Initial Voltage (V):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_initial_voltage.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Final Voltage (V):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_final_voltage.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Energy Retrieved (J):").grid(
            row=2, column=0, padx=10, pady=5
        )
        entry_energy_retrieved.grid(row=2, column=1, padx=10, pady=5)


def create_cap_energy_tab(notebook):
    frame_cap_energy = ttk.Frame(notebook)
    notebook.add(frame_cap_energy, text="Capacitor Energy")

    # Dropdown for selecting the equation
    tk.Label(frame_cap_energy, text="Select Calculation:").grid(
        row=0, column=0, padx=10, pady=5
    )
    global selected_calculation
    selected_calculation = tk.StringVar()
    dropdown = ttk.Combobox(
        frame_cap_energy, textvariable=selected_calculation, width=40
    )
    dropdown["values"] = (
        "Energy Retrieved = 0.5 * C * (Vi^2 - Vf^2)",
        "Initial Voltage = sqrt((2 * E / C) + Vf^2)",
        "Final Voltage = sqrt(Vi^2 - (2 * E / C))",
        "Capacitance = 2 * E / (Vi^2 - Vf^2)",
    )
    dropdown.grid(row=0, column=1, padx=10, pady=5)
    dropdown.set("Select Calculation")
    dropdown.bind("<<ComboboxSelected>>", update_fields)

    # Frame for dynamic input fields
    global frame_inputs
    frame_inputs = ttk.Frame(frame_cap_energy)
    frame_inputs.grid(row=1, column=0, columnspan=2, pady=10)

    # Input fields (initially hidden)
    global \
        entry_capacitance, \
        entry_initial_voltage, \
        entry_final_voltage, \
        entry_energy_retrieved
    entry_capacitance = tk.Entry(frame_inputs)
    entry_initial_voltage = tk.Entry(frame_inputs)
    entry_final_voltage = tk.Entry(frame_inputs)
    entry_energy_retrieved = tk.Entry(frame_inputs)

    # Button for calculation and clear
    btn_calculate = tk.Button(
        frame_cap_energy, text="Calculate", command=calculate, bg="green", fg="white"
    )
    btn_calculate.grid(row=2, column=0, padx=10, pady=10)

    btn_clear = tk.Button(frame_cap_energy, text="Clear", command=clear_fields)
    btn_clear.grid(row=2, column=1, padx=10, pady=10)
