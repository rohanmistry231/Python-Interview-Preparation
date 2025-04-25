# %% Purpose
# Python Object-Oriented Programming: Multiple Inheritance
# Purpose: Multiple inheritance allows a class to inherit from multiple parent classes.
# Key Features: Combines behaviors, complex hierarchies.

# %% 1. Basic Multiple Inheritance
# Explanation: Class inherits from multiple parents using class Child(Parent1, Parent2).
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"{self.name}: ${self.price:.2f}"

class Discountable:
    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Electronics(Product, Discountable):
    pass

laptop = Electronics("Laptop Pro", 999.99)
laptop.apply_discount(0.1)
print(laptop.display())
# Output: Laptop Pro: $899.99

# %% 2. Resolving Method Conflicts
# Explanation: Method Resolution Order (MRO) determines which parent method is called.
# Example:
class Product:
    def display(self):
        return "Product display"

class Warranty:
    def display(self):
        return "Warranty display"

class Smartphone(Product, Warranty):
    pass

smartphone = Smartphone()
print(smartphone.display())
print(Smartphone.__mro__)
# Output: Product display
#         (<class '__main__.Smartphone'>, <class '__main__.Product'>, <class '__main__.Warranty'>, <class 'object'>)

# %% 3. Retail Scenario with Multiple Inheritance
# Explanation: Combine product and promotional features.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"{self.name}: ${self.price:.2f}"

class Promotable:
    def __init__(self, promotion):
        self.promotion = promotion
    def get_promo(self):
        return f"Promotion: {self.promotion}"

class Appliance(Product, Promotable):
    def __init__(self, name, price, promotion):
        Product.__init__(self, name, price)
        Promotable.__init__(self, promotion)

blender = Appliance("Blender", 39.99, "10% off")
print(blender.display())
print(blender.get_promo())
# Output: Blender: $39.99
#         Promotion: 10% off

# %% Notes
# Notes:
# - Use multiple inheritance sparingly to avoid complexity.
# - Check MRO with __mro__ or mro() to understand method resolution.
# - Useful in ML for combining model features or web apps for mixing behaviors.