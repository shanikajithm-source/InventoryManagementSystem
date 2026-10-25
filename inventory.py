
import json
import math
from pathlib import Path


# Product class
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product Name:", self.name)
        print(f"Price: Rs. {self.price:,.2f}")
        print("Quantity:", self.quantity)
        print("------------------------")


# Inventory class
class Inventory:

    def __init__(self):
        self.products = []
        self.file_path = Path(__file__).with_name("inventory.json")
        self.load_inventory()

    # Save inventory to JSON
    def save_inventory(self):

        data = []

        for product in self.products:
            data.append({
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            })

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            print("Inventory saved successfully!")

        except OSError as error:
            print("Error saving inventory:", error)

    # Load inventory from JSON
    def load_inventory(self):

        if not self.file_path.exists():
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Inventory data must be a list")

            loaded_products = []

            for item in data:
                name = item["name"]
                price = float(item["price"])
                quantity = item["quantity"]

                if (
                    not isinstance(name, str)
                    or not name.strip()
                    or not math.isfinite(price)
                    or price < 0
                    or type(quantity) is not int
                    or quantity < 0
                ):
                    raise ValueError("Invalid product data")

                loaded_products.append(
                    Product(name, price, quantity)
                )

            self.products = loaded_products
            print("Saved inventory loaded successfully!")

        except (OSError, ValueError, TypeError, KeyError) as error:
            print("Error loading inventory:", error)

    # Find product by name
    def find_product(self, name):

        for product in self.products:
            if product.name.lower() == name.lower():
                return product

        return None

    # Add product
    def add_product(self):

        name = input("Enter product name: ").strip()

        if not name:
            print("Product name cannot be empty!")
            return

        if self.find_product(name):
            print("Product already exists!")
            return

        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))

            if not math.isfinite(price) or price < 0 or quantity < 0:
                print("Enter a valid non-negative price and quantity!")
                return

        except ValueError:
            print("Invalid price or quantity!")
            return

        product = Product(name, price, quantity)
        self.products.append(product)

        print(name, "added successfully!")
        self.save_inventory()

    # View inventory
    def display_inventory(self):

        print("\n===== INVENTORY =====")

        if not self.products:
            print("Inventory is empty!")
            return

        for product in self.products:
            product.display()

    # Update quantity
    def update_quantity(self):

        name = input("Enter product name to update: ").strip()
        product = self.find_product(name)

        if product is None:
            print("Product not found!")
            return

        try:
            new_quantity = int(input("Enter new quantity: "))

            if new_quantity < 0:
                print("Quantity cannot be negative!")
                return

        except ValueError:
            print("Invalid quantity!")
            return

        product.quantity = new_quantity

        print("Quantity updated successfully!")
        self.save_inventory()

    # Update price
    def update_price(self):

        name = input("Enter product name to update price: ").strip()
        product = self.find_product(name)

        if product is None:
            print("Product not found!")
            return

        try:
            new_price = float(input("Enter new price: "))

            if not math.isfinite(new_price) or new_price < 0:
                print("Enter a valid non-negative price!")
                return

        except ValueError:
            print("Invalid price!")
            return

        product.price = new_price

        print("Price updated successfully!")
        self.save_inventory()

    # Delete product
    def delete_product(self):

        name = input("Enter product name to delete: ").strip()
        product = self.find_product(name)

        if product is None:
            print("Product not found!")
            return

        confirmation = input(
            "Are you sure you want to delete this product? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":
            self.products.remove(product)
            print("Product deleted successfully!")
            self.save_inventory()
        else:
            print("Deletion cancelled.")

    # Calculate total inventory value
    def total_inventory_value(self):

        total = 0

        for product in self.products:
            total += product.price * product.quantity

        print("\n===== INVENTORY VALUE =====")
        print(f"Total Inventory Value: Rs. {total:,.2f}")


# Main program
inventory = Inventory()

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Update Product Quantity")
    print("4. Update Product Price")
    print("5. Delete Product")
    print("6. Total Inventory Value")
    print("7. Exit")

    try:
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            inventory.add_product()

        elif choice == "2":
            inventory.display_inventory()

        elif choice == "3":
            inventory.update_quantity()

        elif choice == "4":
            inventory.update_price()

        elif choice == "5":
            inventory.delete_product()

        elif choice == "6":
            inventory.total_inventory_value()

        elif choice == "7":
            print("Thank you for using Inventory Management System!")
            break

        else:
            print("Invalid choice! Please try again.")

    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed.")
        break
