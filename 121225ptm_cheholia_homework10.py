DEBUG = True
for task in range(1, 3):
    match task:
        case 1:
            print("\nPython Fundamentals 2025: Домашнее задание 10")
            print("1.Торговый автомат")
            price = 127 if DEBUG else int(input("Введите стоимость товара: "))
            for coin in [50, 10, 5, 2, 1]:
                int_part = price // coin
                if int_part:
                    print(f"Внесите монеты номиналом {coin}:", int_part)
                    price %= coin
        case 2:
            print("\n2.Квадрат нечетных чисел")
            numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
            print("Изначальный список: ", numbers)
            print("Измененный список: ", [x ** 2 if x % 2 else x  for x in numbers])


