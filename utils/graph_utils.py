import matplotlib.pyplot as plt
import numpy as np


def plot_impedance_vs_frequency(inductance):
    frequencies = np.linspace(1, 10000, 500)
    impedances = 2 * np.pi * frequencies * inductance

    plt.figure(figsize=(8, 5))
    plt.plot(frequencies, impedances, label="Impedance vs Frequency")
    plt.title("Impedance vs Frequency for Inductor")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Impedance (Ω)")
    plt.grid(True)
    plt.legend()
    plt.show()
