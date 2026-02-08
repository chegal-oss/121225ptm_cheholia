for task in range(1, 4):
    match task:
        case 1:
            print("\nPython Fundamentals 2025: Домашнее задание 11")
            print("1.Звёздочки вместо чисел")
            text = "My number is 123-456-789"
            print("Строка:", text)
            print("Результат: ", "".join([c if not c.isdigit() else "*" for c in text]))
            print("Результат: ", "".join(map(lambda c : "*" if c.isdigit() else c, text)))
            new_string = list(text)
            for i in range(len(new_string)):
                char = new_string[i]
                new_string[i] = "*" if char.isdigit() else char
            print("Результат: ", "".join(new_string))


        case 2:
            print("\n2.Количество символов")
            text = "Programming in python"
            print("Строка:", text)
            text = text.lower()
            while text:
                c = text[0]
                print(f"Символ '{c}' встречается {text.count(c)}") if text.count(c) > 1 else None
                text = text.replace(c, "")

        case 3:
            print("\n3.Увеличение чисел")
            text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
            print(text)
            result = []
            for word in text.split():
                old = new = word.strip(".,")
                if new.isdigit():
                    new = str(int(new) * 10)
                else:
                    test_float = new.split(".")
                    if len(test_float) > 1 and test_float[0].isdigit() and test_float[1].isdigit():
                        new = str(float(new) * 10)
                result.append(word.replace(old, new))
            print(" ".join(result))





