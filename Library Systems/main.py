from books import add_book, borrow_book, return_book, find_book
from members import register_member, find_member

def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            # Call function to add a new book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title,author)
            print(f"Book '{title}' by {author} added successfully.")

        elif choice == "2":
            # Call function to register a new member
            name = input("Enters members name:")
            register_member(name)
            print(f"Member '{name}' registered successfully")

        elif choice == "3":
            # Call function to borrow a book
            name = input ("Enter book title to borrow")
            if find_member(name):
                title = input("Enter book title to borrow")
                if find_book(title):
                    borrow_book(title)
                    print(f"Book '{title}' borrowed successfully.")
                else:
                    print(f"Book '{title}' not found.")
            else:
                print("You are not a registered member")
        elif choice == "4":
            # Call function to return a book
            title = input("Enter book title to return")
            if find_book(title):
                return_book(title)
                print(f"Book ' {title}' returned successfully")
            else:
                print(f"Book '{title}' not found")

        elif choice == "5":
            # Call function to display all books
            print("Library Books:")
            for book in library_books:
                print(f"Title: {book['title']}, "
                      f"Author: {book['author']}, "
                      f"Available:{book['availability']}")
        elif choice == "6":
            # Call function to display all members
            print("Library Members")
            for member in library_members:
                print(member)
        elif choice == "7":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
