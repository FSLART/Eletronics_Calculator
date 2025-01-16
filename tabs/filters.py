import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def calculate_filter():
    try:
        resistance = float(entry_resistance.get())
        capacitance = float(entry_capacitance.get())
        inductance = float(entry_inductance.get())
        cutoff_freq = entry_cutoff_frequency.get()
        if not cutoff_freq:
            cutoff_freq = 1000  # Default value
        else:
            cutoff_freq = float(cutoff_freq)
        
        filter_type = combo_filter_type.get()
        order = combo_order.get()

        if filter_type == "Low Pass" and order == "First Order":
            if resistance is None or capacitance is None:
                raise ValueError("Please enter resistance and capacitance.")
            cutoff_frequency = 1 / (2 * np.pi * resistance * capacitance)
            label_result_filter.config(text=f"Cutoff Frequency: {cutoff_frequency:.2f} Hz")
        elif filter_type == "High Pass" and order == "First Order":
            if resistance is None or capacitance is None:
                raise ValueError("Please enter resistance and capacitance.")
            cutoff_frequency = 1 / (2 * np.pi * resistance * capacitance)
            label_result_filter.config(text=f"Cutoff Frequency: {cutoff_frequency:.2f} Hz")
        elif filter_type == "Band Pass" and order == "Second Order":
            if resistance is None or inductance is None or capacitance is None:
                raise ValueError("Please enter resistance, inductance, and capacitance.")
            resonant_frequency = 1 / (2 * np.pi * np.sqrt(inductance * capacitance))
            quality_factor = resistance / (2 * np.pi * inductance)
            label_result_filter.config(
                text=f"Resonant Frequency: {resonant_frequency:.2f} Hz\nQuality Factor: {quality_factor:.2f}"
            )
        elif filter_type == "Pi Filter":
            if resistance is None or capacitance is None or inductance is None:
                raise ValueError("Please enter resistance, inductance, and capacitance.")
            cutoff_frequency = 1 / (np.pi * np.sqrt(inductance * capacitance))
            label_result_filter.config(text=f"Cutoff Frequency: {cutoff_frequency:.2f} Hz")
        else:
            label_result_filter.config(text="Invalid filter configuration.")

        # Show the plot button if parameters are valid
        btn_graph_filter.grid(row=6, column=0, columnspan=2, pady=10)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero occurred. Check inputs.")

def plot_graph_filter():
    try:
        filter_type = combo_filter_type.get()
        order = combo_order.get()

        frequency_range = np.linspace(1, 10000, 1000)
        if filter_type == "Low Pass" and order == "First Order":
            resistance = float(entry_resistance.get())
            capacitance = float(entry_capacitance.get())
            transfer_function = 1 / np.sqrt(1 + (2 * np.pi * frequency_range * resistance * capacitance) ** 2)
            plt.figure(figsize=(8, 5))
            plt.semilogx(frequency_range, 20 * np.log10(transfer_function), label="Low Pass")
        elif filter_type == "High Pass" and order == "First Order":
            resistance = float(entry_resistance.get())
            capacitance = float(entry_capacitance.get())
            transfer_function = (2 * np.pi * frequency_range * resistance * capacitance) / np.sqrt(1 + (2 * np.pi * frequency_range * resistance * capacitance) ** 2)
            plt.figure(figsize=(8, 5))
            plt.semilogx(frequency_range, 20 * np.log10(transfer_function), label="High Pass")
        elif filter_type == "Band Pass" and order == "Second Order":
            resistance = float(entry_resistance.get())
            inductance = float(entry_inductance.get())
            capacitance = float(entry_capacitance.get())
            omega_0 = 1 / np.sqrt(inductance * capacitance)
            quality_factor = resistance / (2 * np.pi * inductance)
            transfer_function = (
                (frequency_range / omega_0) /
                np.sqrt((1 - (frequency_range / omega_0) ** 2) ** 2 + (frequency_range / (omega_0 * quality_factor)) ** 2)
            )
            plt.figure(figsize=(8, 5))
            plt.semilogx(frequency_range, 20 * np.log10(transfer_function), label="Band Pass")
        elif filter_type == "Pi Filter":
            inductance = float(entry_inductance.get())
            capacitance = float(entry_capacitance.get())
            cutoff_frequency = 1 / (np.pi * np.sqrt(inductance * capacitance))
            transfer_function = 1 / np.sqrt(1 + (frequency_range / cutoff_frequency) ** 2)
            plt.figure(figsize=(8, 5))
            plt.semilogx(frequency_range, 20 * np.log10(transfer_function), label="Pi Filter")
        else:
            raise ValueError("Invalid filter configuration for plotting.")

        plt.title(f"{filter_type} Filter Response")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude (dB)")
        plt.grid(True)
        plt.legend()
        plt.show()

    except ValueError as e:
        messagebox.showerror("Plot Error", str(e))

