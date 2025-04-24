# Python Modules and Packages: Packages

# Purpose: Packages organize related modules into a directory with an __init__.py file.
# Key Features: Hierarchical structure, namespace management.

# Note: This file simulates a package structure. In practice, create a directory with __init__.py.

# Simulated Package Structure
"""
retail_package/
    __init__.py
    products.py
    orders.py
"""
"""
# retail_package/products.py
def calculate_discount(price, rate):
    return price * (1 - rate)
"""
"""
# retail_package/orders.py
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
"""
"""
# retail_package/__init__.py
# (Empty or with imports)
"""

# 1. Importing from a Package
# Explanation: Use dot notation to access modules in a package.
# Example:
try:
    from retail_package import products
    price = 999.99
    discounted = products.calculate_discount(price, 0.1)
    print(f"Discounted price: ${discounted:.2f}")
except ImportError:
    print("Error: retail_package not found (simulated)")
# Output: Discounted price: $899.99 (if package exists)

# 2. Using Package Modules
# Explanation: Import specific modules or classes from a package.
# Example:
try:
    from retail_package import orders
    order = orders.Order(101, 1999.98)
    print(f"Order: {order.order_id}, Total: ${order.total:.2f}")
except ImportError:
    print("Error: retail_package not found (simulated)")
# Output: Order: 101, Total: $1999.98 (if package exists)

# 3. Retail Scenario with Package
# Explanation: Use a package to manage retail operations.
# Example:
try:
    from retail_package.products import calculate_discount
    from retail_package.orders import Order
    product = {"name": "Laptop", "price": 999.99}
    order = Order(102, calculate_discount(product["price"], 0.05))
    print(f"Order {order.order_id}: Total ${order.total:.2f}")
except ImportError:
    print("Error: retail_package not found (simulated)")
# Output: Order 102: Total $949.99 (if package exists)

# Exercise 1: Import a function from a simulated package module to format price.
# Solution:
"""
# retail_package/utils.py
def format_price(price):
    return f"${price:.2f}"
"""
# try:
#     from retail_package.utils import format_price
#     price = 49.99
#     formatted = format_price(price)
#     print("Exercise 1 - Formatted price:", formatted)
# except ImportError:
#     print("Exercise 1 - Error: retail_package.utils not found (simulated)")
# # Output: Formatted price: $49.99 (if package exists)

# Exercise 2: Create and use a class from a package module.
# Solution:
"""
# retail_package/customers.py
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
"""
# try:
#     from retail_package.customers import Customer
#     customer = Customer("Alice", "alice@example.com")
#     print("Exercise 2 - Customer:", customer.name, customer.email)
# except ImportError:
#     print("Exercise 2 - Error: retail_package.customers not found (simulated)")
# # Output: Customer: Alice alice@example.com (if package exists)

# Exercise 3: Use multiple modules from a package for a retail task.
# Solution:
"""
# retail_package/stock.py
def check_stock(stock):
    return "Low" if stock < 50 else "Sufficient"
"""
# try:
#     from retail_package.products import calculate_discount
#     from retail_package.stock import check_stock
#     product = {"price": 699.99, "stock": 30}
#     discounted = calculate_discount(product["price"], 0.1)
#     status = check_stock(product["stock"])
#     print("Exercise 3 - Discounted:", discounted, "Stock:", status)
# except ImportError:
#     print("Exercise 3 - Error: retail_package not found (simulated)")
# # Output: Discounted: 629.991 Stock: Low (if package exists)

# Notes:
# - Packages require an __init__.py file (can be empty) to be recognized.
# - Use in ML for organizing large projects (e.g., data preprocessing packages) or web apps for modular APIs.
# - Handle ImportError for missing packages, especially with third-party dependencies.