from book import Book
from catalogue import LibraryCatalogue

def get_user_input():
    while True:
        print("=========== Library Catalogue System ===========")
        print("1. Add Book")
        print("2. Check Out Book")
        print("3. Return Book")
        print("4. Display All Books")
        print("5. Exit")
        print("===============================================")
        choice = input("Choose an option: ")
        print("===========")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice. Please try again.")
            print("===========")

def execute_choice(choice, catalogue):
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book = Book(title, author)
        catalogue.add_book(book)
    elif choice == "2":
        title = input("Enter book title to check out: ")
        book = catalogue.find_book(title)
        if book:
            book.check_out()
        else:
            print(f"Book '{title}' not found in the catalogue.")
    elif choice == "3":
        title = input("Enter book title to return: ")
        book = catalogue.find_book(title)
        if book:
            book.return_book()
        else:
            print(f"Book '{title}' not found in the catalogue.")
    elif choice == "4":
        catalogue.display_all_books()
    elif choice == "5":
        print("Exiting the system.")
        exit()

def main():
    catalogue = LibraryCatalogue()
    while True:
        choice = get_user_input()
        execute_choice(choice, catalogue)

if __name__ == "__main__":
    main()