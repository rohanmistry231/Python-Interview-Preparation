# %% Purpose
# Python Object-Oriented Programming: Classes and Objects
# Purpose: Classes define blueprints for objects, which are instances of classes.
# Key Features: Encapsulates data and behavior, foundation of OOP.

# %% 1. Defining a Class and Creating an Object
# Explanation: Use 'class' keyword to define a class; instantiate with class name.
# Example:
class Product:
    pass

# Create objects
laptop = Product()
smartphone = Product()
print("Objects created:", laptop, smartphone)
# Output: Objects created: <__main__.Product object at ...> <__main__.Product object at ...>

# %% 2. Initializing Objects with __init__
# Explanation: __init__ method initializes object attributes.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

laptop = Product("Laptop Pro", 999.99)
print(f"Product: {laptop.name}, Price: ${laptop.price:.2f}")
# Output: Product: Laptop Pro, Price: $999.99

# %% 3. Retail Scenario with Classes
# Explanation: Model a retail product with attributes.
# Example:
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

coffee_maker = Product("Coffee Maker", 49.99, 30)
print(f"Product: {coffee_maker.name}, Price: ${coffee_maker.price:.2f}, Stock: {coffee_maker.stock}")
# Output: Product: Coffee Maker, Price: $49.99, Stock: 30

# %% Notes
# Notes:
# - Classes are templates; objects are instances with specific data.
# - Use in ML for modeling entities (e.g., datasets) or web apps for data structures (e.g., user models).
# - __init__ is a constructor, called automatically when an object is created.