from library_management import Book, Library

def main():
    # Create library
    library = Library()

    # Add books
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    # Check out a book
    print("\n" + library.check_out_book("1984"))
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Return a book
    print("\n" + library.return_book("1984"))
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
