# Python Modules and Packages: Importing Modules

# Purpose: Importing modules allows reusing code from Python's standard library or third-party packages.
# Key Features: Access functions, classes, and variables defined in other files.

# 1. Basic Import
# Explanation: Use 'import' to access a module's contents.
# Example:
import math

price = 49.99
rounded_price = math.ceil(price)
print(f"Rounded price: ${rounded_price:.2f}")
# Output: Rounded price: $50.00

# 2. Importing Specific Items
# Explanation: Use 'from module import item' to import specific functions or classes.
# Example:
from random import randint

# Simulate random stock levels for a product
stock = randint(10, 100)
print(f"Random stock level: {stock}")
# Output: Random stock level: (random number between 10 and 100)

# 3. Using Aliases and Retail Scenario
# Explanation: Use 'import as' for shorter names; apply to retail data processing.
# Example:
import datetime as dt

# Record order timestamp
order_time = dt.datetime.now()
print(f"Order placed at: {order_time.strftime('%Y-%m-%d %H:%M:%S')}")
# Output: Order placed at: 2025-04-19 HH:MM:SS (current time)

# Exercise 1: Import math module and use floor() to round down a price.
# Solution:
# import math
# price = 29.99
# floored_price = math.floor(price)
# print("Exercise 1 - Floored price:", floored_price)
# # Output: Floored price: 29

# Exercise 2: Import random and use choice() to select a random product.
# Solution:
# from random import choice
# products = ["Laptop", "Smartphone", "Coffee Maker"]
# selected_product = choice(products)
# print("Exercise 2 - Random product:", selected_product)
# # Output: Random product: (random item from list)

# Exercise 3: Import datetime and print the current year.
# Solution:
# import datetime
# current_year = datetime.datetime.now().year
# print("Exercise 3 - Current year:", current_year)
# # Output: Current year: 2025

# Notes:
# - Use imports to leverage Python’s standard library or third-party packages in ML (e.g., NumPy) or web apps (e.g., Flask).
# - Avoid 'from module import *' to prevent namespace pollution.
# - Modules are loaded once per session, improving performance.