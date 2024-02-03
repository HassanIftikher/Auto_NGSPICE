import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_last_values(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    last_values = [float(line.strip().split()[-1]) for line in data]
    return np.array(last_values)

def apply_uniform_difference(signal_values, uniform_difference):
    rounded_values = np.unique(np.round(signal_values / uniform_difference) * uniform_difference)
    return rounded_values

def plot_analog_signal(signal_values, sampling_rate=150):
    time_values = np.linspace(0, len(signal_values) / sampling_rate, num=len(signal_values))

    plt.figure(figsize=(10, 6))
    plt.step(time_values, signal_values, where='post')
    plt.title('Analog Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Voltage Level')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    input_file_path = '/home/hassan/Desktop/ADCoutput.txt'
    excel_output_path = '/home/hassan/Desktop/output_excel_file.xlsx'

    uniform_difference = 0.00900  # Adjust as needed

    signal_values = read_last_values(input_file_path)
    rounded_values = apply_uniform_difference(signal_values, uniform_difference)
    print(rounded_values)
    plot_analog_signal(rounded_values)

    #generate_excel_file(input_file_path, excel_output_path)
