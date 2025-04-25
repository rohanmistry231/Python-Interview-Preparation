# %% Purpose
# Python Comprehensions: List Comprehensions
# Purpose: List comprehensions provide a concise way to create lists using a single line of code.
# Key Features: Compact syntax, readable, combines loops and conditionals.

# %% 1. Basic List Comprehension
# Explanation: Create a list from an iterable using [expression for item in iterable].
# Example:
prices = [100, 200, 300, 400]
discounted_prices = [price * 0.9 for price in prices]
print("Discounted prices:", discounted_prices)
# Output: Discounted prices: [90.0, 180.0, 270.0, 360.0]

# %% 2. List Comprehension with Condition
# Explanation: Include only items meeting a condition using [expression for item in iterable if condition].
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker", "Blender"]
electronics = [product for product in products if "phone" in product.lower() or "laptop" in product.lower()]
print("Electronics products:", electronics)
# Output: Electronics products: ['Laptop', 'Smartphone']

# %% 3. Nested List Comprehension
# Explanation: Use nested loops within a comprehension for complex transformations.
# Example:
categories = ["Electronics", "Appliances"]
items = ["Laptop", "Blender"]
product_pairs = [f"{item} ({cat})" for cat in categories for item in items]
print("Product pairs:", product_pairs)
# Output: Product pairs: ['Laptop (Electronics)', 'Blender (Electronics)', 'Laptop (Appliances)', 'Blender (Appliances)']

# %% Notes
# Notes:
# - List comprehensions are faster than equivalent for loops but can reduce readability if overused.
# - Use in ML for data preprocessing (e.g., filtering features) or web apps for generating lists (e.g., product displays).
# - Avoid complex nested comprehensions; use regular loops for clarity if needed.