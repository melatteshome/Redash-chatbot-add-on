import csv

def get_csv_headers(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
    return headers