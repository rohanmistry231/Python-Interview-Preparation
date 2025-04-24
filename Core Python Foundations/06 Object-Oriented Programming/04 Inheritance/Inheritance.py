# Python Object-Oriented Programming: Inheritance

# Purpose: Inheritance allows a class to inherit attributes and methods from another class.
# Key Features: Code reuse, hierarchical modeling.

# 1. Basic Inheritance
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

# 2. Extending Child Class
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

# 3. Retail Scenario with Inheritance
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

# Exercise 1: Create a class Order and a child class OnlineOrder with an additional delivery_fee.
# Solution:
# class Order:
#     def __init__(self, order_id, total):
#         self.order_id = order_id
#         self.total = total
# class OnlineOrder(Order):
#     def __init__(self, order_id, total, delivery_fee):
#         super().__init__(order_id, total)
#         self.delivery_fee = delivery_fee
# order = OnlineOrder(101, 999.99, 10.00)
# print("Exercise 1 - Order:", order.order_id, order.total, order.delivery_fee)
# # Output: Order: 101 999.99 10.0

# Exercise 2: Extend Product class with a Furniture class that adds material attribute.
# Solution:
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Furniture(Product):
#     def __init__(self, name, price, material):
#         super().__init__(name, price)
#         self.material = material
# chair = Furniture("Chair", 99.99, "Wood")
# print("Exercise 2 - Furniture:", chair.name, chair.material)
# # Output: Furniture: Chair Wood

# Exercise 3: Override a display method in a child class Electronics.
# Solution:
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def display(self):
#         return f"{self.name}: ${self.price:.2f}"
# class Electronics(Product):
#     def display(self):
#         return f"Electronics - {self.name}: ${self.price:.2f}"
# mouse = Electronics("Mouse", 29.99)
# print("Exercise 3 -", mouse.display())
# # Output: Electronics - Mouse: $29.99

# Notes:
# - Use super() to call parent class methods/constructors.
# - Inheritance promotes reuse in ML (e.g., model hierarchies) or web apps (e.g., user types).
# - Avoid deep inheritance hierarchies for simplicity.