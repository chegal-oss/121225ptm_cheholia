print("\nPython Fundamentals 2025: Домашнее задание 35")
print("\nСчётчик экземпляров + Проверка данных пользователя")


class User:
    _total_user = 0

    def __init__(self, username: str, password: str):
        User._total_user += 1
        if username and len(password) > 5:
            self.username = username
            self.password = password
            print("Created:", username)
        else:
            raise ValueError("Empty username" if not username else f"Invalid password '{password}'")

    def __del__(self):
        User._total_user -= 1

    @staticmethod
    def get_total():
        return f"Total user: {User._total_user}"


temp = [("Вася", "qwerty"), ("", "qweqwewq"), ("Вася", "qwe")]
ref_collector = []
for n, p in temp:
    try:
        ref_collector.append(User(n, p))
    except ValueError as e:
        print("Value error:", e)

print(User.get_total())
ref_collector.clear()
print(User.get_total())
