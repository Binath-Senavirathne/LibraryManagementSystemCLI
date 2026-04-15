import csv
import re
import os

FILE_PATH = "../data/student.csv"

def validate_student_id(student_id):
    return bool(re.fullmatch(r"\d{8}", student_id))


def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z]{1,10}", name))


def load_students():
    students = []
    if not os.path.exists(FILE_PATH):
        return students

    with open(FILE_PATH, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            students.append(row)
    return students


def save_students(students):
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)


def add_student():
    student_id = input("Enter Student ID (8 digits): ")
    if not validate_student_id(student_id):
        print("Invalid Student ID")
        return

    name = input("Enter First Name: ")
    if not validate_name(name):
        print("Invalid Name")
        return

    students = load_students()

    # Check duplicate
    for student in students:
        if student[0] == student_id:
            print("Student already exists")
            return

    students.append([student_id, name])
    save_students(students)

    print("Student added successfully")