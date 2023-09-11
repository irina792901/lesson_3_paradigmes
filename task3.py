class SimpleBookShelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


book_shelf = SimpleBookShelf()
book_shelf.add_book("Книга 1")
book_shelf.add_book("Книга 2")

for book in book_shelf.books:
    print(book)
