print("\nPython Fundamentals 2025: Домашнее задание 13")
print("\n1. Прогрессия увеличения")
numbers = (3, 7, 2, 8, 5, 10, 1)
print(numbers)
new_num = ()
for i, x in enumerate(numbers):
    if i == 0 or x > numbers[i - 1]:
        new_num += (x,)
print(new_num)

print("\n2. Повторяющиеся элементы")
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
tmp = ()
for i, x in enumerate(numbers):
    if numbers.count(x) > 1 and x not in tmp:
        tmp += (x,)
        print(f"Индексы элемента {x}:", end=" ")
        for j in range(i, len(numbers)):
            if x == numbers[j]:
                print(j, end=" ")
        print()

