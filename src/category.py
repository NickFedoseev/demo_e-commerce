from typing import List

from src.product import Product


class Category:
    """
    Класс для представления категории товаров.

    Атрибуты класса:
        category_count (int): Общее количество категорий
        product_count (int): Общее количество товаров во всех категориях

    Атрибуты экземпляра:
        name (str): Название категории
        description (str): Описание категории
        __products (List[Product]): Список товаров (приватный)
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """Инициализирует категорию с заданными параметрами."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию и увеличивает общий счётчик товаров.

        Использует isinstance() для проверки, что объект является
        экземпляром Product или его наследником.
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех товаров в категории."""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    @property
    def products_list(self) -> List[Product]:
        """Возвращает список товаров (для тестов и внутреннего использования)."""
        return self.__products
