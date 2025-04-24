# Python Data Structures: Sets
# Purpose: Learn Sets, unordered, mutable collections of unique elements.
# Key Features: Fast membership testing, deduplication, set operations (union, intersection).

# %% 1. Creating and Accessing Sets
# Explanation: Sets are created with curly braces {} or set(). Elements must be hashable (immutable).
# No duplicates allowed. Access is limited to membership tests (in) since sets are unordered.
categories = {"Electronics", "Appliances", "Furniture"}
print("1.1 Set:", categories)
print("1.2 Is 'Electronics' in set?:", "Electronics" in categories)
print("1.3 Is 'Books' in set?:", "Books" in categories)
print("1.4 Length of set:", len(categories))  # Number of elements
empty_set = set()  # Empty set (not {})
print("1.5 Empty set:", empty_set)

# Mini-Exercise: Create a set of 3 colors and check if one color is present.
colors = {"Red", "Blue", "Green"}
print("1.6 Mini-Exercise: Is 'Blue' in colors?:", "Blue" in colors)

# %% 2. Modifying Sets
# Explanation: Add elements with add() or update(). Remove with remove() (raises error if absent),
# discard() (no error), or pop() (removes arbitrary element). clear() empties the set.
categories.add("Clothing")  # Add single item
print("2.1 After add:", categories)
categories.update(["Books", "Toys"])  # Add multiple items
print("2.2 After update:", categories)
categories.remove("Furniture")  # Remove item (raises KeyError if not found)
print("2.3 After remove:", categories)
categories.discard("Books")  # Remove if exists, no error
print("2.4 After discard:", categories)
popped = categories.pop()  # Remove and return arbitrary item
print("2.5 Popped:", popped, "Set:", categories)

# Mini-Exercise: Add a new color to colors, discard one, and print the set.
colors.add("Yellow")
colors.discard("Red")
print("2.6 Mini-Exercise: Updated colors:", colors)

# %% 3. Set Operations
# Explanation: Sets support union (|), intersection (&), difference (-), and symmetric difference (^).
# Operations can use operators or methods (union(), intersection(), etc.).
set1 = {"Laptop", "Smartphone", "Tablet"}
set2 = {"Smartphone", "Tablet", "Headphones"}
union = set1 | set2  # All unique elements
print("3.1 Union:", union)
intersection = set1 & set2  # Common elements
print("3.2 Intersection:", intersection)
difference = set1 - set2  # Elements in set1 but not set2
print("3.3 Difference:", difference)
sym_diff = set1 ^ set2  # Elements in either but not both
print("3.4 Symmetric Difference:", sym_diff)

# Mini-Exercise: Find the union and difference of two sets of numbers.
nums1 = {1, 2, 3}
nums2 = {2, 3, 4}
print("3.5 Mini-Exercise: Union:", nums1 | nums2, "Difference:", nums1 - nums2)

# %% 4. Set Methods
# Explanation: Methods like issubset(), issuperset(), isdisjoint(), and clear() enhance functionality.
# update() adds multiple items, copy() creates a shallow copy.
set3 = {"Smartphone", "Tablet"}
print("4.1 Is set3 a subset of set1?:", set3.issubset(set1))
print("4.2 Is set1 a superset of set3?:", set1.issuperset(set3))
print("4.3 Are set1 and {4, 5} disjoint?:", set1.isdisjoint({4, 5}))
set_copy = set1.copy()  # Shallow copy
print("4.4 Copy:", set_copy)
# set1.clear()  # Clears all items (commented to preserve data)
# print("4.5 After clear:", set1)

# Mini-Exercise: Create a copy of colors and check if it’s a superset of {"Blue"}.
colors_copy = colors.copy()
print("4.6 Mini-Exercise: Colors copy:", colors_copy, "Superset of {'Blue'}?:", colors_copy.issuperset({"Blue"}))

# %% 5. Exercises for Practice
# Exercise 1: Create a set of product IDs, add a new ID, and remove one.
product_ids = {1, 2, 3, 4}
product_ids.add(5)
product_ids.remove(2)
print("5.1 Exercise 1 - Updated set:", product_ids)

# Exercise 2: Find the intersection of two sets of product categories.
cat1 = {"Electronics", "Appliances"}
cat2 = {"Appliances", "Furniture"}
common = cat1.intersection(cat2)  # Using method instead of &
print("5.2 Exercise 2 - Intersection:", common)

# Exercise 3: Use update() to add items to a set and check if it’s a superset of another set.
items = {"Mouse", "Keyboard"}
items.update(["Monitor", "Printer"])
print("5.3 Exercise 3 - Updated set:", items, "Is superset of {'Mouse', 'Monitor'}?:", items.issuperset({"Mouse", "Monitor"}))

# Exercise 4: Create two sets, find their symmetric difference, and check if they’re disjoint.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
sym_diff = set_a.symmetric_difference(set_b)
disjoint = set_a.isdisjoint(set_b)
print("5.4 Exercise 4 - Symmetric difference:", sym_diff, "Disjoint?:", disjoint)

# %% 6. Notes for Further Learning
# - Sets are ideal for deduplication, membership tests, and set operations (e.g., unique ML labels, user roles).
# - Sets are unordered; no indexing or slicing. Use lists or tuples for ordered data.
# - Elements must be hashable (immutable types like strings, numbers, tuples).
# - Frozen sets (immutable sets) are covered next for hashable collections.
# - Common use cases: Removing duplicates, filtering unique items, comparing datasets.
# - Try the projects below to apply these concepts!