# %% Purpose
# Python Object-Oriented Programming: Static Methods
# Purpose: Static methods belong to a class, not instances, and don’t access instance data.
# Key Features: Utility functions, no 'self' parameter.

# %% 1. Defining a Static Method
# Explanation: Use @staticmethod decorator, no 'self' or 'cls'.
# Example:
class Product:
    @staticmethod
    def calculate_tax(price):
        return price * 0.1

tax = Product.calculate_tax(999.99)
print(f"Tax: ${tax:.2f}")
# Output: Tax: $99.99

# %% 2. Static Method in Retail Context
# Explanation: Use for class-level utilities (e.g., price formatting).
# Example:
class Product:
    @staticmethod
    def format_price(price):
        return f"${price:.2f}"

    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"{self.name}: {Product.format_price(self.price)}"

laptop = Product("Laptop Pro", 999.99)
print(laptop.display())
print(Product.format_price(49.99))
# Output: Laptop Pro: $999.99
#         $49.99

# %% 3. Combining with Instance Methods
# Explanation: Static methods can be called from instance methods.
# Example:
class Product:
    @staticmethod
    def is_valid_price(price):
        return isinstance(price, (int, float)) and price >= 0
    def __init__(self, name, price):
        if not Product.is_valid_price(price):
            raise ValueError("Invalid price")
        self.name = name
        self.price = price

blender = Product("Blender", 39.99)
print(f"Product: {blender.name}, Price: ${blender.price:.2f}")
# Output: Product: Blender, Price: $39.99

# %% Notes
# Notes:
# - Static methods are class-level utilities, used in ML for helper functions or web apps for formatting.
# - No access to instance or class state unless passed explicitly.
# - Call via class or instance (e.g., Product.method() or obj.method()).