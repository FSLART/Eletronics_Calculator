import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def create_converters_window():
    # tab = ttk.Frame(notebook)
    # notebook.add(tab, text="Converters")

    tab = tk.Toplevel()
    tab.title("Converters")
    tab.geometry("800x600")

    # Dropdown menu for selecting converter type
    converter_label = ttk.Label(tab, text="Select Converter Type:")
    converter_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    converter_types = ["Buck", "Buck-Boost", "Boost", "SEPIC"]
    selected_converter = tk.StringVar()
    converter_dropdown = ttk.Combobox(
        tab, textvariable=selected_converter, values=converter_types
    )
    converter_dropdown.grid(row=0, column=1, padx=10, pady=10)
    converter_dropdown.current(0)

    # Image display
    image_label = ttk.Label(tab)
    image_label.grid(row=0, column=2, rowspan=10, padx=10, pady=10)

    def update_image(converter_type):
        image_path = f"res/{converter_type.lower()}_converter.png"
        image = Image.open(image_path)
        image = image.resize((400, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

    update_image(converter_types[0])
    converter_dropdown.bind(
        "<<ComboboxSelected>>", lambda event: update_image(selected_converter.get())
    )

    # Input fields and calculation logic
    vin_label = ttk.Label(tab, text="Input Voltage (V_in):")
    vin_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    vin_entry = ttk.Entry(tab)
    vin_entry.grid(row=1, column=1, padx=10, pady=5)

    vout_label = ttk.Label(tab, text="Output Voltage (V_out):")
    vout_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    vout_entry = ttk.Entry(tab)
    vout_entry.grid(row=2, column=1, padx=10, pady=5)

    result_label = ttk.Label(tab, text="Result will appear here.")
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate():
        try:
            vin = float(vin_entry.get())
            vout = float(vout_entry.get())
            converter_type = selected_converter.get()

            if converter_type == "Buck":
                duty_cycle = vout / vin
            elif converter_type == "Buck-Boost":
                duty_cycle = vout / (vin + vout)
            elif converter_type == "Boost":
                duty_cycle = 1 - (vin / vout)
            elif converter_type == "SEPIC":
                duty_cycle = vout / (vin + vout)

            result_label.config(text=f"Duty Cycle: {duty_cycle:.2f}")
        except ValueError:
            result_label.config(text="Invalid input. Please enter numeric values.")

    calc_button = ttk.Button(tab, text="Calculate", command=calculate)
    calc_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
