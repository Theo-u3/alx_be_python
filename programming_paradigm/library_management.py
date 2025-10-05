class Book:
    """A class representing a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"'{self.title}' has been checked out."
        return f"'{self.title}' is already checked out."

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return f"'{self.title}' has been returned."
        return f"'{self.title}' was not checked out."

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class that manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def list_available_books(self):
        """Display all available books."""
        available_books = [
            f"{book.title} by {book.author}"
            for book in self._books
            if book.is_available()
        ]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.check_out()
        return f"Book '{title}' not found."

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"Book '{title}' not found."
