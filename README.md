# Python Script to Automate NGSPICE Simulation

This project focuses on developing a Python script to automate the parameter sweeping of transistors in an NGSPICE simulation for an Analog-to-Digital Converter (ADC) comparator circuit.

## Table of Contents
- [Introduction](#introduction)
- [Implementation](#implementation)
- [Results Validation](#results-validation)
- [Conclusion](#conclusion)
- [References](#references)
- [Appendix](#appendix)

## Introduction
The report analyzes the NGSPICE simulation and the parameter sweep conducted on the ADC comparator circuit. The primary focus is on varying the length (L) and width (W) of the NMOS (XM3) and PMOS (XM2) transistors to investigate the influence of transistor size variations on the ADC comparator circuit's functionality.

## Implementation
The implementation section covers the following key steps:
1. Setting up the simulation framework using NGSPICE and the Sky130 libraries.
   Install and configure the NGSPICE for circuit simulation on the Linux server. 
Download the sky 130 libraries [3] for the given project and create an environment for simulating 
NGSPICE netlist file and this allows simulating the given ngspice netlist file shown in figures 1 & 2. 
The Sky 130 libraries are essential for simulating circuits designed with in the Skywater process using 
tools like Xschem and NGSPICE. The main purpose of these libraries is to provide accurate models for 
the components used in the electronic circuit simulations. 
3. Developing Python scripts to extract transistor parameters from the NGSPICE netlist, perform parameter sweeping, and automate the simulation process.

## Results Validation
This section discusses the methods used to conduct simulations, organize the data, and analyze the simulation outputs. It includes:
1. Merging simulation data, processing, and exporting to Excel format.
2. Analyzing the impact of transistor size variations on the ADC comparator circuit's performance.

## Conclusion
The project's conclusion summarizes the key findings and the developed Python script's ability to automate the parameter sweeping process for an ADC comparator circuit.

## References
The report includes a list of references used throughout the project.

## Appendix
The appendix provides additional details and code samples related to the project.
