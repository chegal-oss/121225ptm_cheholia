from typing import Iterable

print("\nPython Fundamentals 2025: Домашнее задание 29")
print("\n1. Генератор Фибоначчи")

def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b ,a + b

for i in fib_gen():
    if i > 50:
        break
    print(i)

print("\n2. Генератор уникальных элементов")
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
def gen_list(data : list[int]) -> Iterable[int]:
    seen = set()
    for item in data:
        if item not in seen:
            seen.add(item)
            yield item

for x in gen_list(data):
    print(x)
