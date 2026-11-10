import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_efficiency_factor():
    try:
        T = float(entry_T.get()) if entry_T.get() else None
        E = float(entry_E.get() ) if entry_E.get() else None
        regen = float(entry_regen.get()) if entry_regen.get() else 0.0
        if T is not None and E is not None:
            # D 7.9.4: E85 fuel mass is divided by 1.45; D 7.9.5: 0.9 x regenerated energy is subtracted
            E = (E / 1.45 if e85.get() else E) - 0.9 * regen
            efficiency_factor = T**2 * E
            label_result_efficiency_factor.config(text=f"Efficiency Factor: {efficiency_factor:.2f}")
        else:
            label_result_efficiency_factor.config(text="Por favor, preencha os campos necessários.")
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_T.delete(0, tk.END)
    entry_E.delete(0, tk.END)
    entry_regen.delete(0, tk.END)
    e85.set(False)

def create_efficiency_factor_tab():
    global entry_T, entry_E, entry_regen, e85, label_result_efficiency_factor

    frame_efficiency_factor = tk.Toplevel()
    frame_efficiency_factor.title("Efficiency Factor")


    tk.Label(frame_efficiency_factor, text="T").grid(row=1, column=0, padx=10, pady=5)
    entry_T = tk.Entry(frame_efficiency_factor)
    entry_T.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_efficiency_factor, text="Uncorrected elapsed driving timer").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_efficiency_factor, text="E").grid(row=2, column=0, padx=10, pady=5)
    entry_E = tk.Entry(frame_efficiency_factor) 
    entry_E.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_efficiency_factor, text="Used fuel mass [CV] / Used energy [EV]").grid(row=2, column=2, padx=10, pady=5)

    tk.Label(frame_efficiency_factor, text="E regen").grid(row=3, column=0, padx=10, pady=5)
    entry_regen = tk.Entry(frame_efficiency_factor)
    entry_regen.grid(row=3, column=1, padx=10, pady=5)
    tk.Label(frame_efficiency_factor, text="[EV] Regenerated energy, same unit as E (optional) - D 7.9.5").grid(row=3, column=2, padx=10, pady=5)

    e85 = tk.BooleanVar()
    tk.Checkbutton(frame_efficiency_factor, text="[CV] E85 fuel (mass / 1.45) - D 7.9.4", variable=e85).grid(row=4, column=1, columnspan=2, sticky="w", padx=10, pady=5)

    btn_calculate_efficiency_factor_score = tk.Button(frame_efficiency_factor, text="Calcular", command=calculate_efficiency_factor)
    btn_calculate_efficiency_factor_score.grid(row=6, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_efficiency_factor, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2, columnspan=2, pady=10)

    label_result_efficiency_factor = tk.Label(frame_efficiency_factor, text="O resultado aparecerá aqui.")
    label_result_efficiency_factor.grid(row=5, column=0, columnspan=4, pady=10)
