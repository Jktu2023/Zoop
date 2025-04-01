# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


class Animal:
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def eat(self):
        pass
    def info(self):
        print(f'{self.kind}, имя: {self.name}, возраст: {self.age} года\n')

class Zoo:
    def __init__(self):
        self.personal = []
        self.animal = []
    def add_personal(self, kind, name, age):
        new_personal = Animal(kind, name, age)
        self.personal.append(new_personal)
        print('\nДобавлен персонал:', new_personal.kind, new_personal.name, new_personal.age)
    def add_animal(self, kind, name, age):
        new_animal = Animal(kind, name, age)
        self.animal.append(new_animal)
        print('\nДобавлено животное:', new_animal.kind, new_animal.name, new_animal.age)

    def show_personal(self):
        for person in self.personal:
            person.info()  # Выводим информацию о каждом сотруднике в зоопарке

    def show_animals(self):
        for animal in self.animals:
            animal.info()  # Выводим информацию о каждом животном в зоопарке


zoo = Zoo()
zoo.add_animal('Зебра', 'Валя', 10)
zoo.add_personal('Дворник', 'Кoля', 30)

class ZooKeeper(Zoo): #`feed_animal()` для `ZooKeeper`
    def feed_animal(self):
        print(f'ZooKeeper это хранитель животных')

storozh = ZooKeeper()
storozh.add_personal('Сторож', 'Иван', 40)
storozh.feed_animal()

class Veterinarian(Zoo):#`heal_animal()` для `Veterinarian`
    def heal_animal(self):
        print('Ветеринар лечит животных')
veterinar = Veterinarian()
veterinar.add_personal('Ветеринар', 'Костя', 30)
veterinar.heal_animal()

zoo.show_personal()


print()
print()
class Bird(Animal):
    def make_sound(self):
        print('Karrr!')
    def eat(self):
        print('черви')

class Mammal(Animal):
    def make_sound(self):
        print('AAAA!')
    def eat(self):
        print('мясо')

class Reptile(Animal):
    def make_sound(self):
        print('Shhh!')
    def eat(self):
        print('Трава')

lion_gerl = Mammal('Львица', 'Murca', 3)
lion_gerl.info()

animals = [Bird('Орел', 'Ugas', 5), Bird('Соловей', 'Ptaha', 2),
           Mammal('Лев','Sam', 3), Mammal('Обезьяна','Lucy', 1), Mammal('Слон','Gorge', 4),
           Reptile('Кобра', 'Elsa', 7), Reptile('Удав', 'Kaa', 10)]

for animal in animals:
    print(animal.kind)
    print(animal.name)
    animal.make_sound()
    animal.eat()
    print()

animals[0].info()

