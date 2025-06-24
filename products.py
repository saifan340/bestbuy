from typing import List, Tuple
#from products import Product


class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: name cannot be empty, price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy should be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price


class Store:
    def __init__(self, products: List[Product]):
        self.products = products


    def add_product(self, product: Product):
        self.products.append(product)


    def remove_product(self, product: Product):
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        total_quantity = sum(product.get_quantity() for product in self.products)
        return total_quantity


    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if product.is_active():
                total_price += product.buy(quantity)
        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
if __name__ == "__main__":
    main()