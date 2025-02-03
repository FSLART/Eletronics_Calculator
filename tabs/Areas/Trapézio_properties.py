import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_trapezoid_properties():
    try:
        base_maior = float(entry_base_maior.get()) if entry_base_maior.get() else None
        base_menor = float(entry_base_menor.get()) if entry_base_menor.get() else None
        altura = float(entry_altura_trapezio.get()) if entry_altura_trapezio.get() else None
        lado1 = float(entry_lado1_trapezio.get()) if entry_lado1_trapezio.get() else None
        lado2 = float(entry_lado2_trapezio.get()) if entry_lado2_trapezio.get() else None
        perimetro = float(entry_perimetro_trapezio.get()) if entry_perimetro_trapezio.get() else None
        area = float(entry_area_trapezio.get()) if entry_area_trapezio.get() else None

        # Cálculo da área, perímetro e outros valores
        if base_maior is not None and base_menor is not None and altura is not None:
            result_area = ((base_maior + base_menor) * altura) / 2
            label_result_trapezio.config(text=f"Área: {result_area:.2f}")

        elif area is not None and base_menor is not None and altura is not None:
            result_base_maior = (2 * area / altura) - base_menor
            label_result_trapezio.config(text=f"Base Maior: {result_base_maior:.2f}")

        elif area is not None and base_maior is not None and altura is not None:
            result_base_menor = (2 * area / altura) - base_maior
            label_result_trapezio.config(text=f"Base Menor: {result_base_menor:.2f}")

        elif area is not None and base_maior is not None and base_menor is not None:
            result_altura = (2 * area) / (base_maior + base_menor)
            label_result_trapezio.config(text=f"Altura: {result_altura:.2f}")

        if base_maior is not None and base_menor is not None and lado1 is not None and lado2 is not None:
            result_perimetro = base_maior + base_menor + lado1 + lado2
            label_result_trapezio.config(text=f"Perímetro: {result_perimetro:.2f}")

        elif perimetro is not None and base_menor is not None and lado1 is not None and lado2 is not None:
            result_base_maior = perimetro - (base_menor + lado1 + lado2)
            label_result_trapezio.config(text=f"Base Maior: {result_base_maior:.2f}")

        elif perimetro is not None and base_maior is not None and lado1 is not None and lado2 is not None:
            result_base_menor = perimetro - (base_maior + lado1 + lado2)
            label_result_trapezio.config(text=f"Base Menor: {result_base_menor:.2f}")

        elif perimetro is not None and base_maior is not None and base_menor is not None and lado2 is not None:
            result_lado1 = perimetro - (base_maior + base_menor + lado2)
            label_result_trapezio.config(text=f"Lado 1: {result_lado1:.2f}")

        elif perimetro is not None and base_maior is not None and base_menor is not None and lado1 is not None:
            result_lado2 = perimetro - (base_maior + base_menor + lado1)
            label_result_trapezio.config(text=f"Lado 2: {result_lado2:.2f}")
        
        else:
            label_result_trapezio.config(text="Por favor, preencha os campos necessários.")
    
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números válidos.")

def clear_trapezoid_fields():
    # Habilitar os campos para poder limpar
    entry_base_maior.config(state=tk.NORMAL)
    entry_base_menor.config(state=tk.NORMAL)
    entry_altura_trapezio.config(state=tk.NORMAL)
    entry_lado1_trapezio.config(state=tk.NORMAL)
    entry_lado2_trapezio.config(state=tk.NORMAL)
    entry_perimetro_trapezio.config(state=tk.NORMAL)
    entry_area_trapezio.config(state=tk.NORMAL)

    # Limpar os campos
    entry_base_maior.delete(0, tk.END)
    entry_base_menor.delete(0, tk.END)
    entry_altura_trapezio.delete(0, tk.END)
    entry_lado1_trapezio.delete(0, tk.END)
    entry_lado2_trapezio.delete(0, tk.END)
    entry_perimetro_trapezio.delete(0, tk.END)
    entry_area_trapezio.delete(0, tk.END)

    # Reaplicar a desabilitação nos campos conforme necessário
    update_fields_based_on_trapezoid_selection(None)

