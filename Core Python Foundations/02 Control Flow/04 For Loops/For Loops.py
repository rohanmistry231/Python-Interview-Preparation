# Python Control Flow: For Loops
# Purpose: Learn For Loops to iterate over sequences (lists, tuples, strings, etc.).
# Key Features: Simplifies repetitive tasks over iterable objects.

# %% 1. Basic For Loop
# Explanation: Iterate over each element in a sequence, executing the loop body.
# Ideal for processing collections.
products = ["Laptop", "Smartphone", "Coffee Maker"]
for product in products:
    print("1.1 Product:", product)
# Example with string
word = "Python"
for char in word:
    print("1.2 Character:", char)

# Mini-Exercise: Loop over a list of numbers and print each doubled.
numbers = [1, 2, 3]
for num in numbers:
    print("1.3 Mini-Exercise: Doubled:", num * 2)

# %% 2. Using range()
# Explanation: Generate numbers with range(start, stop, step) for controlled iteration.
# Common for indexed operations or counters.
for i in range(5):
    print(f"1.1 Item {i + 1}")
# Example with step
for i in range(0, 10, 2):
    print(f"1.2 Even number {i}")

# Mini-Exercise: Print numbers from 1 to 3 using range().
for i in range(1, 4):
    print("2.3 Mini-Exercise: Number:", i)

# %% 3. Iterating Over Dictionaries
# Explanation: Loop over keys, values, or key-value pairs using .keys(), .values(), or .items().
# Useful for processing structured data.
product = {"name": "Laptop Pro", "price": 999.99, "stock": 50}
for key, value in product.items():
    print(f"3.1 {key}: {value}")
# Example with keys only
for key in product:
    print(f"3.2 Key: {key}")

# Mini-Exercise: Loop over a dictionary’s values and print each.
for value in product.values():
    print("3.3 Mini-Exercise: Value:", value)

# %% 4. Exercises for Practice
# Exercise 1: Loop over a list of prices and print each with a 10% discount.
prices = [100, 200, 300]
for price in prices:
    discounted = price * 0.9
    print("4.1 Exercise 1 - Discounted price:", discounted)

# Exercise 2: Use range() to print the first 5 even numbers.
for i in range(2, 11, 2):
    print("4.2 Exercise 2 - Even number:", i)

# Exercise 3: Iterate over a dictionary of product details and print keys in uppercase.
item = {"id": 1, "name": "Smartphone", "category": "Electronics"}
for key in item:
    print("4.3 Exercise 3 - Uppercase key:", key.upper())

# Exercise 4: Loop over a list of products and print only those starting with 'S'.
items = ["Smartphone", "Laptop", "Speaker", "Blender"]
for item in items:
    if item.startswith("S"):
        print("4.4 Exercise 4 - Product starting with S:", item)

# %% 5. Notes for Further Learning
# - For loops are ideal for iterating over datasets in ML (e.g., feature processing) or web apps (e.g., rendering lists).
# - Use enumerate() for index-element pairs (e.g., for i, item in enumerate(products)).
# - Avoid modifying lists during iteration to prevent errors; use list comprehension for transformations.
# - Combine with conditionals or break/continue for advanced control.
# - Try the projects below to apply these concepts!