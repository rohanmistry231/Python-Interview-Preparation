# Python Object-Oriented Programming: Methods

# Purpose: Methods are functions defined in a class that operate on objects.
# Key Features: Encapsulate behavior, access instance/class data.

# 1. Instance Methods
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

# 2. Calling Methods
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

# 3. Methods with Parameters
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

# Exercise 1: Define a method in Order class to display order details.
# Solution:
# class Order:
#     def __init__(self, order_id, total):
#         self.order_id = order_id
#         self.total = total
#     def display(self):
#         return f"Order {self.order_id}: ${self.total:.2f}"
# order = Order(101, 1999.98)
# print("Exercise 1 -", order.display())
# # Output: Order 101: $1999.98

# Exercise 2: Create a method in Product class to restock by a given amount.
# Solution:
# class Product:
#     def __init__(self, name, stock):
#         self.name = name
#         self.stock = stock
#     def restock(self, amount):
#         self.stock += amount
#         return self.stock
# blender = Product("Blender", 20)
# new_stock = blender.restock(10)
# print("Exercise 2 - New stock:", new_stock)
# # Output: New stock: 30

# Exercise 3: Define a method to calculate tax (10%) in a Product class.
# Solution:
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def calculate_tax(self):
#         return self.price * 0.1
# mouse = Product("Mouse", 29.99)
# tax = mouse.calculate_tax()
# print("Exercise 3 - Tax:", tax)
# # Output: Tax: 2.999

# Notes:
# - Methods define object behavior, used in ML for model operations or web apps for business logic.
# - Always include 'self' as first parameter in instance methods.
# - Methods can return values or modify object state.