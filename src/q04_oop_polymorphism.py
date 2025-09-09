class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = float(price)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price:.2f}"

class EBook(Book):
    def __init__(self, title: str, author: str, price: float, file_size: float):
        super().__init__(title, author, price)
        self.file_size = float(file_size)

    def get_details(self) -> str:
        return f"{super().get_details()}, File Size: {self.file_size:.1f}MB"

def print_details(obj):
    
    if not hasattr(obj, "get_details"):
        raise TypeError("Object does not support get_details()")
    print(obj.get_details())

if __name__ == "__main__":
    items = [
        Book("Clean Code", "Robert C. Martin", 500),
        EBook("Fluent Python", "Luciano Ramalho", 900, 2.5),
        Book("Atomic Habits", "James Clear", 399),
        EBook("Deep Learning", "Ian Goodfellow", 1200, 5.0),
    ]
    for it in items:
        print_details(it)
