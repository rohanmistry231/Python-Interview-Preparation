# Python Decorators: Function Decorators

# Purpose: Function decorators wrap functions to add functionality (e.g., logging, timing) without modifying their code.
# Key Features: Reusability, separation of concerns, use of @ syntax.

# 1. Basic Function Decorator
# Explanation: A decorator is a function that takes another function and extends its behavior.
# Example:
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logging_decorator
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(999.99, 2)
# Output: Calling calculate_total with args: (999.99, 2), kwargs: {}
#         calculate_total returned: 1999.98

# 2. Decorator with Arguments
# Explanation: Use a decorator factory to pass arguments to the decorator.
# Example:
def discount_decorator(discount_rate):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_price = func(*args, **kwargs)
            discounted_price = original_price * (1 - discount_rate)
            return discounted_price
        return wrapper
    return decorator

@discount_decorator(0.1)  # 10% discount
def calculate_order_total(items):
    return sum(items)

order_total = calculate_order_total([999.99, 699.99])
print(f"Discounted order total: ${order_total:.2f}")
# Output: Discounted order total: $1499.98

# 3. Retail Scenario with Function Decorator
# Explanation: Use a decorator to log retail order processing time.
# Example:
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timing_decorator
def process_orders(orders):
    # Simulate processing
    for order in orders:
        time.sleep(0.1)  # Simulate work
    return len(orders)

orders = [{"order_id": 101, "total": 1999.98}, {"order_id": 102, "total": 49.99}]
processed = process_orders(orders)
print(f"Processed {processed} orders")
# Output: process_orders took 0.20 seconds (approx)
#         Processed 2 orders

# Exercise 1: Create a decorator to print a message before and after a function call.
# Solution:
# def message_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Starting function...")
#         result = func(*args, **kwargs)
#         print("Function completed!")
#         return result
#     return wrapper
# @message_decorator
# def get_product_name(product_id):
#     return f"Product_{product_id}"
# name = get_product_name(101)
# print("Exercise 1 - Product name:", name)
# # Output: Starting function...
# #         Function completed!
# #         Product name: Product_101

# Exercise 2: Write a decorator to round the result of a function to 2 decimal places.
# Solution:
# def round_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return round(result, 2)
#     return wrapper
# @round_decorator
# def calculate_tax(price, tax_rate):
#     return price * tax_rate
# tax = calculate_tax(999.99, 0.075)
# print("Exercise 2 - Tax:", tax)
# # Output: Tax: 75.0

# Exercise 3: Create a decorator to validate positive inputs for a retail function.
# Solution:
# def positive_input_decorator(func):
#     def wrapper(*args, **kwargs):
#         if any(arg <= 0 for arg in args if isinstance(arg, (int, float))):
#             raise ValueError("Inputs must be positive")
#         return func(*args, **kwargs)
#     return wrapper
# @positive_input_decorator
# def calculate_inventory_value(quantity, price):
#     return quantity * price
# value = calculate_inventory_value(10, 99.99)
# print("Exercise 3 - Inventory value:", value)
# # Output: Inventory value: 999.9
# # Note: Try calculate_inventory_value(-10, 99.99) to see ValueError

# Notes:
# - Function decorators are used in ML for logging model training or web apps for authentication.
# - Use *args and **kwargs in wrappers to handle any function signature.
# - Stack multiple decorators (@dec1 @dec2) for combined functionality.