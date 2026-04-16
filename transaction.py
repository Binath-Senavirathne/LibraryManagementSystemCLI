import csv
import re
import os
from book import load_books, save_books
from student import load_students

FILE_PATH = "../data/transactions.csv"

def validate_date(date):
    return bool(re.fullmatch(r"\d{2}/\d{2}/\d{4}", date))


def load_transactions():
    transactions = []
    if not os.path.exists(FILE_PATH):
        return transactions

    with open(FILE_PATH, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            transactions.append(row)
    return transactions


def save_transactions(transactions):
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transactions)


def issue_book():
    book_id = input("Enter Book ID: ")
    student_id = input("Enter Student ID: ")
    date = input("Enter Date (DD/MM/YYYY): ")

    if not validate_date(date):
        print("Invalid Date")
        return

    books = load_books()
    students = load_students()
    transactions = load_transactions()

    # Check book exists
    book_found = None
    for book in books:
        if book[0] == book_id:
            book_found = book
            break

    if not book_found:
        print("Invalid Book ID")
        return

    # Check student exists
    student_found = any(student[0] == student_id for student in students)
    if not student_found:
        print("Invalid Student ID")
        return

    # Check already issued
    for t in transactions:
        if t[1] == book_id and t[2] == student_id and t[3] == "1":
            print("Book already issued to this student")
            return

    # Check availability
    if int(book_found[5]) <= 0:
        print("No copies available")
        return

    # Update availability
    book_found[5] = str(int(book_found[5]) - 1)
    save_books(books)

    # Save transaction
    transactions.append([date, book_id, student_id, "1"])
    save_transactions(transactions)

    print("Book issued successfully")


def return_book():
    book_id = input("Enter Book ID: ")
    student_id = input("Enter Student ID: ")
    date = input("Enter Date (DD/MM/YYYY): ")

    if not validate_date(date):
        print("Invalid Date")
        return

    books = load_books()
    transactions = load_transactions()

    # Check book exists
    book_found = None
    for book in books:
        if book[0] == book_id:
            book_found = book
            break

    if not book_found:
        print("Invalid Book ID")
        return

    # Check issued before returning
    issued = False
    for t in transactions:
        if t[1] == book_id and t[2] == student_id and t[3] == "1":
            issued = True

    if not issued:
        print("Book was not issued")
        return

    # Check already returned
    for t in transactions:
        if t[1] == book_id and t[2] == student_id and t[3] == "2":
            print("Book already returned")
            return

    # Update availability
    if int(book_found[5]) < int(book_found[4]):
        book_found[5] = str(int(book_found[5]) + 1)
    else:
        print("Availability exceeds copies")
        return

    save_books(books)

    # Save transaction
    transactions.append([date, book_id, student_id, "2"])
    save_transactions(transactions)

    print("Book returned successfully")