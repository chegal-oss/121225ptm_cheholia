import random

_DEBUG = True
for task in range(1, 4):
    match task:
        case 1:
            # 1.Сумма цифр числа
            number = "12345" if _DEBUG else input("Введите число: ")
            number_sum = 0
            i = 0
            while i < len(number):
                number_sum += int(number[i])
                i += 1
            print("Сумма цифр:", number_sum)
        case 2:
            # 2.Палиндром
            number = "12321" if _DEBUG else input("Введите число: ")
            palindrome = ""
            i = len(number) - 1
            while i >= 0:
                palindrome += number[i]
                i -= 1

            print("Палиндром" if number == palindrome else "Не палиндром")
            #Или
            print("Палиндром" if number == number[::-1] else "Не палиндром")
        case 3:
            # 3.Проверь интуицию
            random_number = random.randint(1, 100)
            count = 0
            print("Угадайте число от 1 до 100. У вас 10 попыток.")
            while count < 10:
                number = random.randint(1, 100) if _DEBUG else int(input(str(count + 1) + ". Ваше предположение: "))
                print((str(count + 1) +". Ваше предположение: "), number)
                if number == random_number:
                    print("Поздравляем! Вы угадали число: ", random_number)
                    break
                print("Загаданное число меньше вашего" if random_number < number else "Загаданное число больше вашего")
                count += 1
            else:
                print("Вы не угадали, число:", count)
