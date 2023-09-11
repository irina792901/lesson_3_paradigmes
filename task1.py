# This is a sample Python script.
# # Определяем класс Person
class Person:
    #     # Конструктор класса, инициализирующий атрибуты имя и возраст
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод для представления информации о человеке
    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")


# Создаем объекты класса Person
person1 = Person("Анна", 25)
person2 = Person("Иван", 30)

# Вызываем методы объектов
person1.introduce()  # Вывод: Привет, меня зовут Анна и мне 25 лет.
person2.introduce()  # Вывод: Привет, меня зовут Иван и мне 30 лет.
