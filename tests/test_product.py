from src.product import LawnGrass, Product, Smartphone


def test_product_init() -> None:
    """Проверка корректной инициализации объекта Product."""
    product = Product("Товар", "Описание", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 10


def test_price_setter_positive() -> None:
    """Проверка установки положительной цены."""
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_negative() -> None:
    """Проверка попытки установить отрицательную цену (должна игнорироваться)."""
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = -50.0
    assert product.price == 100.0


def test_price_setter_zero() -> None:
    """Проверка попытки установить нулевую цену (должна игнорироваться)."""
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 0.0
    assert product.price == 100.0


def test_new_product_classmethod() -> None:
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


# ============ ТЕСТЫ ДЛЯ НАСЛЕДНИКОВ ============


def test_smartphone_init() -> None:
    """Проверка корректной инициализации объекта Smartphone."""
    smartphone = Smartphone(
        name="Samsung Galaxy S23",
        description="256GB, Серый",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )
    # Проверяем базовые атрибуты из Product
    assert smartphone.name == "Samsung Galaxy S23"
    assert smartphone.description == "256GB, Серый"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5

    # Проверяем дополнительные атрибуты Smartphone
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_init() -> None:
    """Проверка корректной инициализации объекта LawnGrass."""
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
    # Проверяем базовые атрибуты из Product
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20

    # Проверяем дополнительные атрибуты LawnGrass
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


# ============ ТЕСТЫ ДЛЯ СЛОЖЕНИЯ ============


def test_addition_same_class_product() -> None:
    """Проверка сложения двух объектов базового класса Product."""
    p1 = Product("P1", "D1", 100.0, 2)
    p2 = Product("P2", "D2", 200.0, 3)

    result = p1 + p2
    # 100 * 2 + 200 * 3 = 200 + 600 = 800
    assert result == 800.0


def test_addition_same_class_smartphone() -> None:
    """Проверка сложения двух объектов Smartphone."""
    phone1 = Smartphone("P1", "D1", 100.0, 2, 90.0, "M1", 128, "Red")
    phone2 = Smartphone("P2", "D2", 200.0, 3, 95.0, "M2", 256, "Blue")

    result = phone1 + phone2
    # 100 * 2 + 200 * 3 = 200 + 600 = 800
    assert result == 800.0


def test_addition_same_class_lawn_grass() -> None:
    """Проверка сложения двух объектов LawnGrass."""
    grass1 = LawnGrass("G1", "D1", 10.0, 5, "USA", "5 дней", "Green")
    grass2 = LawnGrass("G2", "D2", 15.0, 10, "Russia", "7 дней", "Dark Green")

    result = grass1 + grass2
    # 10 * 5 + 15 * 10 = 50 + 150 = 200
    assert result == 200.0


def test_addition_different_classes_raises_error() -> None:
    """Проверка, что сложение разных классов вызывает TypeError."""
    phone = Smartphone("P", "D", 100.0, 1, 90.0, "M", 128, "Red")
    grass = LawnGrass("G", "D", 10.0, 5, "USA", "5 дней", "Green")

    try:
        _ = phone + grass
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError as e:
        assert str(e) == "Нельзя складывать товары разных классов"


def test_addition_product_and_smartphone_raises_error() -> None:
    """Проверка, что сложение Product и Smartphone вызывает TypeError."""
    product = Product("P", "D", 100.0, 1)
    phone = Smartphone("S", "D", 200.0, 2, 90.0, "M", 128, "Blue")

    try:
        _ = product + phone
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError as e:
        assert str(e) == "Нельзя складывать товары разных классов"


def test_addition_smartphone_and_lawn_grass_raises_error() -> None:
    """Проверка, что сложение Smartphone и LawnGrass вызывает TypeError."""
    phone = Smartphone("P", "D", 100.0, 1, 90.0, "M", 128, "Red")
    grass = LawnGrass("G", "D", 10.0, 5, "USA", "5 дней", "Green")

    try:
        _ = phone + grass
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError as e:
        assert str(e) == "Нельзя складывать товары разных классов"
