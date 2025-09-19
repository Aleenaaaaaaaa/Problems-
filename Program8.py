class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print("📖", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You have borrowed '{book_name}'")
        else:
            print("Sorry, this book is not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"You have returned '{book_name}'")


# Example
library = Library(["Python Basics", "Data Science", "Machine Learning"])
library.display_books()
library.borrow_book("Python Basics")
library.display_books()
library.return_book("Python Basics")
library.display_books()
