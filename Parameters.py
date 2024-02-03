import re

def extract_transistor_parameters(file_path):
    transistor_params = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Check for transistor definitions (generic)
            match = re.match(r'X([A-Za-z0-9]+)\s', line)
            if match:
                transistor_name = match.group(1)
                L_match = re.search(r'\bL=(\d+\.?\d*)\b', line)
                W_match = re.search(r'\bW=(\d+\.?\d*)\b', line)
                L_value = float(L_match.group(1)) if L_match else None
                W_value = float(W_match.group(1)) if W_match else None
                transistor_params[transistor_name] = {'L': L_value, 'W': W_value}

    return transistor_params

# Replace with the path to your netlist file
file_path = '/home/hassan/Desktop/adc_comp_circuit_min_blank.spice'
transistor_parameters = extract_transistor_parameters(file_path)
def print_transistor_parameters_in_columns(transistor_parameters):
    # Print the header
    print(f"{'Transistor':<10} {'L':<10} {'W':<10}")
    print("-" * 30)

    # Print each transistor's parameters
    for name, params in transistor_parameters.items():
        L_value = params['L'] if params['L'] is not None else 'N/A'
        W_value = params['W'] if params['W'] is not None else 'N/A'
        print(f"{name:<10} {L_value:<10} {W_value:<10}")
print_transistor_parameters_in_columns(transistor_parameters)