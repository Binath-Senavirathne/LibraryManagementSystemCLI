import re

def validate_book_id(book_id):
    return bool(re.fullmatch(r"[A-Za-z]{2}\d{2}", book_id))


def validate_title(title):
    return bool(re.fullmatch(r"[A-Za-z ]{1,20}", title))


def validate_copies(copies):
    return copies.isdigit() and 0 < int(copies) <= 2


def validate_price(price):
    return bool(re.fullmatch(r"\d+\.\d{2}", price))


def validate_student_id(student_id):
    return bool(re.fullmatch(r"\d{8}", student_id))


def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z]{1,10}", name))


def validate_date(date):
    return bool(re.fullmatch(r"\d{2}/\d{2}/\d{4}", date))


def validate_isbn13(isbn):
    if not re.fullmatch(r"\d{13}", isbn):
        return False

    total = 0
    for i in range(12):
        digit = int(isbn[i])
        total += digit if i % 2 == 0 else digit * 3

    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(isbn[-1])