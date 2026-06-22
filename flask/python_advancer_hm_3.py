from decimal import Decimal

from sqlalchemy.orm import DeclarativeBase, Mapped, Session, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine, Integer, String, Numeric, Boolean, ForeignKey, Engine, inspect, select
import pytest


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






@pytest.fixture
def engine():
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session


def test_tables_created(engine):
    tables = inspect(engine).get_table_names()
    assert "category" in tables
    assert "products" in tables

def test_insert(session):
    category = Category(name="Notebook", description="IT")
    session.add(category)
    session.commit()
    assert session.scalar(select(Category).where(Category.name == "Notebook"))

    product = Product(name="MackBook", category_id=category.id,
                      price=Decimal("3000.00"),
                      in_stock=True)
    session.add(product)
    session.commit()

    assert session.scalar(select(Product).where(Product.category.has(Category.name == "Notebook")))

