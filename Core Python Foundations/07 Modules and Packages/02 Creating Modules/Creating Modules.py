# Python Modules and Packages: Creating Modules

# Purpose: Creating modules organizes code into reusable files.
# Key Features: Encapsulates functions, classes, or variables in a .py file.

# Note: This file demonstrates creating and using a module. In practice, the module would be a separate .py file.

# Simulated Module Content (e.g., retail_utils.py)
"""
# retail_utils.py
def calculate_discount(price, rate):
    return price * (1 - rate)

def check_stock(stock):
    return "Low" if stock < 50 else "Sufficient"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
"""

# 1. Importing a Custom Module
# Explanation: Import a module from the same directory.
# Example:
# Assuming retail_utils.py exists
try:
    import retail_utils
    price = 999.99
    discounted_price = retail_utils.calculate_discount(price, 0.1)
    print(f"Discounted price: ${discounted_price:.2f}")
except ImportError:
    print("Error: retail_utils module not found (simulated)")
# Output: Discounted price: $899.99 (if module exists)

# 2. Using Module Functions and Classes
# Explanation: Access module contents like functions or classes.
# Example:
try:
    import retail_utils
    stock = 30
    status = retail_utils.check_stock(stock)
    print(f"Stock status: {status}")
    product = retail_utils.Product("Laptop", 999.99)
    print(f"Product: {product.name}, Price: ${product.price:.2f}")
except ImportError:
    print("Error: retail_utils module not found (simulated)")
# Output: Stock status: Low
#         Product: Laptop, Price: $999.99 (if module exists)

# 3. Retail Scenario with Custom Module
# Explanation: Use a module for retail calculations.
# Example:
try:
    import retail_utils
    order = {"name": "Smartphone", "price": 699.99, "stock": 100}
    discounted = retail_utils.calculate_discount(order["price"], 0.05)
    stock_status = retail_utils.check_stock(order["stock"])
    print(f"Order: {order['name']}, Discounted: ${discounted:.2f}, Stock: {stock_status}")
except ImportError:
    print("Error: retail_utils module not found (simulated)")
# Output: Order: Smartphone, Discounted: $664.99, Stock: Sufficient (if module exists)

# Exercise 1: Create and use a function from a simulated module to format price.
# Solution:
"""
# price_utils.py
def format_price(price):
    return f"${price:.2f}"
"""
# try:
#     import price_utils
#     price = 49.99
#     formatted = price_utils.format_price(price)
#     print("Exercise 1 - Formatted price:", formatted)
# except ImportError:
#     print("Exercise 1 - Error: price_utils module not found (simulated)")
# # Output: Formatted price: $49.99 (if module exists)

# Exercise 2: Use a class from a simulated module to create an Order object.
# Solution:
"""
# order_utils.py
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
"""
# try:
#     import order_utils
#     order = order_utils.Order(101, 999.99)
#     print("Exercise 2 - Order:", order.order_id, order.total)
# except ImportError:
#     print("Exercise 2 - Error: order_utils module not found (simulated)")
# # Output: Order: 101 999.99 (if module exists)

# Exercise 3: Use a function from a simulated module to validate stock.
# Solution:
"""
# stock_utils.py
def validate_stock(stock):
    return stock >= 0
"""
# try:
#     import stock_utils
#     stock = 20
#     valid = stock_utils.validate_stock(stock)
#     print("Exercise 3 - Stock valid:", valid)
# except ImportError:
#     print("Exercise 3 - Error: stock_utils module not found (simulated)")
# # Output: Stock valid: True (if module exists)

# Notes:
# - Save module code in a separate .py file in the same directory or a package.
# - Use in ML for organizing data preprocessing (e.g., feature engineering modules) or web apps for utilities (e.g., API helpers).
# - Handle ImportError for robust code, especially in production.