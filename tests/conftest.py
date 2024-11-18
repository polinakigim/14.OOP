import pytest

from scr.category import Category
from scr.product import Product


@pytest.fixture
def first_category():
    return Category(name="Phone",
                    description="smt des phone",
                    products=[Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 14),
                              Product("Iphone 15", "512GB, Gray space", 210000.0, 8)])


@pytest.fixture
def second_category():
    return Category(name="television",
                    description="smt des tele",
                    products=[Product("55\" QLED 4K",
                                      "Фоновая подсветка",
                                      123000.0,
                                      7)])


@pytest.fixture
def product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
