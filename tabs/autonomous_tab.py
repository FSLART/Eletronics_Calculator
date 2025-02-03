import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tabs.AD.skidpad_points import create_skidpad_points_window
from tabs.AD.camera_calculations import create_camera_window

def create_autonomous_tab(notebook):
    frame_autonomous = ttk.Frame(notebook)
    notebook.add(frame_autonomous, text="Autonomous Driving")
    # for correct spacing and positioning
    frame_autonomous.grid_rowconfigure(0, weight=1)  # Top empty row
    frame_autonomous.grid_rowconfigure(1, weight=1)  # Row with first button
    frame_autonomous.grid_rowconfigure(2, weight=1)  # Row with second button
    frame_autonomous.grid_rowconfigure(3, weight=1)   # Bottom empty row
    frame_autonomous.grid_columnconfigure(0, weight=1)  # Left empty column 
    frame_autonomous.grid_columnconfigure(1, weight=1)  # Center column
    frame_autonomous.grid_columnconfigure(2, weight=1)  # Right column

    button_options = {'bg': '#36454F', 'fg': 'white', 'width': 20, 'height': 5, 'font': ('Arial', 14, 'bold')}

    tk.Button(frame_autonomous, text="Skidpad Points", **button_options, command= create_skidpad_points_window).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    tk.Button(frame_autonomous, text="Camera Calculations", **button_options, command=create_camera_window).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
