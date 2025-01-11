import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def calculate_discharge():
    try:
        initial_current = float(entry_initial_current.get())
        final_current = float(entry_final_current.get())
        resistance = float(entry_resistance.get())
        inductance = float(entry_inductance.get())

        if (
            initial_current <= 0
            or final_current < 0
            or resistance <= 0
            or inductance <= 0
        ):
            raise ValueError(
                "All values must be positive, and final current must be non-negative."
            )

        time_constant = inductance / resistance
        time = np.linspace(0, 5 * time_constant, 500)
        current_discharge = final_current + (initial_current - final_current) * np.exp(
            -time / time_constant
        )
        voltage_discharge = resistance * (initial_current - current_discharge)

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(time, current_discharge, label="Current vs Time", color="blue")
        ax.plot(time, voltage_discharge, label="Voltage vs Time", color="green")
        ax.set_title("Inductor Discharge Curve")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Current (A) / Voltage (V)")
        ax.grid(True)
        ax.legend()

        def on_click(event):
            if event.inaxes is not None:
                x, y = event.xdata, event.ydata
                print(f"Selected point: Time = {x:.2f} s, Value = {y:.2f}")
                messagebox.showinfo(
                    "Selected Point", f"Time = {x:.2f} s\nValue = {y:.2f}"
                )

        fig.canvas.mpl_connect("button_press_event", on_click)
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers.")

def calculate_charge():
    try:
        initial_current = float(entry_initial_current.get())
        final_current = float(entry_final_current.get())
        resistance = float(entry_resistance.get())
        inductance = float(entry_inductance.get())

        if (
            initial_current < 0
            or final_current <= 0
            or resistance <= 0
            or inductance <= 0
        ):
            raise ValueError(
                "All values must be positive, and initial current must be non-negative."
            )

        time_constant = inductance / resistance
        time = np.linspace(0, 5 * time_constant, 500)
        current_charge = initial_current + (final_current - initial_current) * (
            1 - np.exp(-time / time_constant)
        )
        voltage_charge = resistance * (final_current - current_charge)

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(time, current_charge, label="Current vs Time", color="blue")
        ax.plot(time, voltage_charge, label="Voltage vs Time", color="green")
        ax.set_title("Inductor Charge Curve")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Current (A) / Voltage (V)")
        ax.grid(True)
        ax.legend()

        def on_click(event):
            if event.inaxes is not None:
                x, y = event.xdata, event.ydata
                print(f"Selected point: Time = {x:.2f} s, Value = {y:.2f}")
                messagebox.showinfo(
                    "Selected Point", f"Time = {x:.2f} s\nValue = {y:.2f}"
                )

        fig.canvas.mpl_connect("button_press_event", on_click)
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers.")

def clear_fields():
    entry_initial_current.delete(0, tk.END)
    entry_final_current.delete(0, tk.END)
    entry_resistance.delete(0, tk.END)
    entry_inductance.delete(0, tk.END)

def create_charge_discharge_tab_Ind(notebook):
    frame_inductor = ttk.Frame(notebook)
    notebook.add(frame_inductor, text="Inductor Charge/Discharge")

    # Input fields
    tk.Label(frame_inductor, text="Initial Current (A):").grid(
        row=0, column=0, padx=10, pady=5
    )
    global entry_initial_current
    entry_initial_current = tk.Entry(frame_inductor)
    entry_initial_current.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_inductor, text="Final Current (A):").grid(
        row=1, column=0, padx=10, pady=5
    )
    global entry_final_current
    entry_final_current = tk.Entry(frame_inductor)
    entry_final_current.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_inductor, text="Resistance (\u03A9):").grid(
        row=2, column=0, padx=10, pady=5
    )
    global entry_resistance
    entry_resistance = tk.Entry(frame_inductor)
    entry_resistance.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_inductor, text="Inductance (H):").grid(
        row=3, column=0, padx=10, pady=5
    )
    global entry_inductance
    entry_inductance = tk.Entry(frame_inductor)
    entry_inductance.grid(row=3, column=1, padx=10, pady=5)

    # Buttons for calculation and clear
    btn_calculate_discharge = tk.Button(
        frame_inductor,
        text="Calculate Discharge",
        command=calculate_discharge,
        bg="green",
        fg="white",
    )
    btn_calculate_discharge.grid(row=4, column=0, padx=10, pady=10)

    btn_calculate_charge = tk.Button(
        frame_inductor,
        text="Calculate Charge",
        command=calculate_charge,
        bg="blue",
        fg="white",
    )
    btn_calculate_charge.grid(row=4, column=1, padx=10, pady=10)

    btn_clear = tk.Button(frame_inductor, text="Clear", command=clear_fields)
    btn_clear.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
