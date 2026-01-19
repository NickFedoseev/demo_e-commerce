class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list["Product"]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """Возвращает строковое представление товаров в категории."""
        result = []
        for product in self.__products:
            # Важно: не меняем формат цены — оставляем как float (например, 180000.0)
            result.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(result)

    @property
    def products_list(self) -> list["Product"]:
        """
        Возвращает список объектов Product
        (для тестов и внутреннего использования).
        """
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
                price=prod_info["price"],  # float
                quantity=prod_info["quantity"],  # int
            )
            products.append(product)

        category = Category(
            name=cat_info["name"],
            description=cat_info["description"],
            products=products,
        )
        categories.append(category)

    return categories
