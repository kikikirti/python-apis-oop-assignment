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

if __name__ == "__main__":
    b = Book("Clean Code", "Robert C. Martin", 500)
    print("Default discount:", b.discount)
    print("Discounted price:", f"{b.get_price_after_discount():.2f}")

    b.discount = 0.25
    print("New discount:", b.discount)
    print("Discounted price:", f"{b.get_price_after_discount():.2f}")
