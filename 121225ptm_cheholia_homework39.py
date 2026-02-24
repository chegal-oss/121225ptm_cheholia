import math
from abc import ABC, abstractmethod

print("\nPython Fundamentals 2025: Домашнее задание 39")
print("Фигуры и площади")

class InvalidSizeError(Exception):
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, h, w):
        if h > 0 and w > 0:
            self.h = h
            self.w = w
        else:
            raise InvalidSizeError("Wrong parameters")

    def area(self):
        return self.h * self.w


class Circle(Shape):
    def __init__(self, r):
        if r > 0:
            self.r = r
        else:
            raise InvalidSizeError("Wrong parameters")

    def area(self):
        return math.pi * self.r ** 2

for shape in [Circle(3), Rectangle(4, 5)]:
    print(f"Area: {shape.area():.2f}")

try:
    Circle(-1)
except InvalidSizeError as e:
    print(e)




