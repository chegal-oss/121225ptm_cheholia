print("\nPython Fundamentals 2025: Домашнее задание 11")
print("1.Звёздочки вместо чисел")
text = "My number is 123-456-789"
print("Строка:", text)
# print("Результат: ", "".join([c if not c.isdigit() else "*" for c in text]))
# print("Результат: ", "".join(map(lambda c : "*" if c.isdigit() else c, text)))
new_string = list(text)
for i in range(len(new_string)):
    char = new_string[i]
    new_string[i] = "*" if char.isdigit() else char
print("Результат: ", "".join(new_string))

print("\n2.Количество символов")
text = "Programming in python"
print("Строка:", text)
text = text.lower()
while text:
    c = text[0]
    print(f"Символ '{c}' встречается {text.count(c)}") if text.count(c) > 1 else None
    text = text.replace(c, "")

print("\n3.Увеличение чисел")
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
print(text)
result = []
for word in text.split():
    old = new = word.strip(".")
    if new.isdigit():
        new = str(int(new) * 10)
    else:
        test_float = new.split(".")
        if len(test_float) == 2 and test_float[0].isdigit() and test_float[1].isdigit():
            new = str(float(new) * 10)
    result.append(word.replace(old, new))
print(" ".join(result))

# если номер карты не считать числом которое нужно увеличить
print(" ".join([str(int(x) * 10) if x.isdigit() else str(float(x) * 10) if len(
    (test_float := x.split("."))) == 2 and test_float[0].isdigit() and test_float[1].isdigit() else x for x in
                text.split()]))

# универсальное решение без split() + шаблон строк (необязательно, но интересно)
text = "I have.!5apples and ll10oranges, price is0.5! each. Card number is ....3672.ура!"

variables, template, buf = [], [], ""
for c in text + " ":
    if c.isdigit() or (c == "." and buf):
        buf += c
    elif buf:
        s = buf.strip(".")
        variables.append(int(s) if s.isdigit() else float(s))
        template.append("{}")
        if buf.endswith("."):
            template.append(".")
        template.append(c)
        buf = ""
    else:
        template.append(c)

print("".join(template).format(*[x * 10 for x in variables]))
