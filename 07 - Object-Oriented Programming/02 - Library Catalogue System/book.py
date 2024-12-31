class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' checked out successfully.")
        else:
            print(f"Book '{self.title}' is currently unavailable.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.title}' returned successfully.")
        else:
            print(f"Book '{self.title}' was not checked out.")

    def display_info(self):
        status = "Available" if self.is_available else "Checked out"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")