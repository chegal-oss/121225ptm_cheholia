import math
from abc import ABC, abstractmethod
from datetime import datetime
from functools import total_ordering

print("\nPython Fundamentals 2025: Домашнее задание 40")
print("Электронное письмо")
print("*" * 50)
print()


@total_ordering
class Email:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __lt__(self, other):
        if isinstance(self, Email):
            return self.date < other.date
        return NotImplemented

    def __eq__(self, other):
        if isinstance(self, Email):
            return self.date == other.date
        return NotImplemented

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body)

    def __repr__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n-{self.body}-"


e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)
