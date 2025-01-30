import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_triangle_properties():
    try:
        base = float(entry_base.get()) if entry_base.get() else None
        altura = float(entry_altura.get()) if entry_altura.get() else None
        lado1 = float(entry_lado1.get()) if entry_lado1.get() else None
        lado2 = float(entry_lado2.get()) if entry_lado2.get() else None
        lado3 = float(entry_lado3.get()) if entry_lado3.get() else None
        perimetro = float(entry_perimetro_triangulo.get()) if entry_perimetro_triangulo.get() else None
        area = float(entry_area_triangulo.get()) if entry_area_triangulo.get() else None

        # Cálculo da área, perímetro e outros valores
        if base is not None and altura is not None:
            result_area = (base * altura) / 2
            label_result_triangulo.config(text=f"Área: {result_area:.2f}")

        elif area is not None and base is not None:
            result_altura = (2 * area) / base
            label_result_triangulo.config(text=f"Altura: {result_altura:.2f}")
        
        elif area is not None and altura is not None:
            result_base = (2 * area) / altura
            label_result_triangulo.config(text=f"Base: {result_base:.2f}")
        
        elif lado1 is not None and lado2 is not None and lado3 is not None:
            result_perimetro = lado1 + lado2 + lado3
            label_result_triangulo.config(text=f"Perímetro: {result_perimetro:.2f}")

        elif perimetro is not None and lado1 is not None and lado2 is not None:
            result_lado3 = perimetro - (lado1 + lado2)
            label_result_triangulo.config(text=f"Lado 3: {result_lado3:.2f}")

        elif perimetro is not None and lado2 is not None and lado3 is not None:
            result_lado1 = perimetro - (lado2 + lado3)
            label_result_triangulo.config(text=f"Lado 1: {result_lado1:.2f}")

        elif perimetro is not None and lado1 is not None and lado3 is not None:
            result_lado2 = perimetro - (lado1 + lado3)
            label_result_triangulo.config(text=f"Lado 2: {result_lado2:.2f}")
        else:
            label_result_triangulo.config(text="Por favor, preencha os campos necessários.")
    
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números válidos.")

def clear_triangle_fields():
    # Habilitar os campos para poder limpar
    entry_base.config(state=tk.NORMAL)
    entry_altura.config(state=tk.NORMAL)
    entry_lado1.config(state=tk.NORMAL)
    entry_lado2.config(state=tk.NORMAL)
    entry_lado3.config(state=tk.NORMAL)
    entry_perimetro_triangulo.config(state=tk.NORMAL)
    entry_area_triangulo.config(state=tk.NORMAL)

    # Limpar os campos
    entry_base.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_lado1.delete(0, tk.END)
    entry_lado2.delete(0, tk.END)
    entry_lado3.delete(0, tk.END)
    entry_perimetro_triangulo.delete(0, tk.END)
    entry_area_triangulo.delete(0, tk.END)

    # Reaplicar a desabilitação nos campos conforme necessário
    update_fields_based_on_selection(None)

def update_fields_based_on_selection(event):
    selected_option = combo_formula.get()
    if selected_option == "Área":
        entry_base.config(state=tk.NORMAL)
        entry_altura.config(state=tk.NORMAL)
        entry_lado1.config(state=tk.DISABLED)
        entry_lado2.config(state=tk.DISABLED)
        entry_lado3.config(state=tk.DISABLED)
        entry_perimetro_triangulo.config(state=tk.DISABLED)
        entry_area_triangulo.config(state=tk.NORMAL)
    elif selected_option == "Perimetro":
        entry_base.config(state=tk.DISABLED)
        entry_altura.config(state=tk.DISABLED)
        entry_lado1.config(state=tk.NORMAL)
        entry_lado2.config(state=tk.NORMAL)
        entry_lado3.config(state=tk.NORMAL)
        entry_perimetro_triangulo.config(state=tk.NORMAL)
        entry_area_triangulo.config(state=tk.DISABLED)

def create_triangle_tab():
    global entry_base, entry_altura, entry_lado1, entry_lado2, entry_lado3, entry_perimetro_triangulo, entry_area_triangulo, label_result_triangulo, combo_formula

    #frame_triangulo = ttk.Frame(notebook)
    #notebook.add(frame_triangulo, text="Triângulo")
    frame_triangulo = tk.Toplevel();
    frame_triangulo.title("Triângulo")
    
    tk.Label(frame_triangulo, text="Tipo de dados").grid(row=0, column=2, padx=10, pady=5)
    equations = ["Área", "Perimetro"]
    combo_formula = ttk.Combobox(frame_triangulo, values=equations)
    combo_formula.set("Área")  # Set a default value from the list
    combo_formula.grid(row=1, column=2, padx=10, pady=5)
    combo_formula.bind("<<ComboboxSelected>>", update_fields_based_on_selection)

    tk.Label(frame_triangulo, text="Base").grid(row=0, column=0, padx=10, pady=5)
    entry_base = tk.Entry(frame_triangulo)
    entry_base.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_triangulo, text="Altura").grid(row=1, column=0, padx=10, pady=5)
    entry_altura = tk.Entry(frame_triangulo)
    entry_altura.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_triangulo, text="Lado 1").grid(row=2, column=0, padx=10, pady=5)
    entry_lado1 = tk.Entry(frame_triangulo)
    entry_lado1.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_triangulo, text="Lado 2").grid(row=3, column=0, padx=10, pady=5)
    entry_lado2 = tk.Entry(frame_triangulo)
    entry_lado2.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_triangulo, text="Lado 3").grid(row=4, column=0, padx=10, pady=5)
    entry_lado3 = tk.Entry(frame_triangulo)
    entry_lado3.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame_triangulo, text="Perímetro").grid(row=5, column=0, padx=10, pady=5)
    entry_perimetro_triangulo = tk.Entry(frame_triangulo)
    entry_perimetro_triangulo.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(frame_triangulo, text="Área").grid(row=6, column=0, padx=10, pady=5)
    entry_area_triangulo = tk.Entry(frame_triangulo)
    entry_area_triangulo.grid(row=6, column=1, padx=10, pady=5)

    btn_calculate_triangle_properties = tk.Button(frame_triangulo, text="Calcular", command=calculate_triangle_properties)
    btn_calculate_triangle_properties.grid(row=8, column=0, columnspan=2, pady=10)

    btn_clear_triangle_fields = tk.Button(frame_triangulo, text="Limpar", command=clear_triangle_fields)
    btn_clear_triangle_fields.grid(row=8, column=2, columnspan=2, pady=10)

    label_result_triangulo = tk.Label(frame_triangulo, text="O resultado aparecerá aqui.")
    label_result_triangulo.grid(row=5, column=2, columnspan=2, pady=10)

    # Atualizar os campos inicialmente
    update_fields_based_on_selection(None)

