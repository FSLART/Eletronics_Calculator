import tkinter as tk
from tkinter import messagebox
from tabs.points_tab import default_scoring_formula

def acceleration_calculation():
    try:
        PMAX = 75   
        Rdv = int(entry_Rdv.get())
        NAll = int(entry_NAll.get())
        if Rdv < 1 or Rdv > NAll:
            messagebox.showerror("Error", "Ranking must be between 1 and NAll.")
            return
        score = PMAX * ((NAll + 1 - Rdv) / NAll)
        # messagebox.showinfo("Result", f"Your Acceleration DV Score = {score:.2f}")
        return score

    except ValueError:
        return -1
def dc_acceleration_calculation():
    try:
        pMax = 75
        tMaxFactor = 2.25
        pMinFactor = 0.05
        tTeam_value = float(tTeam.get())
        Tmin_value = float(Tmin.get())
        return default_scoring_formula(tMaxFactor, Tmin_value, pMinFactor, pMax, tTeam_value)

    except ValueError:
        return -1

def calculate():
    dv_acceleration_points = acceleration_calculation()
    dc_acceleration_points = dc_acceleration_calculation()

    messagebox.showinfo("Results", f"Acceleration DV Points: {dv_acceleration_points:.2f}\nDC Acceleration Points: {dc_acceleration_points:.2f}")

def clear_fields():
    entry_Rdv.delete(0, tk.END)
    entry_NAll.delete(0, tk.END)

def create_accelaration_points_window():
    acceleration_points_window = tk.Toplevel()
    acceleration_points_window.title("Acceleration Points")
    acceleration_points_window.geometry("600x300")

    global entry_Rdv, entry_NAll, tTeam, Tmin

    tk.Label(acceleration_points_window, text = "DV Acceleration", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=5)

    tk.Label(acceleration_points_window, text="Team's Ranking (Rdv):").grid(row=1, column=0, padx=10, pady=5)
    entry_Rdv = tk.Entry(acceleration_points_window)
    entry_Rdv.grid(row=1, column=1, padx=10, pady=5) 

    tk.Label(acceleration_points_window, text="Total Teams (NAll):").grid(row=2, column=0, padx=10, pady=5)
    entry_NAll = tk.Entry(acceleration_points_window)
    entry_NAll.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(acceleration_points_window, text = "DC Acceleration", font=("Arial", 14, "bold")).grid(row=3, column=0, padx=10, pady=5)


    tk.Label(acceleration_points_window, text="Team time with penalties (tTeam):").grid(row=4, column=0, padx=10, pady=5)
    tTeam = tk.Entry(acceleration_points_window)
    tTeam.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(acceleration_points_window, text="Fastest team time (Tmin):").grid(row=5, column=0, padx=10, pady=5)
    Tmin = tk.Entry(acceleration_points_window)
    Tmin.grid(row=5, column=1, padx=10, pady=5)
    tk.Button(acceleration_points_window, text="Calculate", command=calculate, bg="green", fg="white").grid(row=6, column=1, pady=10)
    tk.Button(acceleration_points_window, text="Clear", command=clear_fields).grid(row=6, column=0, pady=10)