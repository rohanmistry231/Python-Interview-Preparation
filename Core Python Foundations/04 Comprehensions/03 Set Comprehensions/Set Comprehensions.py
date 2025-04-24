# Python Comprehensions: Set Comprehensions

# Purpose: Set comprehensions create sets concisely, ensuring unique elements.
# Key Features: Eliminates duplicates, supports conditionals.

# 1. Basic Set Comprehension
# Explanation: Create a set using {expression for item in iterable}.
# Example:
products = ["Laptop", "Smartphone", "Laptop", "Coffee Maker"]
unique_products = {product for product in products}
print("Unique products:", unique_products)
# Output: Unique products: {'Laptop', 'Smartphone', 'Coffee Maker'}

# 2. Set Comprehension with Condition
# Explanation: Filter items with {expression for item in iterable if condition}.
# Example:
prices = [100, 200, 150, 999.99, 200]
high_prices = {price for price in prices if price > 500}
print("High prices:", high_prices)
# Output: High prices: {999.99}

# 3. Transforming Elements
# Explanation: Apply transformations to elements during set creation.
# Example:
categories = ["Electronics", "Appliances", "Electronics", "Furniture"]
upper_categories = {cat.upper() for cat in categories}
print("Uppercase categories:", upper_categories)
# Output: Uppercase categories: {'ELECTRONICS', 'APPLIANCES', 'FURNITURE'}

# Exercise 1: Create a set comprehension to extract unique product categories from a list with duplicates.
# Solution:
# cats = ["Electronics", "Appliances", "Electronics", "Clothing"]
# unique_cats = {cat for cat in cats}
# print("Exercise 1 - Unique categories:", unique_cats)
# # Output: Unique categories: {'Electronics', 'Appliances', 'Clothing'}

# Exercise 2: Use a set comprehension to collect quantities above 50 from a list of quantities.
# Solution:
# quantities = [10, 60, 20, 75, 60]
# high_quantities = {qty for qty in quantities if qty > 50}
# print("Exercise 2 - High quantities:", high_quantities)
# # Output: High quantities: {60, 75}

# Exercise 3: Create a set comprehension to convert product names to lowercase.
# Solution:
# products = ["Laptop", "SMARTPHONE", "Coffee Maker"]
# lower_products = {name.lower() for name in products}
# print("Exercise 3 - Lowercase products:", lower_products)
# # Output: Lowercase products: {'laptop', 'smartphone', 'coffee maker'}

# Notes:
# - Set comprehensions automatically remove duplicates, useful in ML for unique labels or web apps for unique tags.
# - Sets are unordered; use lists if order matters.
# - Keep comprehensions simple to avoid readability issues.