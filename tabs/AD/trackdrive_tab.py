import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def calculate():
    try:
        tMax = float(entry_Tmax.get()) if entry_Tmax.get() else None
        tTeam= float(entry_Tteam.get()) if entry_Tteam.get() else None
        tLaps = int(entry_Tlaps.get()) if entry_Tlaps.get() else None
        uss = int(entry_uss.get()) if entry_uss.get() else 0
        pMax = 200
        if tMax is not None and tTeam is not None and tLaps is not None and tLaps <=10:
            # Tmax = 2 * fastest time; a DNF (0) still gets the lap points (D 9.3.3, D 9.3.4)
            if tTeam <= 0 or tTeam > 2*tMax:
                tTeam = 2*tMax
            total= 0.75*pMax*(2*tMax/tTeam -1)+ tLaps*0.025*pMax
            # USS is -50 points (D 10.1.7), result bounded by 0 <= P <= Pmax (A 1.2.8)
            total = min(max(total - 50*uss, 0), pMax)
            messagebox.showinfo("Results", f"Total Points: {total}")
        else:
            raise ValueError("Please enter all values.")
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")


def clear_fields():
    entry_Tmax.delete(0, tk.END)
    entry_Tteam.delete(0, tk.END)
    entry_Tlaps.delete(0, tk.END)
    entry_uss.delete(0, tk.END)


def create_trakdrive_points_window():
    trackdrive_points_window = tk.Toplevel() 
    trackdrive_points_window.title("TrackDrive Points")
    trackdrive_points_window.geometry("700x400")

    global entry_Tmax, entry_Tteam, entry_Tlaps, entry_uss

    tk.Label(trackdrive_points_window, text="Fastest team time:").grid(row=0, column=0, padx=10, pady=5)
    entry_Tmax = tk.Entry(trackdrive_points_window)
    entry_Tmax.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(trackdrive_points_window, text="My team's corrected time (0 if DNF):").grid(row=1, column=0, padx=10, pady=5)
    entry_Tteam = tk.Entry(trackdrive_points_window)
    entry_Tteam.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(trackdrive_points_window, text="Number of laps my team completed:").grid(row=2, column=0, padx=10, pady=5)
    entry_Tlaps = tk.Entry(trackdrive_points_window)
    entry_Tlaps.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(trackdrive_points_window, text="Unsafe stops (USS, -50 points each):").grid(row=3, column=0, padx=10, pady=5)
    entry_uss = tk.Entry(trackdrive_points_window)
    entry_uss.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(trackdrive_points_window, text="Calculate", command=calculate, bg="green", fg="white").grid(row=4, column=1, columnspan=2, pady=10)
    tk.Button(trackdrive_points_window, text="Clear", command=clear_fields).grid(row=4, column=0, columnspan=2, pady=10)
