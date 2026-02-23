import random

print("\nPython Fundamentals 2025: Домашнее задание 34")
print("\n1. Класс Rectangle")


class Rectangle:
    def __init__(self, w: int, h: int):
        self.width: int = w
        self.height: int = h

    def get_area(self) -> int:
        return self.width * self.height


rectangle = Rectangle(4, 5)
print(f"Площадь:", rectangle.get_area())
rectangle.width = 5
rectangle.height = 7
print(f"Новая площадь:", rectangle.get_area())

print("\n2. Класс Counter")


class Counter:
    def __init__(self):
        self._counter = 0

    def add_one(self):
        self._counter += 1
        print("Значение увеличено.", self)
    def sub_one(self):
        self._counter -= 1
        print("Значение уменьшено.", self)

    def __gt__(self, other: int):
        return self._counter > other

    def __str__(self):
        return f"Текущее значение: {self._counter}"


counter = Counter()
for i in range(5):
    if random.randint(0, 1) and counter > 0:
        counter.sub_one()
    else:
        counter.add_one()

print(counter)


