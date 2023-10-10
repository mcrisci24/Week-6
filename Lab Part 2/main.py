# library_ui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import main  # Assuming main.py contains the functions for the library operations
from books import *
from members import *


def register_member():
    name = simpledialog.askstring("Input",                              # This defines a function to register new members.
                                  "Enter the member's name: ")        # This creates a box to enter to search member's names
    if name:
        register_member(name)                                                 # This allows to add new members to system
    # Call the function to register a member
        messagebox.showinfo("Info",                                     # This creates a message box that displays this string "Register member functionality here"
                            "Register member functionality here")
    else:
        messagebox.showwarning("Warning",                                               # This message box will appear if name is not provided then return a warning an cancel registration.
                               "Registration cancelled. Name was not provided.")



def borrow_book():
    title = simpledialog.askstring("Input",                                             # This defines a function that designs a tab for members to borrow books
                                   "Enter title of the book you want to borrow: ")
    if title:
        if borrow_book(title):
            messagebox.showinfo("Success",                                           # If book is available return string that displays a congratulations message
                                f"Congratulations! You borrowed {title}. "
                                f"Enjoy {title}, fellow book junkie! As a courtesy to other members, "
                                f"please return by due date to avoid late fees.")
        else:
            messagebox.showerror("Error",                                            # This creates a error message if book is unavailable or does not exist in the library system.
                                 f"The book {title} is either unavailable or doesn't exist. "
                                 f"Please try another book title.")
    else:
        messagebox.showwarning("Warning",                                           # This string displays a warning message if a book title is not provided and asks member to try again.
                               "Borrowing process was cancelled. Book title was not provided. Please try again!")


    messagebox.showinfo("Info",
                        "Borrow book functionality here")                       # This calls the function to borrow a book


def return_book():
    title = simpledialog.askstring("Input",
                                   "Hello, enter title of the book you would like to return: ")     # This defines a function and the string asks member what book title they would like to return.
    if title:
        if return_book(title):
            messagebox.showinfo("Success",                                                          # This if statement returns string that congratulates members who successfully return books.
                                f"Congratulations! You successfully returned {title}."
                                f" You're a the bookworm!")
        else:
            messagebox.showerror("Error",                                                # This message box uses a string to display an error if the book title is not found in the library system.
                                 f"Uh Oh! "
                                 f"The book, {title} you entered was not found in our system."
                                 f" Please try again.")
    else:
        messagebox.showwarning("Warning!",
                               f"The return process was cancelled."             # This message box displays when a book title is not provided and cancels the return process.
                               f" Book title not was not provided."                     
                               f" Please try again!")

    # Call the function to return a book
    messagebox.showinfo("Info", "Return book functionality here")           # This calls the function to return books


def display_books():
    title = simpledialog.askstring("Input",
                                   "Enter the title of the books")
    # Call the function to display all books
    messagebox.showinfo("Info", "Display books functionality here")


def display_members():
    books_list = '\n'.join(f"Title:{book['title']}, "
                           f"Author:{book['author']}, "
                           f"Available:{book['availability']}"
                           for book in library_books)
    member_list = '\n'.join(library_members)

    messagebox.showinfo("Info", "Display members functionality here")   # Call the function to display all members


def add_book():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input",
                                   "Enter the book's title:")
    if title:                                                               # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input",
                                        "Enter the book's author:")
        if author:  # Check if the user provided an author
            add_book(title, author)  # Using the function from books.py
            messagebox.showinfo("Success",
                                "Book added successfully!")
        else:
            messagebox.showwarning("Warning",
                                   "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning",
                               "Book addition cancelled. Title was not provided.")


root = tk.Tk()
root.title("Library Management System")

# Menu buttons
add_book_btn = tk.Button(root, text="Add a new book", command=add_book)
add_book_btn.pack(pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=register_member)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrow_book)
borrow_book_btn.pack(pady=10)

return_book_btn = tk.Button(root, text="Return a book", command=return_book)
return_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=display_books)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=display_members)
display_members_btn.pack(pady=10)

exit_btn = tk.Button(root, text= "Exit", command=root.destroy)
exit_btn.pack(pady=50)

root.mainloop()