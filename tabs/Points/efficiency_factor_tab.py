import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_efficiency_factor():
    try:
        T = float(entry_T.get()) if entry_T.get() else None
        E = float(entry_E.get() ) if entry_E.get() else None
        if T is not None and E is not None:
            efficiency_factor = T**2 * E
            label_result_efficiency_factor.config(text=f"Efficiency Factor: {efficiency_factor:.2f}")
        else:
            label_result_efficiency_factor.config(text="Por favor, preencha os campos necessários.")
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_T.delete(0, tk.END)
    entry_E.delete(0, tk.END)

def create_efficiency_factor_tab():
    global entry_T, entry_E, label_result_efficiency_factor

    frame_efficiency_factor = tk.Toplevel()
    frame_efficiency_factor.title("Efficiency Factor")


    tk.Label(frame_efficiency_factor, text="T").grid(row=1, column=0, padx=10, pady=5)
    entry_T = tk.Entry(frame_efficiency_factor)
    entry_T.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_efficiency_factor, text="Uncorrected elapsed driving timer").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_efficiency_factor, text="E").grid(row=2, column=0, padx=10, pady=5)
    entry_E = tk.Entry(frame_efficiency_factor) 
    entry_E.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_efficiency_factor, text="Corrected used fuel mass / Used energy").grid(row=2, column=2, padx=10, pady=5)
    
    

    btn_calculate_efficiency_factor_score = tk.Button(frame_efficiency_factor, text="Calcular", command=calculate_efficiency_factor)
    btn_calculate_efficiency_factor_score.grid(row=4, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_efficiency_factor, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2, columnspan=2, pady=10)

    label_result_efficiency_factor = tk.Label(frame_efficiency_factor, text="O resultado aparecerá aqui.")
    label_result_efficiency_factor.grid(row=3, column=0, columnspan=4, pady=10)
