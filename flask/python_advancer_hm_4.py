from decimal import Decimal

import pytest
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import create_engine, Integer, String, Numeric, ForeignKey, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, relationship
from sqlalchemy.orm import mapped_column


# Models
class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    in_stock: Mapped[bool]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="products")


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(255))
    products: Mapped[list["Product"]] = relationship(back_populates="category")

class ProductCreate(BaseModel):
    name: str
    price: Decimal
    in_stock: bool

class CategoryCreate(BaseModel):
    name: str
    description: str

    products: list[ProductCreate] = Field(default_factory=list)


class ProductRead(BaseModel):
    id: int
    name: str
    price: Decimal
    in_stock: bool

    model_config = ConfigDict(from_attributes=True)


class CategoryRead(BaseModel):
    id: int
    name: str
    description: str
    products: list[ProductRead] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


# ******************************************************************************


data_list = [
    {
        "name": "Электроника",
        "description": "Гаджеты и устройства",
        "products": [
            {
                "name": "Смартфон",
                "price": "299.99",
                "in_stock": True,
            },
            {
                "name": "Ноутбук",
                "price": "499.99",
                "in_stock": True,
            }
        ],
    },
    {
        "name": "Книги",
        "description": "Печатные книги и электронные книги",
        "products": [
            {
                "name": "Научно-фантастический роман",
                "price": "15.99",
                "in_stock": True,
            }
        ],
    },
    {
        "name": "Одежда",
        "description": "Одежда для мужчин и женщин",
        "products": [
            {
                "name": "Джинсы",
                "price": "40.50",
                "in_stock": True,
            },
            {
                "name": "Футболка",
                "price": "20.00",
                "in_stock": True,
            }
        ],
    }
]


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        for data in data_list:
            category_data = CategoryCreate.model_validate(data)
            category = Category(name=category_data.name,
                                description=category_data.description,
                                products=[Product(name=p.name,
                                                  price=p.price,
                                                  in_stock=p.in_stock)
                                          for p in category_data.products])
            session.add(category)
        session.commit()
        yield session


#Задача 1: Наполнение данными
def test_homework_4_1(session):
    assert session.scalar(select(func.count(Category.id))) == len(data_list)

#Задача 2: Чтение данных
def test_homework_4_2(session):
    result1 = [CategoryRead.model_validate(x) for x in session.scalars(select(Category).order_by(Category.id)).all()]
    result2 = [CategoryCreate.model_validate(x) for x in data_list]
    assert len(result1) == len(result2)

    for c1, c2 in zip(result1, result2):
        assert c1.name == c2.name
        for p1, p2 in zip(c1.products, c2.products):
            assert p1.name == p2.name
            assert p1.price == p2.price

#Задача 3: Обновление данных
def test_homework_4_3(session):
    product = session.scalar(select(Product).where(Product.name == "Смартфон"))
    product.price = Decimal("399.99")
    session.commit()
    assert session.scalar(select(Product).where(Product.id == product.id)).price == Decimal("399.99")

#Задача 4, 5: Агрегация и группировка и фильтрация
@pytest.mark.parametrize("min_count", [0, 1])
def test_homework_4_4(session, min_count):
    result1 = list(session.execute(select(Category.name,
                                     func.count(Product.id))
                        .join(Category.products)
                        .group_by(Category.id)
                        .having(func.count(Product.id) > min_count)
                        .order_by(Category.id)).all())
    result2 = [(item["name"], len(item["products"])) for item in data_list if len(item["products"]) > min_count]
    assert result1 == result2
