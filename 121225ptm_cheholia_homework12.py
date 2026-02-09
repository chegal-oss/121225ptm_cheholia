print("\nPython Fundamentals 2025: Домашнее задание 12")
print("\n1.Сумма положительных чисел")
numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
print(numbers)
print(f"Сумма положительных чисел: ${sum(x for x in numbers if x > 0):.2f}")

print("\n2.Счета клиентов")
data_list = ["John 23 12345.678", "Alice 30 200.50", "Bob 35 15000.3", "Charlie 40 500.75"]
for name, age, balance in [item.split() for item in data_list]:
    print(f"Имя: {name:10} | Возраст: {age:>3} | Баланс: {float(balance):10.2f}")
