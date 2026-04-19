from file_handler import load_csv, save_csv
from validation import *

BOOK_FILE = "../data/book.csv"
STUDENT_FILE = "../data/student.csv"
TRANS_FILE = "../data/transactions.csv"


def issue_book():
    book_id = input("Book ID: ")
    student_id = input("Student ID: ")
    date = input("Date: ")

    if not validate_date(date):
        print("Invalid date")
        return

    books = load_csv(BOOK_FILE)
    students = load_csv(STUDENT_FILE)
    transactions = load_csv(TRANS_FILE)

    book = next((b for b in books if b[0] == book_id), None)
    if not book:
        print("Invalid book ID")
        return

    if not any(s[0] == student_id for s in students):
        print("Invalid student ID")
        return

    if any(t[1] == book_id and t[2] == student_id and t[3] == "1" for t in transactions):
        print("Book already issued")
        return

    if int(book[5]) <= 0:
        print("Book ios not Available")
        return

    book[5] = str(int(book[5]) - 1)
    save_csv(BOOK_FILE, books)

    transactions.append([date, book_id, student_id, "1"])
    save_csv(TRANS_FILE, transactions)

    print("Issued")


def return_book():
    book_id = input("Enter Book ID: ")
    student_id = input("Enter Student ID: ")
    date = input("Enter Date (DD/MM/YYYY): ")

    if not validate_date(date):
        print("Invalid Date")
        return

    books = load_csv(BOOK_FILE)
    students = load_csv(STUDENT_FILE)
    transactions = load_csv(TRANS_FILE)

    # Check book exists
    book = next((b for b in books if b[0] == book_id), None)
    if not book:
        print("Invalid Book ID")
        return

    # Check student exists
    if not any(s[0] == student_id for s in students):
        print("Invalid Student ID")
        return

    # Check if book was issued
    issued = any(
        t[1] == book_id and t[2] == student_id and t[3] == "1"
        for t in transactions
    )

    if not issued:
        print("Book was not issued to this student")
        return

    # Check already returned
    returned = any(
        t[1] == book_id and t[2] == student_id and t[3] == "2"
        for t in transactions
    )

    if returned:
        print("Book already returned")
        return

    # Update availability
    if int(book[5]) < int(book[4]):
        book[5] = str(int(book[5]) + 1)
    else:
        print("Availability exceeds copies")
        return

    save_csv(BOOK_FILE, books)

    # Save transaction
    transactions.append([date, book_id, student_id, "2"])
    save_csv(TRANS_FILE, transactions)

    print("Book returned successfully")