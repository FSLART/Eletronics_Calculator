import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cmath

def calculate_complex_to_phasor():
    try:
        real = float(entry_real.get()) if entry_real.get() else None
        imag = float(entry_imag.get()) if entry_imag.get() else None
        magnitude = float(entry_magnitude.get()) if entry_magnitude.get() else None
        angle = float(entry_angle.get()) if entry_angle.get() else None

        if real is not None and imag is not None:
            complex_number = complex(real, imag)
            magnitude, angle = cmath.polar(complex_number)
            angle = angle * (180/cmath.pi)
            label_result_complex.config(text=f"Fasor: {magnitude:.4f} ∠ {angle:.4f}°")

        elif magnitude is not None and angle is not None:
            angle_rad = angle / (180/cmath.pi)
            complex_number = cmath.rect(magnitude, angle_rad)
            label_result_complex.config(text=f"Número Complexo: {complex_number.real:.4f} + {complex_number.imag:.4f}j")

        else:
            label_result_complex.config(text="Por favor, preencha os campos necessários.")
    
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números válidos.")

def clear_complex_fields():
    entry_real.config(state=tk.NORMAL)
    entry_imag.config(state=tk.NORMAL)
    entry_magnitude.config(state=tk.NORMAL)
    entry_angle.config(state=tk.NORMAL)

    entry_real.delete(0, tk.END)
    entry_imag.delete(0, tk.END)
    entry_magnitude.delete(0, tk.END)
    entry_angle.delete(0, tk.END)

    update_complex_fields_based_on_selection(None)

def update_complex_fields_based_on_selection(event):
    selected_option = combo_formula_complex.get()
    if selected_option == "Complexo para Fasor":
        entry_real.config(state=tk.NORMAL)
        entry_imag.config(state=tk.NORMAL)
        entry_magnitude.config(state=tk.DISABLED)
        entry_angle.config(state=tk.DISABLED)
    elif selected_option == "Fasor para Complexo":
        entry_real.config(state=tk.DISABLED)
        entry_imag.config(state=tk.DISABLED)
        entry_magnitude.config(state=tk.NORMAL)
        entry_angle.config(state=tk.NORMAL)

def create_complex_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Complexo")

    global entry_real, entry_imag, entry_magnitude, entry_angle, label_result_complex, combo_formula_complex

    tk.Label(tab, text="Real:").grid(row=0, column=0, padx=10, pady=5)
    entry_real = tk.Entry(tab)
    entry_real.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(tab, text="Imaginário:").grid(row=1, column=0, padx=10, pady=5)
    entry_imag = tk.Entry(tab)
    entry_imag.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(tab, text="Magnitude:").grid(row=2, column=0, padx=10, pady=5)
    entry_magnitude = tk.Entry(tab)
    entry_magnitude.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(tab, text="Ângulo:").grid(row=3, column=0, padx=10, pady=5)
    entry_angle = tk.Entry(tab)
    entry_angle.grid(row=3, column=1, padx=10, pady=5)

    combo_formula_complex = ttk.Combobox(tab, values=["Complexo para Fasor", "Fasor para Complexo"])
    combo_formula_complex.grid(row=4, column=1, padx=10, pady=5)
    combo_formula_complex.bind("<<ComboboxSelected>>", update_complex_fields_based_on_selection)
    combo_formula_complex.current(0)

    tk.Button(tab, text="Calcular", command=calculate_complex_to_phasor).grid(row=5, column=0, padx=10, pady=5)
    tk.Button(tab, text="Limpar", command=clear_complex_fields).grid(row=5, column=1, padx=10, pady=5)

    label_result_complex = tk.Label(tab, text="")
    label_result_complex.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    update_complex_fields_based_on_selection(None)