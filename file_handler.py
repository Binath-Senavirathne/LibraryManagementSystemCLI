import csv
import os

#Loading CSV files to the System
def load_csv(file_path):
    data = []
    if not os.path.exists(file_path):
        return data

    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                data.append(row)
    return data

#Saving data to CSV files
def save_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)