import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from tabs.ohms_tab import create_ohms_window
from tabs.power_tab import create_power_window
from tabs.inductor_tab import create_inductor_window
from tabs.capacitor_tab import create_capacitor_window
from tabs.capacitor_charge_discharge import create_cap_charge_discharge_window
from tabs.phase_angle_tab import create_phase_angle_window
from tabs.cap_energy_tab import create_cap_energy_window
from tabs.inductor_charge_discharge import create_ind_charge_discharge_window

from tabs.converters_tab import create_converters_window
from tabs.resistivity_conductivity_tab import create_resistivity_conductivity_window
from tabs.parallels_tab import create_parallels_window
from tabs.filters import create_filter_window


def create_eletronics_tab(notebook):
    frame_eletronics = ttk.Frame(notebook)
    notebook.add(frame_eletronics, text="Eletronics")

    # for correct spacing and positioning
    frame_eletronics.grid_rowconfigure(0, weight=1)  # Top empty row
    frame_eletronics.grid_rowconfigure(1, weight=1)  # Row with first button
    frame_eletronics.grid_rowconfigure(2, weight=1)  # Row with second button
    frame_eletronics.grid_rowconfigure(3, weight=1)  # Row with third button
    frame_eletronics.grid_rowconfigure(4, weight=1)  # Bottom empty row
    frame_eletronics.grid_columnconfigure(0, weight=1)  # Left empty column
    frame_eletronics.grid_columnconfigure(1, weight=1)  # Center column
    frame_eletronics.grid_columnconfigure(2, weight=1)  # Right column

    button_options = {
        "bg": "#36454F",
        "fg": "white",
        "width": 20,
        "height": 5,
        "font": ("Arial", 14, "bold"),
    }

    tk.Button(
        frame_eletronics,
        text="Capacitor Energy",
        **button_options,
        command=create_cap_energy_window,
    ).grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Capacitor Charge/Discharge",
        **button_options,
        command=create_cap_charge_discharge_window,
    ).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Capacitor Calculator",
        **button_options,
        command=create_capacitor_window,
    ).grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Inductor Charge/Discharge",
        **button_options,
        command=create_ind_charge_discharge_window,
    ).grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Inductor Calculator",
        **button_options,
        command=create_inductor_window,
    ).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics, text="Ohm's Law", **button_options, command=create_ohms_window
    ).grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Power Calculator",
        **button_options,
        command=create_power_window,
    ).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Phase Angle Calculator",
        **button_options,
        command=create_phase_angle_window,
    ).grid(row=3, column=2, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Converters",
        **button_options,
        command=create_converters_window,
    ).grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Resistivity/Conductivity",
        **button_options,
        command=create_resistivity_conductivity_window,
    ).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Parallels",
        **button_options,
        command=create_parallels_window,
    ).grid(row=4, column=2, sticky="nsew", padx=5, pady=5)
    tk.Button(
        frame_eletronics,
        text="Filters",
        **button_options,
        command=create_filter_window,
    ).grid(row=5, column=1, sticky="nsew", padx=5, pady=5)
