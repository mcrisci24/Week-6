library_books = []                             # This is a list of library books

def add_book(title, author):                                    # This defines a function that adds books to the library
    books = {"title": title, "author": author, "availability": True}
    library_books.append(book)

def borrow_book(title):                                         # This defines a functions that changes the availability of a book to false if unavailable because it is has been loaned out.
    for book in library_books:
        if book ["title"] == title and book ["availability"]:
            book["availability"] = False                        # This line tells function that if availability is not present, then return false to inform book unavailable
            return True
        return False                                            # Return false if unavailable

def return_book (title):                                        # Defines a function when book is returned to library to switch avaibility from unavailable (false) to available (true)
    for book in library_books:                                  # Looks for books in list called library_books
        if book["title"] == title and not book["availability"]:
            book["availability"] = True
            return True
        return False
def find_book(title):
    for book in library_books:
        if book["title"] == title:
            return book
        return None
