import os
import sys
from typing import OrderedDict

print("\nPython Fundamentals 2025: Домашнее задание 27")
print("\n1. Фильтрация по ключевому слову")
in_filename = "/var/log/system.log"
word = "Error"
out_filename = word.lower() + "_" + in_filename.split("/")[-1]
print("Введите имя файла для поиска:", in_filename)
print("Введите ключевое слово:", word)
with open(in_filename) as in_file, open(out_filename, "w") as out_file:
    out_file.write("\n".join(s for s in in_file.read().split("\n") if s.count(word)))
print(f"Строки, содержащие '{word}', сохранены в {out_filename}.")

print("\n2. Поиск и удаление дубликатов")
in_filename = "/Users/chegal/Downloads/test.txt"
print("Введите имя файла для поиска:", in_filename)
file_text = "test\ntest\ntest\ntest1\ntest2\ntest4\n"
out_filename = "unique" + "_" + in_filename.split("/")[-1]
with open(out_filename, "w") as out_file:
    out_file.write("\n".join(OrderedDict([(x, "") for x in file_text.split("\n")]).keys()))
print(f"Дубликаты удалены. Уникальные строки сохранены в {out_filename}.")


