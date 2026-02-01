_DEBUG = True
for task in range(1, 4):
    match task:
        case 1:
            print("\nPython Fundamentals 2025: Домашнее задание 9")
            print("1.Таблица умножения")
            number = 5 if _DEBUG else int(input("Введите число: "))
            for i in range(1, number + 1):
                for j in range(1, number + 1):
                    print(i * j, end="\t")
                print()
        case 2:
            print("\n2.Лестница чисел")
            number = 5 if _DEBUG else int(input("Введите число: "))
            for row in range(1, number + 1):
                for line in range(1, row + 1):
                    print(line, end=" ")
                print()
        case 3:
            print("\n3.Удаление всех повторяющихся символов")
            string = "Python programming" if _DEBUG else input("Введите строку: ")
            result = ""
            for char in string:
                if char not in result:
                    result += char
            print(result)
