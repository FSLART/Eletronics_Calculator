import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def parse_complex(value):
    """Parse a complex number input with 'i' or 'j'."""
    try:
        if 'i' in value:
            value = value.replace('i', 'j')  # Replace 'i' with 'j' for Python compatibility
        return complex(value)
    except ValueError:
        raise ValueError("Invalid complex number format. Please use 'a + bi' or 'a + bj', where 'a' and 'b' are numbers.")


def calculate_inductor():
    try:
        voltage = float(entry_voltage_inductor.get()) if entry_voltage_inductor.get() else None
        current = float(entry_current_inductor.get()) if entry_current_inductor.get() else None
        impedance = parse_complex(entry_impedance_inductor.get()) if entry_impedance_inductor.get() else None
        frequency = float(entry_frequency_inductor.get()) if entry_frequency_inductor.get() else None
        inductance = float(entry_inductance.get()) if entry_inductance.get() else None

        if selected_formula.get() == "L = Z / (2πf)":
            if impedance is None or frequency is None:
                raise ValueError("Both impedance and frequency are required for the formula 'L = Z / (2πf)'. Please provide valid values.")
            inductance = abs(impedance) / (2 * np.pi * frequency)
            label_result_inductor.config(text=f"Inductance: {inductance:.6e} H")
        elif selected_formula.get() == "Z = 2πfL":
            if inductance is None or frequency is None:
                raise ValueError("Both inductance and frequency are required for the formula 'Z = 2πfL'. Please provide valid values.")
            impedance = 2 * np.pi * frequency * inductance * 1j
            label_result_inductor.config(text=f"Impedance: {impedance.real:.2f} + {impedance.imag:.2f}j Ω")
        elif selected_formula.get() == "f = Z / (2πL)":
            if impedance is None or inductance is None:
                raise ValueError("Both impedance and inductance are required for the formula 'f = Z / (2πL)'. Please provide valid values.")
            frequency = abs(impedance) / (2 * np.pi * inductance)
            label_result_inductor.config(text=f"Frequency: {frequency:.2f} Hz")
        elif current is not None and voltage is not None:
            impedance = voltage / current
            label_result_inductor.config(text=f"Impedance (from V/I): {impedance:.2f} Ω")
        else:
            label_result_inductor.config(text="Insufficient or conflicting inputs. Please provide at least two valid parameters.")

        # Show the plot button if inductance is available
        if inductance is not None:
            btn_graph_inductor.grid(row=3, column=0, columnspan=2, pady=10)
        else:
            btn_graph_inductor.grid_forget()

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero occurred. Please check your inputs for any zero values.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {str(e)}")


def update_fields(event):
    """Update input fields and indicate selected formula."""
    # Hide all input fields
    for widget in frame_inputs.winfo_children():
        widget.grid_forget()

    selected_equation = combo_equation.get()
    selected_formula.set(selected_equation)  # Update selected formula indicator

    if selected_equation == "L = Z / (2πf)":
        tk.Label(frame_inputs, text="Voltage (V):").grid(row=0, column=0, padx=10, pady=5)
        entry_voltage_inductor.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Impedance (Ω):").grid(row=1, column=0, padx=10, pady=5)
        entry_impedance_inductor.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Frequency (Hz):").grid(row=2, column=0, padx=10, pady=5)
        entry_frequency_inductor.grid(row=2, column=1, padx=10, pady=5)
    elif selected_equation == "Z = 2πfL":
        tk.Label(frame_inputs, text="Voltage (V):").grid(row=0, column=0, padx=10, pady=5)
        entry_voltage_inductor.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Frequency (Hz):").grid(row=1, column=0, padx=10, pady=5)
        entry_frequency_inductor.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Inductance (H):").grid(row=2, column=0, padx=10, pady=5)
        entry_inductance.grid(row=2, column=1, padx=10, pady=5)
    elif selected_equation == "f = Z / (2πL)":
        tk.Label(frame_inputs, text="Voltage (V):").grid(row=0, column=0, padx=10, pady=5)
        entry_voltage_inductor.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Impedance (Ω):").grid(row=1, column=0, padx=10, pady=5)
        entry_impedance_inductor.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Inductance (H):").grid(row=2, column=0, padx=10, pady=5)
        entry_inductance.grid(row=2, column=1, padx=10, pady=5)

    # Hide the plot button initially
    btn_graph_inductor.grid_forget()


