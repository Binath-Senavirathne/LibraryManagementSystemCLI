from file_handler import load_csv, save_csv
from validation import *
from datetime import datetime

BOOK_FILE = "../data/book.csv"
STUDENT_FILE = "../data/student.csv"
TRANS_FILE = "../data/transactions.csv"

#Issue Book
def issue_book():
    books = load_csv(BOOK_FILE)
    students = load_csv(STUDENT_FILE)
    transactions = load_csv(TRANS_FILE)

    book_id = input("Book ID: ")
    book = next((b for b in books if b[0] == book_id), None)
    if not book:
        print("Invalid book ID")
        return

    student_id = input("Student ID: ")
    if not any(s[0] == student_id for s in students):
        print("Invalid student ID")
        return
    #Check book issued to student or not
    currently_issued = any(
        t[1] == book_id and t[2] == student_id and t[3] == "1"
        for t in transactions
    ) and not any(
        t[1] == book_id and t[2] == student_id and t[3] == "2"
        for t in transactions
    )
    if currently_issued:
        print("Book already issued")
        return

    if int(book[5]) <= 0:
        print("Book is not Available")
        return

    date = input("Date: ")
    if not validate_date(date):
        print("Invalid date")
        return

    book[5] = str(int(book[5]) - 1)
    save_csv(BOOK_FILE, books)

    transactions.append([date, book_id, student_id, "1"])
    save_csv(TRANS_FILE, transactions)

    print("Book Issued")

#Return Book
def return_book():
    books = load_csv(BOOK_FILE)
    students = load_csv(STUDENT_FILE)
    transactions = load_csv(TRANS_FILE)

    book_id = input("Enter Book ID: ")
    book = next((b for b in books if b[0] == book_id), None)
    if not book:
        print("Invalid Book ID")
        return

    student_id = input("Enter Student ID: ")
    if not any(s[0] == student_id for s in students):
        print("Invalid Student ID")
        return

    # Check if book was issued
    issue_transactions = [t for t in transactions if t[1] == book_id and t[2] == student_id and t[3] == "1"]
    if not issue_transactions:
        print("Book was not issued to this student")
        return

    # Check already returned
    returned_transactions = [t for t in transactions if t[1] == book_id and t[2] == student_id and t[3] == "2"]
    if len(returned_transactions) >= len(issue_transactions):
        print("Book already returned")
        return

    last_issue_date_str = issue_transactions[-1][0]

    date = input("Enter Date (DD/MM/YYYY): ")
    if not validate_date(date):
        print("Invalid Date")
        return

    try:
        issue_date = datetime.strptime(last_issue_date_str, "%d/%m/%Y")
        return_date = datetime.strptime(date, "%d/%m/%Y")
        if return_date < issue_date:
            print("Error: Return date cannot be before the issue date.")
            return
    except ValueError:
        pass

    # Update availability
    if int(book[5]) < int(book[4]):
        book[5] = str(int(book[5]) + 1)
    else:
        print("Availability exceeds copies")
        return

    save_csv(BOOK_FILE, books)

    transactions.append([date, book_id, student_id, "2"])
    save_csv(TRANS_FILE, transactions)

    print("Book returned successfully")