# Python Script to Automate NGSPICE Simulation

This project focuses on developing a Python script to automate the parameter sweeping of transistors in an NGSPICE simulation for an Analog-to-Digital Converter (ADC) comparator circuit.

## Introduction
### ADC Comparator Circuit Overview
An Analog-to-Digital Converter (ADC) is an essential component in electronic systems that convert continuous analog signals into discrete digital representations. The heart of many ADCs is the comparator circuit, which determines whether the input signal is above or below a certain threshold.

### NGSPICE Netlist Circuit Overview
The given NGSPICE netlist file (`adc_comp_circuit_min_blank.spice`) describes an ADC comparator circuit. It includes voltage sources, transistors (NMOS and PMOS), and various simulation control directives.

### Problem Statement
The main objective of this project is to "Examine the effect of transistor size variations on ADC comparator circuit behavior using NGSPICE simulation". This involves assessing the impact of changes in transistor length (L) and width (W) on the performance indicators of the comparator circuit.

## Implementation
### Setting up the Simulation Framework
The project requires setting up the NGSPICE simulation environment, including installing and configuring the necessary tools and libraries (such as the Sky130 libraries) to run the provided NGSPICE netlist file.

### Parameter Sweeping Using Python
The core of the implementation involves developing Python scripts to:
1. Extract transistor parameters (length and width) from the NGSPICE netlist file.
2. Automatically generate modified netlists with varying transistor parameter combinations.
3. Run the NGSPICE simulations for each modified netlist and capture the results.
4. Organize and process the simulation data for further analysis.

## Results Validation
### Conducting Simulations and Data Organization
The project includes scripts to manage the simulation process, including:
- Merging simulation data from various sources (e.g., MEAS_LOG.TXT, output files).
- Filtering, combining, and sorting the data based on specific criteria.
- Exporting the organized data into a structured format, such as an Excel file.

### Analyzing Simulation Outputs
The processed data is then used to analyze the impact of transistor size variations on the ADC comparator circuit's performance. This includes visualizing the "staircase output" of the comparator and interpreting the simulation results.

## Conclusion
The project's conclusion summarizes the key findings and the developed Python script's ability to automate the parameter sweeping process for an ADC comparator circuit. It also discusses the insights gained into the sensitivity of the ADC comparator circuit to transistor dimensions.

## References
1. [ADC Comparator Circuit Overview](https://www.electronics-lab.com/article/analog-to-digital-converter-adc/)
2. [NGSPICE Tutorial](https://ngspice.sourceforge.io/ngspice-tutorial.html)
3. [SkyWater PDK Documentation](https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html)

## Appendix
The appendix provides additional details and code samples related to the project, such as:
- Python script to run NGSPICE netlist files
- Approaches for parameter sweeping of transistor length
- Python script for parameter sweeping of multiple transistors
