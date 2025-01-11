import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def highlight_point(ax, time, voltage):
    ax.plot(time, voltage, "ro")  # Highlight the point in red
    plt.draw()


def on_calc_mode_change(event):
    mode = combo_calc_mode.get()
    if mode == "Voltage for Given Time":
        entry_desired_time.configure(state="normal")
        entry_desired_voltage.configure(state="readonly")
    else:
        entry_desired_time.configure(state="readonly")
        entry_desired_voltage.configure(state="normal")


def convert_with_units(value_str, unit):
    base_value = float(value_str)
    match unit:
        case "pΩ":
            return base_value * 1e-12
        case "nΩ":
            return base_value * 1e-9
        case "µΩ":
            return base_value * 1e-6
        case "mΩ":
            return base_value * 1e-3
        case "kΩ":
            return base_value * 1e3
        case "MΩ":
            return base_value * 1e6
        case "GΩ":
            return base_value * 1e9
        case "kF":
            return base_value * 1e3
        case "mF":
            return base_value * 1e-3
        case "µF":
            return base_value * 1e-6
        case "nF":
            return base_value * 1e-9
        case "pF":
            return base_value * 1e-12
        case _:
            return base_value


def calculate_discharge():
    try:
        initial_voltage = float(entry_initial_voltage.get())
        final_voltage = float(entry_final_voltage.get())
        resistance = convert_with_units(
            entry_resistance.get(), combo_resistance_unit.get()
        )
        capacitance = convert_with_units(
            entry_capacitance.get(), combo_capacitance_unit.get()
        )

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
            if combo_calc_mode.get() == "Voltage for Given Time":
                # The user wants to calculate voltage for a specified time
                if desired_time:
                    desired_time = float(desired_time)
                    desired_voltage = final_voltage + (
                        initial_voltage - final_voltage
                    ) * np.exp(-desired_time / time_constant)
                    highlight_point(ax, desired_time, desired_voltage)
                    entry_desired_voltage.delete(0, tk.END)
                    entry_desired_voltage.insert(0, f"{desired_voltage:.5f}")
            elif combo_calc_mode.get() == "Time for Given Voltage":
                # The user wants to calculate time for a specified voltage
                if desired_voltage:
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
        resistance = convert_with_units(
            entry_resistance.get(), combo_resistance_unit.get()
        )
        capacitance = convert_with_units(
            entry_capacitance.get(), combo_capacitance_unit.get()
        )

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
            if combo_calc_mode.get() == "Voltage for Given Time":
                # The user wants to calculate voltage for a specified time
                if desired_time:
                    desired_time = float(desired_time)
                    desired_voltage = initial_voltage + (
                        final_voltage - initial_voltage
                    ) * (1 - np.exp(-desired_time / time_constant))
                    highlight_point(ax, desired_time, desired_voltage)
                    entry_desired_voltage.delete(0, tk.END)
                    entry_desired_voltage.insert(0, f"{desired_voltage:.5f}")
            elif combo_calc_mode.get() == "Time for Given Voltage":
                # The user wants to calculate time for a specified voltage
                if desired_voltage:
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
    tk.Label(frame_capacitor, text="Initial Voltage (V):", fg="red").grid(
        row=0, column=0, padx=10, pady=5
    )
    global entry_initial_voltage
    entry_initial_voltage = tk.Entry(frame_capacitor)
    entry_initial_voltage.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_capacitor, text="Final Voltage (V):", fg="red").grid(
        row=1, column=0, padx=10, pady=5
    )
    global entry_final_voltage
    entry_final_voltage = tk.Entry(frame_capacitor)
    entry_final_voltage.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_capacitor, text="Resistance (Ω):", fg="red").grid(
        row=2, column=0, padx=10, pady=5
    )
    global entry_resistance
    entry_resistance = tk.Entry(frame_capacitor)
    entry_resistance.grid(row=2, column=1, padx=10, pady=5)

    global combo_resistance_unit
    combo_resistance_unit = ttk.Combobox(
        frame_capacitor, values=["mΩ", "mΩ", "Ω", "kΩ", "MΩ", "GΩ"], width=5
    )
    combo_resistance_unit.current(0)
    combo_resistance_unit.grid(row=2, column=2, padx=0, pady=0)

    tk.Label(frame_capacitor, text="Capacitance (F):", fg="red").grid(
        row=3, column=0, padx=10, pady=5
    )
    global entry_capacitance
    entry_capacitance = tk.Entry(frame_capacitor)
    entry_capacitance.grid(row=3, column=1, padx=10, pady=5)

    global combo_capacitance_unit
    combo_capacitance_unit = ttk.Combobox(
        frame_capacitor, values=["kF", "F", "mF", "µF", "nF", "pF"], width=5
    )
    combo_capacitance_unit.current(0)
    combo_capacitance_unit.grid(row=3, column=2, padx=0, pady=0)

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

    # Explanation label
    explanation_text = "CAMPOS A VERMELHO SAO OBRIGATORIOS!! \nPrencher Tempo para obter Tensão,\nou preencher tensão para obter tempo!\n"
    lbl_explanation = tk.Label(frame_capacitor, text=explanation_text, justify=tk.LEFT)
    lbl_explanation.grid(row=0, column=2, rowspan=8, padx=10, pady=5, sticky="nw")

    tk.Label(frame_capacitor, text="Calculation Mode:").grid(
        row=4, column=2, padx=5, pady=5
    )
    global combo_calc_mode
    combo_calc_mode = ttk.Combobox(
        frame_capacitor,
        values=["Voltage for Given Time", "Time for Given Voltage"],
        width=20,
    )
    combo_calc_mode.current(0)
    combo_calc_mode.bind("<<ComboboxSelected>>", on_calc_mode_change)
    combo_calc_mode.grid(row=5, column=2, padx=5, pady=5)

    # Make sure the initial states reflect the default combobox selection
    entry_desired_time.configure(state="normal")
    entry_desired_voltage.configure(state="readonly")
