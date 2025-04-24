# Python Exception Handling: Custom Exceptions

# Purpose: Custom exceptions allow user-defined error types for specific scenarios.
# Key Features: Extends built-in exceptions, enhances code modularity.

# 1. Defining a Custom Exception
# Explanation: Create a class inheriting from Exception or its subclasses.
# Example:
class InvalidStockError(Exception):
    pass

try:
    stock = -10
    if stock < 0:
        raise InvalidStockError("Stock cannot be negative")
except InvalidStockError as e:
    print(f"Error: {e}")
# Output: Error: Stock cannot be negative

# 2. Custom Exception with Attributes
# Explanation: Add attributes to custom exceptions for detailed error info.
# Example:
class PriceError(Exception):
    def __init__(self, message, price):
        super().__init__(message)
        self.price = price

try:
    price = -50
    if price < 0:
        raise PriceError("Price must be non-negative", price)
except PriceError as e:
    print(f"Error: {e}, Invalid price: {e.price}")
# Output: Error: Price must be non-negative, Invalid price: -50

# 3. Retail Scenario with Custom Exception
# Explanation: Use custom exceptions for retail business rules.
# Example:
class OrderError(Exception):
    def __init__(self, message, order_details):
        super().__init__(message)
        self.order_details = order_details

order = {"name": "Smartphone", "quantity": 200, "price": 699.99}
try:
    if order["quantity"] > 100:
        raise OrderError("Quantity exceeds maximum limit", order)
    total = order["quantity"] * order["price"]
    print(f"Order total for {order['name']}: ${total:.2f}")
except OrderError as e:
    print(f"Order error: {e}, Details: {e.order_details}")
# Output: Order error: Quantity exceeds maximum limit, Details: {'name': 'Smartphone', 'quantity': 200, 'price': 699.99}

# Exercise 1: Define a custom exception for low stock and raise it if stock is below 10.
# Solution:
# class LowStockError(Exception):
#     pass
# try:
#     stock = 5
#     if stock < 10:
#         raise LowStockError("Stock too low")
#     print("Exercise 1 - Stock:", stock)
# except LowStockError as e:
#     print("Exercise 1 - Error:", e)
# # Output: Error: Stock too low

# Exercise 2: Create a custom exception with a price attribute and raise it for negative prices.
# Solution:
# class NegativePriceError(Exception):
#     def __init__(self, message, price):
#         super().__init__(message)
#         self.price = price
# try:
#     price = -20
#     if price < 0:
#         raise NegativePriceError("Price cannot be negative", price)
#     print("Exercise 2 - Price:", price)
# except NegativePriceError as e:
#     print(f"Exercise 2 - Error: {e}, Price: {e.price}")
# # Output: Error: Price cannot be negative, Price: -20

# Exercise 3: Define a custom exception for invalid orders and raise it for zero quantity.
# Solution:
# class InvalidOrderError(Exception):
#     def __init__(self, message, order):
#         super().__init__(message)
#         self.order = order
# order = {"name": "Mouse", "quantity": 0}
# try:
#     if order["quantity"] == 0:
#         raise InvalidOrderError("Quantity cannot be zero", order)
#     print("Exercise 3 - Valid order")
# except InvalidOrderError as e:
#     print(f"Exercise 3 - Error: {e}, Order: {e.order}")
# # Output: Error: Quantity cannot be zero, Order: {'name': 'Mouse', 'quantity': 0}

# Notes:
# - Custom exceptions improve code readability and maintainability in ML (e.g., model validation) or web apps (e.g., API error responses).
# - Inherit from Exception or specific subclasses (e.g., ValueError) for appropriate context.
# - Include attributes for detailed error reporting.