from src.product import Product


def test_product_init():
    """Проверка корректной инициализации объекта Product."""
    product = Product("Товар", "Описание", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 10


def test_price_setter_positive():
    """Проверка установки положительной цены."""
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_negative():
    """Проверка попытки установить отрицательную цену (должна игнорироваться)."""
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = -50.0
    assert product.price == 100.0


def test_price_setter_zero():
    """Проверка попытки установить нулевую цену (должна игнорироваться)."""
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 0.0
    assert product.price == 100.0


def test_new_product_classmethod():
    """Проверка создания продукта через класс-метод new_product."""
    data = {
        "name": "Новый Товар",
        "description": "Описание",
        "price": 99.9,
        "quantity": 3,
    }
    product = Product.new_product(data)
    assert product.name == "Новый Товар"
    assert product.description == "Описание"
    assert product.price == 99.9
    assert product.quantity == 3


# === НОВЫЕ ТЕСТЫ ДЛЯ 15.1 ===


def test_product_str():
    """Проверка строкового представления продукта."""
    product = Product("Samsung", "Телефон", 180000.0, 5)
    assert str(product) == "Samsung, 180000.0 руб. Остаток: 5 шт."


def test_product_add():
    """Проверка сложения двух продуктов (общая стоимость)."""
    p1 = Product("A", "Описание", 100.0, 5)  # 500
    p2 = Product("B", "Описание", 200.0, 3)  # 600
    assert p1 + p2 == 1100.0


def test_product_add_type_error():
    """Проверка защиты от сложения с не-Product."""
    p1 = Product("Товар", "Описание", 100.0, 1)
    try:
        p1 + "не товар"
        assert False, "Должно было возникнуть исключение"
    except TypeError as e:
        assert str(e) == "Можно складывать только объекты Product"
