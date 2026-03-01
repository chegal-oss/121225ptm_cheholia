from pymongo import MongoClient

print("\nPython Fundamentals 2025: Домашнее задание 43")
print("Добавление товаров, Увеличение цен")
print("*" * 50)

uri = ("mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de"
       "/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit")

client = MongoClient(uri)
try:
    client.admin.command("ping")
    db = client["ich_edit"]
    products = db["products_121225_ptm_serg"]
    products.delete_many({})
    items = [
        {"name": "Pen", "price": 1.50, "stock": 300},
        {"name": "Pencil", "price": 0.99, "stock": 500},
        {"name": "Eraser", "price": 0.75, "stock": 200},
    ]
    result = products.insert_many(items)
    print(len(result.inserted_ids), "products inserted.")

    result = products.update_many({}, {"$mul": {"price": 1.2}})
    print(result.modified_count, "products updated.")

    for item in products.find({}, {"_id": 0, "name": 1, "price": 1}):
        print("{name} {price:.2f}".format(**item))
except Exception as e:
    print(f"Connection error {e}")
finally:
    client.close()
