# Python Control Flow: For Loops

# Purpose: For loops iterate over a sequence (e.g., list, tuple, string).
# Key Features: Simplifies repetitive tasks over iterable objects.

# 1. Basic For Loop
# Explanation: Iterate over elements in a sequence.
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker"]
for product in products:
    print("Product:", product)
# Output: Product: Laptop, Product: Smartphone, Product: Coffee Maker

# 2. Using range()
# Explanation: Generate numbers for iteration with range().
# Example:
for i in range(5):
    print(f"Item {i + 1}")
# Output: Item 1, Item 2, ..., Item 5

# 3. Iterating Over Dictionaries
# Explanation: Loop over keys, values, or items in a dictionary.
# Example:
product = {"name": "Laptop Pro", "price": 999.99, "stock": 50}
for key, value in product.items():
    print(f"{key}: {value}")
# Output: name: Laptop Pro, price: 999.99, stock: 50

# Exercise 1: Loop over a list of prices and print each with a 10% discount.
# Solution:
# prices = [100, 200, 300]
# for price in prices:
#     discounted = price * 0.9
#     print("Exercise 1 - Discounted price:", discounted)
# # Output: 90.0, 180.0, 270.0

# Exercise 2: Use range() to print the first 5 even numbers.
# Solution:
# for i in range(2, 11, 2):
#     print("Exercise 2 - Even number:", i)
# # Output: 2, 4, 6, 8, 10

# Exercise 3: Iterate over a dictionary of product details and print keys in uppercase.
# Solution:
# item = {"id": 1, "name": "Smartphone", "category": "Electronics"}
# for key in item:
#     print("Exercise 3 - Uppercase key:", key.upper())
# # Output: ID, NAME, CATEGORY

# Notes:
# - For loops are ideal for iterating over datasets in ML (e.g., processing features) or web apps (e.g., rendering lists).
# - Use enumerate() for index-element pairs (e.g., for i, item in enumerate(products)).
# - Avoid modifying lists during iteration to prevent errors.