class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the catalogue.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_all_books(self):
        if not self.books:
            print("No books in the catalogue.")
        else:
            for book in self.books:
                book.display_info()