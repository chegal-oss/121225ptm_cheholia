import datetime
import time

print("\nPython Fundamentals 2025: Домашнее задание 33  ")
print("\n1-2. Среднее время выполнения + Среднее время выполнения с количеством вызовов")

def measure_time(repeat_count: int = 5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            res = None
            for _ in range(repeat_count): res = func(*args, **kwargs)
            time_exec = datetime.datetime.now() - start
            print(f"Среднее время выполнения для {repeat_count} вызовов: {round(time_exec.microseconds / 1000000 / repeat_count, 2)} секунд")
            return res
        return wrapper
    return decorator

@measure_time(7)
def test():
    time.sleep(0.11)
    return "OK"

print(test())


