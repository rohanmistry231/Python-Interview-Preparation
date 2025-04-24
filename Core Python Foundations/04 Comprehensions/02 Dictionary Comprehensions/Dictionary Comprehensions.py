# Python Comprehensions: Dictionary Comprehensions

# Purpose: Dictionary comprehensions create dictionaries concisely using a single line.
# Key Features: Generates key-value pairs, supports conditionals.

# 1. Basic Dictionary Comprehension
# Explanation: Create a dictionary using {key_expr: value_expr for item in iterable}.
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker"]
product_ids = {name: idx + 1 for idx, name in enumerate(products)}
print("Product IDs:", product_ids)
# Output: Product IDs: {'Laptop': 1, 'Smartphone': 2, 'Coffee Maker': 3}

# 2. Dictionary Comprehension with Condition
# Explanation: Filter items with [key_expr: value_expr for item in iterable if condition].
# Example:
prices = {"Laptop": 999.99, "Smartphone": 699.99, "Coffee Maker": 49.99}
expensive_items = {name: price for name, price in prices.items() if price > 500}
print("Expensive items:", expensive_items)
# Output: Expensive items: {'Laptop': 999.99, 'Smartphone': 699.99}

# 3. Transforming Keys or Values
# Explanation: Modify keys or values during creation (e.g., formatting, calculations).
# Example:
stock = {"Laptop": 50, "Smartphone": 100, "Blender": 20}
stock_status = {f"{name}_stock": "Low" if qty < 50 else "Sufficient" for name, qty in stock.items()}
print("Stock status:", stock_status)
# Output: Stock status: {'Laptop_stock': 'Sufficient', 'Smartphone_stock': 'Sufficient', 'Blender_stock': 'Low'}

# Exercise 1: Create a dictionary comprehension mapping product names to their lengths.
# Solution:
# items = ["Mouse", "Keyboard", "Monitor"]
# name_lengths = {item: len(item) for item in items}
# print("Exercise 1 - Name lengths:", name_lengths)
# # Output: Name lengths: {'Mouse': 5, 'Keyboard': 8, 'Monitor': 7}

# Exercise 2: Use a dictionary comprehension to filter products with stock below 30 from a stock dictionary.
# Solution:
# stock_levels = {"Mouse": 25, "Keyboard": 50, "Monitor": 10}
# low_stock = {name: qty for name, qty in stock_levels.items() if qty < 30}
# print("Exercise 2 - Low stock:", low_stock)
# # Output: Low stock: {'Mouse': 25, 'Monitor': 10}

# Exercise 3: Create a dictionary comprehension to map product names to discounted prices (10% off).
# Solution:
# prices = {"Laptop": 1000, "Smartphone": 700}
# discounted_prices = {name: price * 0.9 for name, price in prices.items()}
# print("Exercise 3 - Discounted prices:", discounted_prices)
# # Output: Discounted prices: {'Laptop': 900.0, 'Smartphone': 630.0}

# Notes:
# - Dictionary comprehensions are efficient for creating key-value mappings in ML (e.g., feature dictionaries) or web apps (e.g., API responses).
# - Ensure keys are unique and hashable (e.g., strings, numbers, tuples).
# - Use sparingly for complex logic to maintain readability.