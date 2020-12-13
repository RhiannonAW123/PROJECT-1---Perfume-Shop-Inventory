import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Chance", "Romantic", 20, 60, 70) 


    def test_product_has_name(self):
        self.assertEqual("Chance", self.product.name)

    def test_product_has_description(self):
        self.assertEqual("Romantic", self.product.description)

    def test_product_has_stock(self):
        self.assertEqual(20, self.product.stock)

    def test_product_has_buy_price(self):
        self.assertEqual(60, self.product.buy_price)

    def test_product_has_sell_price(self):
        self.assertEqual(70, self.product.sell_price)