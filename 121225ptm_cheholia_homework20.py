print("\nPython Fundamentals 2025: Домашнее задание 20")
print("\n1. Простое число")
n = 17
def simple_number(number: int) -> bool:
    for i in range(2, number):
        if not number % i:
            return False
    return True
print(f"Число {n}","является простым" if simple_number(n) else "не является простым")

print("\n2. Фильтрация чисел по чётности")
def filter_numbers(filter_type: str, *args) -> list | str:
    if filter_type not in ("even", "odd"):
        return "Некорректный фильтр"
    return [x for x in args if x % 2 == (filter_type != "even")]

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

print("\n3. Объединение словарей")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
def merge_dicts(*args) -> dict:
    res = {}
    for item in args:
        res.update(item)
    return res

print(merge_dicts(dict1, dict2, dict3))


