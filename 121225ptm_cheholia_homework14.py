print("\nPython Fundamentals 2025: Домашнее задание 14")
print("\n1. Число в конце")
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
print(strings)
for x in reversed(strings):
    if not x.rstrip("0123456789").isalpha():
        strings.remove(x)
print(strings)

print("\n2. Удаление кратных")
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
print(numbers)
num = 3
for i in numbers.copy():
    if not i % num:
        numbers.remove(i)
print(numbers)

print("\n3. Порядок четных")
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
print(numbers)
new_numbers = []
even = []
for i in numbers:
    if not i % 2:
        even.append(i)
even.sort()

for i in numbers:
    if i % 2:
        new_numbers.append(i)
    else:
        new_numbers.append(even.pop())
print(new_numbers)






