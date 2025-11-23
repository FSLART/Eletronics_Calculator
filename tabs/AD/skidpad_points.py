import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math


SKIDPAD_DC_PMAX = 75  # maximum points for DC Skidpad (FSG 2026 Table 3)
SKIDPAD_DV_PMAX = 75  # Maximu points for Driverless Skidpad (FSG 2026 Table 3)

def calculate():
    if cones_run1 == []:
        messagebox.showerror("Error", "Please insert at least one time, this isn't Mario Kart")
        return
    if selected_calculation.get() == "Average time is given":
        final_times_all_teams = []
        team_final_time = avg_times[0] + 0.2 * cones_run1[0]
        # 25s DISQUALIFICATION RULE (FSG_2026): based on raw time without penalties
        if avg_times[0] > 25:
            messagebox.showerror("DISQUALIFIED", "DISQUALIFIED: Run time without penalties > 25s - please be faster next time!")
            clear_fields()
            return
        for i in range(len(avg_times)):
            final_times_all_teams.append(avg_times[i] + 0.2*cones_run1[i])
        sorted_final_times = sorted(final_times_all_teams)

        try:
            team_rank = int(entry_rank.get())
        except:
            messagebox.showerror("Error", "Please insert a valid rank.")
            return

        dv_skidpad_score = SKIDPAD_DV_PMAX * ((len(final_times_all_teams) + 1 - team_rank) / len(final_times_all_teams))

        # --- DC SKIDPAD SCORING (FSG rulebook 2026) ---
        # Generic dynamic formula:
        # Score = (Pmax - Pmin) * ((Tmax - Tteam)/(Tmax - Tmin))^2 + Pmin
        Pmax = SKIDPAD_DC_PMAX
        Pmin = 0.05 * Pmax
        Tmin = sorted_final_times[0]       # Best valid time across all teams
        Tteam = team_final_time            # This team's best time after penalties
        Tmax = 1.7 * Tmin                  # DC skidpad multiplier

        # Cap team time at Tmax according to FSG D9.1.1
        Tteam_effective = min(Tteam, Tmax)

        dc_skidpad_score = (Pmax - Pmin) * ((Tmax - Tteam_effective) / (Tmax - Tmin))**2 + Pmin
        
    elif selected_calculation.get() == "All times are given":
        first_runs_avg = []
        second_runs_avg = []
        final_times_all_teams = []

        for i in range(len(left_run1)):
            first_runs_avg.append( ((left_run1[i]+right_run1[i])/2)+0.2*cones_run1[i] )
            second_runs_avg.append( ((left_run2[i]+right_run2[i])/2)+0.2*cones_run2[i] )

            if first_runs_avg[i] < second_runs_avg[i]:
                final_times_all_teams.append(first_runs_avg[i])
            else:
                final_times_all_teams.append(second_runs_avg[i])

        team_final_time = final_times_all_teams[0]
        # 25s DISQUALIFICATION RULE (FSG_2026): based on raw time without penalties
        raw_first_run = (left_run1[0] + right_run1[0]) / 2
        raw_second_run = (left_run2[0] + right_run2[0]) / 2
        best_raw_run = raw_first_run if raw_first_run < raw_second_run else raw_second_run

        if best_raw_run > 25:
            messagebox.showerror("DISQUALIFIED", "DISQUALIFIED: Run time without penalties > 25s -> try the pedal is on the right")
            clear_fields()
            return
        sorted_final_times = sorted(final_times_all_teams)

        #team_rank = sorted_final_times.index(team_final_time) + 1
        try:
            team_rank = int(entry_rank.get())
        except:
            messagebox.showerror("Error", "Please insert a valid rank.")
            return
        
        dv_skidpad_score = SKIDPAD_DV_PMAX * ((len(final_times_all_teams) + 1 - team_rank) / len(final_times_all_teams))
        # --- DC SKIDPAD SCORING (FSG rulebook 2026) ---
        # Generic dynamic scoring formula:
        # Score = (Pmax - Pmin) * ((Tmax - Tteam)/(Tmax - Tmin))^2 + Pmin
        Pmax = SKIDPAD_DC_PMAX
        Pmin = 0.05 * Pmax
        Tmin = sorted_final_times[0]       # Best valid time across all teams
        Tteam = team_final_time            # This (LART :) team's best time after penalties
        Tmax = 1.7 * Tmin                  # DC skidpad multiplier

        # Cap team time at Tmax according to FSG D9.1.1
        Tteam_effective = min(Tteam, Tmax)
        dc_skidpad_score = (Pmax - Pmin) * ((Tmax - Tteam_effective) / (Tmax - Tmin))**2 + Pmin

    messagebox.showinfo("Results", f"Driverless points: {dv_skidpad_score}\nDriverless Cup points: {dc_skidpad_score}")
    clear_fields()
        

