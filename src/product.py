from typing import Dict


class Product:
    """
    Класс для представления товара.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара (приватный атрибут)
        quantity (int): Количество товара на складе
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализирует товар с заданными параметрами."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой на положительность."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    def __add__(self, other: "Product") -> float:
        """
        Складывает товары одного класса по формуле:
        общая стоимость = цена * количество

        Использует type() для проверки, что объекты одного класса.
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_info: Dict[str, any]) -> "Product":
        """Создаёт новый продукт из словаря."""
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"],
        )


class Smartphone(Product):
    """
    Класс для представления смартфона — наследник Product.

    Дополнительные атрибуты:
        efficiency (float): Производительность
        model (str): Модель смартфона
        memory (int): Объем встроенной памяти (ГБ)
        color (str): Цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует смартфон с дополнительными параметрами."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для представления газонной травы — наследник Product.

    Дополнительные атрибуты:
        country (str): Страна-производитель
        germination_period (str): Срок прорастания
        color (str): Цвет травы
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует газонную траву с дополнительными параметрами."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
