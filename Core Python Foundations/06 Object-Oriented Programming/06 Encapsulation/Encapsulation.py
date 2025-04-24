# Python Object-Oriented Programming: Encapsulation

# Purpose: Encapsulation restricts access to attributes/methods, protecting data integrity.
# Key Features: Private attributes (using _ or __), getter/setter methods.

# 1. Private Attributes with Single Underscore
# Explanation: Single underscore (_) indicates "protected" (convention, not enforced).
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Protected attribute
    def get_price(self):
        return self._price

laptop = Product("Laptop Pro", 999.99)
print(f"Price: ${laptop.get_price():.2f}")
# Output: Price: $999.99
print("Accessing _price:", laptop._price)  # Accessible but discouraged
# Output: Accessing _price: 999.99

# 2. Private Attributes with Double Underscore
# Explanation: Double underscore (__) triggers name mangling for stronger protection.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  # Private attribute
    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Price cannot be negative")

smartphone = Product("Smartphone X", 699.99)
print(f"Price: ${smartphone.get_price():.2f}")
smartphone.set_price(649.99)
print(f"Updated price: ${smartphone.get_price():.2f}")
# Output: Price: $699.99
#         Updated price: $649.99
# Accessing __price directly raises AttributeError
# print(smartphone.__price)  # Error

# 3. Retail Scenario with Encapsulation
# Explanation: Protect sensitive data like stock in a retail context.
# Example:
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock
    def get_stock(self):
        return self.__stock
    def update_stock(self, amount):
        if amount >= 0:
            self.__stock = amount
        else:
            raise ValueError("Stock cannot be negative")

blender = Product("Blender", 20)
print(f"Stock: {blender.get_stock()}")
blender.update_stock(30)
print(f"Updated stock: {blender.get_stock()}")
# Output: Stock: 20
#         Updated stock: 30

# Exercise 1: Create a class Order with a private total attribute and getter method.
# Solution:
# class Order:
#     def __init__(self, order_id, total):
#         self.order_id = order_id
#         self.__total = total
#     def get_total(self):
#         return self.__total
# order = Order(101, 999.99)
# print("Exercise 1 - Total:", order.get_total())
# # Output: Total: 999.99

# Exercise 2: Define a class Product with a private price and setter method.
# Solution:
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#     def set_price(self, price):
#         self.__price = price
#     def get_price(self):
#         return self.__price
# mouse = Product("Mouse", 29.99)
# mouse.set_price(25.99)
# print("Exercise 2 - Price:", mouse.get_price())
# # Output: Price: 25.99

# Exercise 3: Use encapsulation to protect customer email with getter/setter.
# Solution:
# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.__email = email
#     def get_email(self):
#         return self.__email
#     def set_email(self, email):
#         self.__email = email
# customer = Customer("Alice", "alice@example.com")
# customer.set_email("alice@new.com")
# print("Exercise 3 - Email:", customer.get_email())
# # Output: Email: alice@new.com

# Notes:
# - Encapsulation ensures data safety in ML (e.g., model parameters) or web apps (e.g., user data).
# - Use _ for convention-based protection, __ for stricter access control.
# - Getter/setter methods validate data before modification.