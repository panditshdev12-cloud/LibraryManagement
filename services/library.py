from models.book import Book
from models.member import Member
from models.transaction import Transaction
from utils.file_handler import FileHandler


class Library:
    """Main class that manages library operations."""

    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

        self.books_file = "data/books.csv"
        self.members_file = "data/members.csv"
        self.transactions_file = "data/transactions.csv"

        self.load_data()

    def load_data(self):
        books = FileHandler.load_data(self.books_file)
        members = FileHandler.load_data(self.members_file)
        transactions = FileHandler.load_data(
            self.transactions_file
        )

        self.books = [
            Book.from_dict(book)
            for book in books
        ]

        self.members = [
            Member.from_dict(member)
            for member in members
        ]

        self.transactions = [
            Transaction.from_dict(transaction)
            for transaction in transactions
        ]

    def save_data(self):
        FileHandler.save_data(
            self.books_file,
            [book.to_dict() for book in self.books],
            [
                "book_id",
                "title",
                "author",
                "genre",
                "isbn",
                "publication_year",
                "available"
            ]
        )

        FileHandler.save_data(
            self.members_file,
            [member.to_dict() for member in self.members],
            [
                "member_id",
                "name",
                "email",
                "phone",
                "borrowed_books"
            ]
        )

        FileHandler.save_data(
            self.transactions_file,
            [
                transaction.to_dict()
                for transaction in self.transactions
            ],
            [
                "transaction_id",
                "member_id",
                "book_id",
                "action",
                "date"
            ]
        )

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                return False

        self.books.append(book)
        self.save_data()
        return True

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_data()
                return True

        return False

    def search_book(self, keyword):
        results = []

        for book in self.books:
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
            ):
                results.append(book)

        return results

    def register_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                return False

        self.members.append(member)
        self.save_data()
        return True

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                self.save_data()
                return True

        return False

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            return False

        if not book.borrow():
            return False

        member.borrow_book(book_id)

        transaction = Transaction(
            f"T{len(self.transactions) + 1}",
            member_id,
            book_id,
            "Borrow"
        )

        self.transactions.append(transaction)
        
        self.save_data()

        return True

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            return False

        if not member.return_book(book_id):
            return False

        book.return_book()

        transaction = Transaction(
            f"T{len(self.transactions) + 1}",
            member_id,
            book_id,
            "Return"
        )

        self.transactions.append(transaction)
        
        self.save_data()

        return True

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def display_books(self):
        if not self.books:
            print("No books available.")

        for book in self.books:
            book.display_info()

    def display_members(self):
        if not self.members:
            print("No members registered.")

        for member in self.members:
            member.display_info()

    def display_transactions(self):
        if not self.transactions:
            print("No transactions found.")

        for transaction in self.transactions:
            transaction.display_info()

    def generate_report(self):
        total_books = len(self.books)
        available_books = len(
            [
                book
                for book in self.books
                if book.available
            ]
        )

        total_members = len(self.members)
        total_transactions = len(self.transactions)

        print("\n===== Library Report =====")
        print(f"Total Books: {total_books}")
        print(f"Available Books: {available_books}")
        print(f"Borrowed Books: {total_books - available_books}")
        print(f"Total Members: {total_members}")
        print(f"Transactions: {total_transactions}")