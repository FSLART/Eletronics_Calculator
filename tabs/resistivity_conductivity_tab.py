import tkinter as tk
from tkinter import ttk


def create_resistivity_conductivity_window():
    # tab = ttk.Frame(notebook)
    # notebook.add(tab, text="Resistivity & Conductivity")
    tab = tk.Toplevel()
    tab.title("Resistivity & Conductivity")

    # Resistivity input
    resistivity_label = ttk.Label(tab, text="Resistivity (Ω·m):")
    resistivity_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    resistivity_entry = ttk.Entry(tab)
    resistivity_entry.grid(row=0, column=1, padx=10, pady=5)

    # Conductivity input
    conductivity_label = ttk.Label(tab, text="Conductivity (S/m):")
    conductivity_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    conductivity_entry = ttk.Entry(tab)
    conductivity_entry.grid(row=1, column=1, padx=10, pady=5)

    # Length input
    length_label = ttk.Label(tab, text="Length:")
    length_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    length_entry = ttk.Entry(tab)
    length_entry.grid(row=2, column=1, padx=10, pady=5)
    length_unit_var = tk.StringVar(value="m")
    length_unit_cb = ttk.Combobox(
        tab, textvariable=length_unit_var, values=["m", "cm", "mm"], width=5
    )
    length_unit_cb.grid(row=2, column=2, padx=5, pady=5)

    # Area input
    area_label = ttk.Label(tab, text="Area:")
    area_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    area_entry = ttk.Entry(tab)
    area_entry.grid(row=3, column=1, padx=10, pady=5)
    area_unit_var = tk.StringVar(value="m²")
    area_unit_cb = ttk.Combobox(
        tab, textvariable=area_unit_var, values=["m²", "cm²", "mm²"], width=5
    )
    area_unit_cb.grid(row=3, column=2, padx=5, pady=5)

    # Dropdown to select calculation type
    calc_type_var = tk.StringVar(value="Conductivity")
    calc_type_cb = ttk.Combobox(
        tab,
        textvariable=calc_type_var,
        values=["Conductivity", "Resistivity"],
        width=15,
    )
    calc_type_cb.grid(row=4, column=0, padx=10, pady=10)

    # Function to update the state of the entry fields based on the dropdown selection
    def update_entry_state(*args):
        if calc_type_var.get() == "Conductivity":
            resistivity_entry.config(state="normal")
            conductivity_entry.config(state="disabled")
        elif calc_type_var.get() == "Resistivity":
            resistivity_entry.config(state="disabled")
            conductivity_entry.config(state="normal")

    calc_type_var.trace("w", update_entry_state)
    update_entry_state()

    # Calculate based on dropdown selection
    def calc_based_on_selection():
        try:
            length_str = length_entry.get().strip()
            area_str = area_entry.get().strip()
            resistivity_str = resistivity_entry.get().strip()
            conductivity_str = conductivity_entry.get().strip()

            if not length_str or not area_str:
                raise ValueError("Length and area must be provided")

            length = float(length_str)
            area = float(area_str)

            # Convert length to meters
            if length_unit_var.get() == "cm":
                length /= 100
            elif length_unit_var.get() == "mm":
                length /= 1000

            # Convert area to square meters
            if area_unit_var.get() == "cm²":
                area /= 10000
            elif area_unit_var.get() == "mm²":
                area /= 1000000

            if calc_type_var.get() == "Conductivity":
                if not resistivity_str:
                    raise ValueError("Resistivity must be provided")
                rho = float(resistivity_str)
                if rho != 0:
                    sigma = 1.0 / rho
                    conductivity_entry.config(state="normal")
                    conductivity_entry.delete(0, tk.END)
                    conductivity_entry.insert(0, f"{sigma:.4e}")
                    conductivity_entry.config(state="disabled")
                    R = rho * length / area
                    resistance_entry.delete(0, tk.END)
                    resistance_entry.insert(0, f"{R:.4e}")
                else:
                    conductivity_entry.config(state="normal")
                    conductivity_entry.delete(0, tk.END)
                    conductivity_entry.insert(0, "Infinity")
                    conductivity_entry.config(state="disabled")
            elif calc_type_var.get() == "Resistivity":
                if not conductivity_str:
                    raise ValueError("Conductivity must be provided")
                sigma = float(conductivity_str)
                if sigma != 0:
                    rho = 1.0 / sigma
                    resistivity_entry.config(state="normal")
                    resistivity_entry.delete(0, tk.END)
                    resistivity_entry.insert(0, f"{rho:.4e}")
                    resistivity_entry.config(state="disabled")
                    R = rho * length / area
                    resistance_entry.delete(0, tk.END)
                    resistance_entry.insert(0, f"{R:.4e}")
                else:
                    resistivity_entry.config(state="normal")
                    resistivity_entry.delete(0, tk.END)
                    resistivity_entry.insert(0, "Infinity")
                    resistivity_entry.config(state="disabled")
        except ValueError as e:
            if calc_type_var.get() == "Conductivity":
                conductivity_entry.config(state="normal")
                conductivity_entry.delete(0, tk.END)
                conductivity_entry.insert(0, str(e))
                conductivity_entry.config(state="disabled")
            elif calc_type_var.get() == "Resistivity":
                resistivity_entry.config(state="normal")
                resistivity_entry.delete(0, tk.END)
                resistivity_entry.insert(0, str(e))
                resistivity_entry.config(state="disabled")

    # Button to calculate based on selection
    calc_button = ttk.Button(tab, text="Calculate", command=calc_based_on_selection)
    calc_button.grid(row=4, column=1, padx=10, pady=10)

    # Button to clear all fields
    def clear_fields():
        resistivity_entry.config(state="normal")
        conductivity_entry.config(state="normal")
        resistivity_entry.delete(0, tk.END)
        conductivity_entry.delete(0, tk.END)
        length_entry.delete(0, tk.END)
        area_entry.delete(0, tk.END)
        resistance_entry.delete(0, tk.END)
        update_entry_state()

    clear_button = ttk.Button(tab, text="Clear", command=clear_fields)
    clear_button.grid(row=4, column=2, padx=10, pady=10)

    # Resistance output
    resistance_label = ttk.Label(tab, text="Resistance (Ω):")
    resistance_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    resistance_entry = ttk.Entry(tab)
    resistance_entry.grid(row=5, column=1, padx=10, pady=5)

    # Equation formula
    calc_eq_label = ttk.Label(tab, text="σ = 1 / ρ")
    calc_eq_label.grid(row=1, column=3, columnspan=2, padx=10, pady=5)

    # Equation formula of resistance and units
    resistance_eq_label = ttk.Label(tab, text="R = ρ * L / A")
    resistance_eq_label.grid(row=5, column=3, columnspan=2, padx=10, pady=5)
