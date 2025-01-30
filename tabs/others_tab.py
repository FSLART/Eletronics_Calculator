import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tabs.complex_tab import create_complex_tab
from tabs.Retangulo_properties import create_retangulo_tab
from tabs.Circulo_properties import create_circulo_tab
from tabs.Triangulo_properties import create_triangle_tab
from tabs.Senos_Properties import create_sine_law_tab
from tabs.Trapézio_properties import create_trapezoid_tab
from tabs.Volume_properties import   create_volume_tab
from tabs.Calculadora_de_reatancias import create_complex_tab

 



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
    
    tk.Button(frame_others, text="Retângulo", **button_options, command=create_retangulo_tab).grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
    
    tk.Button(frame_others, text="Círculo", **button_options, command=create_circulo_tab).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
    
    tk.Button(frame_others, text="Triângulo", **button_options, command=create_triangle_tab).grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
    
    tk.Button(frame_others, text="Lei dos Senos", **button_options, command=create_sine_law_tab).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
    
    tk.Button(frame_others, text="Trapézio", **button_options, command=create_trapezoid_tab).grid(row=3, column=2, sticky="nsew", padx=5, pady=5)
    
    tk.Button(frame_others, text="Volume", **button_options, command=create_volume_tab).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
