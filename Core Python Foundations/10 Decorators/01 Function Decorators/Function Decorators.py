# %% Purpose
# Python Decorators: Function Decorators
# Purpose: Function decorators wrap functions to add functionality (e.g., logging, timing) without modifying their code.
# Key Features: Reusability, separation of concerns, use of @ syntax.

# %% 1. Basic Function Decorator
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

# %% 2. Decorator with Arguments
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

# %% 3. Retail Scenario with Function Decorator
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

# %% Notes
# Notes:
# - Function decorators are used in ML for logging model training or web apps for authentication.
# - Use *args and **kwargs in wrappers to handle any function signature.
# - Stack multiple decorators (@dec1 @dec2) for combined functionality.