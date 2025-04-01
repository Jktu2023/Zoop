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
        print(f'{self.kind}, имя: {self.name}, возраст: {self.age} года\n')


class Zoo:  # класс зоопарка  дочерний от Animal по композиции
    def __init__(self):
        self.personal = []  # Список для персонала
        self.animals = []  # Список для животных

    def add_personal(self, kind, name, age):  # Добавить сотрудника
        new_personal = Animal(kind, name, age)  # создаем экземпляр Animal
        self.personal.append(new_personal)  # в собственный список self.personal довавляем сотрудника
        print('\nДобавлен сотрудник:', new_personal.kind, new_personal.name, new_personal.age)
        print('список персонала после добавления содержит:', len(self.personal))

    def add_animal(self, kind, name, age):  # Добавить животное
        new_animal = Animal(kind, name, age)  # создаем экземпляр Animal
        self.animals.append(new_animal)  # добавляем его в список животных
        print('\nДобавлено животное:', new_animal.kind, new_animal.name, new_animal.age)

    def show_personal(self):
        print('В списке:', len(self.personal))
        for person in self.personal:
            person.info()  # выводим информацию о каждом сотруднике в зоопарке

    def show_animals(self):
        print('В списке:', len(self.animals))  # Исправлено: показывать количество животных
        for animal in self.animals:
            animal.info()  # выводим информацию о каждом животном


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


# Пример использования
zoo = Zoo()  # создаем экземпляр от Zoo
zoo.add_animal('Зебра', 'Валя', 10)  # добавляем животное
zoo.add_personal('Дворник', 'Коля', 30)  # добавляем сотрудника

storozh = ZooKeeper(zoo, 'Сторож', 'Иван', 40)  # Создаем экземпляр ZooKeeper
storozh.feed_animal()  # печатаем что делает сторож

veterinar = Veterinarian(zoo, 'Ветеринар', 'Костя', 30)  # Создаем экземпляр Veterinarian
veterinar.heal_animal()  # печатаем что делает

# Печатаем списки персонала
zoo.show_personal()
