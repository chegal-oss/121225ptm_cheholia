print("\nPython Fundamentals 2025: Домашнее задание 16")
print("\n1. Оценки текстом")
grades = [5, 3, 4, 2, 1, 5, 3]
rating = ("отлично", "хорошо", "неудовлетворительно")
print([[x, rating[0 if x == 5 else 2 if x < 3 else 1]] for x in grades])

print("\n2. Правильные скобки")
for text in "({[}])", "({[}])", "([({}()){}])":
    temp = []
    valid = True
    pattern = "({[)}]"
    for c in text:
        index = pattern.find(c)
        if index != -1:
            if index < 3:
                temp.append(c)
            else:
                valid = len(temp) > 0 and temp.pop() == pattern[index - 3]
                if not valid:
                    break
    valid = valid and not temp
    print(text)
    print("Валидны", valid)





