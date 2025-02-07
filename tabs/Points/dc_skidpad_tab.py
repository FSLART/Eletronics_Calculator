import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_dc_skidpad_score():
    try:
        Pmax = float(entry_Pmax.get()) if entry_Pmax.get() else None
        Tteam = float(entry_Tteam.get()) if entry_Tteam.get() else None
        Tmax = (float(entry_Tmax.get()) * 1.5 ) if entry_Tmax.get() else None
        doo = float(entry_doo.get()) if entry_doo.get() else None

        if Pmax is not None and Tteam is not None and Tmax is not None:
            dc_skidpad_score = (.95*Pmax*((((Tmax/(Tteam+(doo*0.2)))**2)-1)/1.25)) + (0.05*Pmax)
            label_result_dc_skidpad.config(text=f"dc_skidpad Score: {dc_skidpad_score:.3f}")
        else:
            label_result_dc_skidpad.config(text="Por favor, preencha os campos necessários.")
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_Pmax.delete(0, tk.END)
    entry_Tteam.delete(0, tk.END)
    entry_Tmax.delete(0, tk.END)

def create_dc_skidpad_tab():
    global entry_Pmax, entry_Tteam, entry_Tmax, label_result_dc_skidpad, entry_doo, doo

    frame_dc_skidpad = tk.Toplevel()
    frame_dc_skidpad.title("Dc Skidpad Points --> Pag 124")

    tk.Label(frame_dc_skidpad, text="Pmax").grid(row=0, column=0, padx=10, pady=5)
    entry_Pmax = tk.Entry(frame_dc_skidpad)
    entry_Pmax.grid(row=0, column=1, padx=10, pady=5)
    entry_Pmax.insert(0, "75")
    tk.Label(frame_dc_skidpad, text="Maximum points for the event (75) --> Pag 10").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="Tteam [s]").grid(row=1, column=0, padx=10, pady=5)
    entry_Tteam = tk.Entry(frame_dc_skidpad)
    entry_Tteam.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_dc_skidpad, text="Team's best autonomous mode time").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="DOO").grid(row=2, column=0, padx=10, pady=5)
    entry_doo = tk.Entry(frame_dc_skidpad)
    entry_doo.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_dc_skidpad, text="Cones Dow Or Out --> Pag 132").grid(row=2, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="Tmax [s]").grid(row=3, column=0, padx=10, pady=5)
    entry_Tmax = tk.Entry(frame_dc_skidpad) 
    entry_Tmax.grid(row=3, column=1, padx=10, pady=5)
    tk.Label(frame_dc_skidpad, text="Fastest autonomous mode vehicle including penalties.").grid(row=3, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="Runs with a run time without penalties >25 s will be disqualified --> Pag 123 ").grid(row=4, column=2, padx=10, pady=5)
    
    

    btn_calculate_dc_skidpad_score = tk.Button(frame_dc_skidpad, text="Calcular", command=calculate_dc_skidpad_score)
    btn_calculate_dc_skidpad_score.grid(row=6, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_dc_skidpad, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2, columnspan=2, pady=10)

    label_result_dc_skidpad = tk.Label(frame_dc_skidpad, text="O resultado aparecerá aqui.")
    label_result_dc_skidpad.grid(row=5, column=2, columnspan=4, pady=10)