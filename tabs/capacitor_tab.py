import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def calculate_capacitor():
    try:
        current = float(entry_current.get()) if entry_current.get() else None
        voltage = float(entry_voltage.get()) if entry_voltage.get() else None
        impedance = entry_impedance.get()
        frequency = float(entry_frequency.get()) if entry_frequency.get() else None
        capacitance = (
            float(entry_capacitance.get()) if entry_capacitance.get() else None
        )

        # Parse impedance as a complex number
        if impedance:
            if "j" in impedance or "+" in impedance or "-" in impedance:
                impedance = complex(impedance.replace(" ", ""))
            else:
                impedance = float(impedance)
                impedance = complex(
                    impedance, 0
                )  # Treat as real with zero imaginary part
        else:
            impedance = None

        selected_equation = combo_equation.get()

        if selected_equation == "C = 1 / (2πfZ)":
            if impedance is None or frequency is None:
                raise ValueError("Please enter impedance and frequency.")
            capacitance = 1 / (2 * np.pi * frequency * abs(impedance))
            label_result_capacitor.config(text=f"Capacitance: {capacitance:.6e} F")
        elif selected_equation == "Z = 1 / (2πfC)":
            if (
                capacitance is None
                or frequency is None
                or capacitance <= 0
                or frequency <= 0
            ):
                raise ValueError("Capacitance and frequency must be positive numbers.")
            # Calculate impedance
            impedance = 1 / (1j * 2 * np.pi * frequency * capacitance)
            label_result_capacitor.config(
                text=f"Impedance: {impedance.real:.2f} + {impedance.imag:.2f}j Ω"
            )
        elif selected_equation == "f = 1 / (2πCZ)":
            if capacitance is None or impedance is None:
                raise ValueError("Please enter capacitance and impedance.")
            frequency = 1 / (2 * np.pi * capacitance * abs(impedance))
            label_result_capacitor.config(text=f"Frequency: {frequency:.2f} Hz")
        elif selected_equation == "Z = V / I":
            if voltage is None or current is None:
                raise ValueError("Please enter voltage and current.")
            impedance = voltage / current
            label_result_capacitor.config(
                text=f"Impedance (from V/I): {impedance:.2f} Ω"
            )
        else:
            label_result_capacitor.config(text="Invalid equation selected.")

        # Show the plot button if capacitance is available
        if capacitance is not None:
            btn_graph_capacitor.grid(row=3, column=0, columnspan=2, pady=10)
        else:
            btn_graph_capacitor.grid_forget()

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero occurred. Check inputs.")


def update_fields(event):
    # Hide all input fields
    for widget in frame_inputs.winfo_children():
        widget.grid_forget()

    selected_equation = combo_equation.get()
    if selected_equation == "C = 1 / (2πfZ)":
        tk.Label(frame_inputs, text="Impedance (Ω):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_impedance.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Frequency (Hz):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_frequency.grid(row=1, column=1, padx=10, pady=5)
    elif selected_equation == "Z = 1 / (2πfC)":
        tk.Label(frame_inputs, text="Frequency (Hz):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_frequency.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Capacitance (F):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_capacitance.grid(row=1, column=1, padx=10, pady=5)
    elif selected_equation == "f = 1 / (2πCZ)":
        tk.Label(frame_inputs, text="Impedance (Ω):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_impedance.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Capacitance (F):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_capacitance.grid(row=1, column=1, padx=10, pady=5)
    elif selected_equation == "Z = V / I":
        tk.Label(frame_inputs, text="Voltage (V):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_voltage.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Current (A):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_current.grid(row=1, column=1, padx=10, pady=5)

    # Hide the plot button initially
    btn_graph_capacitor.grid_forget()


def plot_graph_capacitor():
    try:
        voltage = float(entry_voltage.get())
        capacitance = float(entry_capacitance.get())
        resistance = (
            float(entry_impedance.get().split("+")[0])
            if "+" in entry_impedance.get()
            else None
        )

        if resistance is None or not voltage or not capacitance:
            raise ValueError("Missing required input for plotting.")

        time = np.linspace(0, 5 * capacitance * resistance, 500)
        current = voltage / resistance * np.exp(-time / (resistance * capacitance))

        plt.figure(figsize=(8, 5))
        plt.plot(time, current, label="Current vs Time")
        plt.title("Current Decay in an RC Circuit")
        plt.xlabel("Time (s)")
        plt.ylabel("Current (A)")
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError:
        messagebox.showerror(
            "Input Error", "Ensure voltage, capacitance, and resistance are valid."
        )


def clear_fields():
    entry_current.delete(0, tk.END)
    entry_voltage.delete(0, tk.END)
    entry_impedance.delete(0, tk.END)
    entry_frequency.delete(0, tk.END)
    entry_capacitance.delete(0, tk.END)
    label_result_capacitor.config(text="Result will appear here.")
    btn_graph_capacitor.grid_forget()


def create_capacitor_tab(notebook):
    frame_capacitor = ttk.Frame(notebook)
    notebook.add(frame_capacitor, text="Capacitor Calculator")

    # Dropdown for selecting the equation
    tk.Label(frame_capacitor, text="Select Equation:").grid(
        row=0, column=0, padx=10, pady=5
    )
    global combo_equation
    combo_equation = ttk.Combobox(
        frame_capacitor,
        values=["C = 1 / (2πfZ)", "Z = 1 / (2πfC)", "f = 1 / (2πCZ)", "Z = V / I"],
    )
    combo_equation.grid(row=0, column=1, padx=10, pady=5)
    combo_equation.set("Select an equation")
    combo_equation.bind("<<ComboboxSelected>>", update_fields)

    # Frame for dynamic input fields
    global frame_inputs
    frame_inputs = ttk.Frame(frame_capacitor)
    frame_inputs.grid(row=1, column=0, columnspan=2, pady=10)

    # Input fields (initially hidden)
    global \
        entry_current, \
        entry_voltage, \
        entry_impedance, \
        entry_frequency, \
        entry_capacitance
    entry_current = tk.Entry(frame_inputs)
    entry_voltage = tk.Entry(frame_inputs)
    entry_impedance = tk.Entry(frame_inputs)
    entry_frequency = tk.Entry(frame_inputs)
    entry_capacitance = tk.Entry(frame_inputs)

    # Buttons for calculation, graph, and clear
    btn_calculate_capacitor = tk.Button(
        frame_capacitor,
        text="Calculate",
        command=calculate_capacitor,
        bg="green",
        fg="white",
    )
    btn_calculate_capacitor.grid(row=2, column=0, columnspan=2, pady=10)

    global btn_graph_capacitor
    btn_graph_capacitor = tk.Button(
        frame_capacitor, text="Plot Graph", command=plot_graph_capacitor
    )
    # Initially hidden
    btn_graph_capacitor.grid_forget()

    btn_clear_capacitor = tk.Button(frame_capacitor, text="Clear", command=clear_fields)
    btn_clear_capacitor.grid(row=4, column=0, columnspan=2, pady=10)

    # Result label
    global label_result_capacitor
    label_result_capacitor = tk.Label(frame_capacitor, text="Result will appear here.")
    label_result_capacitor.grid(row=5, column=0, columnspan=2, pady=10)
