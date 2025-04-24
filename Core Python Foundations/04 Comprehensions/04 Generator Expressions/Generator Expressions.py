# Python Comprehensions: Generator Expressions

# Purpose: Generator expressions create iterators lazily, yielding items one at a time.
# Key Features: Memory-efficient, single-use iteration.

# 1. Basic Generator Expression
# Explanation: Use (expression for item in iterable) to create a generator.
# Example:
prices = [100, 200, 300, 400]
discounted_gen = (price * 0.9 for price in prices)
print("Generator object:", discounted_gen)
# Convert to list for display
discounted_list = list(discounted_gen)
print("Discounted prices:", discounted_list)
# Output: Generator object: <generator object ...>, Discounted prices: [90.0, 180.0, 270.0, 360.0]

# 2. Generator with Condition
# Explanation: Filter items with (expression for item in iterable if condition).
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker", "Blender"]
electronics_gen = (product for product in products if "phone" in product.lower() or "laptop" in product.lower())
print("Electronics (generator):", list(electronics_gen))
# Output: Electronics (generator): ['Laptop', 'Smartphone']

# 3. Using Generators in Loops
# Explanation: Iterate over a generator directly to save memory.
# Example:
quantities = [10, 20, 30, 40]
stock_gen = (qty * 2 for qty in quantities)
for doubled_qty in stock_gen:
    print(f"Doubled quantity: {doubled_qty}")
# Output: Doubled quantity: 20, Doubled quantity: 40, Doubled quantity: 60, Doubled quantity: 80

# Exercise 1: Create a generator expression to yield squares of quantities.
# Solution:
# quantities = [5, 10, 15]
# squares_gen = (qty ** 2 for qty in quantities)
# print("Exercise 1 - Squared quantities:", list(squares_gen))
# # Output: Squared quantities: [25, 100, 225]

# Exercise 2: Use a generator expression to yield product names longer than 6 characters.
# Solution:
# products = ["Mouse", "Keyboard", "Monitor"]
# long_names_gen = (name for name in products if len(name) > 6)
# print("Exercise 2 - Long names:", list(long_names_gen))
# # Output: Long names: ['Keyboard']

# Exercise 3: Iterate over a generator expression for prices above 200 directly in a loop.
# Solution:
# prices = [100, 300, 50, 400]
# high_prices_gen = (price for price in prices if price > 200)
# for price in high_prices_gen:
#     print("Exercise 3 - High price:", price)
# # Output: High price: 300, High price: 400

# Notes:
# - Generators are memory-efficient for large datasets in ML (e.g., streaming data) or web apps (e.g., lazy API responses).
# - Generators are single-use; convert to list if multiple iterations are needed.
# - Use parentheses () for generator expressions, unlike [] for list comprehensions.