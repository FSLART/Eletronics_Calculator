import tkinter as tk
from tkinter import ttk

from tabs.endurance_tab import create_endurance_tab

def create_points_tab(notebook):
    frame_points = ttk.Frame(notebook)
    notebook.add(frame_points, text="Points")

    # for correct spacing and positioning
    frame_points.grid_rowconfigure(0, weight=1)  # Top empty row
    frame_points.grid_rowconfigure(1, weight=1)  # Row with first button
    frame_points.grid_rowconfigure(2, weight=1)  # Row with second button
    frame_points.grid_rowconfigure(3, weight=1)  # Row with third button
    frame_points.grid_rowconfigure(4, weight=1)  # Bottom empty row
    frame_points.grid_columnconfigure(0, weight=1)  # Left empty column
    frame_points.grid_columnconfigure(1, weight=1)  # Center column
    frame_points.grid_columnconfigure(2, weight=1)  # Right column

    button_options = {
        "bg": "#36454F",
        "fg": "white",
        "width": 20,
        "height": 5,
        "font": ("Arial", 14, "bold"),
    }

    tk.Button(
        frame_points,
        text="Endurance Calculator",
        **button_options,
        command = create_endurance_tab
    ).grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    tk.Button(
        frame_points,
        text="Efficienccy Calculator",
        **button_options,
  #      command=create_point_midpoint_window,  # Placeholder for actual function
    ).grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    