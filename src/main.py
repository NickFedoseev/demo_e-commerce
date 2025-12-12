class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        # Увеличиваем счётчики при создании категории
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        result = []
        for product in self.__products:
            result.append(
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт."
            )
        return "\n".join(result)

    @property
    def products_list(self) -> list[Product]:
        """Возвращает список продуктов (для тестов)."""
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
