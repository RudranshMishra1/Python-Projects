class Book:

    def __init__(self, book_name, book_author, book_id):
        self.book_name = book_name
        self.book_author = book_author
        self.book_id = book_id
        self.available = True

    def book_details(self):
        print(f"Title : {self.book_name}")
        print(f"Author : {self.book_author}")
        print(f"Book ID : {self.book_id}")
        print(f"Book Availability : {self.available}")

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"{self.book_name} has been borrowed successfully.")
            
        else:
            print(f"{self.book_name} is already borrowed.")


    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.book_name} has been returned successfully.")
        else:
            print(f"{self.book_name} is already in the library")



class Library:

    def __init__(self):
       self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.book_name} added successfully! ✅")

    def view_books(self):
        for book in self.books:
            book.book_details()

    def search_book(self, book_id):
        found = False

        for book in self.books:
            if book.book_id == book_id:
                print("\n📚 Book Found!\n")
                book.book_details()
                found = True
                break

        if not found:
            print("Book not found ❌")


library = Library()


while True:

    print("\n========== 📚 LIBRARY MANAGEMENT SYSTEM ==========\n")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit\n")
    print("=" * 50)

    user = input("Choose an option: ")

    if user == "1":

        name = input("Enter the Name of the book: ")
        author = input("Enter the Name of the Author: ")
        bkid = input("Enter the book id: ")

        bookk = Book(name,author,bkid)
        library.add_book(bookk)

    elif user == "2":

        if not library.books:
            print("No books in the library.")
            
        else:
            library.view_books()


    elif user == "3":
            
            book_id = input("Enter the Book ID: ")
            library.search_book(book_id)


    elif user == "4":
            
            book_id = input("Enter the ID of the Book you want to borrow: ")

            for book in library.books:
                if book.book_id == book_id:
                    book.borrow_book()


    elif user == "5":

            book_id = input("Enter the ID of the Book you want to return: ")

            for book in library.books:
                if book.book_id == book_id:
                    book.return_book()

    elif user == "6":
        print("Thanks for visiting the library 😊")
        break

    else:
        print("Please choose a valid option (1-6)")