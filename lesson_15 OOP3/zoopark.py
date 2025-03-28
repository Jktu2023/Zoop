# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.

class Animal():
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass
    def info(self):
        print(f'{self.kind}, kличка: {self.name}, возраст: {self.age} года')

class Lion(Animal):
    def make_sound(self):
        print('RRRR!')
    def eat(self):
        print('мясо')

class Monky(Animal):
    def make_sound(self):
        print('AAAA!')
    def eat(self):
        print('бананы')

class Elefant(Animal):
    def make_sound(self):
        print('UUUU!')
    def eat(self):
        print('Трава')

lion1 = Lion('Лев', 'Sam', 3)
lion1.info()

animals = [Lion('Лев','Sam', 3), Monky('Обезьяна','Lucy', 1), Elefant('Слон','Gorge', 4)]


for animal in animals:
    print(animal.kind)
    print(animal.name)
    animal.make_sound()
    animal.eat()
    print()
