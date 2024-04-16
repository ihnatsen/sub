# 06.03.2024


class Library:
    def __init__(self):
        self.books = list()
        self.readers = list()

    def add_book(self, *books):
        """Add a book for list books"""
        for book in books:
            self.books.append(book)

    def add_reader(self, *readers_):
        """Add a new reader in the library"""
        for reader in readers_:
            self.readers.append(reader)

    def print_free_books(self):
        """print list free books"""
        free_books = [book.title for book in self.books if book.state]
        if free_books:
            print('Free books:')
            for title in free_books:
                print(title)
        else:
            print('None books')


class Book:
    def __init__(self, title, author, year_public):
        self.title = title
        self.author = author
        self.year_public = year_public
        self.state = True

    def borrow_book(self):
        self.state = False

    def back_book(self):
        self.state = True


class Reader:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_book = list()

    def take_book(self, book: Book):
        if book.state:
            self.borrowed_book.append(book)
            book.borrow_book()

    def back_book(self, book: Book):
        self.borrowed_book.remove(book)
        book.back_book()


library = Library()
book1 = Book('Whispers of Eternity', 'Isabella', 2002)
book2 = Book('Echoes in the Moonlight', 'Victor ', 2001)
book3 = Book('Harmony of the Spheres', 'Lila', 2000)
library.add_book(book1, book2, book3)

reader1 = Reader('Ivan', 'Ihnatsenkau')
reader2 = Reader('Anna', 'Kowalska')
library.add_reader(reader1, reader2)

reader1.take_book(book1)
library.print_free_books()
