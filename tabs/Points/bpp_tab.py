import tkinter as tk
from tkinter import messagebox

def calculate_bpp_score():
    try:
        # S 2.4.5: the team's score is the average of the judges' scores
        judges = [float(s) for s in entry_Pteam.get().split(",")]
        Pteam = sum(judges) / len(judges)
        Pmax = float(entry_Pmax.get())

        # S 2.4.6: non-finalists get 65 * Pteam / Pmax (finalists get 75 to 71, S 2.4.7)
        bpp_score = 65 * Pteam / Pmax
        if penalty.get():
            bpp_score -= 15  # S 2.4.2: business model fails S 2.1.1 / S 2.1.2
        bpp_score = max(bpp_score, 0)  # A 1.2.8: 0 <= P <= Pmax

        label_result_bpp.config(text=f"Team score (judges' average): {Pteam:.2f}\nBPP score: {bpp_score:.2f}")
    except (ValueError, ZeroDivisionError):
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_Pteam.delete(0, tk.END)
    entry_Pmax.delete(0, tk.END)
    penalty.set(False)

def create_bpp_tab():
    global entry_Pteam, entry_Pmax, penalty, label_result_bpp

    frame_bpp = tk.Toplevel()
    frame_bpp.title("Business Plan Presentation Points (non-finalists) --> S 2.4, Pag 96")

    tk.Label(frame_bpp, text="Pteam").grid(row=0, column=0, padx=10, pady=5)
    entry_Pteam = tk.Entry(frame_bpp)
    entry_Pteam.grid(row=0, column=1, padx=10, pady=5)
    tk.Label(frame_bpp, text="Team's score, or each judge's score separated by commas (out of 100)").grid(row=0, column=2, padx=10, pady=5)

    tk.Label(frame_bpp, text="Pmax").grid(row=1, column=0, padx=10, pady=5)
    entry_Pmax = tk.Entry(frame_bpp)
    entry_Pmax.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(frame_bpp, text="Highest score of any team NOT in the finals").grid(row=1, column=2, padx=10, pady=5)

    penalty = tk.BooleanVar()
    tk.Checkbutton(frame_bpp, text="Business model fails S 2.1.1 / S 2.1.2 (-15 points)", variable=penalty).grid(row=2, column=1, columnspan=2, sticky="w", padx=10, pady=5)

    btn_calculate_bpp_score = tk.Button(frame_bpp, text="Calcular", command=calculate_bpp_score)
    btn_calculate_bpp_score.grid(row=4, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_bpp, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2, columnspan=2, pady=10)

    label_result_bpp = tk.Label(frame_bpp, text="O resultado aparecerá aqui.")
    label_result_bpp.grid(row=3, column=0, columnspan=4, pady=10)
