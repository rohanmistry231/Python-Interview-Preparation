# %% Purpose
# Python Object-Oriented Programming: Methods
# Purpose: Methods are functions defined in a class that operate on objects.
# Key Features: Encapsulate behavior, access instance/class data.

# %% 1. Instance Methods
# Explanation: Methods that take 'self' as first parameter, access instance attributes.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, discount):
        self.price *= (1 - discount)
        return self.price

laptop = Product("Laptop Pro", 999.99)
new_price = laptop.apply_discount(0.1)
print(f"Discounted price: ${new_price:.2f}")
# Output: Discounted price: $899.99

# %% 2. Calling Methods
# Explanation: Methods are called on objects using dot notation.
# Example:
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def check_stock(self):
        return f"{self.name}: {self.stock} in stock"

coffee_maker = Product("Coffee Maker", 49.99, 30)
print(coffee_maker.check_stock())
# Output: Coffee Maker: 30 in stock

# %% 3. Methods with Parameters
# Explanation: Methods can take additional parameters for complex logic.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def calculate_total(self, quantity):
        return self.price * quantity

smartphone = Product("Smartphone X", 699.99)
total = smartphone.calculate_total(2)
print(f"Total for 2 units: ${total:.2f}")
# Output: Total for 2 units: $1399.98

# %% Notes
# Notes:
# - Methods define object behavior, used in ML for model operations or web apps for business logic.
# - Always include 'self' as first parameter in instance methods.
# - Methods can return values or modify object state.