import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def parse_complex(value):
    """Parse a complex number input with 'i' or 'j'."""
    try:
        if 'i' in value:
            value = value.replace('i', 'j')  # Replace 'i' with 'j' for Python compatibility
        return complex(value)
    except ValueError:
        raise ValueError("Invalid complex number format. Please use 'a + bi' or 'a + bj', where 'a' and 'b' are numbers.")


def calculate_1_resistors(entry_resistor1, entry_resistor2, entry_resistor3, entry_resistor4, entry_resistor5, entry_resistor6, label_result1):
    # Coletar entradas das resistências
    resistors = []
    for entry in [entry_resistor1, entry_resistor2, entry_resistor3, entry_resistor4, entry_resistor5, entry_resistor6]:
        try:
            value = float(entry.get())
            if value > 0:  # Ignorar valores zero ou negativos
                resistors.append(value)
        except ValueError:
            pass  # Ignorar entradas inválidas

    # Garantir que haja pelo menos duas resistências válidas
    if len(resistors) < 2:
        messagebox.showerror("Input Error", "Please enter at least two valid resistor values greater than zero.")
        return

    # Calcular a resistência equivalente
    result1 = sum(1 / r for r in resistors) ** -1
    label_result1.config(text=f"Equivalent Resistance: {result1:.2f} Ω")

def calculate_2_inductors(entry_inductor1, entry_inductor2, entry_inductor3, entry_inductor4, entry_inductor5, entry_inductor6, label_result2, entry_frequency, ):
    try:
        frequency = float(entry_frequency.get())
        if frequency <= 0:
            raise ValueError("Frequency must be greater than zero.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid frequency greater than zero.")
        return

    inductors = []
    for entry in [entry_inductor1, entry_inductor2, entry_inductor3, entry_inductor4, entry_inductor5, entry_inductor6]:
        try:
            value = float(entry.get())
            if value > 0:
                inductors.append(value)
        except ValueError:
            pass 

    if len(inductors) < 2:
        messagebox.showerror("Input Error", "Please enter at least two valid inductive values greater than zero.")
        return

    impedances = [2 * np.pi * frequency * L * 1j for L in inductors]

    result2 = sum(1 / z for z in impedances) ** -1
    label_result2.config(text=f"Equivalent Impedance: {result2:.2f} Ω")

def calculate_3_capacitor(entry_capacitor1, entry_capacitor2, entry_capacitor3, entry_capacitor4, entry_capacitor5, entry_capacitor6, entry_frequency, label_result3, ):
    try:
        frequency = float(entry_frequency.get())
        if frequency <= 0:
            raise ValueError("Frequency must be greater than zero.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid frequency greater than zero.")
        return
    capacitors = []
    for entry in [entry_capacitor1, entry_capacitor2, entry_capacitor3, entry_capacitor4, entry_capacitor5, entry_capacitor6]:
        try:
            value = float(entry.get())
            if value > 0:
                capacitors.append(value)
        except ValueError:
            pass 
    if len(capacitors) < 2:
        messagebox.showerror("Input Error", "Please enter at least two valid capacitive values greater than zero.")
        return
    capacitances = [-1j / (2 * np.pi * frequency * C) for C in capacitors]

    result3 = sum(1 / z for z in capacitances) ** -1
    label_result3.config(text=f"Equivalent Capacitance: {result3:.2f} Ω")

def calculate_4_series(label_result1, label_result2, label_result3, label_result4):
    def parse_label_value(label):
        try:
            # Tenta extrair um número complexo do texto da label
            value_text = label.cget("text").split(":")[1].strip().split()[0]
            if "j" not in value_text and "i" not in value_text:
                # Trata como número real
                return float(value_text)
            # Substituir 'i' por 'j' para compatibilidade com Python
            value_text = value_text.replace("i", "j")
            return complex(value_text)
        except (ValueError, IndexError):
            # Se não for possível, retorna 0
            return 0
    
    value1 = parse_label_value(label_result1)
    value2 = parse_label_value(label_result2)
    value3 = parse_label_value(label_result3)

    total = value1 + value2 + value3

    label_result4.config(text=f"Sum of Equivalent Resistence: {total:.2f} Ω")

