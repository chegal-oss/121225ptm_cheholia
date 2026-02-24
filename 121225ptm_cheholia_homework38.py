print("\nPython Fundamentals 2025: Домашнее задание 38")
print("Банковский счёт")


class BankAccount:

    def __init__(self, owner_name, balance):
        self.__owner_name = owner_name
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        self.__history.append(("Deposit", amount))
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__history.append(("Withdraw", amount))
            self.__balance -= amount
        else:
            raise ValueError("Not enough funds.")

    def balance(self):
        print("Current balance:", self.__balance)

    @property
    def history(self):
        return [f"{o}: {a:.2f}" for o, a in self.__history]


bob_account = BankAccount("Bob", 50)
bob_account.balance()
bob_account.deposit(150)
bob_account.withdraw(100)
print("Operation history:", "\n\t" + "\n\t".join(bob_account.history))
