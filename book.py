from file_handler import load_csv, save_csv
from validation import *

FILE_PATH = "../data/book.csv"


def add_book():
    book_id = input("Enter Book ID: ")
    if not validate_book_id(book_id):
        print("Invalid Book ID")
        return

    isbn = input("Enter ISBN-13: ")
    if not validate_isbn13(isbn):
        print("Invalid ISBN")
        return

    title = input("Enter Title: ")
    if not validate_title(title):
        print("Invalid Title")
        return

    author = input("Enter Author: ")

    copies = input("Enter Copies: ")
    if not validate_copies(copies):
        print("Invalid Copies")
        return

    price = input("Enter Price: ")
    if not validate_price(price):
        print("Invalid Price")
        return

    books = load_csv(FILE_PATH)

    for book in books:
        if book[0] == book_id:
            print("Book ID exists")
            return

    books.append([book_id, title, isbn, author, copies, copies, price])
    save_csv(FILE_PATH, books)

    print("Book added")


def view_books():
    books = load_csv(FILE_PATH)
    for book in books:
        print(book)

def search_book():
    search_id = input("Enter Book ID: ")

    books = load_csv(FILE_PATH)

    for book in books:
        if book[0] == search_id:
            print("\nBook Found:")
            print(f"ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"ISBN: {book[2]}")
            print(f"Author: {book[3]}")
            print(f"Copies: {book[4]}")
            print(f"Available: {book[5]}")
            print(f"Price: {book[6]}")
            return

    print("Book not found")

def edit_book():
    book_id = input("Enter Book ID : ")

    books = load_csv(FILE_PATH)

    for i, book in enumerate(books):
        if book[0] == book_id:
            print("\nCurrent Details:", book)

            new_title = input("Enter New Title: ")
            if not validate_title(new_title):
                print("Invalid Title")
                return

            new_author = input("Enter New Author: ")

            new_price = input("Enter New Price: ")
            if not validate_price(new_price):
                print("Invalid Price")
                return

            books[i][1] = new_title
            books[i][3] = new_author
            books[i][6] = new_price

            save_csv(FILE_PATH, books)

            print("Book updated successfully")
            return

    print("Book not found")