import tkinter as tk
from tkinter import messagebox

def acceleration_calculation():
    try:
        PMAX = 50   
        Rdv = int(entry_Rdv.get())
        NAll = int(entry_NAll.get())
        if Rdv < 1 or Rdv > NAll:
            messagebox.showerror("Error", "Ranking must be between 1 and NAll.")
            return
        score = PMAX * ((NAll + 1 - Rdv) / NAll)
        messagebox.showinfo("Result", f"Your Acceleration DV Score = {score:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def clear_fields():
    entry_Rdv.delete(0, tk.END)
    entry_NAll.delete(0, tk.END)

def create_accelaration_points_window():
    acceleration_points_window = tk.Toplevel()
    acceleration_points_window.title("Acceleration Points")
    acceleration_points_window.geometry("400x200")

    global entry_Rdv, entry_NAll

    tk.Label(acceleration_points_window, text="Team's Ranking (Rdv):").grid(row=0, column=0, padx=10, pady=5)
    entry_Rdv = tk.Entry(acceleration_points_window)
    entry_Rdv.grid(row=0, column=1, padx=10, pady=5) 

    tk.Label(acceleration_points_window, text="Total Teams (NAll):").grid(row=1, column=0, padx=10, pady=5)
    entry_NAll = tk.Entry(acceleration_points_window)
    entry_NAll.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(acceleration_points_window, text="Calculate", command=acceleration_calculation, bg="green", fg="white").grid(row=3, column=1, pady=10)
    tk.Button(acceleration_points_window, text="Clear", command=clear_fields).grid(row=3, column=0, pady=10)

