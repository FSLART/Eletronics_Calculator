import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_manual_skidpad_score():
    try:
        # 1) Ler inputs
        Pmax = float(entry_Pmax.get()) if entry_Pmax.get() else None
        Tteam_raw = float(entry_Tteam.get()) if entry_Tteam.get() else None # sem penalizações
        Tmin = float(entry_Tmax.get()) if entry_Tmax.get() else None
        doo = float(entry_doo.get()) if entry_doo.get() else 0.0

        if Pmax is None or Tteam_raw is None or Tmin is None:
            label_result_manual_skidpad.config(text="Põe lá os campos necessários faz favor.")
            return
        # 2) Aplicar penalizações DOO (0.2 s por cone)
        Tteam_with_penalties = Tteam_raw + 0.2 * doo
        # 3) Parâmetros da disciplina (Skidpad manual)
        Pmin = 0.05 * Pmax          # 5% de Pmax
        Tmax = 1.35 * Tmin          # Skidpad manual → Tmax = 1.35 × Tmin
        # 4) Cap em Tmax: tempos piores que Tmax não baixam mais que Pmin
        Tteam_effective = min(Tteam_with_penalties, Tmax)
        # 5) Fórmula oficial de 2026:
        # SCORE = (Pmax - Pmin) * ((Tmax - Tteam) / (Tmax - Tmin))^2 + Pmin
        manual_skidpad_score = (Pmax - Pmin) * ((Tmax - Tteam_effective) / (Tmax - Tmin))**2 + Pmin

        label_result_manual_skidpad.config(
            text=f"Manual Skidpad score: {manual_skidpad_score:.3f}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Já disse! Insere números válidos.")
        
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
    entry_Pmax.insert(0, "75")
    tk.Label(frame_manual_skidpad, text="Maximum points for Skidpad manual (Pmax = 75, FSG 2026)").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(frame_manual_skidpad, text="Tteam [s]").grid(row=1, column=0, padx=10, pady=5)
    entry_Tteam = tk.Entry(frame_manual_skidpad)
    entry_Tteam.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_manual_skidpad, text="Team's best manual mode time").grid(row=1, column=2, padx=10, pady=5)

    tk.Label(frame_manual_skidpad, text="DOO").grid(row=2, column=0, padx=10, pady=5)
    entry_doo = tk.Entry(frame_manual_skidpad)
    entry_doo.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(frame_manual_skidpad, text="Cones Dow Or Out --> Pag 132").grid(row=2, column=2, padx=10, pady=5)

    tk.Label(frame_manual_skidpad, text="Tmin [s]").grid(row=3, column=0, padx=10, pady=5)
    entry_Tmax = tk.Entry(frame_manual_skidpad) 
    entry_Tmax.grid(row=3, column=1, padx=10, pady=5)
    tk.Label(frame_manual_skidpad, text="Tmin = best event time including penalties (Tmax = 1.35 × Tmin)").grid(row=3, column=2, padx=10, pady=5)


    btn_calculate_manual_skidpad_score = tk.Button(frame_manual_skidpad, text="Calcular", command=calculate_manual_skidpad_score)
    btn_calculate_manual_skidpad_score.grid(row=6, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_manual_skidpad, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2, columnspan=2, pady=10)

    label_result_manual_skidpad = tk.Label(frame_manual_skidpad, text="O resultado aparecerá aqui.")
    label_result_manual_skidpad.grid(row=5, column=2, columnspan=4, pady=10)