import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



def calculate_retangle_properties():
    try:
        l1 = float(entry_l1.get()) if entry_l1.get() else None
        l2 = float(entry_l2.get()) if entry_l2.get() else None
        perimetro = float(entry_perimetro.get()) if entry_perimetro.get() else None
        area = float(entry_area.get()) if entry_area.get() else None
        if perimetro is None and  area is None:
            result1 = (2*l1) + (2*l2)
            result2 = l1 * l2
            label_result_retangulo.config(text=f"Perimento: {result1:.2f} , Area: {result2:.2f} ")
            
        elif l2 is None and area is None:
            result1 = (perimetro/2) - l1
            result2 = l1 * result1
            label_result_retangulo.config(text=f"L2: {result1:.2f} , Area: {result2:.2f} ")
            
        elif l2 is None and perimetro :
            result1 = area/l1
            result2 = (2*l1) + (2*result1)
            label_result_retangulo.config(text=f"L2: {result1:.2f} , Perimetro: {result2:.2f} ")
            
        elif l1 is None and area is None:
            result1 = (perimetro / 2) - l2
            result2 = l2 * result1
            label_result_retangulo.config(text=f"L1: {result1:.2f} , Área: {result2:.2f}")
        
        elif l1 is None and perimetro:
            result1 = area / l2
            result2 = (2 * result1) + (2 * l2)
            label_result_retangulo.config(text=f"L1: {result1:.2f} , Perímetro: {result2:.2f}")
        else:
            label_result_retangulo.config(text="Por favor, preencha os campos necessários.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        
def clear_fields():
    entry_l1.delete(0, tk.END)
    entry_l2.delete(0, tk.END)
    entry_area.delete(0, tk.END)
    entry_perimetro.delete(0, tk.END)

def create_retangulo_tab():
    global entry_l1, entry_l2, entry_perimetro, entry_area, label_result_retangulo
     
    # Tab 1: Retângulo
    #frame_retangulo = ttk.Frame(notebook)
    #notebook.add(frame_retangulo, text="Retângulo")
    frame_retangulo = tk.Toplevel();
    frame_retangulo.title("Retângulo")	

    tk.Label(frame_retangulo, text="L1").grid(row=0, column=0, padx=10, pady=5)
    entry_l1 = tk.Entry(frame_retangulo)
    entry_l1.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_retangulo, text="L2").grid(row=1, column=0, padx=10, pady=5)
    entry_l2 = tk.Entry(frame_retangulo)
    entry_l2.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_retangulo, text="Perimetro").grid(row=2, column=0, padx=10, pady=5)
    entry_perimetro = tk.Entry(frame_retangulo)
    entry_perimetro.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_retangulo, text="Area").grid(row=3, column=0, padx=10, pady=5)
    entry_area = tk.Entry(frame_retangulo)
    entry_area.grid(row=3, column=1, padx=10, pady=5)

    btn_calculate_retangle_properties = tk.Button(frame_retangulo, text="Calcular", command=calculate_retangle_properties)
    btn_calculate_retangle_properties.grid(row=5, column=0, columnspan=2, pady=10)

    btn_calculate_retangle_properties = tk.Button(frame_retangulo, text="Limpar", command=clear_fields)
    btn_calculate_retangle_properties.grid(row=5, column=2, columnspan=2, pady=10)


    label_result_retangulo = tk.Label(frame_retangulo, text="O resultado aparecerá aqui.")
    label_result_retangulo.grid(row=2, column=3, columnspan=2, pady=10)
