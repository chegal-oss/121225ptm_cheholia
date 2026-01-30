_DEBUG = True
for task in range(1, 5):
    match task:
        case 1:
            # 1 Проверка кодировки
            symbol = "A" if _DEBUG else input("Введите символ: ")
            print("Код Unicode = ", ord(symbol))
            print("ASCII символ: ", bool(ord(symbol) < 128))
        case 2:
            #2 Подстрока с заполнением
            string = "Программирование" if _DEBUG else input("Введи строку: ")
            #first, last = int(input("Введите начальный индекс: ")), int(input("Введите конечный индекс: "))
            first, last = 3, 20
            substring = string[first:last]
            print("Подстрока:", substring + "_" * (last - len(substring)))
        case 3:
            #3 Подсчёт символа
            string = "Hello, world!" if _DEBUG else input("Введи строку: ")
            symbol = "o" if _DEBUG else input("Введите символ: ")
            print("Символ o встречается", string.count(symbol), "раз(а).")
        case 4:
            #4 Инвертирование строки без цифр
            string = "n52uFs6Inoh67ty8P" if _DEBUG else input("Введи строку: ")
            i = len(string)
            parts = []
            while i > 0:
                i -= 1
                if string[i].isdigit():
                    continue
                parts += string[i]
            print("".join(parts))
            # или
            print("".join([x for x in string[::-1] if not x.isdigit()]))
