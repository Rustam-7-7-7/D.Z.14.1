import unittest
from io import StringIO
import sys
from src.main import Product, Category, Smartphone, LawnGrass, InitPrintMixin


class TestProductCategory(unittest.TestCase):

    def setUp(self):
        # Сброс счетчиков перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

        # Создаем продукты и категорию для тестов
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        self.category = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [self.product1, self.product2, self.product3]
        )

    def test_product_initialization(self):
        product = Product("Test Product", "Description", 100.0, 10)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 10)

    def test_category_initialization(self):
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        product2 = Product("Product 2", "Description 2", 60.0, 6)
        category = Category("Test Category", "Category Description", [product1, product2])
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Category Description")
        self.assertEqual(len(category._Category__products), 2)

    def test_product_count(self):
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        product2 = Product("Product 2", "Description 2", 60.0, 6)
        category = Category("Test Category", "Category Description", [product1, product2])
        self.assertEqual(Category.product_count, 5)

    def test_category_count(self):
        Category("Category 1", "Description 1", [])
        Category("Category 2", "Description 2", [])
        self.assertEqual(Category.category_count, 3)

    def test_add_product(self):
        category = Category("Test", "Description", [])
        product = Product("Test Product", "Description", 100.0, 10)
        category.add_product(product)
        self.assertIn(product, category._Category__products)
        self.assertEqual(Category.product_count, 4)

    def test_product_price_setter(self):
        product = Product("Test Product", "Description", 100.0, 10)
        product.price = 50.0
        self.assertEqual(product.price, 50.0)
        product.price = -10.0
        self.assertEqual(product.price, 50.0)
        product.price = 0.0
        self.assertEqual(product.price, 50.0)

    def test_product_new_method(self):
        product_info = {
            "name": "Test Product",
            "description": "Description",
            "price": 100.0,
            "quantity": 10
        }
        product = Product.new_product(product_info)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 10)

    def test_category_product_list(self):
        product = Product("Test Product", "Description", 100.0, 10)
        category = Category("Test", "Description", [product])
        expected_output = "Test Product, 100.0 руб. Остаток: 10 шт."
        self.assertEqual(category.products, expected_output)

    def test_product_str(self):
        self.assertEqual(str(self.product1), "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.")
        self.assertEqual(str(self.product2), "Iphone 15, 210000.0 руб. Остаток: 8 шт.")
        self.assertEqual(str(self.product3), "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.")

    def test_product_addition(self):
        self.assertEqual(self.product1 + self.product2, 2580000.0)
        self.assertEqual(self.product1 + self.product3, 1334000.0)
        self.assertEqual(self.product2 + self.product3, 2114000.0)

    def test_category_str(self):
        self.assertEqual(str(self.category), "Смартфоны, количество продуктов: 27 шт.")

    def test_category_products(self):
        expected_products = (
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
            "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        )
        self.assertEqual(self.category.products, expected_products)

    def test_smartphone_initialization(self):
        smartphone = Smartphone("Test Smartphone", "Description", 1000.0, 10, 95.5, "Model X", 256, "Black")
        self.assertEqual(smartphone.efficiency, 95.5)
        self.assertEqual(smartphone.model, "Model X")
        self.assertEqual(smartphone.memory, 256)
        self.assertEqual(smartphone.color, "Black")

    def test_lawngrass_initialization(self):
        grass = LawnGrass("Test Grass", "Description", 50.0, 20, "Country", "7 days", "Green")
        self.assertEqual(grass.country, "Country")
        self.assertEqual(grass.germination_period, "7 days")
        self.assertEqual(grass.color, "Green")

    def test_invalid_addition(self):
        smartphone = Smartphone("Test Smartphone", "Description", 1000.0, 10, 95.5, "Model X", 256, "Black")
        grass = LawnGrass("Test Grass", "Description", 50.0, 20, "Country", "7 days", "Green")
        with self.assertRaises(TypeError):
            _ = smartphone + grass

    def test_invalid_product_addition(self):
        category = Category("Test Category", "Description", [])
        with self.assertRaises(TypeError):
            category.add_product("Not a product")


class TestNewFunctionalities(unittest.TestCase):

    def test_init_print_mixin(self):
        # Перенаправляем стандартный вывод в StringIO, чтобы поймать вывод
        captured_output = StringIO()
        sys.stdout = captured_output

        product = Product("Test Product", "Description", 100.0, 10)

        # Возвращаем стандартный вывод обратно
        sys.stdout = sys.__stdout__

        # Проверяем, что вывод содержит правильное сообщение
        expected_output = ("Создан объект класса Product с параметрами: ('Test Product', 'Description', 100.0, 10),"
                           " {}\n")
        self.assertIn(expected_output, captured_output.getvalue())

    def test_calculate_total_price(self):
        product = Product("Test Product", "Description", 100.0, 10)
        self.assertEqual(product.calculate_total_price(), 1000.0)

        smartphone = Smartphone("Test Smartphone", "Description", 1000.0, 5, 95.5, "Model X", 256, "Black")
        self.assertEqual(smartphone.calculate_total_price(), 5000.0)

        grass = LawnGrass("Test Grass", "Description", 50.0, 20, "Country", "7 days", "Green")
        self.assertEqual(grass.calculate_total_price(), 1000.0)

    # Тест для проверки исключения при нулевом количестве товара
    def test_product_with_zero_quantity(self):
        with self.assertRaises(ValueError):
            _ = Product("Test Product", "Description", 100.0, 0)

    # Тест для проверки расчета средней цены
    def test_category_middle_price(self):
        # Категория с продуктами
        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 10)
        category = Category("Test Category", "Description", [product1, product2])
        self.assertEqual(category.middle_price(), 150.0)

        # Пустая категория
        empty_category = Category("Empty Category", "Description", [])
        self.assertEqual(empty_category.middle_price(), 0)


if __name__ == '__main__':
    unittest.main()
