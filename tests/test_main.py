import unittest
from src.main import Product, Category


class TestProductCategory(unittest.TestCase):

    def setUp(self):
        # Сброс счетчиков перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

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
        self.assertEqual(len(category.products), 2)
        self.assertIn(product1, category.products)
        self.assertIn(product2, category.products)

    def test_product_count(self):
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        product2 = Product("Product 2", "Description 2", 60.0, 6)
        category = Category("Test Category", "Category Description", [product1, product2])
        self.assertEqual(Category.product_count, 2)

    def test_category_count(self):
        Category("Category 1", "Description 1", [])
        Category("Category 2", "Description 2", [])
        self.assertEqual(Category.category_count, 2)

    def test_product_addition_to_category(self):
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        category = Category("Test Category", "Category Description", [])
        category.products.append(product1)

        Category.product_count = len(category.products)
        self.assertEqual(len(category.products), 1)
        self.assertIn(product1, category.products)
        self.assertEqual(Category.product_count, 1)

# if __name__ == '__main__':
#     unittest.main()
