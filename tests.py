import unittest 
from shopping_cart.py import * 
from constants import *

class TestShoppingCartPrice(unittest.TestCase):

    # when each item is only added once
    def test_item_quantity_one(self):
        items = list(SKU_PRICE_MAP.keys())
        iter = 0
        cart = Cart()
        for iter in range(len(items)):
            cart.add(items[iter%len(items)])
        self.assertEqual(cart.total_amount,)

    # when each item is added more than once
    def test_item_quantity_many(self):
        items = list(SKU_PRICE_MAP.keys())
        iter = 0
        cart = Cart()
        for iter in range(2*len(items)):
            cart.add(items[iter%len(items)])
        self.assertEqual(cart.total_amount,)

    # no item is added 
    def test_zero_items(self):
        cart = Cart()
        self.assertEqual(cart.total_amount,0)

if __name__ == '__main__':
    unittest.main()


