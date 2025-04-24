# Python Data Structures: Strings

# Purpose: Strings are immutable sequences of characters.
# Key Features: Text manipulation, formatting, and methods.

# 1. Creating and Accessing Strings
# Explanation: Strings use single ('') or double ("") quotes, support indexing/slicing.
# Example:
product_name = "Laptop Pro"
print("String:", product_name)
print("First char:", product_name[0])  # Indexing
print("Slice [0:6]:", product_name[0:6])  # Slicing
print("Last char:", product_name[-1])  # Negative indexing

# 2. String Operations
# Explanation: Concatenation, repetition, membership, and length.
# Example:
category = "Electronics"
combined = product_name + " - " + category  # Concatenation
print("Concatenated:", combined)
repeated = product_name * 2  # Repetition
print("Repeated:", repeated)
print("Is 'Pro' in string?:", "Pro" in product_name)
print("Length:", len(product_name))

# 3. String Methods
# Explanation: Methods like upper(), lower(), strip(), replace(), split(), join().
# Example:
print("Uppercase:", product_name.upper())
print("Lowercase:", product_name.lower())
print("Stripped spaces:", "  Laptop  ".strip())
print("Replaced:", product_name.replace("Pro", "Elite"))
print("Split:", product_name.split(" "))  # Split into list
items = ["Laptop", "Smartphone"]
print("Joined:", ", ".join(items))  # Join list into string

# 4. String Formatting
# Explanation: Format strings using %, .format(), or f-strings.
# Example:
price = 999.99
print("Product: %s, Price: $%.2f" % (product_name, price))  # % formatting
print("Product: {}, Price: ${:.2f}".format(product_name, price))  # .format()
print(f"Product: {product_name}, Price: ${price:.2f}")  # f-string

# Exercise 1: Create a string for a product name, convert it to uppercase, and slice the first 3 characters.
# Solution:
# name = "Smartphone X"
# upper_name = name.upper()
# first_three = name[:3]
# print("Exercise 1 - Uppercase:", upper_name, "First 3 chars:", first_three)

# Exercise 2: Join a list of categories into a string and replace one word.
# Solution:
# cats = ["Electronics", "Appliances"]
# joined = ", ".join(cats)
# replaced = joined.replace("Appliances", "Home Goods")
# print("Exercise 2 - Joined and replaced:", replaced)

# Exercise 3: Format a string with product name and price using an f-string.
# Solution:
# prod = "Coffee Maker"
# cost = 49.99
# formatted = f"Item: {prod}, Cost: ${cost:.2f}"
# print("Exercise 3 - Formatted:", formatted)

# Notes:
# - Strings are immutable; methods return new strings.
# - Use f-strings for modern, readable formatting (Python 3.6+).
# - Common in ML (text preprocessing) and web apps (user input handling).