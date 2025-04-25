# Function Decorators Projects
# Purpose: Apply function decorator concepts through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Message Decorator
# Difficulty: Basic
# Description: Create a decorator to print messages before and after function execution.
# Objective: Practice basic function decorator creation.
# Tasks:
# - Define a decorator to print "Starting..." and "Completed!" around a function call.
# - Apply to a function that returns a product name.
# Expected Output: Starting...
#                 Completed!
#                 Product name: Product_101
def message_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Completed!")
        return result
    return wrapper

@message_decorator
def get_product_name(product_id):
    return f"Product_{product_id}"

name = get_product_name(101)
print("Product name:", name)

# %% Project 2: Round Result Decorator
# Difficulty: Basic
# Description: Create a decorator to round function results to 2 decimal places.
# Objective: Practice modifying function output.
# Tasks:
# - Define a decorator to round numerical results.
# - Apply to a tax calculation function.
# Expected Output: Tax: 75.00
def round_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result, 2)
    return wrapper

@round_decorator
def calculate_tax(price, tax_rate):
    return price * tax_rate

tax = calculate_tax(999.99, 0.075)
print("Tax:", tax)

# %% Project 3: Positive Input Decorator
# Difficulty: Basic
# Description: Create a decorator to validate positive numerical inputs.
# Objective: Practice input validation.
# Tasks:
# - Define a decorator to check for positive inputs.
# - Apply to an inventory value calculation function.
# Expected Output: Inventory value: 999.90
def positive_input_decorator(func):
    def wrapper(*args, **kwargs):
        if any(arg <= 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Inputs must be positive")
        return func(*args, **kwargs)
    return wrapper

@positive_input_decorator
def calculate_inventory_value(quantity, price):
    return quantity * price

value = calculate_inventory_value(10, 99.99)
print("Inventory value:", value)

# %% Project 4: Logging Input Decorator
# Difficulty: Basic
# Description: Create a decorator to log function inputs.
# Objective: Practice logging with decorators.
# Tasks:
# - Define a decorator to print function arguments.
# - Apply to a function that calculates order totals.
# Expected Output: Inputs: (1000.00, 2)
#                 Total: 2000.00
def logging_input_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Inputs: {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logging_input_decorator
def calculate_order_total(price, quantity):
    return price * quantity

total = calculate_order_total(1000.00, 2)
print("Total:", total)

# %% Project 5: Retry Decorator
# Difficulty: Intermediate
# Description: Create a decorator to retry a function on failure.
# Objective: Practice error handling with decorators.
# Tasks:
# - Define a decorator to retry a function up to 3 times on ValueError.
# - Apply to a function that processes order data.
# Expected Output: Retrying after error...
#                 Processed: 2 orders
def retry_decorator(func):
    def wrapper(*args, **kwargs):
        attempts = 3
        while attempts > 0:
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print("Retrying after error...")
                attempts -= 1
        raise ValueError("Max retries exceeded")
    return wrapper

@retry_decorator
def process_order_data(orders):
    if not orders:
        raise ValueError("Empty order list")
    return len(orders)

orders = [{"order_id": 101, "total": 1999.98}, {"order_id": 102, "total": 49.99}]
processed = process_order_data(orders)
print("Processed:", processed, "orders")

# %% Project 6: Discount Decorator
# Difficulty: Intermediate
# Description: Create a decorator to apply a dynamic discount rate.
# Objective: Practice decorators with arguments.
# Tasks:
# - Define a decorator factory for a 15% discount.
# - Apply to a function that sums item prices.
# Expected Output: Discounted total: 849.99
def discount_decorator(discount_rate):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_total = func(*args, **kwargs)
            return round(original_total * (1 - discount_rate), 2)
        return wrapper
    return decorator

@discount_decorator(0.15)
def sum_items(items):
    return sum(items)

total = sum_items([999.99])
print("Discounted total:", total)

# %% Project 7: Timing Decorator
# Difficulty: Intermediate
# Description: Create a decorator to measure function execution time.
# Objective: Practice performance monitoring.
# Tasks:
# - Define a decorator to log execution time.
# - Apply to a function that simulates stock updates.
# Expected Output: update_stock took 0.30 seconds
#                 Updated: 3 items
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
def update_stock(items):
    for _ in items:
        time.sleep(0.1)
    return len(items)

items = ["Mouse", "Keyboard", "Monitor"]
updated = update_stock(items)
print("Updated:", updated, "items")

# %% Project 8: Authorization Decorator
# Difficulty: Intermediate
# Description: Create a decorator to check user authorization.
# Objective: Practice conditional execution.
# Tasks:
# - Define a decorator to check if user is "admin".
# - Apply to a function that generates sales reports.
# Expected Output: Authorized: Sales report generated
def authorization_decorator(func):
    def wrapper(*args, user_role="guest", **kwargs):
        if user_role != "admin":
            raise PermissionError("Unauthorized access")
        return func(*args, **kwargs)
    return wrapper

@authorization_decorator
def generate_sales_report(sales):
    return "Sales report generated"

report = generate_sales_report([1000.00, 500.00], user_role="admin")
print("Authorized:", report)

# %% Project 9: Cache Decorator
# Difficulty: Advanced
# Description: Create a decorator to cache function results.
# Objective: Practice memoization with decorators.
# Tasks:
# - Define a decorator to cache results based on arguments.
# - Apply to a function that calculates product margins.
# Expected Output: Margin: 300.00 (cached on second call)
def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache_decorator
def calculate_margin(price, cost):
    return price - cost

margin = calculate_margin(999.99, 699.99)
print("Margin:", margin)
margin = calculate_margin(999.99, 699.99)  # Cached
print("Margin:", margin)

# %% Project 10: Comprehensive Retail Decorator
# Difficulty: Advanced
# Description: Create a decorator to log, time, and validate retail order processing.
# Objective: Practice stacking multiple decorators.
# Tasks:
# - Combine logging, timing, and positive input validation in one decorator stack.
# - Apply to a function that processes order totals.
# Expected Output: Calling process_order_totals with args: ([1000.00, 500.00],)
#                 process_order_totals took 0.20 seconds
#                 Total: 1500.00
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

def positive_input_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, list) and any(x <= 0 for x in arg if isinstance(x, (int, float))):
                raise ValueError("Order totals must be positive")
        return func(*args, **kwargs)
    return wrapper

@logging_decorator
@timing_decorator
@positive_input_decorator
def process_order_totals(totals):
    time.sleep(0.2)  # Simulate processing
    return sum(totals)

total = process_order_totals([1000.00, 500.00])
print("Total:", total)