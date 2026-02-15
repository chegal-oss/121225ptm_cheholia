print("\nPython Fundamentals 2025: Домашнее задание 15")
print("\n1. Одно слово")
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
print(text_list)
for i in range(len(text_list)-1,-1,-1):
    if len(text_list[i].split()) > 1:
        del text_list[i]
    else:
        text_list[i] = text_list[i].lower()
print(text_list)
#или
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
text_list[:] = [x.lower() for x in text_list if len(x.split()) == 1]
print(text_list)


print("\n1. Обновление цен товаров")
products = [["Laptop", 1200.0], ["Mouse", 25.0], ["Keyboard", 75.0], ["Monitor", 200.0]]
discount = 17
pattern = "{:15} | {:15} | {:15}"
head = pattern.format("Товар", "Старая цена", "Новая цена")
print(head)
print("-" * len(head))
for item in products:
    item.append(item[1] - item[1] * discount / 100)
    print(pattern.format(*item))