def clear_fields():
    entry_left_1.delete(0, tk.END)
    entry_right_1.delete(0, tk.END)
    entry_left_2.delete(0, tk.END)
    entry_right_2.delete(0, tk.END)
    entry_cones_1.delete(0, tk.END)
    entry_cones_2.delete(0, tk.END)
    entry_average.delete(0, tk.END)
    entry_rank.delete(0, tk.END)
    left_run1.clear()
    right_run1.clear()
    left_run2.clear()
    right_run2.clear()
    cones_run1.clear()
    cones_run2.clear()
    avg_times.clear()
    total_values_inserted.set(f"Total of times inserted: {len(cones_run1)}")
    

def add_times():
    if selected_calculation.get() == "All times are given":
        try:
            left_run1.append(float(entry_left_1.get()))
            right_run1.append(float(entry_right_1.get()))
            left_run2.append(float(entry_left_2.get()))
            right_run2.append(float(entry_right_2.get()))
            cones_run1.append(int(entry_cones_1.get()))
            cones_run2.append(int(entry_cones_2.get()))
            entry_left_1.delete(0, tk.END)
            entry_right_1.delete(0, tk.END)
            entry_left_2.delete(0, tk.END)
            entry_right_2.delete(0, tk.END)
            entry_cones_1.delete(0, tk.END)
            entry_cones_2.delete(0, tk.END)
            entry_average.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Please insert all times. I can't guess them")


    elif selected_calculation.get() == "Average time is given":
        try:
            avg_times.append(float(entry_average.get()))
            cones_run1.append(int(entry_cones_1.get()))
            entry_average.delete(0, tk.END)
            entry_cones_1.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Please insert all times. Telepathy not supported...YET!")
    # print(len(cones_run1))
    total_values_inserted.set(f"Total of times inserted: {len(cones_run1)}")

    

def update_fields(event):
    for widget in frame_inputs.winfo_children():
        widget.grid_forget()


    calculation = selected_calculation.get()
    warning_text.grid(row=0, column=0, padx=10, pady=5)
    warning_text_2.grid(row=1, column=0, padx=10, pady=5)
    selection_box.grid(row=2, column=0, padx=10, pady=5)
    dropdown.grid(row=2, column=1, padx=10, pady=5)

    if calculation == "Average time is given":
        clear_fields()
        tk.Label(frame_inputs, text="Average Time(s):").grid(
            row=3, column=0, padx=10, pady=5
        )
        entry_average.grid(row=3, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Number of Cones Hit:").grid(
            row=4, column=0, padx=10, pady=5
        )
        entry_cones_1.grid(row=4, column=1, padx=10, pady=5)

        if len(cones_run1) == 0:
            entry_rank.grid(row=5, column=1, padx=10, pady=5)
            tk.Label(frame_inputs, text="Overall rank of your team:").grid(row=5, column=0, padx=10, pady=5)

        total.grid(row=6, column=0, padx=10, pady=5)
        btn_add_times.grid(row=6, column=1, padx=100, pady=10)
        btn_calculate.grid(row=7, column=1, padx=0, pady=10)
        btn_clear.grid(row=7, column=0, padx=10, pady=10)


    elif calculation == "All times are given":
        clear_fields()
        tk.Label(frame_inputs, text="Left Time 1(s):").grid(
            row=3, column=0, padx=10, pady=5
        )
        entry_left_1.grid(row=3, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Right Time 1(s):").grid(
            row=4, column=0, padx=10, pady=5
        )
        entry_right_1.grid(row=4, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Left Time 2(s):").grid(
            row=5, column=0, padx=10, pady=5
        )
        entry_left_2.grid(row=5, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Right Time 2(s):").grid(
            row=6, column=0, padx=10, pady=5
        )
        entry_right_2.grid(row=6, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Number of Cones Hit 1st run:").grid(
            row=7, column=0, padx=10, pady=5
        )
        entry_cones_1.grid(row=7, column=1, padx=10, pady=5)
        tk.Label(frame_inputs, text="Number of Cones Hit 2nd run:").grid(
            row=8, column=0, padx=10, pady=5
        )
        entry_cones_2.grid(row=8, column=1, padx=10, pady=5)

        if len(cones_run1) == 0:
            entry_rank.grid(row=9, column=1, padx=10, pady=5)
            tk.Label(frame_inputs, text="Overall rank of your team:").grid(row=9, column=0, padx=10, pady=5)

        total.grid(row=10, column=0, padx=10, pady=5)
        btn_add_times.grid(row=10, column=1, padx=100, pady=10)
        btn_calculate.grid(row=11, column=1, padx=0, pady=10)
        btn_clear.grid(row=11, column=0, padx=10, pady=10)

