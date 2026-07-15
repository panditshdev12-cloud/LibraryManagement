from datetime import datetime


class Transaction:
    """Represents a borrow or return transaction."""

    def __init__(
        self,
        transaction_id,
        member_id,
        book_id,
        action,
        date=None
    ):
        self.transaction_id = transaction_id
        self.member_id = member_id
        self.book_id = book_id
        self.action = action
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_info(self):
        print("\n----- Transaction Details -----")
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Member ID: {self.member_id}")
        print(f"Book ID: {self.book_id}")
        print(f"Action: {self.action}")
        print(f"Date: {self.date}")
        print("-" * 30)

    def update_action(self, action):
        self.action = action

    def get_summary(self):
        return (
            f"{self.member_id} "
            f"{self.action.lower()}ed "
            f"{self.book_id} on {self.date}"
        )

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "member_id": self.member_id,
            "book_id": self.book_id,
            "action": self.action,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            transaction_id=data["transaction_id"],
            member_id=data["member_id"],
            book_id=data["book_id"],
            action=data["action"],
            date=data["date"]
        )