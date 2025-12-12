import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import Category, Product, load_data


def test_product_init() -> None:
    product = Product("Товар", "Описание", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_init() -> None:
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание категории", [product])
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert len(category.products_list) == 1


def test_category_products_property() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    category = Category("Смартфоны", "Описание", [product])
    output = category.products
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert expected in output


def test_category_counters() -> None:
    # Обнуляем счётчики
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)
    p3 = Product("P3", "D3", 30.0, 3)

    Category("C1", "DC1", [p1, p2])
    Category("C2", "DC2", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_load_data() -> None:
    # Подготовим временный JSON-файл
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
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
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
        assert "Смартфоны, как средство" in cat.description
        assert len(cat.products_list) == 2

        prod0 = cat.products_list[0]
        assert prod0.name == "Samsung Galaxy S23 Ultra"
        assert prod0.price == 180000.0
        assert prod0.quantity == 5

        prod1 = cat.products_list[1]
        assert prod1.name == "Iphone 15"
        assert prod1.quantity == 8
    finally:
        os.unlink(temp_path)
