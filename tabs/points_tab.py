import tkinter as tk
from tkinter import ttk

from tabs.Points.endurance_tab import create_endurance_tab
from tabs.Points.efficiency_tab import create_efficiency_tab
from tabs.Points.efficiency_factor_tab import create_efficiency_factor_tab
from tabs.Points.autocross_tab import create_autocross_tab
from tabs.Points.manual_skidpad_tab import create_manual_skidpad_tab

def default_scoring_formula(tMinFactor, tMin, pMinFactor,pMax, tTeam):
    '''
    Pmax is the maximum points for the discipline according to table 3
    Pmin is the minimum points for the discipline according to table 11
    Tteam is the team's best time including penalties. Tteam is capped to Tmax .
    Tmax is defined in table 11.
    Tmin is the time of the fastest vehicle including penalties.
    '''
    pMin= pMinFactor*pMax
    tMax = tMinFactor*tMin

    return (pMax-pMin)*((tMax-tTeam)/(tMax - tMin))**2 + pMin

def create_points_tab(notebook):
    frame_points = ttk.Frame(notebook)
    notebook.add(frame_points, text="Points")

    # for correct spacing and positioning
    frame_points.grid_rowconfigure(0, weight=1)  # Top empty row
    frame_points.grid_rowconfigure(1, weight=1)  # Row with first button
    frame_points.grid_rowconfigure(2, weight=1)  # Row with second button
    frame_points.grid_rowconfigure(3, weight=1)  # Row with third button
    frame_points.grid_rowconfigure(4, weight=1)  # Bottom empty row
    frame_points.grid_columnconfigure(0, weight=1)  # Left empty column
    frame_points.grid_columnconfigure(1, weight=1)  # Center column
    frame_points.grid_columnconfigure(2, weight=1)  # Center column
    frame_points.grid_columnconfigure(3, weight=1)  # Right column

    button_options = {
        "bg": "#36454F",
        "fg": "white",
        "width": 20,
        "height": 5,
        "font": ("Arial", 14, "bold"),
    }

    tk.Button(
        frame_points,
        text="Endurance Points Calculator",
        **button_options,
        command = create_endurance_tab
    ).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    tk.Button(
        frame_points,
        text="Efficiency Points Calculator",
        **button_options,
        command=create_efficiency_tab  
    ).grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

    tk.Button(
        frame_points,
        text="Autocross Points Calculator",
        **button_options,
        command=create_autocross_tab 
    ).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
    
    tk.Button(
        frame_points,
        text="Efficiency Factor Calculator",
        **button_options,
        command= create_efficiency_factor_tab 
    ).grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
    
    tk.Button(
        frame_points,
        text="Manual Skidpad Points Calculator",
        **button_options,
        command= create_manual_skidpad_tab 
    ).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
    