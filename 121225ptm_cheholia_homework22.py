from functools import reduce

print("\nPython Fundamentals 2025: Домашнее задание 22")
print("\n1. Выбор заказов")
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
print(sorted(map(lambda x: x["product"], filter(lambda x : x["price"] > 500, orders))))

print("\n2. Статистика продаж")
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]
print(dict(sorted(map(lambda x : (x[0], x[1] * x[2]), sales),key=lambda x : x[1], reverse=True)))



