import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_endurance_score():
    try:
        Pmax = float(entry_Pmax.get()) if entry_Pmax.get() else None
        Tteam = float(entry_Tteam.get()) if entry_Tteam.get() else None
        Tmax = (float(entry_Tmax.get()) * 1.333 ) if entry_Tmax.get() else None

        if Pmax is not None and Tteam is not None and Tmax is not None:
            endurance_score = (0.9 * Pmax * (((Tmax / Tteam) - 1) / 0.333)) + (0.1 * Pmax)
            label_result_endurance.config(text=f"Endurance Score: {endurance_score:.2f}")
        else:
            label_result_endurance.config(text="Por favor, preencha os campos necessários.")
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_Pmax.delete(0, tk.END)
    entry_Tteam.delete(0, tk.END)
    entry_Tmax.delete(0, tk.END)

def create_endurance_tab():
    global entry_Pmax, entry_Tteam, entry_Tmax, label_result_endurance

    frame_endurance = tk.Toplevel()
    frame_endurance.title("Endurance Points")

    tk.Label(frame_endurance, text="Pmax").grid(row=0, column=0, padx=10, pady=5)
    entry_Pmax = tk.Entry(frame_endurance)
    entry_Pmax.grid(row=0, column=1, padx=10, pady=5)
    entry_Pmax.insert(0, "250")
    tk.Label(frame_endurance, text="Maximum points for the event (250)").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(frame_endurance, text="Tteam").grid(row=1, column=0, padx=10, pady=5)
    entry_Tteam = tk.Entry(frame_endurance)
    entry_Tteam.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_endurance, text="Team corrected elapsed time. Tteam is capped at Tmax").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_endurance, text="Tmax").grid(row=2, column=0, padx=10, pady=5)
    entry_Tmax = tk.Entry(frame_endurance) 
    entry_Tmax.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_endurance, text="Corrected elapsed time of the fastest vehicle.").grid(row=2, column=2, padx=10, pady=5)
    
    

    btn_calculate_endurance_score = tk.Button(frame_endurance, text="Calcular", command=calculate_endurance_score)
    btn_calculate_endurance_score.grid(row=4, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_endurance, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2, columnspan=2, pady=10)

    label_result_endurance = tk.Label(frame_endurance, text="O resultado aparecerá aqui.")
    label_result_endurance.grid(row=3, column=0, columnspan=4, pady=10)