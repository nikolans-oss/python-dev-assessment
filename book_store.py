class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026
        return current_year - self.publication_year
    
    def get_summary(self):
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Published: {self.publication_year}"
        )
    
book1 = Book(
    title = "Harry Potter and the Philosopher's Stone", 
    author = "J. K. Rowling",
    isbn = "978-0-7475-3269-9",
    publication_year = 1997)

book2 = Book(
    title = "The Alchemist", 
    author = "Paulo Coelho",
    isbn = "0-06-250217-4",
    publication_year = 1988)

book3 = Book(
    title = "A Man Called Ove", 
    author = "Fredrik Backman",
    isbn = "9781476738024",
    publication_year = 2012)
    
print(book1.get_summary())
print(f"Book age: {book1.get_age()} years")

print("\n")

print(book2.get_summary())
print(f"Book age: {book2.get_age()} years")

print("\n")

print(book3.get_summary())
print(f"Book age: {book3.get_age()} years")