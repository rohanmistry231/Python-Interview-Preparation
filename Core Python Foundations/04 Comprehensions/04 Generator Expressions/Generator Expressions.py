# %% Purpose
# Python Comprehensions: Generator Expressions
# Purpose: Generator expressions create iterators lazily, yielding items one at a time.
# Key Features: Memory-efficient, single-use iteration.

# %% 1. Basic Generator Expression
# Explanation: Use (expression for item in iterable) to create a generator.
# Example:
prices = [100, 200, 300, 400]
discounted_gen = (price * 0.9 for price in prices)
print("Generator object:", discounted_gen)
# Convert to list for display
discounted_list = list(discounted_gen)
print("Discounted prices:", discounted_list)
# Output: Generator object: <generator object ...>, Discounted prices: [90.0, 180.0, 270.0, 360.0]

# %% 2. Generator with Condition
# Explanation: Filter items with (expression for item in iterable if condition).
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker", "Blender"]
electronics_gen = (product for product in products if "phone" in product.lower() or "laptop" in product.lower())
print("Electronics (generator):", list(electronics_gen))
# Output: Electronics (generator): ['Laptop', 'Smartphone']

# %% 3. Using Generators in Loops
# Explanation: Iterate over a generator directly to save memory.
# Example:
quantities = [10, 20, 30, 40]
stock_gen = (qty * 2 for qty in quantities)
for doubled_qty in stock_gen:
    print(f"Doubled quantity: {doubled_qty}")
# Output: Doubled quantity: 20, Doubled quantity: 40, Doubled quantity: 60, Doubled quantity: 80

# %% Notes
# Notes:
# - Generators are memory-efficient for large datasets in ML (e.g., streaming data) or web apps (e.g., lazy API responses).
# - Generators are single-use; convert to list if multiple iterations are needed.
# - Use parentheses () for generator expressions, unlike [] for list comprehensions.