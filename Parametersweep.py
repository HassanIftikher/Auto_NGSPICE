import subprocess
import re
import numpy as np
from itertools import product

ngspice_executable = "ngspice"

def extract_transistor_parameters(file_path):
    transistor_params = {}
    with open(file_path, 'r') as file:
        for line in file:

            if 'L=' in line and 'W=' in line:
                name_match = re.match(r'(\S+)\s', line)
                L_match = re.search(r'\bL=(\d+\.?\d*)\b', line)
                W_match = re.search(r'\bW=(\d+\.?\d*)\b', line)
                if name_match and L_match and W_match:
                    transistor_name = name_match.group(1)
                    L_value = float(L_match.group(1))
                    W_value = float(W_match.group(1))
                    transistor_params[transistor_name] = {'L': L_value, 'W': W_value}

    return transistor_params

# Replace with the path to your netlist file
file_path = '/home/hassan/Desktop/adc_comp_circuit_min_blank.spice'
transistor_parameters = extract_transistor_parameters(file_path)
print(transistor_parameters)


def read_netlist(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_netlist(file_path, content):
    with open(file_path, 'w') as file:
        file.writelines(content)

def generate_sweep_netlists(original_netlist, transistor_params, L_values, W_values, output_file):
    with open(output_file, 'w') as output_txt:
        sys.stdout = output_txt  # Redirect standard output to the output text file
        
        for (L1, L2), (W1, W2) in product(zip(L_values, L_values[1:]), zip(W_values, W_values[1:])):
            modified_netlist = []
            for line in original_netlist:
                for transistor, params in transistor_params.items():
                    if transistor in line:
                        # Replace L and W values
                        line = re.sub(r'\bL=\d+\.?\d*\b', f'L={L1:.2f}', line) if params['use_L1'] else re.sub(r'\bL=\d+\.?\d*\b', f'L={L2:.2f}', line)
                        line = re.sub(r'\bW=\d+\.?\d*\b', f'W={W1:.2f}', line) if params['use_W1'] else re.sub(r'\bW=\d+\.?\d*\b', f'W={W2:.2f}', line)
                modified_netlist.append(line)

            sweep_file_name = f'netlist_L{L1:.2f}_W{W1:.2f}_L{L2:.2f}_W{W2:.2f}.spice'
            print(sweep_file_name)
            ngspice_command = [ngspice_executable, "-b", sweep_file_name]
            subprocess.run(ngspice_command)
# Example usage
import os
import sys

output_dir = '/home/hassan/Desktop/'
output_file = '/home/hassan/Desktop/output.txt'
keys = list(transistor_parameters.keys())
print(keys)
transistor_parameters = {
    keys[0]: {'use_L1': True, 'use_W1': True},  # Use L1 and W1 for "XM3"
    keys[1]: {'use_L1': False, 'use_W1': False},  # Use L2 and W2 for "XM2"
}

original_netlist = read_netlist(file_path)
L_range = np.arange(0.25, 1, 0.05) # Define your L sweep range
W_range = np.arange(1, 1.5, 0.1) # Define your W sweep range

generate_sweep_netlists(original_netlist, transistor_parameters, L_range, W_range, output_file)
#print(generate_sweep_netlists)
for (L1, L2), (W1, W2) in product(zip(L_range, L_range[1:]), zip(W_range, W_range[1:])):
    sweep_file_name = f'netlist_L{L1:.2f}_W{W1:.2f}_L{L2:.2f}_W{W2:.2f}.spice'
    command = [ngspice_executable, "-b", sweep_file_name]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Results for {sweep_file_name}:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Error running ngspice for {sweep_file_name}:")
        print(e.output)


    
# Example condition using the memory address
#transistor_parameters_address = id(transistor_parameters)
#if transistor_parameters_address in [id(d) for d in [transistor_parameters]]:
 #   print(f"The dictionary at memory address {transistor_parameters_address} exists.")
  #  # Accessing the parameters for the specified memory address
   # parameters = transistor_parameters
    #print(f"Parameters: {parameters}")
#else:
 #   print(f"Dictionary at memory address {transistor_parameters_address} not found.")

        #for line in original_netlist:
            #if any(transistor in line for transistor in transistor_params):
                # Replace L and W values
                #line = re.sub(r'\bL=\d+\.?\d*\b', f'L={L2:.2f}', line)
                #line = re.sub(r'\bW=\d+\.?\d*\b', f'W={W2:.2f}', line)
            #modified_netlist.append(line)
            #print(L2)
            #print(modified_netlist)
        # Write the modified netlist to a new file

