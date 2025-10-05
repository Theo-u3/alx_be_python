import unittest
from library_management import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Set up a new library before each test."""
        self.lib = Library()

    def test_add_book(self):
        result = self.lib.add_book("Python 101")
        self.assertIn("Python 101", self.lib.books)
        self.assertEqual(result, '"Python 101" has been added to the library.')

    def test_borrow_book_success(self):
        self.lib.add_book("AI Basics")
        result = self.lib.borrow_book("AI Basics")
        self.assertEqual(result, 'You have borrowed "AI Basics".')
        self.assertNotIn("AI Basics", self.lib.books)

    def test_borrow_book_not_available(self):
        result = self.lib.borrow_book("Nonexistent Book")
        self.assertEqual(result, 'Sorry, "Nonexistent Book" is not available.')

    def test_return_book(self):
        result = self.lib.return_book("Data Science 101")
        self.assertIn("Data Science 101", self.lib.books)
        self.assertEqual(result, 'Thank you for returning "Data Science 101".')

    def test_display_books(self):
        self.lib.add_book("Python Basics")
        output = self.lib.display_books()
        self.assertIn("Python Basics", output)

if __name__ == "__main__":
    unittest.main()
