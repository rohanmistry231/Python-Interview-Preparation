# %% Purpose
# Python Comprehensions: Set Comprehensions
# Purpose: Set comprehensions create sets concisely, ensuring unique elements.
# Key Features: Eliminates duplicates, supports conditionals.

# %% 1. Basic Set Comprehension
# Explanation: Create a set using {expression for item in iterable}.
# Example:
products = ["Laptop", "Smartphone", "Laptop", "Coffee Maker"]
unique_products = {product for product in products}
print("Unique products:", unique_products)
# Output: Unique products: {'Laptop', 'Smartphone', 'Coffee Maker'}

# %% 2. Set Comprehension with Condition
# Explanation: Filter items with {expression for item in iterable if condition}.
# Example:
prices = [100, 200, 150, 999.99, 200]
high_prices = {price for price in prices if price > 500}
print("High prices:", high_prices)
# Output: High prices: {999.99}

# %% 3. Transforming Elements
# Explanation: Apply transformations to elements during set creation.
# Example:
categories = ["Electronics", "Appliances", "Electronics", "Furniture"]
upper_categories = {cat.upper() for cat in categories}
print("Uppercase categories:", upper_categories)
# Output: Uppercase categories: {'ELECTRONICS', 'APPLIANCES', 'FURNITURE'}

# %% Notes
# Notes:
# - Set comprehensions automatically remove duplicates, useful in ML for unique labels or web apps for unique tags.
# - Sets are unordered; use lists if order matters.
# - Keep comprehensions simple to avoid readability issues.