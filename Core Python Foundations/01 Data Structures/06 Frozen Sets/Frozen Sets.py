# Python Data Structures: Frozen Sets

# Purpose: Frozen sets are immutable, unordered collections of unique elements.
# Key Features: Hashable, used as dictionary keys, supports set operations.

# 1. Creating Frozen Sets
# Explanation: Frozen sets are created using frozenset(), no duplicates allowed.
# Example:
categories = frozenset(["Electronics", "Appliances", "Furniture"])
print("Frozen Set:", categories)
print("Is 'Electronics' in frozen set?:", "Electronics" in categories)

# 2. Frozen Set Operations
# Explanation: Supports union, intersection, difference, symmetric difference (immutable).
# Example:
set1 = frozenset(["Laptop", "Smartphone", "Tablet"])
set2 = frozenset(["Smartphone", "Tablet", "Headphones"])
union = set1 | set2  # Union
print("Union:", union)
intersection = set1 & set2  # Intersection
print("Intersection:", intersection)
difference = set1 - set2  # Difference
print("Difference:", difference)
sym_diff = set1 ^ set2  # Symmetric Difference
print("Symmetric Difference:", sym_diff)

# 3. Frozen Set Methods
# Explanation: Methods like copy(), issubset(), issuperset() (no add/remove due to immutability).
# Example:
set_copy = categories.copy()  # Returns new frozen set
print("Copy:", set_copy)
print("Is {'Electronics', 'Appliances'} a subset?:", 
      frozenset(["Electronics", "Appliances"]).issubset(categories))
print("Is categories a superset of {'Furniture'}?:", 
      categories.issuperset(frozenset(["Furniture"])))

# 4. Using Frozen Sets as Dictionary Keys
# Explanation: Frozen sets are hashable, unlike regular sets.
# Example:
inventory = {
    frozenset(["Laptop", "Smartphone"]): "Electronics Stock",
    frozenset(["Coffee Maker", "Blender"]): "Appliances Stock"
}
print("Dictionary with frozen set keys:", inventory)
print("Value for Electronics:", inventory[frozenset(["Laptop", "Smartphone"])])

# Exercise 1: Create a frozen set of product IDs and check for an ID’s presence.
# Solution:
# product_ids = frozenset([1, 2, 3, 4])
# print("Exercise 1 - Is 3 in frozen set?:", 3 in product_ids)

# Exercise 2: Find the union of two frozen sets of categories.
# Solution:
# cat1 = frozenset(["Electronics", "Appliances"])
# cat2 = frozenset(["Appliances", "Furniture"])
# union = cat1 | cat2
# print("Exercise 2 - Union:", union)

# Exercise 3: Use a frozen set as a dictionary key to store a category description.
# Solution:
# desc = {frozenset(["Mouse", "Keyboard"]): "Peripherals"}
# print("Exercise 3 - Dictionary:", desc)

# Notes:
# - Frozen sets are immutable, making them suitable for dictionary keys or ML model metadata.
# - Use regular sets for mutable operations, frozen sets for fixed data.
# - Set operations are identical to regular sets but return new frozen sets.