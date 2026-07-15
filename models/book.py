class Book:
    """Represents a book in the library."""

    def __init__(
        self,
        book_id,
        title,
        author,
        genre,
        isbn,
        publication_year,
        available=True
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.publication_year = publication_year
        self.available = available

    def display_info(self):
        status = "Available" if self.available else "Borrowed"

        print("\n----- Book Information -----")
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Status: {status}")
        print("-" * 30)

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False

    def update_details(
        self,
        title=None,
        author=None,
        genre=None,
        isbn=None,
        publication_year=None
    ):
        if title:
            self.title = title

        if author:
            self.author = author

        if genre:
            self.genre = genre

        if isbn:
            self.isbn = isbn

        if publication_year:
            self.publication_year = publication_year

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "isbn": self.isbn,
            "publication_year": self.publication_year,
            "available": str(self.available)
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            book_id=data["book_id"],
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            isbn=data["isbn"],
            publication_year=data["publication_year"],
            available=data["available"] == "True"
        )

    def is_available(self):
        return self.available