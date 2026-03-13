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

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию и увеличивает общий счётчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех товаров категории."""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Возвращает список товаров (для тестов и внутреннего использования)."""
        return self.__products

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
