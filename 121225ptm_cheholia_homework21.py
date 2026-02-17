from collections import Counter

print("\nPython Fundamentals 2025: Домашнее задание 21")
print("\n1. Повторения букв")
def change_text(text: str) -> dict:
    return dict(Counter(text.lower().replace(" ","")))
print(change_text("Programming is fun!"))

print("\n2. Группировка студентов по классам")
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
res = {}
for c, n in students:
    res.setdefault(c, []).append(n)
print(res)