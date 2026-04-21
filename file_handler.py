import csv
import os

def load_csv(file_path):
    data = []
    if not os.path.exists(file_path):
        return data

    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = True
        for row in reader:
            if header:
                header = False
                continue
            if row:
                data.append(row)
    return data


def save_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)