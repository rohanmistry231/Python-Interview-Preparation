# Python Object-Oriented Programming: Classes and Objects

# Purpose: Classes define blueprints for objects, which are instances of classes.
# Key Features: Encapsulates data and behavior, foundation of OOP.

# 1. Defining a Class and Creating an Object
# Explanation: Use 'class' keyword to define a class; instantiate with class name.
# Example:
class Product:
    pass

# Create objects
laptop = Product()
smartphone = Product()
print("Objects created:", laptop, smartphone)
# Output: Objects created: <__main__.Product object at ...> <__main__.Product object at ...>

# 2. Initializing Objects with __init__
# Explanation: __init__ method initializes object attributes.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

laptop = Product("Laptop Pro", 999.99)
print(f"Product: {laptop.name}, Price: ${laptop.price:.2f}")
# Output: Product: Laptop Pro, Price: $999.99

# 3. Retail Scenario with Classes
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

# Exercise 1: Define a class Order and create an object with order_id and total.
# Solution:
# class Order:
#     def __init__(self, order_id, total):
#         self.order_id = order_id
#         self.total = total
# order = Order(101, 1999.98)
# print("Exercise 1 - Order ID:", order.order_id, "Total:", order.total)
# # Output: Order ID: 101 Total: 1999.98

# Exercise 2: Create a Product class with category attribute and instantiate two objects.
# Solution:
# class Product:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category
# mouse = Product("Mouse", "Electronics")
# blender = Product("Blender", "Appliances")
# print("Exercise 2 - Mouse:", mouse.name, mouse.category, "Blender:", blender.name, blender.category)
# # Output: Mouse: Mouse Electronics Blender: Blender Appliances

# Exercise 3: Define a class Customer and initialize an object with name and email.
# Solution:
# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
# customer = Customer("Alice", "alice@example.com")
# print("Exercise 3 - Customer:", customer.name, customer.email)
# # Output: Customer: Alice alice@example.com

# Notes:
# - Classes are templates; objects are instances with specific data.
# - Use in ML for modeling entities (e.g., datasets) or web apps for data structures (e.g., user models).
# - __init__ is a constructor, called automatically when an object is created.