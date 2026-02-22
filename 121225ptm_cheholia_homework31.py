import re

print("\nPython Fundamentals 2025: Домашнее задание 31")
print("\n1. Извлечение дат")

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
print(*re.findall(r"\d{2}[./-]\d{2}[./-]\d{4}", text), sep="\n")

print("\n2. Разделение списка тегов")
tag_input = "python, data-science / machine-learning; AI neural-networks"
print(re.findall(r"[\w-]+", tag_input))


