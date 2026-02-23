import random

print("\nPython Fundamentals 2025: Домашнее задание 36")
print("\n1. Класс Person")

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}")
        print(f"My subject is {self.subject}")

alice = Student("Alice", 2)
alice.introduce()

bob = Teacher("Bob", "Mathematics")
bob.introduce()



