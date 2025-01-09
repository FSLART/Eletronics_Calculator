import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def calculate_inductor():
    try:
        voltage = (
            float(entry_voltage_inductor.get())
            if entry_voltage_inductor.get()
            else None
        )
        current = (
            float(entry_current_inductor.get())
            if entry_current_inductor.get()
            else None
        )
        impedance = (
            complex(entry_impedance_inductor.get())
            if entry_impedance_inductor.get()
            else None
        )
        frequency = (
            float(entry_frequency_inductor.get())
            if entry_frequency_inductor.get()
            else None
        )
        inductance = float(entry_inductance.get()) if entry_inductance.get() else None

        if inductance is None and impedance and frequency:
            inductance = abs(impedance) / (2 * np.pi * frequency)
            label_result_inductor.config(text=f"Inductance: {inductance:.6e} H")
        elif impedance is None and inductance and frequency:
            impedance = 2 * np.pi * frequency * inductance * 1j
            label_result_inductor.config(
                text=f"Impedance: {impedance.real:.2f} + {impedance.imag:.2f}j Ω"
            )
        elif frequency is None and inductance and impedance:
            frequency = abs(impedance) / (2 * np.pi * inductance)
            label_result_inductor.config(text=f"Frequency: {frequency:.2f} Hz")
        elif current and voltage:
            impedance = voltage / current
            label_result_inductor.config(
                text=f"Impedance (from V/I): {impedance:.2f} Ω"
            )
        else:
            label_result_inductor.config(text="Insufficient or conflicting inputs.")

        # Show the plot button if inductance is available
        if inductance is not None:
            btn_graph_inductor.grid(row=3, column=0, columnspan=2, pady=10)
        else:
            btn_graph_inductor.grid_forget()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero occurred. Check inputs.")


def update_fields(event):
    # Hide all input fields
    for widget in frame_inputs.winfo_children():
        widget.grid_forget()

    selected_equation = combo_equation.get()
    if selected_equation == "L = Z / (2πf)":
        tk.Label(frame_inputs, text="Impedance (Ω):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_impedance_inductor.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Frequency (Hz):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_frequency_inductor.grid(row=1, column=1, padx=10, pady=5)
    elif selected_equation == "Z = 2πfL":
        tk.Label(frame_inputs, text="Frequency (Hz):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_frequency_inductor.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Inductance (H):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_inductance.grid(row=1, column=1, padx=10, pady=5)
    elif selected_equation == "f = Z / (2πL)":
        tk.Label(frame_inputs, text="Impedance (Ω):").grid(
            row=0, column=0, padx=10, pady=5
        )
        entry_impedance_inductor.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Inductance (H):").grid(
            row=1, column=0, padx=10, pady=5
        )
        entry_inductance.grid(row=1, column=1, padx=10, pady=5)

    # Hide the plot button initially
    btn_graph_inductor.grid_forget()


def plot_graph_inductor():
    try:
        voltage = float(entry_voltage_inductor.get())
        inductance = float(entry_inductance.get())
        resistance = (
            float(entry_impedance_inductor.get().split("+")[0])
            if "+" in entry_impedance_inductor.get()
            else None
        )

        if resistance is None or not voltage or not inductance:
            raise ValueError("Missing required input for plotting.")

        time = np.linspace(0, 5 * inductance * resistance, 500)
        current = voltage / resistance * np.exp(-time / (resistance * inductance))

        plt.figure(figsize=(8, 5))
        plt.plot(time, current, label="Current vs Time")
        plt.title("Current Decay in an RL Circuit")
        plt.xlabel("Time (s)")
        plt.ylabel("Current (A)")
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError:
        messagebox.showerror(
            "Input Error", "Ensure voltage, inductance, and resistance are valid."
        )


def clear_fields():
    entry_voltage_inductor.delete(0, tk.END)
    entry_current_inductor.delete(0, tk.END)
    entry_impedance_inductor.delete(0, tk.END)
    entry_frequency_inductor.delete(0, tk.END)
    entry_inductance.delete(0, tk.END)
    label_result_inductor.config(text="Result will appear here.")
    btn_graph_inductor.grid_forget()


def create_inductor_tab(notebook):
    frame_inductor = ttk.Frame(notebook)
    notebook.add(frame_inductor, text="Inductor Calculator")

    # Dropdown for selecting the equation
    tk.Label(frame_inductor, text="Select Equation:").grid(
        row=0, column=0, padx=10, pady=5
    )
    global combo_equation
    combo_equation = ttk.Combobox(
        frame_inductor, values=["L = Z / (2πf)", "Z = 2πfL", "f = Z / (2πL)"]
    )
    combo_equation.grid(row=0, column=1, padx=10, pady=5)
    combo_equation.set("Select an equation")
    combo_equation.bind("<<ComboboxSelected>>", update_fields)

    # Frame for dynamic input fields
    global frame_inputs
    frame_inputs = ttk.Frame(frame_inductor)
    frame_inputs.grid(row=1, column=0, columnspan=2, pady=10)

    # Input fields (initially hidden)
    global \
        entry_voltage_inductor, \
        entry_current_inductor, \
        entry_impedance_inductor, \
        entry_frequency_inductor, \
        entry_inductance
    entry_voltage_inductor = tk.Entry(frame_inputs)
    entry_current_inductor = tk.Entry(frame_inputs)
    entry_impedance_inductor = tk.Entry(frame_inputs)
    entry_frequency_inductor = tk.Entry(frame_inputs)
    entry_inductance = tk.Entry(frame_inputs)

    # Buttons for calculation, graph, and clear
    btn_calculate_inductor = tk.Button(
        frame_inductor,
        text="Calculate",
        command=calculate_inductor,
        bg="green",
        fg="white",
    )
    btn_calculate_inductor.grid(row=2, column=0, columnspan=2, pady=10)

    global btn_graph_inductor
    btn_graph_inductor = tk.Button(
        frame_inductor, text="Plot Graph", command=plot_graph_inductor
    )
    # Initially hidden
    btn_graph_inductor.grid_forget()

    btn_clear_inductor = tk.Button(frame_inductor, text="Clear", command=clear_fields)
    btn_clear_inductor.grid(row=4, column=0, columnspan=2, pady=10)

    # Result label
    global label_result_inductor
    label_result_inductor = tk.Label(frame_inductor, text="Result will appear here.")
    label_result_inductor.grid(row=5, column=0, columnspan=2, pady=10)
