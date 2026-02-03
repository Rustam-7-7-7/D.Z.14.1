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
        self.assertEqual(len(category.products), 2)
        self.assertIn(product1, category.products)
        self.assertIn(product2, category.products)

    def test_product_count(self):
        # Тестирование подсчета продуктов
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        product2 = Product("Product 2", "Description 2", 60.0, 6)
        category = Category("Test Category", "Category Description", [product1, product2])
        self.assertEqual(Category.product_count, 2)

    def test_category_count(self):
        # Тестирование подсчета категорий
        Category("Category 1", "Description 1", [])
        Category("Category 2", "Description 2", [])
        self.assertEqual(Category.category_count, 2)

    def test_product_addition_to_category(self):
        # Тестирование добавления продукта в категорию
        product1 = Product("Product 1", "Description 1", 50.0, 5)
        category = Category("Test Category", "Category Description", [])
        category.products.append(product1)
        # Обновление подсчета продуктов
        Category.product_count = len(category.products)
        self.assertEqual(len(category.products), 1)
        self.assertIn(product1, category.products)
        self.assertEqual(Category.product_count, 1)

    def test_main_code_execution(self):
        # Тестирование выполнения кода из блока if __name__ == "__main__"
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3]
        )
        category2 = Category(
            "Телевизоры",
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            [product4]
        )

        self.assertEqual(Category.category_count, 2)
        self.assertEqual(Category.product_count, 4)


if __name__ == '__main__':
    unittest.main()
