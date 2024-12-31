class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to inventory.")

    def display_all_products(self):
        if not self.products:
            print("No products in the inventory.")
        else:
            for product in self.products:
                product.display_info()

    def calculate_total_inventory_value(self):
        total_value = sum(product.calculate_total_value() for product in self.products)
        print(f"Total inventory value: {total_value}")
        return total_value