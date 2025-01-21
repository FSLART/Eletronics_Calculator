import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tabs.complex_tab import create_complex_tab

def create_others_tab(notebook):
    frame_others = ttk.Frame(notebook)
    notebook.add(frame_others, text="Others")

    button_options = {'bg': '#36454F', 'fg': 'white', 'width': 20, 'height': 5, 'font': ('Arial', 14, 'bold')}

     # for correct spacing and positioning
    frame_others.grid_rowconfigure(0, weight=1)  # Top empty row
    frame_others.grid_rowconfigure(1, weight=1)  # Row with first button
    frame_others.grid_rowconfigure(2, weight=1)  # Row with second button
    frame_others.grid_rowconfigure(3, weight=1)   # Bottom empty row
    frame_others.grid_columnconfigure(0, weight=1)  # Left empty column 
    frame_others.grid_columnconfigure(1, weight=1)  # Center column
    frame_others.grid_columnconfigure(2, weight=1)  # Right column

    tk.Button(frame_others, text="Complex Numbers", **button_options, command=create_complex_tab).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
