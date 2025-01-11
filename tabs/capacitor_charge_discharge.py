import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def highlight_point(ax, time, voltage):
    ax.plot(time, voltage, "ro")  # Highlight the point in red
    plt.draw()


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
                print(f"Selected point: Time = {x:.5f} s, Voltage = {y:.5f} V")
                messagebox.showinfo(
                    "Selected Point", f"Time = {x:.5f} s\nVoltage = {y:.5f} V"
                )

        fig.canvas.mpl_connect("button_press_event", on_click)

        # Highlight user-specified point
        try:
            desired_time = entry_desired_time.get()
            desired_voltage = entry_desired_voltage.get()
            if desired_time:
                desired_time = float(desired_time)
                desired_voltage = final_voltage + (
                    initial_voltage - final_voltage
                ) * np.exp(-desired_time / time_constant)
                highlight_point(ax, desired_time, desired_voltage)
                entry_desired_voltage.delete(0, tk.END)
                entry_desired_voltage.insert(0, f"{desired_voltage:.5f}")
            elif desired_voltage:
                desired_voltage = float(desired_voltage)
                desired_time = -time_constant * np.log(
                    (desired_voltage - final_voltage)
                    / (initial_voltage - final_voltage)
                )
                highlight_point(ax, desired_time, desired_voltage)
                entry_desired_time.delete(0, tk.END)
                entry_desired_time.insert(0, f"{desired_time:.5f}")
        except ValueError:
            pass  # Ignore if no valid input

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
                print(f"Selected point: Time = {x:.5f} s, Voltage = {y:.5f} V")
                messagebox.showinfo(
                    "Selected Point", f"Time = {x:.5f} s\nVoltage = {y:.5f} V"
                )

        fig.canvas.mpl_connect("button_press_event", on_click)

        # Highlight user-specified point
        try:
            desired_time = entry_desired_time.get()
            desired_voltage = entry_desired_voltage.get()
            if desired_time:
                desired_time = float(desired_time)
                desired_voltage = initial_voltage + (
                    final_voltage - initial_voltage
                ) * (1 - np.exp(-desired_time / time_constant))
                highlight_point(ax, desired_time, desired_voltage)
                entry_desired_voltage.delete(0, tk.END)
                entry_desired_voltage.insert(0, f"{desired_voltage:.5f}")
            elif desired_voltage:
                desired_voltage = float(desired_voltage)
                desired_time = -time_constant * np.log(
                    (initial_voltage - desired_voltage)
                    / (initial_voltage - final_voltage)
                )
                highlight_point(ax, desired_time, desired_voltage)
                entry_desired_time.delete(0, tk.END)
                entry_desired_time.insert(0, f"{desired_time:.5f}")
        except ValueError:
            pass  # Ignore if no valid input

        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers.")


def clear_fields():
    entry_initial_voltage.delete(0, tk.END)
    entry_final_voltage.delete(0, tk.END)
    entry_resistance.delete(0, tk.END)
    entry_capacitance.delete(0, tk.END)
    entry_desired_time.delete(0, tk.END)
    entry_desired_voltage.delete(0, tk.END)


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

    tk.Label(frame_capacitor, text="Desired Time (s):").grid(
        row=4, column=0, padx=10, pady=5
    )
    global entry_desired_time
    entry_desired_time = tk.Entry(frame_capacitor)
    entry_desired_time.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame_capacitor, text="Desired Voltage (V):").grid(
        row=5, column=0, padx=10, pady=5
    )
    global entry_desired_voltage
    entry_desired_voltage = tk.Entry(frame_capacitor)
    entry_desired_voltage.grid(row=5, column=1, padx=10, pady=5)

    # Buttons for calculation and clear
    btn_calculate_discharge = tk.Button(
        frame_capacitor,
        text="Calculate Discharge",
        command=calculate_discharge,
        bg="green",
        fg="white",
    )
    btn_calculate_discharge.grid(row=6, column=0, padx=10, pady=10)

    btn_calculate_charge = tk.Button(
        frame_capacitor,
        text="Calculate Charge",
        command=calculate_charge,
        bg="blue",
        fg="white",
    )
    btn_calculate_charge.grid(row=6, column=1, padx=10, pady=10)

    btn_clear = tk.Button(frame_capacitor, text="Clear", command=clear_fields)
    btn_clear.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