def update_fields_based_on_trapezoid_selection(event):
    selected_option = combo_formula_trapezio.get()
    if selected_option == "Área":
        entry_base_maior.config(state=tk.NORMAL)
        entry_base_menor.config(state=tk.NORMAL)
        entry_altura_trapezio.config(state=tk.NORMAL)
        entry_lado1_trapezio.config(state=tk.DISABLED)
        entry_lado2_trapezio.config(state=tk.DISABLED)
        entry_perimetro_trapezio.config(state=tk.DISABLED)
        entry_area_trapezio.config(state=tk.DISABLED)
    elif selected_option == "Perimetro":
        entry_base_maior.config(state=tk.NORMAL)
        entry_base_menor.config(state=tk.NORMAL)
        entry_altura_trapezio.config(state=tk.DISABLED)
        entry_lado1_trapezio.config(state=tk.NORMAL)
        entry_lado2_trapezio.config(state=tk.NORMAL)
        entry_perimetro_trapezio.config(state=tk.NORMAL)
        entry_area_trapezio.config(state=tk.DISABLED)

def create_trapezoid_tab():
    global entry_base_maior, entry_base_menor, entry_altura_trapezio, entry_lado1_trapezio, entry_lado2_trapezio, entry_perimetro_trapezio, entry_area_trapezio, label_result_trapezio, combo_formula_trapezio

    #frame_trapezio = ttk.Frame(notebook)
    #notebook.add(frame_trapezio, text="Trapézio")
    frame_trapezio = tk.Toplevel();
    frame_trapezio.title("Trapézio")
    
    tk.Label(frame_trapezio, text="Tipo de dados").grid(row=0, column=2, padx=10, pady=5)
    equations = ["Área", "Perimetro"]
    combo_formula_trapezio = ttk.Combobox(frame_trapezio, values=equations)
    combo_formula_trapezio.set("Área")  # Set a default value from the list
    combo_formula_trapezio.grid(row=1, column=2, padx=10, pady=5)
    combo_formula_trapezio.bind("<<ComboboxSelected>>", update_fields_based_on_trapezoid_selection)

    tk.Label(frame_trapezio, text="Base Maior").grid(row=0, column=0, padx=10, pady=5)
    entry_base_maior = tk.Entry(frame_trapezio)
    entry_base_maior.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_trapezio, text="Base Menor").grid(row=1, column=0, padx=10, pady=5)
    entry_base_menor = tk.Entry(frame_trapezio)
    entry_base_menor.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_trapezio, text="Altura").grid(row=2, column=0, padx=10, pady=5)
    entry_altura_trapezio = tk.Entry(frame_trapezio)
    entry_altura_trapezio.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_trapezio, text="Lado 1").grid(row=3, column=0, padx=10, pady=5)
    entry_lado1_trapezio = tk.Entry(frame_trapezio)
    entry_lado1_trapezio.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_trapezio, text="Lado 2").grid(row=4, column=0, padx=10, pady=5)
    entry_lado2_trapezio = tk.Entry(frame_trapezio)
    entry_lado2_trapezio.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame_trapezio, text="Perímetro").grid(row=5, column=0, padx=10, pady=5)
    entry_perimetro_trapezio = tk.Entry(frame_trapezio)
    entry_perimetro_trapezio.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(frame_trapezio, text="Área").grid(row=6, column=0, padx=10, pady=5)
    entry_area_trapezio = tk.Entry(frame_trapezio)
    entry_area_trapezio.grid(row=6, column=1, padx=10, pady=5)

    btn_calculate_trapezoid_properties = tk.Button(frame_trapezio, text="Calcular", command=calculate_trapezoid_properties)
    btn_calculate_trapezoid_properties.grid(row=8, column=0, columnspan=2, pady=10)

    btn_clear_trapezoid_fields = tk.Button(frame_trapezio, text="Limpar", command=clear_trapezoid_fields)
    btn_clear_trapezoid_fields.grid(row=8, column=2, columnspan=2, pady=10)

    label_result_trapezio = tk.Label(frame_trapezio, text="O resultado aparecerá aqui.")
    label_result_trapezio.grid(row=5, column=2, columnspan=2, pady=10)

    # Atualizar os campos inicialmente
    update_fields_based_on_trapezoid_selection(None)