def create_skidpad_points_window():
    # skidpad_points_window = ttk.Frame(notebook) #this creates a tab need to add 'notebook' as a parameter of this function, and comment what is related to the new window
    # notebook.add(skidpad_points_window, text="Skidpad Points")

    skidpad_points_window = tk.Toplevel() 
    skidpad_points_window.title("Skidpad Points")

    global selection_box, warning_text, warning_text_2

    warning_text = tk.Label(skidpad_points_window, text="O primeiro valor a ser inserido tem de ser o da tua equipa!!!", fg="red", font=("Helvetica", 15, "bold"))
    warning_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
    warning_text_2 = tk.Label(skidpad_points_window, text="O rank é o da tua equipa e não importa quando é inserido, é preencher e deixar ficar!", fg="red", font=("Helvetica", 15, "bold"))
    warning_text_2.grid(row=1 , column=0, columnspan=2, padx=10, pady=5)

    
    selection_box = tk.Label(skidpad_points_window, text="Select Calculation:")
    selection_box.grid(row=2, column=0, padx=10, pady=5)
    
    global selected_calculation, dropdown
    selected_calculation = tk.StringVar()
    dropdown = ttk.Combobox(
        skidpad_points_window, textvariable=selected_calculation, width=40
    )
    dropdown["values"] = (
        "Average time is given",
        "All times are given",
    )
    dropdown.set("Select Calculation")
    dropdown.bind("<<ComboboxSelected>>", update_fields)
    dropdown.grid(row=2, column=1, padx=10, pady=5)

    # global variables for the times and cones
    global left_run1, right_run1, left_run2, right_run2, cones_run1, cones_run2, avg_times, rank
    left_run1 = []
    right_run1 = []
    left_run2 = []
    right_run2 = []
    cones_run1 = []
    cones_run2 = []
    avg_times = []
    
    # Frame for dynamic input fields
    global frame_inputs
    frame_inputs = ttk.Frame(skidpad_points_window, width=750, height=300)
    frame_inputs.grid(row=3, column=0, columnspan=2, pady=10)


    # input fields (initially hidden)
    global entry_left_1, entry_right_1, entry_left_2, entry_right_2, entry_cones_1, entry_cones_2, entry_average, entry_rank
    entry_left_1 = tk.Entry(frame_inputs)
    entry_right_1 = tk.Entry(frame_inputs)
    entry_left_2 = tk.Entry(frame_inputs)
    entry_right_2 = tk.Entry(frame_inputs)
    entry_cones_1 = tk.Entry(frame_inputs)
    entry_cones_2 = tk.Entry(frame_inputs)
    entry_average = tk.Entry(frame_inputs)
    entry_rank = tk.Entry(frame_inputs)

    global total_values_inserted
    total_values_inserted = tk.StringVar()
    # print(len(cones_run1))

    global total
    total = tk.Label(skidpad_points_window,textvariable=total_values_inserted)

    total_values_inserted.set(f"Total of times inserted: {len(cones_run1)}")

    global btn_add_times, btn_calculate, btn_clear
    btn_add_times = tk.Button(skidpad_points_window, text="Add Times", command=add_times)
    #btn_add_times.grid(row=6, column=1, padx=100, pady=10)

    btn_calculate = tk.Button(skidpad_points_window, text="Calculate", command=calculate, bg="green", fg="white")
    btn_calculate.grid(row=8, column=1, padx=0, pady=10)

    btn_clear = tk.Button(skidpad_points_window, text="Clear All", command=clear_fields)
    btn_clear.grid(row=8, column=0, padx=10, pady=10)
