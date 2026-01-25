class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
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


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list["Product"]):
        self.name = name
        self.description = description
        self.__products = products  # Приватный список товаров

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию и увеличивает счётчик."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех товаров категории."""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    @property
    def products_list(self) -> list["Product"]:
        """Для внутреннего использования (например, в тестах)."""
        return self.__products


def load_data(file_path: str) -> list[Category]:
    """Загружает категории и товары из JSON-файла."""
    import json

    categories = []
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    for cat_info in data:
        products = []
        for prod_info in cat_info["products"]:
            product = Product(
                name=prod_info["name"],
                description=prod_info["description"],
                price=prod_info["price"],
                quantity=prod_info["quantity"],
            )
            products.append(product)

        category = Category(
            name=cat_info["name"],
            description=cat_info["description"],
            products=products,
        )
        categories.append(category)

    return categories
