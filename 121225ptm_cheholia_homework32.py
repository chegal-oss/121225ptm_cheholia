import datetime

print("\nPython Fundamentals 2025: Домашнее задание 32  ")
print("\n1. Фабрика функций округления")

def make_rounder(n: int):
    def wrapper(number: float):
        return round(number, n)
    return wrapper

round2 = make_rounder(2)
round0 = make_rounder(0)
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

print("\n2. Расширяемый логгер событий")

def get_logger():
    messages = []
    def log(message = None):
        if message:
            messages.append(f"{message} {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
            return None
        else:
            return messages
    return log

log = get_logger()
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for mes in log():
    print(mes)

print("\n3. Рамка вокруг вывода")


def decorator_say_hello(sym = "-", num=50):
    def decorator(func):
        def wrapper():
            print(sym * num)
            func()
            print(sym * num)
        return wrapper
    return decorator

@decorator_say_hello()
def say_hello():
    print("Привет, игрок!")

say_hello()




