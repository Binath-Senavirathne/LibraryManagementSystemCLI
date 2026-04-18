from book import add_book, view_books, search_book, edit_book
from graph import generate_graph
from student import add_student
from transaction import issue_book, return_book


def book_menu():
    while True:
        print("\n---Manage Books---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Edit Book")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            edit_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


def student_menu():
    while True:
        print("\n---Manage Students---")
        print("1. Add Student")
        print("2. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            break
        else:
            print("Invalid choice")


def transaction_menu():
    while True:
        print("\n--- Transactions ---")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            issue_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


def main():
    while True:
        print("\nLibrary Management System")
        print("1. Manage Books")
        print("2. Manage Students")
        print("3. Transactions")
        print("4. Generate Trend Graph")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            book_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            transaction_menu()
        elif choice == "4":
            generate_graph()
        elif choice == "5.":
            print("Exit from the System")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()