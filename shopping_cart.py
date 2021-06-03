from typing import Dict

class Shop:
    def __init__(self):
        self.sku_price_map = 
        self.sku_to_item_map = 
        self.item_to_sku_map = 

class ShoppingCart(Shop):
    def __init__(self, cart: Dict = defaultDict(int)):
        self.cart = cart
        self.sku_price_map = sku_price_map
        self.sku_to_item_map = []

    def add(self, sku:str):
        cart[sku] += 1
    
    def total_amount(self) -> float:
        total_cart_value = 0
        for item,quantity in self.cart:
            total_cart_value += self.sku_price_map[item] * quantity
        return round(total_cart_value,2)

    def items_list:
        items = []
        for sku_item in list(self.cart.values()):
            items.append(sku_item.sku_to_item_map[sku_item])
        return items.sort().join(", ")

Your task is to define a shopping cart for a corner shop. The cart should keep track of the list of items added, and correctly calculate the price.
Items are added to the basket using stock-keeping unit (SKU) codes. The items in the shop are:
Name    	| Price	| SKU
Potatoes	| 10.00	| STAPOT
Rice      | 30.00 | STARIC
Coffee    | 14.99	| STACOF
Newspaper |	2.99 |	MEDNEW

You need to define a ShoppingCart class, with three public methods:

* add: Takes a SKU and adds it to the cart. The SKU is a Symbol comprised of the first three uppercase letters of the product type + the first three uppercase letters of the product name.
* total_amount: The value of the items in the cart as a number with two decimal places (e.g. 3.99).
* items_list: A list of the names of the items in the cart, ordered alphabetically, with no duplicates, separated by a comma and a space.



