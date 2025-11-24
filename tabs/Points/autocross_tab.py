import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate():
    Pmax = 100
    Pmin = 0.1*Pmax

    if selected_calculation.get() == "Manual Mode":
        # Tteam = float(entry_Tteam.get())
        # Tmax = float(entry_Tmax.get())
        # Tmax = Tmax * 1.25
        # result = 0.95 * Pmax * (((Tmax/Tteam) - 1)/0.25) + 0.05 * Pmax
        Tmin = float(entry_Tmin.get())
        Tmax = 1.4 * Tmin
        Tteam = float(entry_Tteam.get())
        if Tteam > Tmax:
            Tteam = Tmax

        result = (Pmax - Pmin) * pow(((Tmax - Tteam)/(Tmax - Tmin)), 2) + Pmin
        
    elif selected_calculation.get() == "DC":
        Tteam1 = float(entry_Tteam1.get())
        Tteam2 = float(entry_Tteam2.get())
        lenght = float(entry_lenght.get())
        Tmax = lenght / 6
        Tmin = float(entry_Tmin.get())
        Ttotal = min(Tteam1, ((Tteam1 + Tteam2)/2))

        if Ttotal > Tmax or Ttotal == -1:
            Ttotal = Tmax

        result = 0.9 * Pmax * ((Tmax - Ttotal)/(Tmax - Tmin)) + 0.1 * Pmax

    messagebox.showinfo("Results", f"Points: {result:.2f}")
    # print("Driverless points:")
    # print(dv_skidpad_score)

    # print("Driverless Cup points:")
    # print(dc_skidpad_score)
    clear_fields()

def update_fields(event):
    for widget in frame_inputs.winfo_children():
        widget.grid_remove()

    calculation = selected_calculation.get()
    selection_box.grid(row=1, column=0, padx=10, pady=5)
    dropdown.grid(row=1, column=1, padx=10, pady=5)

    if calculation == "Manual Mode":
        clear_fields()
        tk.Label(frame_inputs, text="My best time with penalties:").grid(
            row=2, column=0, padx=10, pady=5
        )
        entry_Tteam.grid(row=2, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Best time overall with penalties:").grid(
            row=3, column=0, padx=10, pady=5
        )
        entry_Tmin.grid(row=3, column=1, padx=10, pady=5)
        btn_calculate.grid(row=5, column=1, padx=0, pady=10)
        btn_clear.grid(row=5, column=0, padx=10, pady=10)

    elif calculation == "DC":
        clear_fields()
        tk.Label(frame_inputs, text="1st run with penalties:").grid(
            row=2, column=0, padx=10, pady=5
        )
        entry_Tteam1.grid(row=2, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="2nd run with penalties:").grid(
            row=3, column=0, padx=10, pady=5
        )
        entry_Tteam2.grid(row=3, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Lenght of the track:").grid(
            row=4, column=0, padx=10, pady=5
        )
        entry_lenght.grid(row=4, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Fastest run of all teams:").grid(
            row=5, column=0, padx=10, pady=5
        )
        entry_Tmin.grid(row=5, column=1, padx=10, pady=5)
        btn_calculate.grid(row=9, column=1, padx=0, pady=10)
        btn_clear.grid(row=9, column=0, padx=10, pady=10)

def clear_fields():
    entry_Tteam.delete(0, tk.END)
    entry_Tteam1.delete(0, tk.END)
    entry_Tteam2.delete(0, tk.END)
    entry_lenght.delete(0, tk.END)
    entry_Tmin.delete(0, tk.END)

def create_autocross_tab():
    # skidpad_points_window = ttk.Frame(notebook) #this creates a tab need to add 'notebook' as a parameter of this function, and comment what is related to the new window
    # notebook.add(skidpad_points_window, text="Skidpad Points")

    autocross_points_window = tk.Toplevel() 
    autocross_points_window.title("Autocross Points")
    autocross_points_window.geometry("700x400")

    global selection_box
    
    selection_box = tk.Label(autocross_points_window, text="Select Calculation:")
    selection_box.grid(row=1, column=0, padx=10, pady=5)
    
    global selected_calculation, dropdown
    selected_calculation = tk.StringVar()
    dropdown = ttk.Combobox(
        autocross_points_window, textvariable=selected_calculation, width=40
    )
    dropdown["values"] = (
        "Manual Mode",
        "DC",
    )
    dropdown.set("Select Calculation")
    dropdown.bind("<<ComboboxSelected>>", update_fields)
    dropdown.grid(row=1, column=1, padx=10, pady=5)
    
    # Frame for dynamic input fields
    global frame_inputs
    frame_inputs = ttk.Frame(autocross_points_window)
    frame_inputs.grid(row=2, column=0, columnspan=2, pady=10)

    # input fields (initially hidden)
    global entry_Tteam, entry_Tteam1, entry_Tteam2, entry_lenght, entry_Tmin 
    entry_Tteam = tk.Entry(frame_inputs)
    entry_Tteam1 = tk.Entry(frame_inputs)
    entry_Tteam2 = tk.Entry(frame_inputs)
    entry_lenght = tk.Entry(frame_inputs)
    entry_Tmin = tk.Entry(frame_inputs)

    global btn_calculate, btn_clear

    btn_calculate = tk.Button(autocross_points_window, text="Calculate", command=calculate, bg="green", fg="white")
    btn_calculate.grid(row=7, column=1, padx=0, pady=10)

    btn_clear = tk.Button(autocross_points_window, text="Clear All", command=clear_fields)
    btn_clear.grid(row=7, column=0, padx=10, pady=10)
