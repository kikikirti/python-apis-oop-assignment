class Book:
    def __init__(self, title: str, author: str, price: float, discount: float = 0.1):
        self.title = title
        self.author = author
        self.price = float(price)
        self._discount = 0.0
        self.discount = discount

    @property
    def discount(self) -> float:
        return self._discount

    @discount.setter
    def discount(self, value: float) -> None:
        value = float(value)
        if 0.0 <= value <= 0.9:
            self._discount = value
        else:
            raise ValueError("discount must be between 0.0 and 0.9")

    def get_price_after_discount(self) -> float:
        return self.price * (1 - self._discount)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price:.2f}"

class EBook(Book):
    def __init__(self, title: str, author: str, price: float, file_size: float, discount: float = 0.1):
        super().__init__(title, author, price, discount)
        self.file_size = float(file_size)

    def get_details(self) -> str:
        base = super().get_details()
        return f"{base}, File Size: {self.file_size:.1f}MB"

if __name__ == "__main__":
    e = EBook("Fluent Python", "Luciano Ramalho", 900, file_size=2.5, discount=0.2)
    print(e.get_details())
    print("Discounted price:", f"{e.get_price_after_discount():.2f}")
