class Product:
    """
    Класс для представления товара.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара (приватный атрибут)
        quantity (int): Количество товара на складе
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
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

    @classmethod
    def new_product(cls, product_info: dict) -> "Product":
        """Создаёт новый продукт из словаря."""
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"],
        )

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает общую стоимость двух товаров."""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.price * self.quantity + other.price * other.quantity