def plot_graph_inductor():
    try:
        voltage = float(entry_voltage_inductor.get())
        inductance = float(entry_inductance.get())
        impedance_str = entry_impedance_inductor.get()

        # Extract real part of the impedance for resistance (assuming impedance is given in the form 'R + jX')
        if '+' in impedance_str:
            resistance = float(impedance_str.split('+')[0])  # Real part (resistance)
        elif 'j' in impedance_str:  # If only imaginary part is present
            resistance = 0  # No real part, hence resistance is 0
        else:
            resistance = float(impedance_str)  # Purely real value (e.g., '40')

        if resistance == 0 or not voltage or not inductance:
            raise ValueError("Missing required input for plotting. Ensure voltage, inductance, and resistance are valid.")

        # Time array for the RL circuit response
        time = np.linspace(0, 5 * inductance * resistance, 500)
        # RL circuit current response: I(t) = V/R * exp(-t / (L*R))
        current = voltage / resistance * np.exp(-time / (inductance * resistance))

        plt.figure(figsize=(8, 5))
        plt.plot(time, current, label="Current vs Time")
        plt.title("Current Decay in an RL Circuit")
        plt.xlabel("Time (s)")
        plt.ylabel("Current (A)")
        plt.grid(True)
        plt.legend()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Ensure voltage, inductance, and resistance are valid and non-zero.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero occurred. Check the inputs for voltage, inductance, and resistance.")


def clear_fields():
    entry_voltage_inductor.delete(0, tk.END)
    entry_current_inductor.delete(0, tk.END)
    entry_impedance_inductor.delete(0, tk.END)
    entry_frequency_inductor.delete(0, tk.END)
    entry_inductance.delete(0, tk.END)
    label_result_inductor.config(text="Result will appear here.")
    btn_graph_inductor.grid_forget()


def create_inductor_window():
    # inductor_window = ttk.Frame(notebook) #this creates a tab need to add 'notebook' as a parameter of this function
    # notebook.add(inductor_window, text="Inductor Calculator")
    inductor_window=tk.Toplevel()
    inductor_window.title("Inductor Calculator")
    inductor_window.geometry("500x400")
    # Dropdown for selecting the equation
    tk.Label(inductor_window, text="Select Equation:").grid(row=0, column=0, padx=10, pady=5)
    global combo_equation
    combo_equation = ttk.Combobox(inductor_window, values=["L = Z / (2πf)", "Z = 2πfL", "f = Z / (2πL)"])
    combo_equation.grid(row=0, column=1, padx=10, pady=5)
    combo_equation.set("Select an equation")
    combo_equation.bind("<<ComboboxSelected>>", update_fields)

    # Indicator for the selected formula
    global selected_formula
    selected_formula = tk.StringVar(value="No formula selected")
    tk.Label(inductor_window, textvariable=selected_formula, fg="blue").grid(row=1, column=0, columnspan=2, pady=5)

    # Frame for dynamic input fields
    global frame_inputs
    frame_inputs = ttk.Frame(inductor_window)
    frame_inputs.grid(row=2, column=0, columnspan=2, pady=10)

    # Input fields (initially hidden)
    global entry_voltage_inductor, entry_current_inductor, entry_impedance_inductor, entry_frequency_inductor, entry_inductance
    entry_voltage_inductor = tk.Entry(frame_inputs)
    entry_current_inductor = tk.Entry(frame_inputs)
    entry_impedance_inductor = tk.Entry(frame_inputs)
    entry_frequency_inductor = tk.Entry(frame_inputs)
    entry_inductance = tk.Entry(frame_inputs)

    # Buttons for calculation, graph, and clear
    btn_calculate_inductor = tk.Button(inductor_window, text="Calculate", command=calculate_inductor, bg="green", fg="white")
    btn_calculate_inductor.grid(row=3, column=0, columnspan=2, pady=10)

    global btn_graph_inductor
    btn_graph_inductor = tk.Button(inductor_window, text="Plot Graph", command=plot_graph_inductor)
    btn_graph_inductor.grid_forget()  # Initially hidden

    btn_clear_inductor = tk.Button(inductor_window, text="Clear", command=clear_fields)
    btn_clear_inductor.grid(row=4, column=0, columnspan=2, pady=10)

    # Result label
    global label_result_inductor
    label_result_inductor = tk.Label(inductor_window, text="Result will appear here.")
    label_result_inductor.grid(row=5, column=0, columnspan=2, pady=10)
