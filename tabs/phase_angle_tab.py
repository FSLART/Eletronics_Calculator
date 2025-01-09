import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np


def calculate_phase_angle():
    try:
        resistance = float(entry_resistance.get())
        inductance = float(entry_inductance.get())
        capacitance = float(entry_capacitance.get())
        frequency = float(entry_frequency.get())

        if resistance <= 0 or inductance <= 0 or capacitance <= 0 or frequency <= 0:
            raise ValueError("All values must be positive.")

        omega = 2 * np.pi * frequency
        xl = omega * inductance
        xc = 1 / (omega * capacitance)
        phase_angle = np.arctan((xl - xc) / resistance) * (180 / np.pi)

        messagebox.showinfo(
            "Phase Angle", f"The phase angle is {phase_angle:.2f} degrees"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers.")


def clear_fields():
    entry_resistance.delete(0, tk.END)
    entry_inductance.delete(0, tk.END)
    entry_capacitance.delete(0, tk.END)
    entry_frequency.delete(0, tk.END)


def create_phase_angle_tab(notebook):
    frame_phase_angle = ttk.Frame(notebook)
    notebook.add(frame_phase_angle, text="Phase Angle")

    # Input fields
    tk.Label(frame_phase_angle, text="Resistance (Ω):").grid(
        row=0, column=0, padx=10, pady=5
    )
    global entry_resistance
    entry_resistance = tk.Entry(frame_phase_angle)
    entry_resistance.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_phase_angle, text="Inductance (H):").grid(
        row=1, column=0, padx=10, pady=5
    )
    global entry_inductance
    entry_inductance = tk.Entry(frame_phase_angle)
    entry_inductance.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_phase_angle, text="Capacitance (F):").grid(
        row=2, column=0, padx=10, pady=5
    )
    global entry_capacitance
    entry_capacitance = tk.Entry(frame_phase_angle)
    entry_capacitance.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_phase_angle, text="Frequency (Hz):").grid(
        row=3, column=0, padx=10, pady=5
    )
    global entry_frequency
    entry_frequency = tk.Entry(frame_phase_angle)
    entry_frequency.grid(row=3, column=1, padx=10, pady=5)

    # Display the equation
    equation_text = "Phase Angle (θ) = arctan((ωL - 1/ωC) / R)\nwhere ω = 2πf"
    tk.Label(frame_phase_angle, text=equation_text, justify=tk.LEFT).grid(
        row=0, column=2, rowspan=4, padx=10, pady=5
    )

    # Buttons for calculation and clear
    btn_calculate = tk.Button(
        frame_phase_angle,
        text="Calculate Phase Angle",
        command=calculate_phase_angle,
        bg="green",
        fg="white",
    )
    btn_calculate.grid(row=4, column=0, padx=10, pady=10)

    btn_clear = tk.Button(frame_phase_angle, text="Clear", command=clear_fields)
    btn_clear.grid(row=4, column=1, padx=10, pady=10)
