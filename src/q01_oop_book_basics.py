class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = float(price)
    
    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: Rs{self.price:.2f}"

if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 299.99)
    book2 = Book("1984", "George Orwell", 199.50)
    book3 = Book("To Kill a Mockingbird", "Harper Lee", 249.75)
    print(book1.get_details())
    print(book2.get_details())
    print(book3.get_details())