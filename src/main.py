from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def calculate_total_price(self):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")


class InitPrintMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}, {kwargs}")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Product(InitPrintMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def new_product(cls, product_info):
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"]
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать объекты разных типов")
        return self.price * self.quantity + other.price * other.quantity


class Category:
    # Атрибуты класса, общие для всех объектов
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        # Атрибуты экземпляра класса Category
        self.name = name
        self.description = description
        self.__products = products  # Приватный список продуктов

        # Увеличиваем количество категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем счетчик продуктов на количество переданных продуктов
        Category.product_count += len(products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт "
            "с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
