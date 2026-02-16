print("\nPython Fundamentals 2025: Домашнее задание 18")
print("\n1. Не уникальные числа")
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
print(sorted([x for x in set(numbers) if numbers.count(x) > 1], reverse=True))

print("\n2. Проверка подмножества")

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

if dict1.items() <= dict2.items():
    print("Первый словарь является подмножеством второго")
elif dict1.items() >= dict2.items():
    print("Второй словарь является подмножеством второго")
else:
    print("Словари различны")

