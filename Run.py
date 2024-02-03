import subprocess

def run_ngspice(netlist_file_path):
    ngspice_command = ['ngspice', '-b', netlist_file_path]
    result = subprocess.run(ngspice_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        print("Simulation completed successfully.")
        simulation_output = result.stdout
        print(simulation_output)
    else:
        print("Simulation failed.")
        print("Error message:")
        print(result.stderr)

netlist_file_path = '/home/hassan/Desktop/adc_comp_circuit_min_blank.spice'
run_ngspice(netlist_file_path)
