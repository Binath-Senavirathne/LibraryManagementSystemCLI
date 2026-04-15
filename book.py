import csv
import os
import re

FILE_PATH = "../data/book.csv"

def validate_book_id(book_id):
    return bool(re.fullmatch(r"[A-Za-z]{2}\d{2}", book_id))


def validate_title(title):
    return bool(re.fullmatch(r"[A-Za-z ]{1,20}", title))


def validate_copies(copies):
    return copies.isdigit() and 0 < int(copies) <= 2


def validate_price(price):
    return bool(re.fullmatch(r"\d+\.\d{2}", price))


def validate_isbn13(isbn):
    if not re.fullmatch(r"\d{13}", isbn):
        return False

    total = 0
    for i in range(12):
        digit = int(isbn[i])
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(isbn[-1])

def load_books():
    books = []
    if not os.path.exists(FILE_PATH):
        return books

    with open(FILE_PATH, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            books.append(row)
    return books


def save_books(books):
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)

def add_book():
    book_id = input("Enter Book ID (LLDD): ")
    if not validate_book_id(book_id):
        print("Invalid Book ID")
        return

    isbn = input("Enter ISBN-13: ")
    if not validate_isbn13(isbn):
        print("Invalid ISBN-13")
        return

    title = input("Enter Title: ")
    if not validate_title(title):
        print("Invalid Title")
        return

    author = input("Enter Author: ")

    copies = input("Enter Copies (max 2): ")
    if not validate_copies(copies):
        print("Invalid Copies")
        return

    price = input("Enter Price (xx.xx): ")
    if not validate_price(price):
        print("Invalid Price")
        return

    books = load_books()

    # Check duplicate ID
    for book in books:
        if book[0] == book_id:
            print("Book ID already exists")
            return

    availability = copies

    books.append([book_id, title, isbn, author, copies, availability, price])
    save_books(books)

    print("Book added successfully")


def view_books():
    books = load_books()
    print("\n--- Book List ---")
    for book in books:
        print(book)


def search_book():
    search_id = input("Enter Book ID to search: ")
    books = load_books()

    for book in books:
        if book[0] == search_id:
            print("Book Found:", book)
            return

    print("Book not found")


def edit_book():
    book_id = input("Enter Book ID to edit: ")
    books = load_books()

    for i, book in enumerate(books):
        if book[0] == book_id:
            print("Current Data:", book)

            new_title = input("New Title: ")
            if not validate_title(new_title):
                print("Invalid Title")
                return

            new_author = input("New Author: ")

            new_price = input("New Price: ")
            if not validate_price(new_price):
                print("Invalid Price")
                return

            books[i][1] = new_title
            books[i][3] = new_author
            books[i][6] = new_price

            save_books(books)
            print("Book updated")
            return

    print("Book not found")