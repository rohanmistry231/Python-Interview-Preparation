# Python Comprehensions: List Comprehensions

# Purpose: List comprehensions provide a concise way to create lists using a single line of code.
# Key Features: Compact syntax, readable, combines loops and conditionals.

# 1. Basic List Comprehension
# Explanation: Create a list from an iterable using [expression for item in iterable].
# Example:
prices = [100, 200, 300, 400]
discounted_prices = [price * 0.9 for price in prices]
print("Discounted prices:", discounted_prices)
# Output: Discounted prices: [90.0, 180.0, 270.0, 360.0]

# 2. List Comprehension with Condition
# Explanation: Include only items meeting a condition using [expression for item in iterable if condition].
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker", "Blender"]
electronics = [product for product in products if "phone" in product.lower() or "laptop" in product.lower()]
print("Electronics products:", electronics)
# Output: Electronics products: ['Laptop', 'Smartphone']

# 3. Nested List Comprehension
# Explanation: Use nested loops within a comprehension for complex transformations.
# Example:
categories = ["Electronics", "Appliances"]
items = ["Laptop", "Blender"]
product_pairs = [f"{item} ({cat})" for cat in categories for item in items]
print("Product pairs:", product_pairs)
# Output: Product pairs: ['Laptop (Electronics)', 'Blender (Electronics)', 'Laptop (Appliances)', 'Blender (Appliances)']

# Exercise 1: Create a list comprehension to double the quantities in a list of quantities.
# Solution:
# quantities = [10, 20, 30, 40]
# doubled_quantities = [qty * 2 for qty in quantities]
# print("Exercise 1 - Doubled quantities:", doubled_quantities)
# # Output: Doubled quantities: [20, 40, 60, 80]

# Exercise 2: Use a list comprehension to extract products with prices above 200 from a list of price tuples.
# Solution:
# product_prices = [("Laptop", 999.99), ("Coffee Maker", 49.99), ("Smartphone", 699.99)]
# expensive_products = [name for name, price in product_prices if price > 200]
# print("Exercise 2 - Expensive products:", expensive_products)
# # Output: Expensive products: ['Laptop', 'Smartphone']

# Exercise 3: Create a nested list comprehension to generate a list of product-category combinations for Electronics only.
# Solution:
# products = ["Mouse", "Keyboard"]
# categories = ["Electronics", "Appliances"]
# electronics_pairs = [f"{p} in {c}" for c in categories if c == "Electronics" for p in products]
# print("Exercise 3 - Electronics pairs:", electronics_pairs)
# # Output: Electronics pairs: ['Mouse in Electronics', 'Keyboard in Electronics']

# Notes:
# - List comprehensions are faster than equivalent for loops but can reduce readability if overused.
# - Use in ML for data preprocessing (e.g., filtering features) or web apps for generating lists (e.g., product displays).
# - Avoid complex nested comprehensions; use regular loops for clarity if needed.