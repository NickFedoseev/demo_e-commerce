import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import Category, Product, load_data


def test_product_init():
    product = Product("Товар", "Описание", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_init():
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание категории", [product])
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert len(category.products_list) == 1


def test_category_products_property():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    category = Category("Смартфоны", "Описание", [product])
    output = category.products
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert output == expected


def test_add_product():
    # Сбрасываем счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("P1", "D1", 100.0, 1)
    category = Category("C1", "DC1", [product1])
    assert Category.product_count == 1

    product2 = Product("P2", "D2", 200.0, 2)
    category.add_product(product2)

    assert len(category.products_list) == 2
    assert Category.product_count == 2  # Теперь будет 2!


def test_price_setter_positive():
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_negative():
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = -50.0
    assert product.price == 100.0  # Цена не изменилась


def test_price_setter_zero():
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 0.0
    assert product.price == 100.0  # Цена не изменилась


def test_new_product_classmethod():
    data = {
        "name": "Новый Товар",
        "description": "Описание",
        "price": 99.9,
        "quantity": 3,
    }
    product = Product.new_product(data)
    assert product.name == "Новый Товар"
    assert product.price == 99.9
    assert product.quantity == 3


def test_category_counters():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)
    Category("C1", "DC1", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_load_data():
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации...",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".json", delete=False
    ) as f:
        json.dump(test_data, f, ensure_ascii=False, indent=4)
        temp_path = f.name

    try:
        categories = load_data(temp_path)
        assert len(categories) == 1
        cat = categories[0]
        assert cat.name == "Смартфоны"
        assert len(cat.products_list) == 1
        prod = cat.products_list[0]
        assert prod.name == "Samsung Galaxy S23 Ultra"
        assert prod.price == 180000.0
    finally:
        os.unlink(temp_path)
