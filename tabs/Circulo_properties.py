import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def calculate_circle_properties():
    try:
        raio = float(entry_raio.get()) if entry_raio.get() else None
        diametro = float(entry_diametro.get()) if entry_diametro.get() else None
        perimetro = float(entry_perimetro_circulo.get()) if entry_perimetro_circulo.get() else None
        area = float(entry_area_circulo.get()) if entry_area_circulo.get() else None
        
        if raio is not None:
            result_diametro = 2 * raio
            result_perimetro = 2 * math.pi * raio
            result_area = math.pi * (raio ** 2)
            label_result_circulo.config(text=f"Diâmetro: {result_diametro:.2f}, Perímetro: {result_perimetro:.2f}, Área: {result_area:.2f}")
        
        elif diametro is not None:
            raio = diametro / 2
            result_perimetro = 2 * math.pi * raio
            result_area = math.pi * (raio ** 2)
            label_result_circulo.config(text=f"Raio: {raio:.2f}, Perímetro: {result_perimetro:.2f}, Área: {result_area:.2f}")
        
        elif perimetro is not None:
            raio = perimetro / (2 * math.pi)
            result_diametro = 2 * raio
            result_area = math.pi * (raio ** 2)
            label_result_circulo.config(text=f"Raio: {raio:.2f}, Diâmetro: {result_diametro:.2f}, Área: {result_area:.2f}")
        
        elif area is not None:
            raio = math.sqrt(area / math.pi)
            result_diametro = 2 * raio
            result_perimetro = 2 * math.pi * raio
            label_result_circulo.config(text=f"Raio: {raio:.2f}, Diâmetro: {result_diametro:.2f}, Perímetro: {result_perimetro:.2f}")
        
        else:
            label_result_circulo.config(text="Por favor, preencha pelo menos um campo.")
    
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números válidos.")

def clear_circle_fields():
    entry_raio.delete(0, tk.END)
    entry_diametro.delete(0, tk.END)
    entry_perimetro_circulo.delete(0, tk.END)
    entry_area_circulo.delete(0, tk.END)

def create_circulo_tab():
    global entry_raio, entry_diametro, entry_perimetro_circulo, entry_area_circulo, label_result_circulo
    
    #frame_circulo = ttk.Frame(notebook)
    #notebook.add(frame_circulo, text="Círculo")
    frame_circulo = tk.Toplevel();
    frame_circulo.title("Círculo")

    tk.Label(frame_circulo, text="Raio").grid(row=0, column=0, padx=10, pady=5)
    entry_raio = tk.Entry(frame_circulo)
    entry_raio.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_circulo, text="Diâmetro").grid(row=1, column=0, padx=10, pady=5)
    entry_diametro = tk.Entry(frame_circulo)
    entry_diametro.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_circulo, text="Perímetro").grid(row=2, column=0, padx=10, pady=5)
    entry_perimetro_circulo = tk.Entry(frame_circulo)
    entry_perimetro_circulo.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_circulo, text="Área").grid(row=3, column=0, padx=10, pady=5)
    entry_area_circulo = tk.Entry(frame_circulo)
    entry_area_circulo.grid(row=3, column=1, padx=10, pady=5)

    btn_calculate_circle_properties = tk.Button(frame_circulo, text="Calcular", command=calculate_circle_properties)
    btn_calculate_circle_properties.grid(row=5, column=0, columnspan=2, pady=10)

    btn_clear_circle_fields = tk.Button(frame_circulo, text="Limpar", command=clear_circle_fields)
    btn_clear_circle_fields.grid(row=5, column=2, columnspan=2, pady=10)

    label_result_circulo = tk.Label(frame_circulo, text="O resultado aparecerá aqui.")
    label_result_circulo.grid(row=2, column=2, columnspan=2, pady=10)
