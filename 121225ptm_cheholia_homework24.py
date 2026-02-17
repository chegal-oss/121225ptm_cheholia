print("\nPython Fundamentals 2025: Домашнее задание 24")
print("\n1. Сумма цифр числа")
num = 43197
print(num)
def sum_number(num: int) -> int:
    if num:
        return num % 10 + sum_number(num // 10)
    return 0

print(sum_number(num))

print("\n2. Сумма вложенных чисел")
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
def sum_list(data: list) -> int:
    s = 0
    for item in data:
        if isinstance(item, list):
            s += sum_list(item)
        else:
            s += item
    return s

print(sum_list(nested_numbers))