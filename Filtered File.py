import pandas as pd

def generate_excel_file(text_file_path, output_excel_path):
    try:
        with open(text_file_path, 'r') as file:
            lines = file.readlines()

        data = [line.strip().split() for line in lines]
        df = pd.DataFrame(data, columns=['Config', 'Value'])

        df[['L1', 'W1', 'L2', 'W2']] = df['Config'].str.extract(r'L(\d+\.\d+)_W(\d+\.\d+)_L(\d+\.\d+)_W(\d+\.\d+)')
        df = df.drop(columns=['Config'])

        df.to_excel(output_excel_path, index=False)
        print(f"Data has been successfully exported to {output_excel_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_file_path = '/home/hassan/Desktop/ADCoutput.txt'
excel_output_path = '/home/hassan/Desktop/output_excel_file.xlsx'

generate_excel_file(input_file_path, excel_output_path)
