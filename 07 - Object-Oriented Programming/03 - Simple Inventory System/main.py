from product import Product
from inventory import Inventory

def get_user_input():
    while True:
        print("=========== Inventory System ===========")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Update Product Quantity")
        print("4. Calculate Total Inventory Value")
        print("5. Exit")
        print("========================================")
        choice = input("Choose an option: ")
        print("===========")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice. Please try again.")
            print("===========")

def execute_choice(choice, inventory):
    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        product = Product(name, price, quantity)
        inventory.add_product(product)
    elif choice == "2":
        inventory.display_all_products()
    elif choice == "3":
        name = input("Enter product name to update quantity: ")
        quantity = int(input("Enter quantity to add (use negative numbers to subtract): "))
        product = next((p for p in inventory.products if p.name == name), None)
        if product:
            product.update_quantity(quantity)
        else:
            print(f"Product '{name}' not found in inventory.")
    elif choice == "4":
        inventory.calculate_total_inventory_value()
    elif choice == "5":
        print("Exiting the system.")
        exit()

def main():
    inventory = Inventory()
    while True:
        choice = get_user_input()
        execute_choice(choice, inventory)

if __name__ == "__main__":
    main()