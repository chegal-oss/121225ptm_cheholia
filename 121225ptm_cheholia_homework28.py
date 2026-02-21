import itertools
import os
import sys
import time
from typing import OrderedDict, Iterable

print("\nPython Fundamentals 2025: Домашнее задание 28")
print("\n1. План по дням недели")

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

for i, key in enumerate(itertools.cycle(weekly_schedule.keys())):
    print(key, ", ".join(weekly_schedule[key]))
    if i > 7: break

print("\n2. Объединение списков продуктов")
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def gen_iter(*args:list[str]) -> Iterable[str]:
    return (x.lower() for x in itertools.chain(*args))


for item in gen_iter(fruits, vegetables, dairy):
    print(item)

print("\n3. Комбинации одежды")

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]


def all_comb(*arg:list[str]) -> Iterable[str]:
    return (f"{cl:-<7}--{c:-<7}{s:->5}" for cl, c, s in itertools.product(*arg))


for item in all_comb(clothes, colors, sizes):
    print(item)
