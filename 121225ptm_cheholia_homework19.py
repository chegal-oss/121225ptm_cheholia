print("\nPython Fundamentals 2025: Домашнее задание 19")
print("\n1. Реверс словаря")
data = {"a": 1, "b": 2, "c": 1, "d": 3}
data2 = {}
for k, d in data.items():
    data2.setdefault(d, list()).append(k)
print(data2)

print("\n2. Счётчик букв в словах")
words = ["anna", "bennet", "john"]
data = dict()
for word in words:
    data[word] = {x : word.count(x) for x in set(word)}
print(data)

print("\n3. Распределение студентов по группам")
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
groups_ball = ((85, 100), (70, 84), (50, 69), (0, 50))
data = dict()
for group, (b1, b2) in zip(groups, groups_ball):
    data[group] = {n : b for n, b in students.items() if b1 <= b <= b2}
print(data)


