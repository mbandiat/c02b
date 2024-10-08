# p01sc02_function_files/p01beg_m_sales.py

import csv

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def main():
    filename = 'sales_q1_2021_x.csv'
    content = read_file(filename)
    if content:
        print(content)

if __name__ == "__main__":
    main()
