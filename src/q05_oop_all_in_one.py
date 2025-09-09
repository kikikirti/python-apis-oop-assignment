from typing import Iterable, Iterator, List, Optional

class Price:
    def __init__(self, value: float, currency: str = "INR"):
        try:
            self.value = round(float(value), 2)
        except (TypeError, ValueError):
            raise ValueError("Price value must be a number")
        if self.value < 0:
            raise ValueError("Price value must be non-negative")
        if not isinstance(currency, str) or not currency:
            raise ValueError("Currency must be a non-empty string")
        self.currency = currency

    def __repr__(self) -> str:
        return f"Price(value={self.value:.2f}, currency='{self.currency}')"

    def __str__(self) -> str:
        return f"{self.currency} {self.value:.2f}"

class Book:
    def __init__(self, title: str, author: str, price: Price):
        if not isinstance(price, Price):
            raise TypeError("price must be a Price instance")
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        # Equality by title+author as requested
        return (self.title, self.author) == (other.title, other.author)

    def __repr__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', price={repr(self.price)})"

    def __str__(self) -> str:
        return f"{self.title} by {self.author} — {self.price}"

    @classmethod
    def from_dict(cls, d: dict) -> "Book":
        
        title = d.get("title")
        author = d.get("author")
        value = d.get("price")
        currency = d.get("currency", "INR")
        return cls(title=title, author=author, price=Price(value, currency))

class Inventory:
    def __init__(self, books: Optional[Iterable[Book]] = None):
        self._books: List[Book] = list(books) if books else []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str, author: str) -> bool:
        for i, b in enumerate(self._books):
            if b.title == title and b.author == author:
                del self._books[i]
                return True
        return False

    def find_by_author(self, author: str) -> List[Book]:
        return [b for b in self._books if b.author == author]

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self) -> Iterator[Book]:
        return iter(self._books)

if __name__ == "__main__":
    raw_books = [
        {"title": "Clean Code", "author": "Robert C. Martin", "price": 499},
        {"title": "Fluent Python", "author": "Luciano Ramalho", "price": 999.0},
        {"title": "Atomic Habits", "author": "James Clear", "price": 399.5, "currency": "INR"},
    ]
    inv = Inventory(Book.from_dict(d) for d in raw_books)

    print("All books:")
    for b in inv:
        print("-", b)

    removed = inv.remove_book("Atomic Habits", "James Clear")
    print("Removed Atomic Habits?", removed)
    print("Inventory length:", len(inv))

    print("By author 'Luciano Ramalho':")
    for b in inv.find_by_author("Luciano Ramalho"):
        print("-", b)
