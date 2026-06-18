import json
import unittest

from pydantic import BaseModel, Field, EmailStr, model_validator


class JsonBaseModel(BaseModel):

    @classmethod
    def from_json(cls, json_str):
        return cls.model_validate_json(json_str)

    def to_json(self):
        return self.model_dump_json()

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
        assert User.from_json(json.dumps(self.json_data)).age == 55

    def test_export_json_correct(self):
        assert json.loads(User(**self.json_data).to_json()) == self.json_data

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
