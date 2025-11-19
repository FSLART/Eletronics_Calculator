import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from scipy.spatial.transform import Rotation as R

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')

def create_entry(placeholder):
    entry = tk.Entry(frame_inputs)
    entry.insert(0, placeholder)
    entry.configure(state=tk.DISABLED)
    entry.bind('<Button-1>', lambda x: on_focus_in(entry))
    entry.bind('<FocusOut>', lambda x: on_focus_out(entry, placeholder))
    return entry

def calculate():
    try:
        Rx=(int(entry_roll.get()) if entry_roll.get() else None)
        Ry=(int(entry_pitch.get()) if entry_pitch.get() else None)
        Rz=(int(entry_yaw.get()) if entry_yaw.get() else None)
        Tx=(float(entry_tx.get()) if entry_tx.get() else None)
        Ty=(float(entry_ty.get()) if entry_ty.get() else None)
        Tz=(float(entry_tz.get()) if entry_tz.get() else None)
        cx=(int(entry_cx.get()) if entry_cx.get() else None)
        cy=(int(entry_cy.get()) if entry_cy.get() else None)
        fx=(int(entry_fx.get()) if entry_fx.get() else None)
        fy=(int(entry_fy.get()) if entry_fy.get() else None)
        u=(int(entry_u.get()) if entry_u.get() else None)
        v=(int(entry_v.get()) if entry_v.get() else None)
        d=(float(entry_d.get()) if entry_d.get() else None)

        if Rx is None or Ry is None or Rz is None or Tx is None or Ty is None or Tz is None or cx is None or cy is None or fx is None or fy is None or u is None or v is None or d is None:
            raise ValueError("Please enter all values.")
        
        # ATTENTION: "ZYX" is case-sensitive
        r_tf = R.from_euler('ZYX', [Rz, Ry, Rx], degrees=True)
        r_tf_matrix = r_tf.as_matrix()

        # translation matrix
        t = np.matrix([[Tx], [Ty], [Tz]])

        print("R_tf={}".format(r_tf_matrix))
        print()

        x = np.matrix([[u], [v], [d]])

        # IMAGE PLANE TO CAMERA FRAME
        X_camera = np.matrix([
            [(u - cx) / fx],
            [(v - cy) / fy],
            [1]
            ])

        # normalize to the distance (euclidean)
        X_camera = X_camera / np.linalg.norm(X_camera) * d

        # TRANSFORM TO CAR FRAME
        X = (r_tf_matrix * X_camera) + t

        messagebox.showinfo("Result", f"X={X}")
        print("X={}".format(X))
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    

def clear_fields():
    entry_roll.delete(0, tk.END)
    entry_pitch.delete(0, tk.END)
    entry_yaw.delete(0, tk.END)
    entry_tx.delete(0, tk.END)
    entry_ty.delete(0, tk.END)
    entry_tz.delete(0, tk.END)
    entry_cx.delete(0, tk.END)
    entry_cy.delete(0, tk.END)
    entry_fx.delete(0, tk.END) 
    entry_fy.delete(0, tk.END)
    entry_u.delete(0, tk.END)
    entry_v.delete(0, tk.END)
    entry_d.delete(0, tk.END)
    

def create_camera_window():
    # cam_calcs_window = ttk.Frame(notebook) #this creates a tab need to add 'notebook' as a parameter of this function
    # notebook.add(cam_calcs_window, text="Camera Calculations")
    cam_calcs_window = tk.Toplevel()
    cam_calcs_window.title("Camera Calculations")
    # cam_calcs_window.geometry("900x400")
    global frame_inputs
    frame_inputs = ttk.Frame(cam_calcs_window, width=800, height=400)
    frame_inputs.grid(row=1, column=0, columnspan=2, pady=10)

    # Input fields (initially hidden)
    global \
        entry_roll, \
        entry_pitch, \
        entry_yaw, \
        entry_tx, \
        entry_ty, \
        entry_tz, \
        entry_cx, \
        entry_cy, \
        entry_fx, \
        entry_fy, \
        entry_u, \
        entry_v, \
        entry_d
    # Create input fields and placeHolders
    entry_roll = create_entry("Roll")

    entry_pitch = create_entry("Pitch")
    
    entry_yaw = create_entry("Yaw")
    
    entry_tx = create_entry("Tx")
    
    entry_ty = create_entry("Ty")
    
    entry_tz = create_entry("Tz")
    
    entry_cx = create_entry("Cx")
    
    entry_cy = create_entry("Cy")
    
    entry_fx = create_entry("Fx")
    
    entry_fy = create_entry("Fy")
    
    entry_u = create_entry("U")
    
    entry_v = create_entry("V")
    
    entry_d = create_entry("D (meters)")


    tk.Label(frame_inputs, text="ZY'X'' (degrees):").grid(
            row=0, column=0, padx=10, pady=5
    )
    entry_roll.grid(row=0, column=1, padx=10, pady=5)
    entry_pitch.grid(row=0, column=2, padx=10, pady=5)  
    entry_yaw.grid(row=0, column=3, padx=10, pady=5)
    tk.Label(frame_inputs, text="Translation (meters):").grid(
            row=1, column=0, padx=10, pady=5
    )
    entry_tx.grid(row=1, column=1, padx=10, pady=5)
    entry_ty.grid(row=1, column=2, padx=10, pady=5)
    entry_tz.grid(row=1, column=3, padx=10, pady=5)

    tk.Label(frame_inputs, text="Camera Intrinsics:").grid(
            row=2, column=0, padx=10, pady=5
    )
    entry_cx.grid(row=2, column=1, padx=10, pady=5)
    entry_cy.grid(row=2, column=2, padx=10, pady=5)
    entry_fx.grid(row=2, column=3, padx=10, pady=5)
    entry_fy.grid(row=2, column=4, padx=10, pady=5)

    tk.Label(frame_inputs, text="Principal Point:").grid(
            row=3, column=0, padx=10, pady=5
    )
    entry_u.grid(row=3, column=1, padx=10, pady=5)
    entry_v.grid(row=3, column=2, padx=10, pady=5)
    entry_d.grid(row=3, column=3, padx=10, pady=5)

    btn_calculate = tk.Button(
        cam_calcs_window, text="Calculate", command=calculate, bg="green", fg="white"
    )
    btn_calculate.grid(row=4, column=1, padx=10, pady=10)

    btn_clear = tk.Button(cam_calcs_window, text="Clear", command=clear_fields)
    btn_clear.grid(row=4, column=0, padx=10, pady=10)


