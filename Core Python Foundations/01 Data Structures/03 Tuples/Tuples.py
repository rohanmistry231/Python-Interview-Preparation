# Python Data Structures: Tuples
# Purpose: Learn Tuples, ordered, immutable collections that allow duplicates.
# Key Features: Lightweight, hashable, memory-efficient, ideal for fixed data.

# %% 1. Creating and Accessing Tuples
# Explanation: Tuples are defined with parentheses () or commas. Elements can be of any type.
# Access items using zero-based indexing or slicing. Negative indices count from the end.
order = (101, "Laptop Pro", 2, 1999.98)
print("1.1 Tuple:", order)
print("1.2 Order ID (index 0):", order[0])  # Access by index
print("1.3 Last item (index -1):", order[-1])  # Negative indexing
print("1.4 Slice (items 1 to 2):", order[1:3])  # Slicing
print("1.5 Length of tuple:", len(order))  # Get tuple length

# Mini-Exercise: Create a tuple of 3 coordinates and print the second coordinate.
coords = (10, 20, 30)
print("1.6 Mini-Exercise: Second coordinate:", coords[1])

# %% 2. Tuple Operations
# Explanation: Tuples support concatenation (+), repetition (*), and membership tests (in).
# Tuples are immutable, so operations create new tuples rather than modifying the original.
items = ("Mouse", "Keyboard")
combined = order + items  # Concatenate tuples
print("2.1 Combined tuple:", combined)
repeated = items * 2  # Repeat tuple
print("2.2 Repeated tuple:", repeated)
print("2.3 Is 'Laptop Pro' in order?:", "Laptop Pro" in order)  # Membership test
print("2.4 Is 'Tablet' in order?:", "Tablet" in order)  # Negative membership test

# Mini-Exercise: Concatenate coords with (40, 50) and check if 20 is in the result.
more_coords = (40, 50)
combined_coords = coords + more_coords
print("2.5 Mini-Exercise: Combined coords:", combined_coords, "Is 20 in tuple?:", 20 in combined_coords)

# %% 3. Tuple Methods
# Explanation: Tuples have only two methods: count() and index(), due to immutability.
# count() returns occurrences of an item, index() returns the first index of an item.
numbers = (1, 2, 2, 3, 1)
print("3.1 Count of 2:", numbers.count(2))  # Count occurrences
print("3.2 Index of 3:", numbers.index(3))  # Find first index
print("3.3 Count of 5:", numbers.count(5))  # Count non-existent item

# Mini-Exercise: Create a tuple with repeated items and print the count of one item.
repeated_tuple = ("apple", "banana", "apple", "cherry")
print("3.4 Mini-Exercise: Count of 'apple':", repeated_tuple.count("apple"))

# %% 4. Tuple Unpacking
# Explanation: Unpacking assigns tuple elements to variables. Use * for variable-length unpacking.
# Number of variables must match tuple length or use * to capture extras.
order_id, product_name, quantity, total = order  # Standard unpacking
print("4.1 Unpacked - ID:", order_id, "Product:", product_name, "Quantity:", quantity, "Total:", total)
first, *middle, last = numbers  # Variable-length unpacking
print("4.2 Unpacked numbers - First:", first, "Middle:", middle, "Last:", last)

# Mini-Exercise: Unpack coords into x, y, z and print y.
x, y, z = coords
print("4.3 Mini-Exercise: Y coordinate:", y)

# %% 5. Exercises for Practice
# Exercise 1: Create a tuple of 4 product details, access the third item, and print its length.
product = (1, "Smartphone", 699.99, 100)
third_item = product[2]
print("5.1 Exercise 1 - Third item:", third_item, "Length:", len(product))

# Exercise 2: Concatenate two tuples (product info and stock) and check for an item’s presence.
stock = (50, 20)
combined = product + stock
print("5.2 Exercise 2 - Combined:", combined, "Is 699.99 in tuple?:", 699.99 in combined)

# Exercise 3: Unpack a tuple of order details and print the variables.
order_details = (102, "Coffee Maker", 3, 149.97)
o_id, o_product, o_qty, o_total = order_details
print("5.3 Exercise 3 - Unpacked: ID:", o_id, "Product:", o_product, "Qty:", o_qty, "Total:", o_total)

# Exercise 4: Create a tuple with duplicates, find the index of an item, and count another.
data = (10, 20, 10, 30, 20)
index_30 = data.index(30)
count_10 = data.count(10)
print("5.4 Exercise 4 - Index of 30:", index_30, "Count of 10:", count_10)

# %% 6. Notes for Further Learning
# - Tuples are immutable, ideal for fixed data (e.g., coordinates, database records, dictionary keys).
# - Tuples are hashable, allowing use as dictionary keys or set elements.
# - Use tuples over lists for memory efficiency when data won’t change.
# - Common use cases: Returning multiple values from functions, storing ML dataset points.
# - Try the projects below to apply these concepts!