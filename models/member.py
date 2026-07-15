class Member:
    """Represents a library member."""

    def __init__(
        self,
        member_id,
        name,
        email,
        phone,
        borrowed_books=None
    ):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = borrowed_books or []

    def display_info(self):
        print("\n----- Member Information -----")
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")

        if self.borrowed_books:
            print(
                f"Borrowed Books: {', '.join(self.borrowed_books)}"
            )
        else:
            print("Borrowed Books: None")

        print("-" * 30)

    def borrow_book(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def update_details(self, name=None, email=None, phone=None):
        if name:
            self.name = name

        if email:
            self.email = email

        if phone:
            self.phone = phone

    def total_borrowed_books(self):
        return len(self.borrowed_books)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "borrowed_books": "|".join(self.borrowed_books)
        }

    @classmethod
    def from_dict(cls, data):
        borrowed_books = []

        if data["borrowed_books"]:
            borrowed_books = data["borrowed_books"].split("|")

        return cls(
            member_id=data["member_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            borrowed_books=borrowed_books
        )