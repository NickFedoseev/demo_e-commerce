from src.category import Category
from src.product import LawnGrass, Product, Smartphone


def test_category_init() -> None:
    """Проверка корректной инициализации объекта Category."""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание категории", [product])
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert len(category.products_list) == 1


def test_category_products_property() -> None:
    """Проверка геттера products (формат строки)."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    category = Category("Смартфоны", "Описание", [product])
    output = category.products
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert output == expected


def test_add_product() -> None:
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


def test_category_counters() -> None:
    """Проверка глобальных счётчиков категорий и товаров."""
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)
    Category("C1", "DC1", [p1, p2])

    assert Category.category_count == 1
    assert Category.product_count == 2


# ============ ТЕСТЫ ДЛЯ НОВОЙ ФУНКЦИОНАЛЬНОСТИ ============


def test_add_product_valid_smartphone() -> None:
    """Проверка добавления валидного продукта (Smartphone) в категорию."""
    Category.category_count = 0
    Category.product_count = 0

    phone = Smartphone("Samsung", "Desc", 1000.0, 5, 95.5, "S23", 256, "Black")
    category = Category("Phones", "All phones", [])

    # Добавляем продукт
    category.add_product(phone)

    # Проверяем, что продукт добавлен
    assert len(category.products_list) == 1
    assert category.products_list[0].name == "Samsung"
    assert Category.product_count == 1


def test_add_product_valid_lawn_grass() -> None:
    """Проверка добавления валидного продукта (LawnGrass) в категорию."""
    Category.category_count = 0
    Category.product_count = 0

    grass = LawnGrass("Трава", "Desc", 50.0, 10, "Россия", "7 дней", "Зеленый")
    category = Category("Grass", "All grass", [])

    # Добавляем продукт
    category.add_product(grass)

    # Проверяем, что продукт добавлен
    assert len(category.products_list) == 1
    assert category.products_list[0].name == "Трава"
    assert Category.product_count == 1


def test_add_product_invalid_string_raises_error() -> None:
    """Проверка, что добавление строки вызывает TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Phones", "All phones", [])

    try:
        category.add_product("Not a product")
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError as e:
        assert str(e) == (
            "Можно добавлять только объекты класса " "Product или его наследников"
        )


def test_add_invalid_int_raises_error() -> None:
    """Проверка, что добавление числа вызывает TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Phones", "All phones", [])

    try:
        category.add_product(123)
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError as e:
        assert str(e) == (
            "Можно добавлять только объекты класса " "Product или его наследников"
        )


def test_add_product_invalid_dict_raises_error() -> None:
    """Проверка, что добавление словаря вызывает TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Phones", "All phones", [])

    try:
        category.add_product({"name": "Test"})
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError as e:
        assert str(e) == (
            "Можно добавлять только объекты класса " "Product или его наследников"
        )


def test_add_product_none_raises_error() -> None:
    """Проверка, что добавление None вызывает TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Phones", "All phones", [])

    try:
        category.add_product(None)
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError as e:
        assert str(e) == (
            "Можно добавлять только объекты класса " "Product или его наследников"
        )
