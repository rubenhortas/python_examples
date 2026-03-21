# /usr/bin/env python3

from datetime import datetime


class Book:
    def __init__(self, title: str, author: str, publication_year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.publication_year: int = publication_year

    # The @property decorator allows a method to be accessed like an attribute, enabling computed properties in a class.
    # By default, it makes it read-only.
    @property
    def age(self) -> int:
        current_year = datetime.now().year
        return current_year - self.publication_year

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}, published in {self.publication_year}."


if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)

    print(book)
    # return: '1984' by George Orwell, published in 1949.

    print(f"The book is {book.age} years old.")
    # return: The book is X years old.

    # Attempting to modify it will throw an error
    try:
        book.age = 1901
        print(book.age)
    except AttributeError:
        print("You cannot change the publication year")
