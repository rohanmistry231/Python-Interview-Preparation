# Python Exception Handling: Raise Statement

# Purpose: Raise statement triggers an exception explicitly to enforce conditions.
# Key Features: Custom error handling, program control.

# 1. Basic Raise
# Explanation: Raise an exception with raise ExceptionType("message").
# Example:
price = -50
if price < 0:
    raise ValueError("Price cannot be negative")
# Output: ValueError: Price cannot be negative (program stops unless caught)

# 2. Raise with Try-Except
# Explanation: Raise an exception and handle it in a try-except block.
# Example:
try:
    stock = 0
    if stock <= 0:
        raise ValueError("Stock must be positive")
    print(f"Stock: {stock}")
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Stock must be positive

# 3. Retail Scenario with Raise
# Explanation: Enforce business rules in a retail context.
# Example:
order = {"name": "Laptop", "quantity": 2, "price": 999.99}
try:
    if order["quantity"] > 100:
        raise ValueError("Quantity exceeds maximum limit")
    if order["price"] < 0:
        raise ValueError("Negative price not allowed")
    total = order["quantity"] * order["price"]
    print(f"Order total for {order['name']}: ${total:.2f}")
except ValueError as e:
    print(f"Order error: {e}")
# Output: Order total for Laptop: $1999.98

# Exercise 1: Raise a ValueError if a user-entered price is negative.
# Solution:
# try:
#     price = float(input("Enter price: "))  # Simulating input (e.g., "-10")
#     if price < 0:
#         raise ValueError("Negative price not allowed")
#     print("Exercise 1 - Price:", price)
# except ValueError as e:
#     print("Exercise 1 - Error:", e)
# # Output (if input is "-10"): Error: Negative price not allowed

# Exercise 2: Raise an exception if stock is zero in a product dictionary.
# Solution:
# product = {"name": "Blender", "stock": 0}
# try:
#     if product["stock"] == 0:
#         raise ValueError("Zero stock not allowed")
#     print("Exercise 2 - Stock:", product["stock"])
# except ValueError as e:
#     print("Exercise 2 - Error:", e)
# # Output: Error: Zero stock not allowed

# Exercise 3: Raise a TypeError if an order’s quantity is not an integer.
# Solution:
# order = {"name": "Mouse", "quantity": "5"}
# try:
#     if not isinstance(order["quantity"], int):
#         raise TypeError("Quantity must be an integer")
#     print("Exercise 3 - Quantity:", order["quantity"])
# except TypeError as e:
#     print("Exercise 3 - Error:", e)
# # Output: Error: Quantity must be an integer

# Notes:
# - Use raise to enforce business rules in ML (e.g., invalid model parameters) or web apps (e.g., API validation).
# - Combine with try-except to handle raised exceptions gracefully.
# - Include descriptive error messages for debugging.