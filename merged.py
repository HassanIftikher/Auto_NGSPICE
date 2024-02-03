import os

def merge_files(input_file1, input_file2, output_file):
    with open(input_file1, 'r') as file1, open(input_file2, 'r') as file2, open(output_file, 'w') as merged_file:
        for line1, line2 in zip(file1, file2):
            a = line1.split('_')[1:]
            line = '.'.join('_'.join(a).split('.')[:-1])
            merged_file.write(f'{line} {line2.split()[0]}\n')

    print(f'Merged files {input_file1} and {input_file2} into {output_file}')

def sort_and_save_data(file_path, output_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    lines_with_last_values = [(line, float(line.strip().split()[-1])) for line in data]
    sorted_lines = sorted(lines_with_last_values, key=lambda x: x[1])

    with open(output_path, 'w') as output_file:
        for line, _ in sorted_lines:
            output_file.write(line)

    print(f'Data sorted and saved to {output_path}')

if __name__ == "__main__":
    # Define file paths
    input_file1_path = '/home/hassan/Desktop/output.txt'
    input_file2_path = '/home/hassan/MEAS_LOG.TXT'
    merged_output_path = '/home/hassan/Desktop/merged_output.txt'
    sorted_output_path = '/home/hassan/Desktop/ADCoutput.txt'

    # Merge files
    merge_files(input_file1_path, input_file2_path, merged_output_path)

    # Sort and save data
    sort_and_save_data(merged_output_path, sorted_output_path)

