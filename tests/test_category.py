from src.category import Category
from src.product import Product


def test_category_init():
    """Проверка корректной инициализации объекта Category."""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание категории", [product])
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert len(category.products_list) == 1


def test_category_products_property():
    """Проверка геттера products (формат строки)."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    category = Category("Смартфоны", "Описание", [product])
    output = category.products
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert output == expected


def test_add_product():
    """Проверка добавления товара в категорию и обновления счётчика."""
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 100.0, 1)
    category = Category("C1", "DC1", [p1])
    assert Category.product_count == 1

    p2 = Product("P2", "D2", 200.0, 2)
    category.add_product(p2)

    assert len(category.products_list) == 2
    assert Category.product_count == 2


def test_category_counters():
    """Проверка глобальных счётчиков категорий и товаров."""
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)
    Category("C1", "DC1", [p1, p2])

    assert Category.category_count == 1
    assert Category.product_count == 2
