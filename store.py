import products
from typing import List, Tuple
class Store:
    def __init__(self, products: List[products.Product]):
        self.products = products


    def add_product(self, product: products.Product):
        self.products.append(product)


    def remove_product(self, product: products.Product):
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        total_quantity = sum(product.get_quantity() for product in self.products)
        return total_quantity


    def get_all_products(self) -> List[products.Product]:
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if product.is_active():
                total_price += product.buy(quantity)
        return total_price
