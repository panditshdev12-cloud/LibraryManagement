# main.py

from models.book import Book
from models.member import Member
from services.library import Library


def book_menu(library):
    while True:
        print("\n===== BOOK MANAGEMENT =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            isbn = input("ISBN: ")
            year = input("Publication Year: ")

            book = Book(
                book_id,
                title,
                author,
                genre,
                isbn,
                year
            )

            if library.add_book(book):
                print("Book added successfully.")
            else:
                print("Book ID already exists.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            keyword = input("Search title/author: ")

            results = library.search_book(keyword)

            if results:
                for book in results:
                    book.display_info()
            else:
                print("No books found.")

        elif choice == "4":
            book_id = input("Enter Book ID: ")

            if library.remove_book(book_id):
                print("Book removed.")
            else:
                print("Book not found.")

        elif choice == "5":
            break

        else:
            print("Invalid option.")


def member_menu(library):
    while True:
        print("\n===== MEMBER MANAGEMENT =====")
        print("1. Register Member")
        print("2. View Members")
        print("3. Remove Member")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            member_id = input("Member ID: ")
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")

            member = Member(
                member_id,
                name,
                email,
                phone
            )

            if library.register_member(member):
                print("Member registered.")
            else:
                print("Member already exists.")

        elif choice == "2":
            library.display_members()

        elif choice == "3":
            member_id = input("Member ID: ")

            if library.remove_member(member_id):
                print("Member removed.")
            else:
                print("Member not found.")

        elif choice == "4":
            break

        else:
            print("Invalid option.")


def main():
    library = Library()

    while True:
        print("\n==============================")
        print(" LIBRARY MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Transactions")
        print("6. Reports")
        print("7. Save and Exit")

        try:
            choice = input("Enter choice: ")

            if choice == "1":
                book_menu(library)

            elif choice == "2":
                member_menu(library)

            elif choice == "3":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")

                if library.borrow_book(
                    member_id,
                    book_id
                ):
                    print("Book borrowed successfully.")
                else:
                    print("Borrowing failed. Please check if the book is available or if the member exists.")

            elif choice == "4":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")

                if library.return_book(
                    member_id,
                    book_id
                ):
                    print("Book returned successfully.")
                else:
                    print("Return failed. Please check if the member exists and has borrowed the book.")

            elif choice == "5":
                library.display_transactions()

            elif choice == "6":
                library.generate_report()

            elif choice == "7":
                library.save_data()
                print("Data saved. Goodbye!")
                break

            else:
                print("Invalid option.")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()