def create_parallels_tab(notebook):
    frame_Equivalent_Resistence = tk.Frame(notebook)
    notebook.add(frame_Equivalent_Resistence, text="Equivalent Resistence")

    #Resistencias

    tk.Label(frame_Equivalent_Resistence, text="Resistor 1 (Ω):").grid(row=0, column=0, padx=10, pady=5)
    entry_resistor1 = tk.Entry(frame_Equivalent_Resistence)
    entry_resistor1.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Resistor 2 (Ω):").grid(row=1, column=0, padx=10, pady=5)
    entry_resistor2 = tk.Entry(frame_Equivalent_Resistence)
    entry_resistor2.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Resistor 3 (Ω):").grid(row=2, column=0, padx=10, pady=5)
    entry_resistor3 = tk.Entry(frame_Equivalent_Resistence)
    entry_resistor3.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Resistor 4 (Ω):").grid(row=3, column=0, padx=10, pady=5)
    entry_resistor4 = tk.Entry(frame_Equivalent_Resistence)
    entry_resistor4.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Resistor 5 (Ω):").grid(row=4, column=0, padx=10, pady=5)
    entry_resistor5 = tk.Entry(frame_Equivalent_Resistence)
    entry_resistor5.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Resistor 6 (Ω):").grid(row=5, column=0, padx=10, pady=5)
    entry_resistor6 = tk.Entry(frame_Equivalent_Resistence)
    entry_resistor6.grid(row=5, column=1, padx=10, pady=5)

    btn_calculate = tk.Button(
        frame_Equivalent_Resistence,
        text="Calculate",
        command=lambda: calculate_1_resistors(
            entry_resistor1, entry_resistor2, entry_resistor3, entry_resistor4, entry_resistor5, entry_resistor6, label_result1
        ),
        bg="green",
        fg="white",
    )
    btn_calculate.grid(row=6, column=0, columnspan=2, pady=10)

    label_result1 = tk.Label(frame_Equivalent_Resistence, text="Result will appear here.")
    label_result1.grid(row=7, column=0, columnspan=2, pady=10)

    #Bobines

    tk.Label(frame_Equivalent_Resistence, text="Inductor 1 (H):").grid(row=0, column=2, padx=10, pady=5)
    entry_inductor1 = tk.Entry(frame_Equivalent_Resistence)
    entry_inductor1.grid(row=0, column=3, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Inductor 2 (H):").grid(row=1, column=2, padx=10, pady=5)
    entry_inductor2 = tk.Entry(frame_Equivalent_Resistence)
    entry_inductor2.grid(row=1, column=3, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Inductor 3 (H):").grid(row=2, column=2, padx=10, pady=5)
    entry_inductor3 = tk.Entry(frame_Equivalent_Resistence)
    entry_inductor3.grid(row=2, column=3, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Inductor 4 (H):").grid(row=3, column=2, padx=10, pady=5)
    entry_inductor4 = tk.Entry(frame_Equivalent_Resistence)
    entry_inductor4.grid(row=3, column=3, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Inductor 5 (H):").grid(row=4, column=2, padx=10, pady=5)
    entry_inductor5 = tk.Entry(frame_Equivalent_Resistence)
    entry_inductor5.grid(row=4, column=3, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Inductor 6 (H):").grid(row=5, column=2, padx=10, pady=5)
    entry_inductor6 = tk.Entry(frame_Equivalent_Resistence)
    entry_inductor6.grid(row=5, column=3, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Frequency (Hz):").grid(row=0, column=6, padx=10, pady=5)
    entry_frequency = tk.Entry(frame_Equivalent_Resistence)
    entry_frequency.grid(row=0, column=7, padx=10, pady=5)

    label_result2 = tk.Label(frame_Equivalent_Resistence, text="Result will appear here.")
    label_result2.grid(row=7, column=2, columnspan=2, pady=10)

    btn_calculate = tk.Button(
        frame_Equivalent_Resistence,
        text="Calculate",
        command=lambda: calculate_2_inductors(
            entry_inductor1, entry_inductor2, entry_inductor3, entry_inductor4, entry_inductor5, entry_inductor6, label_result2, entry_frequency
        ),
        bg="blue",
        fg="white",
    )
    btn_calculate.grid(row=6, column=2, columnspan=2, pady=10)

    #Condensadores

    tk.Label(frame_Equivalent_Resistence, text="Capacitor 1 (F):").grid(row=0, column=4, padx=10, pady=5)
    entry_capacitor1 = tk.Entry(frame_Equivalent_Resistence)
    entry_capacitor1.grid(row=0, column=5, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Capacitor 2 (F):").grid(row=1, column=4, padx=10, pady=5)
    entry_capacitor2 = tk.Entry(frame_Equivalent_Resistence)
    entry_capacitor2.grid(row=1, column=5, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Capacitor 3 (F):").grid(row=2, column=4, padx=10, pady=5)
    entry_capacitor3 = tk.Entry(frame_Equivalent_Resistence)
    entry_capacitor3.grid(row=2, column=5, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Capacitor 4 (F):").grid(row=3, column=4, padx=10, pady=5)
    entry_capacitor4 = tk.Entry(frame_Equivalent_Resistence)
    entry_capacitor4.grid(row=3, column=5, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Capacitor 5 (F):").grid(row=4, column=4, padx=10, pady=5)
    entry_capacitor5 = tk.Entry(frame_Equivalent_Resistence)
    entry_capacitor5.grid(row=4, column=5, padx=10, pady=5)

    tk.Label(frame_Equivalent_Resistence, text="Capacitor 6 (F):").grid(row=5, column=4, padx=10, pady=5)
    entry_capacitor6 = tk.Entry(frame_Equivalent_Resistence)
    entry_capacitor6.grid(row=5, column=5, padx=10, pady=5)

    label_result3 = tk.Label(frame_Equivalent_Resistence, text="Result will appear here.")
    label_result3.grid(row=7, column=4, columnspan=2, pady=10)

    btn_calculate = tk.Button(
    frame_Equivalent_Resistence,
    text="Calculate",
    command=lambda: calculate_3_capacitor(
        entry_capacitor1, entry_capacitor2, entry_capacitor3, entry_capacitor4, entry_capacitor5, entry_capacitor6, entry_frequency, label_result3
    ),
    bg="red",
    fg="white",
    )
    btn_calculate.grid(row=6, column=4, columnspan=2, pady=10)

    #Série Total
    label_result4 = tk.Label(frame_Equivalent_Resistence, text="Result will appear here.")
    label_result4.grid(row=7, column=6, columnspan=2, pady=10)
    
    btn_calculate = tk.Button(
    frame_Equivalent_Resistence,
    text="Calculate",
    command=lambda: calculate_4_series(
        label_result1, label_result2, label_result3, label_result4
    ),
    bg="yellow",
    fg="black",
    )
    btn_calculate.grid(row=6, column=6, columnspan=2, pady=10)