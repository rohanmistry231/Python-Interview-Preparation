# Python Data Structures: Frozen Sets
# Purpose: Learn Frozen Sets, immutable, unordered collections of unique elements.
# Key Features: Hashable (usable as dictionary keys), supports set operations, deduplication.

# %% 1. Creating and Accessing Frozen Sets
# Explanation: Frozen sets are created with frozenset() from iterables (lists, sets, etc.).
# Elements must be hashable (immutable). Access is limited to membership tests (in) since unordered.
categories = frozenset(["Electronics", "Appliances", "Furniture"])
print("1.1 Frozen Set:", categories)
print("1.2 Is 'Electronics' in frozen set?:", "Electronics" in categories)
print("1.3 Is 'Books' in frozen set?:", "Books" in categories)
print("1.4 Length of frozen set:", len(categories))  # Number of elements
empty_fset = frozenset()  # Empty frozen set
print("1.5 Empty frozen set:", empty_fset)

# Mini-Exercise: Create a frozen set of 3 numbers and check if one is present.
numbers = frozenset([1, 2, 3])
print("1.6 Mini-Exercise: Is 2 in numbers?:", 2 in numbers)

# %% 2. Frozen Set Operations
# Explanation: Frozen sets support union (|), intersection (&), difference (-), and symmetric difference (^).
# Operations return new frozen sets due to immutability. Identical to regular set operations.
set1 = frozenset(["Laptop", "Smartphone", "Tablet"])
set2 = frozenset(["Smartphone", "Tablet", "Headphones"])
union = set1.union(set2)  # All unique elements
print("2.1 Union:", union)
intersection = set1.intersection(set2)  # Common elements
print("2.2 Intersection:", intersection)
difference = set1.difference(set2)  # Elements in set1 but not set2
print("2.3 Difference:", difference)
sym_diff = set1.symmetric_difference(set2)  # Elements in either but not both
print("2.4 Symmetric Difference:", sym_diff)

# Mini-Exercise: Find the intersection and union of two frozen sets of tags.
tags1 = frozenset(["python", "coding"])
tags2 = frozenset(["coding", "tech"])
print("2.5 Mini-Exercise: Intersection:", tags1 & tags2, "Union:", tags1 | tags2)

# %% 3. Frozen Set Methods
# Explanation: Methods include copy(), issubset(), issuperset(), isdisjoint() (no add/remove due to immutability).
# copy() returns a new frozen set (shallow). Methods mirror regular sets but preserve immutability.
set_copy = categories.copy()  # Shallow copy
print("3.1 Copy:", set_copy)
subset = frozenset(["Electronics", "Appliances"])
print("3.2 Is {'Electronics', 'Appliances'} a subset?:", subset.issubset(categories))
print("3.3 Is categories a superset of {'Furniture'}?:", categories.issuperset(frozenset(["Furniture"])))
print("3.4 Are categories and {'Books', 'Toys'} disjoint?:", categories.isdisjoint(frozenset(["Books", "Toys"])))

# Mini-Exercise: Check if numbers is a superset of {1}.
print("3.5 Mini-Exercise: Is numbers a superset of {1}?:", numbers.issuperset(frozenset([1])))

# %% 4. Using Frozen Sets as Dictionary Keys
# Explanation: Frozen sets are hashable, making them ideal as dictionary keys (unlike regular sets).
# Use for mapping fixed collections to values (e.g., categories to descriptions).
inventory = {
    frozenset(["Laptop", "Smartphone"]): "Electronics Stock",
    frozenset(["Coffee Maker", "Blender"]): "Appliances Stock"
}
print("4.1 Dictionary with frozen set keys:", inventory)
print("4.2 Value for Electronics:", inventory[frozenset(["Laptop", "Smartphone"])])
# Accessing with equivalent frozen set
key = frozenset(["Smartphone", "Laptop"])  # Same elements, different order
print("4.3 Value with equivalent key:", inventory[key])

# Mini-Exercise: Create a dictionary with a frozen set key for tags and access its value.
tag_dict = {frozenset(["python", "coding"]): "Programming Tags"}
print("4.4 Mini-Exercise: Value for tags:", tag_dict[frozenset(["python", "coding"])])

# %% 5. Exercises for Practice
# Exercise 1: Create a frozen set of product IDs and check for an ID’s presence.
product_ids = frozenset([1, 2, 3, 4])
print("5.1 Exercise 1 - Is 3 in frozen set?:", 3 in product_ids)

# Exercise 2: Find the union of two frozen sets of categories.
cat1 = frozenset(["Electronics", "Appliances"])
cat2 = frozenset(["Appliances", "Furniture"])
union = cat1.union(cat2)
print("5.2 Exercise 2 - Union:", union)

# Exercise 3: Use a frozen set as a dictionary key to store a category description.
desc = {frozenset(["Mouse", "Keyboard"]): "Peripherals"}
print("5.3 Exercise 3 - Dictionary:", desc)

# Exercise 4: Create two frozen sets and check if they are disjoint.
set_a = frozenset([1, 2, 3])
set_b = frozenset([4, 5, 6])
disjoint = set_a.isdisjoint(set_b)
print("5.4 Exercise 4 - Are sets disjoint?:", disjoint)

# %% 6. Notes for Further Learning
# - Frozen sets are immutable and hashable, ideal for dictionary keys or set elements (e.g., ML model metadata, fixed configurations).
# - Use regular sets for mutable operations; frozen sets for fixed, hashable data.
# - Set operations (union, intersection, etc.) are identical to regular sets but return frozen sets.
# - Common use cases: Caching unique identifiers, storing immutable groups in dictionaries.
# - Try the projects below to apply these concepts!