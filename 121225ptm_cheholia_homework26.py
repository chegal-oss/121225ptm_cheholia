import os
import sys

print("\nPython Fundamentals 2025: Домашнее задание 26")
print("\n1. Список файлов и папок")

path = "/opt/"
if len(sys.argv) == 2:
    path = sys.argv[1]

for root, dirs, files in os.walk(path):
    print("Содержимое директории:", root)
    print("Папки:")
    for directory in dirs:
        print(directory)
    print("Файлы:")
    for file in files:
        print(file)

print("\n1. Поиск и удаление файлов с указанным расширением")

path, ext = "/Users/chegal/Downloads", "*.txt" #txt, .txt
if len(sys.argv) == 3:
    path = sys.argv[1]
    ext = sys.argv[2]
ext = "." + ext.strip(".*")
files = [root + "/" + file for root, _, files in os.walk(path) for file in files if file.endswith(ext)]
if files:
    print(f"Найдены файлы с расширением {ext} : {len(files)}")
    for file in files:
        print("-", file)
    print("Вы хотите удалить эти файлы? (y/n):")
    answer = "y"
    if answer.lower() == "y":
        for file in files:
            #os.remove(file)
            print(f" -{file} удален.")
else:
    print(f"Фйалов с расширением \"{ext}\" не найдено")


