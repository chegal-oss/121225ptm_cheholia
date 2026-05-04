print("\nPython Fundamentals 2025: Домашнее задание 35")
print("\nСчётчик экземпляров + Проверка данных пользователя")


class User:
    _total_user = 0

    def __init__(self, username: str, password: str):
        if not username:
            raise ValueError("Empty username")

        if len(password) <= 5:
            raise ValueError(f"Invalid password {password}")

        self.username = username
        self.password = password
        print("Created:", username)
        User._total_user += 1

    @staticmethod
    def get_total():
        return f"Total user: {User._total_user}"


for n, p in (("Вася", "qwerty"), ("", "qweqwewq"), ("Вася", "qwe")):
    try:
        _ = User(n, p)
    except ValueError as e:
        print("Value error:", e)

print(User.get_total())
