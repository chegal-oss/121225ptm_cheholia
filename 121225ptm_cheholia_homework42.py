import queue
from typing import Any

import pymysql

print("\nPython Fundamentals 2025: Домашнее задание 43")
print("Создание базы, Добавление заметок")
print("*" * 50)

config = {"host": "ich-edit.edu.itcareerhub.de", "user": "ich1", "password": "ich1_password_ilovedbs",}
database_name = "notes_app_121225_ptm_serg"
with pymysql.connect(**config, cursorclass=pymysql.cursors.DictCursor) as connection:
    with connection.cursor() as cursor:
        #cursor.execute(f"drop database if exists {database_name}")
        cursor.execute(f"create database if not exists {database_name}")
        print(f"Database \"{database_name}\" created or already exists.")

        cursor.execute(f"use {database_name}")

        cursor.execute("""create table if not exists notes 
                (id int primary key auto_increment, title varchar(100), content text)""")

        print("Table \"notes\" created.")

        cursor.execute("select count(*) + 1  as count_row from notes")
        row_cont = next(cursor)["count_row"]

        cursor.execute("insert into notes (title, content) values ('Shopping list %s', 'Content text')", row_cont)

        connection.commit()

        cursor.execute("select title, content from notes")

        for row in cursor:
            row: dict[str, Any]
            print(f"Note added : {row['title']} : {row['content']}")




