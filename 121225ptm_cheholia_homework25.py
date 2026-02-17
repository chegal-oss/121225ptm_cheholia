import logging

print("\nPython Fundamentals 2025: Домашнее задание 25")

print("n2. Логирование ошибок")
log_format = "%(asctime)s - %(filename)s - %(levelname)s - %(lineno)d - %(message)s"
logging.basicConfig(
    filename="errors.log",
    format=log_format,
    level = logging.ERROR
)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(log_format))
logging.getLogger().addHandler(stream_handler)

print("\n1. Деление без ошибок")
a, b = "345", "5a"
print("Введите делимое:", a)
print("Введите делитель:", b)
try:
    print(float(a) / float(b))
except ValueError:
    print("Ошибка: Введено некорректное число.")
    logging.error("Ошибка: Введено некорректное число.")
