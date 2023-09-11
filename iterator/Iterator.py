from abc import ABC, abstractmethod
# Итератор (Iterator): Это интерфейс, который определяет методы для обхода коллекции:
# has_next() (есть ли следующий элемент) и next() (получить следующий элемент).#
# Конкретный Итератор (Concrete Iterator): Реализация интерфейса Iterator для
# конкретной коллекции. Знает текущее положение в коллекции и как получить следующий элемент.#
# Агрегат (Aggregate): Это интерфейс, который определяет метод для получения итератора для коллекции.#
# Конкретный Агрегат (Concrete Aggregate): Конкретная реализация коллекции. Это может быть список,
# массив, дерево или любая другая структура данных.

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.book_shelf = book_shelf
        self.index = 0

    def has_next(self):
        return self.index < len(self.book_shelf.books)

    def next(self):
        book = self.book_shelf.books[self.index]
        self.index += 1
        return book


class BookShelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def iterator(self):
        return BookShelfIterator(self)


book_shelf = BookShelf()
book_shelf.add_book("Книга 1")
book_shelf.add_book("Книга 2")

iterator = book_shelf.iterator()

while iterator.has_next():
    print(iterator.next())
