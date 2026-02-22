import json
from collections import Counter
from datetime import date, datetime

print("\nPython Fundamentals 2025: Домашнее задание 30")
print("\n1. Анализ курсов студентов")

print("Первый вариант O(3N)")
start = datetime.now()
with open("student_courses.json") as file:
    structure = json.load(file, object_hook=lambda x: {
        **x,
        "birth_date": date.strptime(x["birth_date"], "%d.%m.%Y"),
        "enrollment_date": date.strptime(x["enrollment_date"], "%d.%m.%Y")})
    res = json.dumps({
        "total_students": len(structure),
        "average_enrollment_age": sum([x["enrollment_date"].year - x["birth_date"].year for x in structure]) / len(
            structure),
        "students_per_course": dict(Counter([k for x in structure for k in x["courses"]]))
    }, indent=4)
    #print(res)
print("Время выполнения = ", datetime.now() - start)

print("\nВторой вариант O(1N) с датой")
start = datetime.now()
with open("student_courses.json") as file:
    res, counter = {}, Counter()
    for i, student in enumerate(json.load(file)):
        d1 = date.strptime(student["enrollment_date"], "%d.%m.%Y")
        d2 = date.strptime(student["birth_date"], "%d.%m.%Y")
        counter.update(student["courses"])
        res["average_enrollment_age"] = res.setdefault("average_enrollment_age", 0) + d1.year - d2.year
    else:
        res["total_students"] = i + 1
        res["students_per_course"] = dict(counter)
        res["average_enrollment_age"] /= i + 1
    #print(json.dumps(res, indent=4))
print("Время выполнения = ", datetime.now() - start)

print("\nТретий вариант O(1N) с числами")
start = datetime.now()
with open("student_courses.json") as file:
    res, counter = {}, Counter()
    for i, student in enumerate(json.load(file)):
        d1, d2 = int(student["enrollment_date"].split(".")[2]), int(student["birth_date"].split(".")[2])
        counter.update(student["courses"])
        res["average_enrollment_age"] = res.setdefault("average_enrollment_age", 0) + d1 - d2
    else:
        res["total_students"] = i + 1
        res["students_per_course"] = dict(counter)
        res["average_enrollment_age"] /= i + 1
    #print(json.dumps(res, indent=4))
print("Время выполнения = ", datetime.now() - start)

