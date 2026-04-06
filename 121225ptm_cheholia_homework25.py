import logging
import sys

print("\nPython Fundamentals 2025: Домашнее задание 25")

class MyMadFunctionException(BaseException):
    pass

def div_without_error(a: str, b: str) -> float:
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        raise MyMadFunctionException("Ошибка: На ноль делить нельзя.")
    except ValueError:
        raise MyMadFunctionException("Ошибка: Введено некорректное число.")


log_format = "%(asctime)s - %(filename)s - %(levelname)s - %(lineno)d - %(message)s"
logging.basicConfig(
    filename="errors.log",
    format=log_format,
    level=logging.ERROR
)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(log_format))
logging.getLogger().addHandler(stream_handler)


print("\n1. Деление без ошибок")
a, b = "345.2121", "5a"
print("Введите делимое:", a)
print("Введите делитель:", b)

try:
    res = div_without_error(a, b)
except MyMadFunctionException as e:
    logging.error(e)
else:
    print(res)


