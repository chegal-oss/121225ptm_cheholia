from functools import lru_cache
from typing import Generator

import pymysql

print("\nPython Fundamentals 2025: Домашнее задание 41")
print("Список всех стран")
print("*" * 50)
print()


class MyDatabase:
    _instance = None
    _installable = False

    def __new__(cls, *args, **kwargs):
        if not cls._installable:
            raise RuntimeError("Use MyDatabase.get_instance()")
        return super().__new__(cls)

    def __init__(self):
        self._connection = None
        self._config = {"host": "ich-db.edu.itcareerhub.de", "user": "ich1",
                        "password": "password"}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._installable = True
            cls._instance = cls()
            cls._installable = False
        return cls._instance

    def connect(self, database="world"):
        self.disconnect()
        self._config["database"] = database
        self._connection = pymysql.connect(**self._config)

    def disconnect(self):
        if self._connection is not None:
            try:
                self._connection.close()
            except pymysql.Error:
                pass
            finally:
                self._connection = None

    def __del__(self):
        self.disconnect()

    def exec_sql(self, query: str, *params) -> list[tuple]:
        try:
            self._connection.ping(reconnect=True)
        except pymysql.Error:
            self._connection = pymysql.connect(**self._config)
        with self._connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()


myDatabase = MyDatabase.get_instance()
myDatabase.connect()

for i, (name,) in enumerate(myDatabase.exec_sql("select name from country")):
    print(f"{i + 1}. {name}")

print()
print("*" * 50)

countries = list()
for i, (name,) in enumerate(myDatabase.exec_sql("select name from country limit 56, 10")):
    print(f"{i + 1}. {name}")
    countries.append(name)
print()
query = """
        select ci.name, ci.population
        from city as ci inner join country as c on c.code = ci.countrycode and lower(c.name) = lower(%s)
        order by ci.population desc
        limit 5 
        """

for country_name in countries:
    print(f"\nВведите страну: {country_name}")
    for i, (name, population) in enumerate(myDatabase.exec_sql(query, country_name)):
        print(f"{i + 1}. {name} - {population}")
