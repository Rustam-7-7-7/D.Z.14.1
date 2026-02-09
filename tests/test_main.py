import unittest
from src.main import Product, Category


class TestProductCategory(unittest.TestCase):

    def setUp(self):
        # Сброс счетчиков перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

    def test_product_initialization(self):
        # Тестирование инициализации продуктов
        product = Product("Test Product", "Description", 100.0, 10)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 10)

    def test_category_initialization(self):
        # Тестирование инициализации категорий
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        product2 = Product("Product 2", "Description 2", 60.0, 6)
        category = Category("Test Category", "Category Description", [product1, product2])
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Category Description")
        self.assertEqual(len(category._Category__products), 2)

    def test_product_count(self):
        # Тестирование подсчета продуктов
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        product2 = Product("Product 2", "Description 2", 60.0, 6)
        Category("Test Category", "Category Description", [product1, product2])
        self.assertEqual(Category.product_count, 2)

    def test_category_count(self):
        # Тестирование подсчета категорий
        Category("Category 1", "Description 1", [])
        Category("Category 2", "Description 2", [])
        self.assertEqual(Category.category_count, 2)

    def test_add_product(self):
        # Тестирование добавления продукта в категорию
        category = Category("Test", "Description", [])
        product = Product("Test Product", "Description", 100.0, 10)
        category.add_product(product)
        self.assertIn(product, category._Category__products)
        self.assertEqual(Category.product_count, 1)

    def test_product_price_setter(self):
        # Тестирование сеттера цены у продукта
        product = Product("Test Product", "Description", 100.0, 10)
        product.price = 50.0
        self.assertEqual(product.price, 50.0)
        product.price = -10.0
        self.assertEqual(product.price, 50.0)  # Цена не должна измениться
        product.price = 0.0
        self.assertEqual(product.price, 50.0)  # Цена не должна измениться

    def test_product_new_method(self):
        # Тестирование метода new_product
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
        # Тестирование геттера products у категории
        product = Product("Test Product", "Description", 100.0, 10)
        category = Category("Test", "Description", [product])
        expected_output = "Test Product, 100.0 руб. Остаток: 10 шт."
        self.assertEqual(category.products, expected_output)


if __name__ == '__main__':
    unittest.main()
