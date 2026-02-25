import pymysql

print("\nPython Fundamentals 2025: Домашнее задание 41")
print("Список всех стран")
print("*" * 50)

config = {"host": "ich-db.edu.itcareerhub.de", "user": "ich1","password": "password", "database": "world"}
with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("select name from country")
        for i, (name,) in enumerate(cursor):
            print(f"{i + 1}. {name}")

        query = """
        select ci.name, ci.population
        from city as ci inner join country as c on c.code = ci.countrycode and lower(c.name) = lower(%s)
        order by ci.population desc
        """
        country_name = "Germany"
        print(f"\nВведите страну: {country_name}")
        cursor.execute(query, (country_name, ))
        for i, (name, population) in enumerate(cursor):
            print(f"{i + 1}. {name} - {population}")
