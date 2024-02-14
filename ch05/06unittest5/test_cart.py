import unittest

from cart import ShoppingCart
from product import Product


class ShoppingCartTestCase(unittest.TestCase):
    def test_add_remove_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)
