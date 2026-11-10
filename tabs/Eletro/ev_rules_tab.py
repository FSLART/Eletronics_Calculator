import math
import tkinter as tk
from tkinter import messagebox

# Table 3: (up to voltage, clearance, creepage general, creepage with conformal coating) in mm
SPACING = [(50, 1.0, 4, 1.0), (150, 1.0, 5, 1.0), (300, 1.5, 10, 2.0), (600, 3.0, 20, 4.0)]

FIELDS = [
    "Cells in series (whole accumulator)",
    "Cells in parallel",
    "Max cell voltage [V]",
    "Nominal cell capacity [Ah]",
    "Cells in series per section",
    "Cell mass [g] (optional)",
    "Intermediate circuit capacitance [µF] (optional)",
    "Pre-charge resistor [Ω] (optional)",
    "Discharge resistor [Ω] (optional)",
]


def ok(condition):
    return "OK" if condition else "FAIL"


def ev_rules_report(ns, np_, v_cell, cap_ah, ns_section, cell_mass_g=None, c_uf=None, r_pre=None, r_dis=None):
    """Checks an EV accumulator against the FS Rules 2027 numeric limits, one line per rule."""
    u_max = ns * v_cell
    u_section = ns_section * v_cell
    e_cell = v_cell * cap_ah * 3600  # EV 5.1.2: cell energy = max cell voltage x nominal capacity [J]
    e_section = e_cell * ns_section * np_ / 1e6
    r_tsmp = 5e3 if u_max < 200 else 10e3 if u_max <= 400 else 15e3
    test_voltage = 250 if u_max <= 250 else 500 if u_max <= 500 else 1000

    lines = [
        f"Max TS voltage: {u_max:.1f} V  (<= 600 V: {ok(u_max <= 600)})  EV 4.1.1",
        f"Accumulator energy: {e_cell * ns * np_ / 3.6e6:.3f} kWh = {e_cell * ns * np_ / 1e6:.2f} MJ",
        f"Section: {u_section:.1f} V (<= 120 V: {ok(u_section <= 120)}), {e_section:.3f} MJ (<= 6 MJ: {ok(e_section <= 6)})  EV 5.3.4",
    ]
    if cell_mass_g:
        mass = cell_mass_g * ns_section * np_ / 1000
        lines.append(f"Section cell mass: {mass:.2f} kg (<= 12 kg: {ok(mass <= 12)})  EV 5.3.4")
    lines += [
        f"Current for 80 kW at Umax: {80e3 / u_max:.1f} A  (EV 2.2.1, current limit 500 A EV 2.2.2)",
        f"BSPD current threshold (5 kW at Umax): {5e3 / u_max:.2f} A  T 11.7",
        f"IMD response value (500 Ω/V): {500 * u_max / 1e3:.1f} kΩ  EV 6.3.7",
        f"IMD test fault resistor (250 Ω/V): {250 * u_max / 1e3:.1f} kΩ, trip within 30 s  IN 4.2",
        f"Insulation test: {test_voltage} V, min {500 * u_max / 1e3:.1f} kΩ  IN 4.1",
        f"TSMP resistor: {r_tsmp / 1e3:.0f} kΩ each, rated >= {u_max ** 2 / (4 * r_tsmp):.2f} W (both TSMPs shorted)  EV 4.7.6",
    ]
    spacing = next((s for s in SPACING if u_max <= s[0]), None)
    if spacing:
        lines.append(f"TS/LV spacing: clearance {spacing[1]} mm, creepage {spacing[2]} mm ({spacing[3]} mm with conformal coating)  Table 3")
    if c_uf and r_pre:
        tau = r_pre * c_uf * 1e-6
        lines.append(f"Pre-charge to 95 % ({0.95 * u_max:.1f} V): t = RC·ln(20) = {tau * math.log(20):.3f} s  EV 5.7.1")
    if c_uf and r_dis and u_max > 60:
        decay = c_uf * 1e-6 * math.log(u_max / 60)
        t = r_dis * decay
        lines.append(f"Discharge to 60 V: {t:.3f} s (< 5 s: {ok(t < 5)}), max discharge R = {5 / decay:.0f} Ω  EV 6.1.5")
    return lines


def calculate():
    try:
        values = [float(entry.get()) if entry.get() else None for entry in entries]
        if None in values[:5]:
            label_result.config(text="Fill in the first 5 fields.")
            return
        label_result.config(text="\n".join(ev_rules_report(*values)))
    except (ValueError, ZeroDivisionError):
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def clear_fields():
    for entry in entries:
        entry.delete(0, tk.END)
    label_result.config(text="Result will appear here.")


def create_ev_rules_window():
    global entries, label_result

    ev_rules_window = tk.Toplevel()
    ev_rules_window.title("EV Rules Check (FS Rules 2027)")

    entries = []
    for row, text in enumerate(FIELDS):
        tk.Label(ev_rules_window, text=text).grid(row=row, column=0, sticky="w", padx=10, pady=3)
        entry = tk.Entry(ev_rules_window)
        entry.grid(row=row, column=1, padx=10, pady=3)
        entries.append(entry)

    tk.Button(ev_rules_window, text="Calculate", command=calculate, bg="green", fg="white").grid(row=len(FIELDS), column=1, pady=10)
    tk.Button(ev_rules_window, text="Clear", command=clear_fields).grid(row=len(FIELDS), column=0, pady=10)

    label_result = tk.Label(ev_rules_window, text="Result will appear here.", justify="left", font=("Consolas", 10))
    label_result.grid(row=len(FIELDS) + 1, column=0, columnspan=2, sticky="w", padx=10, pady=10)
