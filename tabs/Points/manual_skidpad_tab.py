import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_manual_skidpad_score():
    try:
        Pmax = float(entry_Pmax.get()) if entry_Pmax.get() else None
        Tteam = float(entry_Tteam.get()) if entry_Tteam.get() else None
        Tmax = (float(entry_Tmax.get()) * 1.25 ) if entry_Tmax.get() else None
        doo = float(entry_doo.get()) if entry_doo.get() else None

        if Pmax is not None and Tteam is not None and Tmax is not None:
            manual_skidpad_score = (.95*Pmax*((((Tmax/(Tteam+(doo*0.2))**2)-1)/0.5625))) + (0.05*Pmax)
            label_result_manual_skidpad.config(text=f"manual_skidpad Score: {manual_skidpad_score:.3f}")
        else:
            label_result_manual_skidpad.config(text="Por favor, preencha os campos necessários.")
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_Pmax.delete(0, tk.END)
    entry_Tteam.delete(0, tk.END)
    entry_Tmax.delete(0, tk.END)

def create_manual_skidpad_tab():
    global entry_Pmax, entry_Tteam, entry_Tmax, label_result_manual_skidpad, entry_doo, doo

    frame_manual_skidpad = tk.Toplevel()
    frame_manual_skidpad.title("Manual Skidpad Points --> Pag 123")

    tk.Label(frame_manual_skidpad, text="Pmax").grid(row=0, column=0, padx=10, pady=5)
    entry_Pmax = tk.Entry(frame_manual_skidpad)
    entry_Pmax.grid(row=0, column=1, padx=10, pady=5)
    entry_Pmax.insert(0, "50")
    tk.Label(frame_manual_skidpad, text="Maximum points for the event (50) --> Pag 10").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(frame_manual_skidpad, text="Tteam [s]").grid(row=1, column=0, padx=10, pady=5)
    entry_Tteam = tk.Entry(frame_manual_skidpad)
    entry_Tteam.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_manual_skidpad, text="Team's best manual mode time").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_manual_skidpad, text="DOO").grid(row=2, column=0, padx=10, pady=5)
    entry_doo = tk.Entry(frame_manual_skidpad)
    entry_doo.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_manual_skidpad, text="Cones Dow Or Out --> Pag 132").grid(row=2, column=2, padx=10, pady=5)

    tk.Label(frame_manual_skidpad, text="Tmax [s]").grid(row=3, column=0, padx=10, pady=5)
    entry_Tmax = tk.Entry(frame_manual_skidpad) 
    entry_Tmax.grid(row=3, column=1, padx=10, pady=5)
    tk.Label(frame_manual_skidpad, text="Time of the fastest manual mode vehicle including penalties").grid(row=3, column=2, padx=10, pady=5)
    
    tk.Label(frame_manual_skidpad, text="Runs with a run time without penalties >25 s will be disqualified --> Pag 123 ").grid(row=4, column=2, padx=10, pady=5)


    btn_calculate_manual_skidpad_score = tk.Button(frame_manual_skidpad, text="Calcular", command=calculate_manual_skidpad_score)
    btn_calculate_manual_skidpad_score.grid(row=6, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_manual_skidpad, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2, columnspan=2, pady=10)

    label_result_manual_skidpad = tk.Label(frame_manual_skidpad, text="O resultado aparecerá aqui.")
    label_result_manual_skidpad.grid(row=5, column=2, columnspan=4, pady=10)