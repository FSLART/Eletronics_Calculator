import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import TclError

def calculate_dc_skidpad_score():
    try:
        # Read inputs
        Pmax = float(entry_Pmax.get()) if entry_Pmax.get() else None
        raw_Tteam = float(entry_Tteam.get()) if entry_Tteam.get() else None
        Tmin = float(entry_Tmax.get()) if entry_Tmax.get() else None  # actually Tmin (fastest time)
        doo = float(entry_doo.get()) if entry_doo.get() else 0.0

        if Pmax is not None and raw_Tteam is not None and Tmin is not None:
            # 25 s DISQUALIFICATION RULE (D9.2.1): based on raw time WITHOUT penalties
            if raw_Tteam > 25:
                label_result_dc_skidpad.config(text="DISQUALIFIED: time without penalties > 25s -> Did the stopwatch fell asleep?")
                return

            # DOO penalties: 0.2 s per cone (D10.1.7)
            Tteam_with_penalties = raw_Tteam + 0.2 * doo

            # DC-only Skidpad parameters (Table 11)
            Pmin = 0.05 * Pmax
            Tmax = 1.7 * Tmin

            # Cap team time at Tmax as per D9.1.1
            Tteam_effective = min(Tteam_with_penalties, Tmax)

            # Default dynamic scoring formula (D9.1.1):
            # SCORE = (Pmax - Pmin) * ((Tmax - Tteam)/(Tmax - Tmin))^2 + Pmin
            dc_skidpad_score = (Pmax - Pmin) * ((Tmax - Tteam_effective) / (Tmax - Tmin))**2 + Pmin

            label_result_dc_skidpad.config(text=f"DC Skidpad score: {dc_skidpad_score:.3f}")
        else:
            label_result_dc_skidpad.config(text="Por favor, preencha os campos necessários.")
    except (ValueError, TclError):
        messagebox.showerror("Input Error", "Erro nos campos ou janela inválida. Volta a abrir o DC Skidpad e tenta de novo.")

def clear_fields():
    entry_Pmax.delete(0, tk.END)
    entry_Tteam.delete(0, tk.END)
    entry_Tmax.delete(0, tk.END)

def create_dc_skidpad_tab():
    global entry_Pmax, entry_Tteam, entry_Tmax, label_result_dc_skidpad, entry_doo, doo

    frame_dc_skidpad = tk.Toplevel()
    frame_dc_skidpad.title("DC Skidpad Scoring (FSG 2026 - page 132)")

    tk.Label(frame_dc_skidpad, text="Pmax").grid(row=0, column=0, padx=10, pady=5)
    entry_Pmax = tk.Entry(frame_dc_skidpad)
    entry_Pmax.grid(row=0, column=1, padx=10, pady=5)
    entry_Pmax.insert(0, "75")
    tk.Label(frame_dc_skidpad, text="Maximum points for the discipline - page 10").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="Tteam [s]").grid(row=1, column=0, padx=10, pady=5)
    entry_Tteam = tk.Entry(frame_dc_skidpad)
    entry_Tteam.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_dc_skidpad, text="Team’s best autonomous mode time including penalties (D9.1.1) - page 132").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="DOO").grid(row=2, column=0, padx=10, pady=5)
    entry_doo = tk.Entry(frame_dc_skidpad)
    entry_doo.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_dc_skidpad, text="Down Or Out cones (DOO) – page 134 - D10.1.7").grid(row=2, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="Tmin [s]").grid(row=3, column=0, padx=10, pady=5)
    entry_Tmax = tk.Entry(frame_dc_skidpad) 
    entry_Tmax.grid(row=3, column=1, padx=10, pady=5)
    tk.Label(frame_dc_skidpad, text="Tmin = best event time - Table 11").grid(row=3, column=2, padx=10, pady=5)

    tk.Label(frame_dc_skidpad, text="Runs with time without penalties > 25 s are DISQUALIFIED - page 132 (D9.2.1)").grid(row=4, column=2, padx=10, pady=5)
    
    

    btn_calculate_dc_skidpad_score = tk.Button(frame_dc_skidpad, text="Calcular", command=calculate_dc_skidpad_score)
    btn_calculate_dc_skidpad_score.grid(row=6, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_dc_skidpad, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2, columnspan=2, pady=10)

    label_result_dc_skidpad = tk.Label(frame_dc_skidpad, text="O resultado aparecerá aqui.")
    label_result_dc_skidpad.grid(row=5, column=2, columnspan=4, pady=10)