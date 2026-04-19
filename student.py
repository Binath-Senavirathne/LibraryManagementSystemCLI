from file_handler import load_csv, save_csv
from validation import *

FILE_PATH = "../data/student.csv"


def add_student():
    student_id = input("Enter Student ID: ")
    if not validate_student_id(student_id):
        print("Invalid ID")
        return

    name = input("Enter Name: ")
    if not validate_name(name):
        print("Invalid Name")
        return

    students = load_csv(FILE_PATH)

    for s in students:
        if s[0] == student_id:
            print("Already exists")
            return

    students.append([student_id, name])
    save_csv(FILE_PATH, students)

    print("Student added")