import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

# Função para calcular os valores usando a Lei dos Senos
def calculate_sine_law_properties():
    try:
        # Obtendo os valores inseridos
        a = float(entry_a.get()) if entry_a.get() else None
        b = float(entry_b.get()) if entry_b.get() else None
        c = float(entry_c.get()) if entry_c.get() else None
        A = float(entry_A.get()) if entry_A.get() else None
        B = float(entry_B.get()) if entry_B.get() else None
        C = float(entry_C.get()) if entry_C.get() else None

        # Verificando quais valores foram preenchidos e calculando os valores faltantes
        if a is not None and A is not None and B is not None:
            result_b = (b * math.sin(math.radians(B))) / math.sin(math.radians(A))
            result_c = (c * math.sin(math.radians(C))) / math.sin(math.radians(A))
            label_result_sine_law.config(text=f"B: {result_b:.2f}, C: {result_c:.2f}")
        
        elif b is not None and B is not None and A is not None:
            result_a = (a * math.sin(math.radians(A))) / math.sin(math.radians(B))
            result_c = (c * math.sin(math.radians(C))) / math.sin(math.radians(B))
            label_result_sine_law.config(text=f"A: {result_a:.2f}, C: {result_c:.2f}")

        elif c is not None and C is not None and A is not None:
            result_a = (a * math.sin(math.radians(A))) / math.sin(math.radians(C))
            result_b = (b * math.sin(math.radians(B))) / math.sin(math.radians(C))
            label_result_sine_law.config(text=f"A: {result_a:.2f}, B: {result_b:.2f}")

        elif a is not None and A is not None and C is not None:
            result_b = (b * math.sin(math.radians(B))) / math.sin(math.radians(A))
            result_c = (c * math.sin(math.radians(C))) / math.sin(math.radians(A))
            label_result_sine_law.config(text=f"B: {result_b:.2f}, C: {result_c:.2f}")
        
        else:
            label_result_sine_law.config(text="Por favor, preencha os campos necessários.")
    
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números válidos.")

# Função para limpar os campos de entrada
def clear_fields():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_A.delete(0, tk.END)
    entry_B.delete(0, tk.END)
    entry_C.delete(0, tk.END)

def create_sine_law_tab():
    global entry_a, entry_b, entry_c, entry_A, entry_B, entry_C, label_result_sine_law

    # Criando a aba para a Lei dos Senos
    #frame_sine_law = ttk.Frame(notebook)
    #notebook.add(frame_sine_law, text="Lei dos Senos")
    frame_sine_law = tk.Toplevel();
    frame_sine_law.title("Lei dos Senos")

    # Labels e campos de entrada
    tk.Label(frame_sine_law, text="Lado A").grid(row=0, column=0, padx=10, pady=5)
    entry_a = tk.Entry(frame_sine_law)
    entry_a.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_sine_law, text="Lado B").grid(row=1, column=0, padx=10, pady=5)
    entry_b = tk.Entry(frame_sine_law)
    entry_b.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_sine_law, text="Lado C").grid(row=2, column=0, padx=10, pady=5)
    entry_c = tk.Entry(frame_sine_law)
    entry_c.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_sine_law, text="Ângulo A").grid(row=3, column=0, padx=10, pady=5)
    entry_A = tk.Entry(frame_sine_law)
    entry_A.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_sine_law, text="Ângulo B").grid(row=4, column=0, padx=10, pady=5)
    entry_B = tk.Entry(frame_sine_law)
    entry_B.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame_sine_law, text="Ângulo C").grid(row=5, column=0, padx=10, pady=5)
    entry_C = tk.Entry(frame_sine_law)
    entry_C.grid(row=5, column=1, padx=10, pady=5)

    # Botão para calcular os valores
    btn_calculate_sine_law_properties = tk.Button(frame_sine_law, text="Calcular", command=calculate_sine_law_properties)
    btn_calculate_sine_law_properties.grid(row=6, column=0, columnspan=2, pady=10)

    # Botão para limpar os campos
    btn_clear_fields = tk.Button(frame_sine_law, text="Limpar", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2, columnspan=2, pady=10)

    # Label para exibir o resultado
    label_result_sine_law = tk.Label(frame_sine_law, text="O resultado aparecerá aqui.")
    label_result_sine_law.grid(row=3, column=2, columnspan=2, pady=10)
