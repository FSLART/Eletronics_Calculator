import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def calculate_discharge():
    try:
        initial_voltage = float(entry_initial_voltage.get())
        final_voltage = float(entry_final_voltage.get())
        resistance = float(entry_resistance.get())
        capacitance = float(entry_capacitance.get())

        if (
            initial_voltage <= 0
            or final_voltage < 0
            or resistance <= 0
            or capacitance <= 0
        ):
            raise ValueError(
                "All values must be positive, and final voltage must be non-negative."
            )

        time_constant = resistance * capacitance
        time = np.linspace(0, 5 * time_constant, 500)
        voltage_discharge = final_voltage + (initial_voltage - final_voltage) * np.exp(
            -time / time_constant
        )

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(time, voltage_discharge, label="Voltage vs Time")
        ax.set_title("Capacitor Discharge Curve")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Voltage (V)")
        ax.grid(True)
        ax.legend()

        def on_click(event):
            if event.inaxes is not None:
                x, y = event.xdata, event.ydata
                print(f"Selected point: Time = {x:.2f} s, Voltage = {y:.2f} V")
                messagebox.showinfo(
                    "Selected Point", f"Time = {x:.2f} s\nVoltage = {y:.2f} V"
                )

        fig.canvas.mpl_connect("button_press_event", on_click)
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers.")


def calculate_charge():
    try:
        initial_voltage = float(entry_initial_voltage.get())
        final_voltage = float(entry_final_voltage.get())
        resistance = float(entry_resistance.get())
        capacitance = float(entry_capacitance.get())

        if (
            initial_voltage < 0
            or final_voltage <= 0
            or resistance <= 0
            or capacitance <= 0
        ):
            raise ValueError(
                "All values must be positive, and initial voltage must be non-negative."
            )

        time_constant = resistance * capacitance
        time = np.linspace(0, 5 * time_constant, 500)
        voltage_charge = initial_voltage + (final_voltage - initial_voltage) * (
            1 - np.exp(-time / time_constant)
        )

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(time, voltage_charge, label="Voltage vs Time")
        ax.set_title("Capacitor Charge Curve")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Voltage (V)")
        ax.grid(True)
        ax.legend()

        def on_click(event):
            if event.inaxes is not None:
                x, y = event.xdata, event.ydata
                print(f"Selected point: Time = {x:.2f} s, Voltage = {y:.2f} V")
                messagebox.showinfo(
                    "Selected Point", f"Time = {x:.2f} s\nVoltage = {y:.2f} V"
                )

        fig.canvas.mpl_connect("button_press_event", on_click)
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers.")


def clear_fields():
    entry_initial_voltage.delete(0, tk.END)
    entry_final_voltage.delete(0, tk.END)
    entry_resistance.delete(0, tk.END)
    entry_capacitance.delete(0, tk.END)


def create_charge_discharge_tab(notebook):
    frame_capacitor = ttk.Frame(notebook)
    notebook.add(frame_capacitor, text="Capacitor Charge/Discharge")

    # Input fields
    tk.Label(frame_capacitor, text="Initial Voltage (V):").grid(
        row=0, column=0, padx=10, pady=5
    )
    global entry_initial_voltage
    entry_initial_voltage = tk.Entry(frame_capacitor)
    entry_initial_voltage.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_capacitor, text="Final Voltage (V):").grid(
        row=1, column=0, padx=10, pady=5
    )
    global entry_final_voltage
    entry_final_voltage = tk.Entry(frame_capacitor)
    entry_final_voltage.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_capacitor, text="Resistance (Ω):").grid(
        row=2, column=0, padx=10, pady=5
    )
    global entry_resistance
    entry_resistance = tk.Entry(frame_capacitor)
    entry_resistance.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_capacitor, text="Capacitance (F):").grid(
        row=3, column=0, padx=10, pady=5
    )
    global entry_capacitance
    entry_capacitance = tk.Entry(frame_capacitor)
    entry_capacitance.grid(row=3, column=1, padx=10, pady=5)

    # Buttons for calculation and clear
    btn_calculate_discharge = tk.Button(
        frame_capacitor,
        text="Calculate Discharge",
        command=calculate_discharge,
        bg="green",
        fg="white",
    )
    btn_calculate_discharge.grid(row=4, column=0, padx=10, pady=10)

    btn_calculate_charge = tk.Button(
        frame_capacitor,
        text="Calculate Charge",
        command=calculate_charge,
        bg="blue",
        fg="white",
    )
    btn_calculate_charge.grid(row=4, column=1, padx=10, pady=10)

    btn_clear = tk.Button(frame_capacitor, text="Clear", command=clear_fields)
    btn_clear.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
