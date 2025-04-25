# %% Purpose
# Python Object-Oriented Programming: Polymorphism
# Purpose: Polymorphism allows different classes to be treated via a common interface.
# Key Features: Method overriding, flexible design.

# %% 1. Method Overriding
# Explanation: Child class redefines a parent class method.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"{self.name}: ${self.price:.2f}"

class Electronics(Product):
    def display(self):
        return f"Electronics - {self.name}: ${self.price:.2f}"

laptop = Electronics("Laptop Pro", 999.99)
print(laptop.display())
# Output: Electronics - Laptop Pro: $999.99

# %% 2. Polymorphic Behavior
# Explanation: Use a common interface for different classes.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_details(self):
        return f"{self.name}: ${self.price:.2f}"

class Appliance(Product):
    def __init__(self, name, price, power):
        super().__init__(name, price)
        self.power = power
    def get_details(self):
        return f"{self.name}: ${self.price:.2f}, Power: {self.power}W"

products = [Product("Mouse", 29.99), Appliance("Blender", 39.99, 500)]
for product in products:
    print(product.get_details())
# Output: Mouse: $29.99
#         Blender: $39.99, Power: 500W

# %% 3. Retail Scenario with Polymorphism
# Explanation: Process different product types uniformly.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self):
        return self.price * 0.9

class Electronics(Product):
    def apply_discount(self):
        return self.price * 0.85  # Special discount for electronics

items = [Product("Coffee Maker", 49.99), Electronics("Smartphone", 699.99)]
for item in items:
    print(f"Discounted price for {item.name}: ${item.apply_discount():.2f}")
# Output: Discounted price for Coffee Maker: $44.99
#         Discounted price for Smartphone: $594.99

# %% Notes
# Notes:
# - Polymorphism enables flexible code in ML (e.g., model interfaces) or web apps (e.g., rendering different entities).
# - Use method overriding to customize behavior.
# - Ensure common method names for polymorphic behavior.