# Python Data Structures: Tuples

# Purpose: Tuples are ordered, immutable collections that allow duplicates.
# Key Features: Lightweight, hashable, used for fixed data.

# 1. Creating and Accessing Tuples
# Explanation: Tuples use parentheses (), elements can be mixed types.
# Example:
order = (101, "Laptop Pro", 2, 1999.98)
print("Tuple:", order)
print("Order ID:", order[0])  # Access by index
print("Slice [1:3]:", order[1:3])  # Slicing
print("Last item:", order[-1])  # Negative indexing

# 2. Tuple Operations
# Explanation: Tuples support concatenation, repetition, and membership tests.
# Example:
items = ("Mouse", "Keyboard")
combined = order + items  # Concatenation
print("Combined tuple:", combined)
repeated = items * 2  # Repetition
print("Repeated tuple:", repeated)
print("Is 'Laptop Pro' in tuple?:", "Laptop Pro" in order)

# 3. Tuple Methods
# Explanation: Limited methods (count(), index()) due to immutability.
# Example:
print("Count of 2:", order.count(2))
print("Index of 'Laptop Pro':", order.index("Laptop Pro"))

# 4. Tuple Unpacking
# Explanation: Assign tuple elements to variables directly.
# Example:
order_id, product, quantity, total = order
print("Unpacked - ID:", order_id, "Product:", product, "Quantity:", quantity, "Total:", total)

# Exercise 1: Create a tuple of 4 product details, access the third item, and print its length.
# Solution:
# product = (1, "Smartphone", 699.99, 100)
# third_item = product[2]
# print("Exercise 1 - Third item:", third_item, "Length:", len(product))

# Exercise 2: Concatenate two tuples (product info and stock) and check for an item’s presence.
# Solution:
# stock = (50, 20)
# combined = product + stock
# print("Exercise 2 - Combined:", combined, "Is 699.99 in tuple?:", 699.99 in combined)

# Exercise 3: Unpack a tuple of order details and print the variables.
# Solution:
# order_details = (102, "Coffee Maker", 3, 149.97)
# o_id, o_product, o_qty, o_total = order_details
# print("Exercise 3 - Unpacked: ID:", o_id, "Product:", o_product, "Qty:", o_qty, "Total:", o_total)

# Notes:
# - Tuples are immutable, making them suitable for fixed data (e.g., ML dataset coordinates, web app constants).
# - Tuples are hashable, usable as dictionary keys.
# - Use tuples for memory efficiency over lists when data won’t change.