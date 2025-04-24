# Python Data Structures: Sets

# Purpose: Sets are unordered, mutable collections of unique elements.
# Key Features: Fast membership testing, set operations (union, intersection).

# 1. Creating and Accessing Sets
# Explanation: Sets use curly braces {} or set(), no duplicates allowed.
# Example:
categories = {"Electronics", "Appliances", "Furniture"}
print("Set:", categories)
print("Is 'Electronics' in set?:", "Electronics" in categories)

# 2. Modifying Sets
# Explanation: Add or remove elements using add(), remove(), discard(), pop().
# Example:
categories.add("Clothing")  # Add item
print("After add:", categories)
categories.remove("Furniture")  # Remove item (raises error if not found)
print("After remove:", categories)
categories.discard("Books")  # Remove if exists, no error
print("After discard:", categories)
popped = categories.pop()  # Remove and return arbitrary item
print("Popped:", popped, "Set:", categories)

# 3. Set Operations
# Explanation: Union, intersection, difference, symmetric difference.
# Example:
set1 = {"Laptop", "Smartphone", "Tablet"}
set2 = {"Smartphone", "Tablet", "Headphones"}
union = set1 | set2  # Union
print("Union:", union)
intersection = set1 & set2  # Intersection
print("Intersection:", intersection)
difference = set1 - set2  # Difference
print("Difference:", difference)
sym_diff = set1 ^ set2  # Symmetric difference
print("Symmetric Difference:", sym_diff)

# 4. Set Methods
# Explanation: Methods like update(), clear(), issubset(), issuperset().
# Example:
categories.update(["Books", "Toys"])  # Add multiple items
print("After update:", categories)
print("Is {'Books', 'Toys'} a subset?:", {"Books", "Toys"}.issubset(categories))

# Exercise 1: Create a set of product IDs, add a new ID, and remove one.
# Solution:
# product_ids = {1, 2, 3, 4}
# product_ids.add(5)
# product_ids.remove(2)
# print("Exercise 1 - Updated set:", product_ids)

# Exercise 2: Find the intersection of two sets of product categories.
# Solution:
# cat1 = {"Electronics", "Appliances"}
# cat2 = {"Appliances", "Furniture"}
# common = cat1 & cat2
# print("Exercise 2 - Intersection:", common)

# Exercise 3: Use update() to add items to a set and check if it’s a superset of another set.
# Solution:
# items = {"Mouse", "Keyboard"}
# items.update(["Monitor", "Printer"])
# print("Exercise 3 - Updated set:", items, "Is superset of {'Mouse', 'Monitor'}?:", 
#       items.issuperset({"Mouse", "Monitor"}))

# Notes:
# - Sets are ideal for deduplication and membership tests (e.g., unique ML labels, web app user roles).
# - Sets are unordered; no indexing or slicing.
# - Frozen sets (covered next) are immutable versions of sets.