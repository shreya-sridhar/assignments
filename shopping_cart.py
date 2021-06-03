from typing import Dict
from constants import *

class Shop:
    def __init__(self):
        self.sku_price_map = SKU_PRICE_MAP
        self.sku_to_item_map = SKU_TO_ITEM_MAP
        self.item_to_sku_map = ITEM_TO_SKU_MAP

class ShoppingCart(Shop):
    def __init__(self, cart: Dict = defaultDict(int)):
        self.cart = cart

    def add(self, sku:str):
        cart[sku] += 1
    
    def total_amount(self) -> float:
        total_cart_value = 0
        for item,quantity in self.cart:
            total_cart_value += self.sku_price_map[item] * quantity
        return round(total_cart_value,2)

    def items_list(self) -> str:
        items = []
        for sku_item in list(self.cart.keys()):
            items.append(sku_item.sku_to_item_map[sku_item])
        return items.sort().join(", ")





