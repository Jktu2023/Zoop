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

import csv



# ', 'a', encoding="utf-8") as file:
#     lit = input('Введите текст для сохранения его в файл - ')
#     file.write('\n' + lit+ '\n')

class Animal:
    def __init__(self, kind, name, age):  #
        self.kind = kind  # cобственные переменые: вид, имя, возраст
        self.name = name
        self.age = age

    def make_sound(self):  # заготовка какие звуки издает
        pass

    def eat(self):  # заготовка что ест
        pass

    def info(self):  # информация кто есть уже
        print(f'{self.kind}, имя: {self.name}, возраст: {self.age} лет')


class Zoo:  # класс зоопарка  дочерний от Animal по композиции
    def __init__(self):
        self.personal = []  # Список для персонала
        self.animals = []  # Список для животных

    def write_list_to_csv(self, data, filename):  # with open('personal_data.txt
        """
        Записывает список в CSV файл.

        :param data: Список данных, которые нужно записать.
        :param filename: Имя файла, в который будет записан список.
        """
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            try:
                for item in data:
                    writer.writerow([item])  # Записываем каждый элемент
            except:
                pass

    def add_personal(self, kind, name, age):  # Добавить сотрудника
        lst = []
        new_personal = Animal(kind, name, age)  # создаем экземпляр Animal
        self.personal.append(new_personal)  # в собственный список self.personal довавляем сотрудника
        print('\nДобавлен сотрудник:', new_personal.kind, new_personal.name, new_personal.age)
        stroka = new_personal.kind + ';' + new_personal.name + ';' + str(new_personal.age)
        lst.append(stroka)
        print('список персонала после добавления содержит:', len(self.personal))
        self.write_list_to_csv(lst, 'personal_data.txt')

    def add_animal(self, kind, name, age):  # Добавить животное
        new_animal = Animal(kind, name, age)  # создаем экземпляр Animal
        self.animals.append(new_animal)  # добавляем его в список животных
        print('\nДобавлено животное:', new_animal.kind, new_animal.name, new_animal.age)

    def show_personal(self):
        print('\nВ списке:', len(self.personal))
        for person in self.personal:
            person.info()  # выводим информацию о каждом сотруднике в зоопарке

    def show_animals(self):
        print('В списке:', len(self.animals))  # Исправлено: показывать количество животных
        for animal in self.animals:
            animal.info()  # выводим информацию о каждом животном

class ZooDirector:
    def __init__(self, zoo, kind, name, age):  # передаем экземпляр зоопарка
        self.zoo = zoo
        self.zoo.add_personal(kind, name, age)  # добавляем в список персонала при создании экземпляра
    def feed_animal(self):
        print(f'Директор - это директор!')

class ZooKeeper:
    def __init__(self, zoo, kind, name, age):  # передаем экземпляр зоопарка
        self.zoo = zoo
        self.zoo.add_personal(kind, name, age)  # добавляем в список персонала при создании экземпляра
    def feed_animal(self):
        print(f'ZooKeeper это хранитель животных')


class Veterinarian:
    def __init__(self, zoo, kind, name, age):  # передаем экземпляр зоопарка
        self.zoo = zoo
        self.zoo.add_personal(kind, name, age)  # добавляем в список персонала при создании экземпляра
    def heal_animal(self):
        print('Ветеринар лечит животных')


# запуск
zoo = Zoo()  # создаем экземпляр от Zoo

zoo.add_animal('Зебра', 'Валя', 10)  # добавляем животное
zoo.add_personal('Дворник', 'Коля', 30)  # добавляем сотрудника

director = ZooDirector(zoo, 'Директор', 'Петр Петрович', 45)  # Создаем экземпляр Director
director.feed_animal()  # печатаем что делает Director

storozh = ZooKeeper(zoo, 'Сторож', 'Иван', 40)  # Создаем экземпляр ZooKeeper
storozh.feed_animal()  # печатаем что делает сторож

veterinar = Veterinarian(zoo, 'Ветеринар', 'Костя', 30)  # Создаем экземпляр Veterinarian
veterinar.heal_animal()  # печатаем что делает

# Печатаем списки персонала
zoo.show_personal()

