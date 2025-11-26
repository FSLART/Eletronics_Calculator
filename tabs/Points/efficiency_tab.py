import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_efficiency_score():
    try:
        from tabs.points_tab import default_scoring_formula
        Pmax = float(entry_Pmax.get()) if entry_Pmax.get() else 75.0
        EFteam = float(entry_EFteam.get()) if entry_EFteam.get() else None
        EFmin = float(entry_EFmin.get()) if entry_EFmin.get() else None
        if Pmax is not None and EFteam is not None and EFmin is not None:
            EFmax = EFmin * 2
            
            efficiency_score = Pmax * ((EFmax- EFteam)/(EFmax - EFmin))**2
            
            label_result_efficiency.config(text=f"Efficiency Score: {efficiency_score:.2f}")
        else:
            label_result_efficiency.config(text="Por favor, preencha os campos necessários.")
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_Pmax.delete(0, tk.END)
    entry_EFteam.delete(0, tk.END)
    entry_EFmin.delete(0, tk.END)

def create_efficiency_tab():
    global entry_Pmax, entry_EFteam, entry_EFmin, label_result_efficiency

    frame_efficiency = tk.Toplevel()
    frame_efficiency.title("Efficiency Points")

    tk.Label(frame_efficiency, text="Pmax").grid(row=0, column=0, padx=10, pady=5)
    entry_Pmax = tk.Entry(frame_efficiency)
    entry_Pmax.grid(row=0, column=1, padx=10, pady=5)
    entry_Pmax.insert(0, "75")
    tk.Label(frame_efficiency, text="Maximum points for the event (75)").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(frame_efficiency, text="EFteam").grid(row=1, column=0, padx=10, pady=5)
    entry_EFteam = tk.Entry(frame_efficiency)
    entry_EFteam.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_efficiency, text="Team s efficiency factor").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_efficiency, text="EFmin").grid(row=2, column=0, padx=10, pady=5)
    entry_EFmin = tk.Entry(frame_efficiency) 
    entry_EFmin.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_efficiency, text="Lowest efficiency factor of all teams").grid(row=2, column=2, padx=10, pady=5)
    
    

    btn_calculate_efficiency_score = tk.Button(frame_efficiency, text="Calcular", command=calculate_efficiency_score)
    btn_calculate_efficiency_score.grid(row=4, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_efficiency, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2, columnspan=2, pady=10)

    label_result_efficiency = tk.Label(frame_efficiency, text="O resultado aparecerá aqui.")
    label_result_efficiency.grid(row=3, column=0, columnspan=4, pady=10)
