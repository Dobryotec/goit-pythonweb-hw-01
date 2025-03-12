from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"    

class LibraryInterface(ABC):
    def __init__(self) -> None:
         self.books = []
         
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass    
    
    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        pass

class Library(LibraryInterface):
    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def get_books(self) -> list[Book]:
        return self.books

class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library
    
    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f"Book with title {title} added successfully")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info(f"Book with title {title} removed successfully")

    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            for book in books:
                logger.info(f"{book}")
        else:
            logger.info("Library is empty")

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")

if __name__ == "__main__":
    logger.info("Library Manager started")
    main()
