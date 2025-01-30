import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_volume_properties():
    try:
        area = float(entry_area.get()) if entry_area.get() else None
        altura = float(entry_altura.get()) if entry_altura.get() else None
        volume = float(entry_volume.get()) if entry_volume.get() else None

        if area is not None and altura is not None:
            result_volume = area * altura
            label_result_volume.config(text=f"Volume: {result_volume:.2f}")

        elif volume is not None and altura is not None:
            result_area = volume / altura
            label_result_volume.config(text=f"Área: {result_area:.2f}")

        elif volume is not None and area is not None:
            result_altura = volume / area
            label_result_volume.config(text=f"Altura: {result_altura:.2f}")

        else:
            label_result_volume.config(text="Por favor, preencha os campos necessários.")

    except ValueError:
        messagebox.showerror("Input Error", "Por favor, insira números válidos.")

def clear_fields():
    entry_area.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_volume.delete(0, tk.END)

def create_volume_tab():
    global entry_area, entry_altura, entry_volume, label_result_volume

    # Tab: Volume
    #frame_volume = ttk.Frame(notebook)
    #notebook.add(frame_volume, text="Volume")
    frame_volume = tk.Toplevel();
    frame_volume.title("Volume")

    tk.Label(frame_volume, text="Área").grid(row=0, column=0, padx=10, pady=5)
    entry_area = tk.Entry(frame_volume)
    entry_area.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_volume, text="Altura").grid(row=1, column=0, padx=10, pady=5)
    entry_altura = tk.Entry(frame_volume)
    entry_altura.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_volume, text="Volume").grid(row=2, column=0, padx=10, pady=5)
    entry_volume = tk.Entry(frame_volume)
    entry_volume.grid(row=2, column=1, padx=10, pady=5)

    btn_calculate_volume_properties = tk.Button(frame_volume, text="Calcular", command=calculate_volume_properties)
    btn_calculate_volume_properties.grid(row=4, column=0, columnspan=2, pady=10)

    btn_clear_fields = tk.Button(frame_volume, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2, columnspan=2, pady=10)

    label_result_volume = tk.Label(frame_volume, text="O resultado aparecerá aqui.")
    label_result_volume.grid(row=3, column=0, columnspan=4, pady=10)
