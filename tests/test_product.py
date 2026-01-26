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
