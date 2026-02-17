from typing import Any, Iterable

print("\nPython Fundamentals 2025: Домашнее задание 23")
print("\n1. Объединение данных в строку")
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]


def str_union(data: list[Any]) -> str:
    """
    Принимает список любых данных (строки, числа, списки, словари)
    и возвращает их строковое представление, объединённое через " | "
    :param data: список
    :return: строка
    """
    return "|".join(map(str, data))


print(str_union(data))

print("\n2. Сумма вложенных чисел")
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]


def sum_number(data: list[dict]) -> int:
    """
    Принимает список словарей, где каждый словарь
    содержит имя пользователя и список баллов. Функция должна вернуть сумму всех чисел
    :param data: список словарей
    :return: число
    """
    return sum([s for d in data for s in d["scores"]])


print("Итоговый балл:", sum_number(data))