def clear_fields_filter():
    entry_resistance.delete(0, tk.END)
    entry_capacitance.delete(0, tk.END)
    entry_inductance.delete(0, tk.END)
    entry_cutoff_frequency.delete(0, tk.END)
    label_result_filter.config(text="Result will appear here.")
    btn_graph_filter.grid_forget()

def create_filter_tab(notebook):
    frame_filter = ttk.Frame(notebook)
    notebook.add(frame_filter, text="Filter Calculator")

    tk.Label(frame_filter, text="Filter Type:").grid(row=0, column=0, padx=10, pady=5)
    global combo_filter_type
    combo_filter_type = ttk.Combobox(frame_filter, values=["Low Pass", "High Pass", "Band Pass", "Pi Filter"])
    combo_filter_type.grid(row=0, column=1, padx=10, pady=5)
    combo_filter_type.set("Select a filter")

    tk.Label(frame_filter, text="Order:").grid(row=1, column=0, padx=10, pady=5)
    global combo_order
    combo_order = ttk.Combobox(frame_filter, values=["First Order", "Second Order"])
    combo_order.grid(row=1, column=1, padx=10, pady=5)
    combo_order.set("Select an order")

    tk.Label(frame_filter, text="Resistance (Ω):").grid(row=2, column=0, padx=10, pady=5)
    global entry_resistance
    entry_resistance = tk.Entry(frame_filter)
    entry_resistance.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_filter, text="Capacitance (F):").grid(row=3, column=0, padx=10, pady=5)
    global entry_capacitance
    entry_capacitance = tk.Entry(frame_filter)
    entry_capacitance.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_filter, text="Inductance (H):").grid(row=4, column=0, padx=10, pady=5)
    global entry_inductance
    entry_inductance = tk.Entry(frame_filter)
    entry_inductance.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame_filter, text="Cutout Frequency (Hz):").grid(row=5, column=0, padx=10, pady=5)
    global entry_cutoff_frequency
    entry_cutoff_frequency = tk.Entry(frame_filter)
    entry_cutoff_frequency.grid(row=5, column=1, padx=10, pady=5)

    btn_calculate_filter = tk.Button(
        frame_filter,
        text="Calculate",
        command=calculate_filter,
        bg="green",
        fg="white",
        state=tk.NORMAL
    )
    btn_calculate_filter.grid(row=6, column=3, columnspan=2, pady=10)

    global btn_graph_filter
    btn_graph_filter = tk.Button(frame_filter, text="Plot Graph", command=plot_graph_filter)
    btn_graph_filter.grid(row=7, column=0, columnspan=2, pady=10)

    btn_clear_filter = tk.Button(frame_filter, text="Clear", command=clear_fields_filter)
    btn_clear_filter.grid(row=8, column=0, columnspan=2, pady=10)

    global label_result_filter
    label_result_filter = tk.Label(frame_filter, text="Result will appear here.")
    label_result_filter.grid(row=9, column=0, columnspan=2, pady=10)

