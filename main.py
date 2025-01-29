import tkinter as tk
from tkinter import ttk

from tabs.eletronics_tab import create_eletronics_tab
from tabs.autonomous_tab import create_autonomous_tab
from tabs.others_tab import create_others_tab

# Main application window
root = tk.Tk()
root.title("Electronics Calculator")
root.geometry("800x600")

# Create notebook (tab manager)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

create_eletronics_tab(notebook)
create_autonomous_tab(notebook)
create_others_tab(notebook)

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
