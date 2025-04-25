# %% Purpose
# Python Object-Oriented Programming: Inheritance
# Purpose: Inheritance allows a class to inherit attributes and methods from another class.
# Key Features: Code reuse, hierarchical modeling.

# %% 1. Basic Inheritance
# Explanation: Child class inherits from parent using class Child(Parent).
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"{self.name}: ${self.price:.2f}"

class Electronics(Product):
    pass

laptop = Electronics("Laptop Pro", 999.99)
print(laptop.display())
# Output: Laptop Pro: $999.99

# %% 2. Extending Child Class
# Explanation: Add or override methods/attributes in child class.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"{self.name}: ${self.price:.2f}"

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
    def display(self):
        return f"{self.name}: ${self.price:.2f}, Warranty: {self.warranty} years"

smartphone = Electronics("Smartphone X", 699.99, 2)
print(smartphone.display())
# Output: Smartphone X: $699.99, Warranty: 2 years

# %% 3. Retail Scenario with Inheritance
# Explanation: Model specialized products with inheritance.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Appliance(Product):
    def __init__(self, name, price, power):
        super().__init__(name, price)
        self.power = power
    def display(self):
        return f"{self.name}: ${self.price:.2f}, Power: {self.power}W"

blender = Appliance("Blender", 39.99, 500)
blender.apply_discount(0.1)
print(blender.display())
# Output: Blender: $35.99, Power: 500W

# %% Notes
# Notes:
# - Use super() to call parent class methods/constructors.
# - Inheritance promotes reuse in ML (e.g., model hierarchies) or web apps (e.g., user types).
# - Avoid deep inheritance hierarchies for simplicity.