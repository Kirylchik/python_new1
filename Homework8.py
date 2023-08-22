# Первое задание
class Auto:
    def __init__(self, brand, age, mark, color, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


my_auto = Auto(brand="Четырка", age=35, mark="Седан", color="Ржавая", weight="Имеет")
# Цвет и вес можно опустить
print("Данные автомобиля:")
print("Бренд:", my_auto.brand)
print("Возраст:", my_auto.age)
print("Марка:", my_auto.mark)
print("Цвет:", my_auto.color)
print("Вес:", my_auto.weight)

my_auto.move()
my_auto.stop()

print("Увеличение возраста:")
print("Возраст до:", my_auto.age)
my_auto.birthday()
print("Возраст после:", my_auto.age)

# Второе задание

import time


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


# Truck и Car
truck1 = Truck(brand="MAN", age=3, mark="МАЗ", max_load=10000)
truck2 = Truck(brand="МАЗ", age=5, mark="МАЗ", max_load=12000)

car1 = Car(brand="Lifan", age=2, mark="Китаец", max_speed=160)
car2 = Car(brand="Chery", age=4, mark="Китаец", max_speed=120)

# Проверка методов и атрибутов
print("Truck 1:")
truck1.move()
truck1.load()
print("Max Load:", truck1.max_load)
print("Age:", truck1.age)

print("\nTruck 2:")
truck2.move()
truck2.load()
print("Max Load:", truck2.max_load)
print("Age:", truck2.age)

print("\nCar 1:")
car1.move()
print("Max Speed:", car1.max_speed)
print("Age:", car1.age)

print("\nCar 2:")
car2.move()
print("Max Speed:", car2.max_speed)
print("Age:", car2.age)
