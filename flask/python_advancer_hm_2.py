import json
import unittest

from pydantic import BaseModel, Field, EmailStr, model_validator, ValidationError


class JsonBaseModel(BaseModel):

    #Очень странный метод из п.2 задания
    @classmethod
    def is_json_correct(cls, json_str):
        try:
            obj = cls.model_validate_json(json_str)
            return obj.model_dump_json()
        except ValidationError:
            raise ValueError("Json is incorrect")

class Address(JsonBaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)


class User(JsonBaseModel):
    name: str = Field(min_length=2, pattern=r"^[^\W\d_]+(?: [^\W\d_]+)*$")
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    is_employed: bool = False
    address: Address

    @model_validator(mode="after")
    def check_age(self) -> User:
        if self.is_employed and not 18 <= self.age <= 65:
            raise ValueError("Age not correct")
        return self


# --- tests ----
class TestUser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json_data = json.loads("""{
            "name": "John Doe",
            "age": 55,
            "email": "john.doe@example.com",
            "is_employed": true,
            "address": {
                "city": "New York",
                "street": "5th Avenue",
                "house_number": 123
            }
        }""")

    def test_user_correct(self):
        assert User(**self.json_data).age == 55

    def test_json_incorrect(self):
        with self.assertRaisesRegex(ValueError, "Json is incorrect"):
            User.is_json_correct("{}")

    def test_user_name_incorrect(self):
        self.json_data["name"] = "A212121"
        with self.assertRaisesRegex(ValueError, "String should match pattern"):
            User(**self.json_data)

    def test_user_age_and_is_employed_incorrect(self):
        self.json_data["age"] = 75
        with self.assertRaisesRegex(ValueError, "Age not correct"):
            User(**self.json_data)

    def test_user_validation_incorrect(self):
        self.json_data["age"] = 123
        self.json_data["address"]["city"] = "N"
        self.json_data["address"]["street"] = "5"
        self.json_data["address"]["house_number"] = -1
        with self.assertRaisesRegex(ValueError, "4 validation errors"):
            User(**self.json_data)
