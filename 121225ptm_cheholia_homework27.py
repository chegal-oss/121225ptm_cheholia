import os
import sys
from typing import OrderedDict

print("\nPython Fundamentals 2025: Домашнее задание 27")
print("\n1. Фильтрация по ключевому слову")
text = """2024-03-01 12:00:01 - Info: System started successfully.
2024-03-01 12:05:32 - Error: Failed to connect to the database.
2024-03-01 12:10:15 - Warning: Low memory detected.
2024-03-01 12:15:47 - Error: Access denied to the file.
2024-03-01 12:20:02 - Info: User logged in.
2024-03-01 12:25:19 - Error: Network connection lost.
2024-03-01 12:30:41 - Info: System shutdown completed."""
in_filename = "system.log"
with open(in_filename, "w") as in_file:
    in_file.write(text)

word = "Error"
out_filename = word.lower() + "_" + in_filename
print("Введите имя файла для поиска:", in_filename)
print("Введите ключевое слово:", word)

with open(in_filename) as in_file, open(out_filename, "w") as out_file:
    out_file.write("\n".join(s for s in in_file.read().lower().split("\n") if s.count(word.lower())))
print(f"Строки, содержащие '{word}', сохранены в {out_filename}.")

with open(out_filename) as out_file:
    text = out_file.read()
    print(text)
    assert text.lower().count(word.lower()) > 0

os.remove(in_filename)
os.remove(out_filename)


print("\n2. Поиск и удаление дубликатов")
in_filename = "movies_to_watch.txt"
text = """Inception (2010)
The Dark Knight (2008)
Interstellar (2014)
The Matrix (1999)
Pulp Fiction (1994)
Inception (2010)
The Matrix (1999)
Forrest Gump (1994)
The Shawshank Redemption (1994)
The Godfather (1972)
The Dark Knight (2008)
Fight Club (1999)
Forrest Gump (1994)
Gladiator (2000)"""
with open(in_filename, "w") as in_file:
    in_file.write(text)

out_filename = "unique" + "_" + in_filename
print("Введите имя файла для поиска:", in_filename)

with open(in_filename) as in_file, open(out_filename, "w") as out_file:
    out_file.write("\n".join(OrderedDict([(x, "") for x in in_file.read().split("\n")]).keys()))

print(f"Дубликаты удалены. Уникальные строки сохранены в {out_filename}.")

with open(out_filename) as out_file:
    text = out_file.read()
    print(text)
    assert len(set(text.split("\n"))) == len(text.split("\n"))

os.remove(out_filename)
os.remove(in_filename)

