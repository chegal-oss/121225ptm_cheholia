print("\nPython Fundamentals 2025: Домашнее задание 17")
print("\n1. Проверка на подмножество")
set1 = {1, 2, 3, 4}
set2 = {2, 3}
print(set2 <= set1)
print(len(set2 - set1) == 0)
print({x for x in set2 if x in set1} == set2)
f = True
for i in set2:
    if i not in set1:
        f = False
        break
print(f)

print("\n2. Зеркальное подмножество")
set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}
print("Подмножества: ", set1 <= set2 or set2 <= set1 )
print("Разница:", set1 - set2 if set1 >= set2 else set2 - set1)