import tkinter as tk
from tkinter import ttk
from tabs.ohms_tab import create_ohms_tab
from tabs.power_tab import create_power_tab
from tabs.inductor_tab import create_inductor_tab
from tabs.capacitor_tab import create_capacitor_tab
from tabs.intrumentation_amplifier_tab import create_instrumentation_amplifier_tab

# Main application window
root = tk.Tk()
root.title("Electronics Calculator")

# Create notebook (tab manager)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Add tabs
create_ohms_tab(notebook)
create_power_tab(notebook)
create_inductor_tab(notebook)
create_capacitor_tab(notebook)
create_instrumentation_amplifier_tab(notebook)


# Function to clear fields when switching tabs
def clear_fields(event):
    for tab in notebook.winfo_children():
        for widget in tab.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, tk.Label) and "Result" in widget.cget("text"):
                widget.config(text="Result will appear here.")


# Bind the tab change event
notebook.bind("<<NotebookTabChanged>>", clear_fields)

# Run the application
root.mainloop()
