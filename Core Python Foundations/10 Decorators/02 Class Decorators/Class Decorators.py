# Python Decorators: Class Decorators

# Purpose: Class decorators modify or enhance class definitions, often for adding methods or validation.
# Key Features: Metaprogramming, class-level functionality, reusable class modifications.

# 1. Basic Class Decorator
# Explanation: A class decorator is a function that takes a class and returns a modified class.
# Example:
def add_display_method(cls):
    def display(self):
        return f"{self.__class__.__name__}: {vars(self)}"
    cls.display = display
    return cls

@add_display_method
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999.99)
print(product.display())
# Output: Product: {'name': 'Laptop', 'price': 999.99}

# 2. Class Decorator with Arguments
# Explanation: Use a decorator factory to pass arguments to the class decorator.
# Example:
def add_discount(discount_rate):
    def decorator(cls):
        original_init = cls.__init__
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.discounted_price = self.price * (1 - discount_rate)
        cls.__init__ = new_init
        return cls
    return decorator

@add_discount(0.1)  # 10% discount
class Order:
    def __init__(self, order_id, price):
        self.order_id = order_id
        self.price = price

order = Order(101, 999.99)
print(f"Order {order.order_id}: Original ${order.price:.2f}, Discounted ${order.discounted_price:.2f}")
# Output: Order 101: Original $999.99, Discounted $899.99

# 3. Retail Scenario with Class Decorator
# Explanation: Use a class decorator to add validation for retail product attributes.
# Example:
def validate_positive_attributes(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for attr, value in vars(self).items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"{attr} must be non-negative")
    cls.__init__ = new_init
    return cls

@validate_positive_attributes
class InventoryItem:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

item = InventoryItem("Mouse", 30, 29.99)
print(f"Item: {item.name}, Stock: {item.stock}, Price: ${item.price:.2f}")
# Output: Item: Mouse, Stock: 30, Price: $29.99
# Note: Try InventoryItem("Mouse", -30, 29.99) to see ValueError

# Exercise 1: Create a class decorator to add a method to get class name.
# Solution:
# def add_class_name_method(cls):
#     def get_class_name(self):
#         return self.__class__.__name__
#     cls.get_class_name = get_class_name
#     return cls
# @add_class_name_method
# class Customer:
#     def __init__(self, name):
#         self.name = name
# customer = Customer("Alice")
# print("Exercise 1 - Class name:", customer.get_class_name())
# # Output: Class name: Customer

# Exercise 2: Write a class decorator to add a tax attribute (8% of price).
# Solution:
# def add_tax_attribute(cls):
#     original_init = cls.__init__
#     def new_init(self, *args, **kwargs):
#         original_init(self, *args, **kwargs)
#         self.tax = self.price * 0.08
#     cls.__init__ = new_init
#     return cls
# @add_tax_attribute
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# product = Product("Smartphone", 699.99)
# print("Exercise 2 - Tax:", product.tax)
# # Output: Tax: 55.9992

# Exercise 3: Create a class decorator to validate string attributes (non-empty).
# Solution:
# def validate_string_attributes(cls):
#     original_init = cls.__init__
#     def new_init(self, *args, **kwargs):
#         original_init(self, *args, **kwargs)
#         for attr, value in vars(self).items():
#             if isinstance(value, str) and not value.strip():
#                 raise ValueError(f"{attr} must be non-empty")
#     cls.__init__ = new_init
#     return cls
# @validate_string_attributes
# class Order:
#     def __init__(self, order_id, customer_name):
#         self.order_id = order_id
#         self.customer_name = customer_name
# order = Order(102, "Bob")
# print("Exercise 3 - Customer:", order.customer_name)
# # Output: Customer: Bob
# # Note: Try Order(102, "") to see ValueError

# Notes:
# - Class decorators are useful in ML for model validation or web apps for ORM enhancements.
# - Preserve original methods (e.g., __init__) to avoid breaking functionality.
# - Use for metaprogramming tasks like adding methods or enforcing invariants.