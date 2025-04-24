# Python Frozen Set Projects
# Purpose: Apply Python Frozen Set knowledge through 5 optimized projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Category Key Generator
# Difficulty: Basic
# Description: Create a frozen set of product categories for use as a dictionary key.
# Objective: Practice creating frozen sets and using them as keys.
# Tasks:
# - Create a frozen set of 3 product categories.
# - Use it as a key in a dictionary to store a description.
# - Check if a category is in the frozen set.
# - Print the dictionary and membership result.
categories = frozenset(["Electronics", "Appliances", "Furniture"])
category_dict = {categories: "Main Categories"}
is_present = "Electronics" in categories
print("Dictionary:", category_dict)
print("Is 'Electronics' present?:", is_present)

# %% Project 2: Unique ID Store
# Difficulty: Basic
# Description: Store unique product IDs in a frozen set.
# Objective: Practice frozen set creation and membership testing.
# Tasks:
# - Create a frozen set from a list with duplicate IDs.
# - Check if two IDs are present (one in, one out).
# - Print the frozen set and membership results.
ids = [1, 2, 2, 3, 4, 4]
unique_ids = frozenset(ids)
is_2_present = 2 in unique_ids
is_5_present = 5 in unique_ids
print("IDs:", unique_ids)
print("Is 2 present?:", is_2_present)
print("Is 5 present?:", is_5_present)

# %% Project 3: Tag Overlap Analyzer
# Difficulty: Intermediate
# Description: Analyze overlapping tags between two frozen sets.
# Objective: Use set operations (intersection, union).
# Tasks:
# - Create two frozen sets of tags.
# - Find their intersection and union.
# - Check if one is a subset of the other.
# - Print the results.
tags1 = frozenset(["python", "coding", "tutorial"])
tags2 = frozenset(["coding", "tech"])
intersection = tags1.intersection(tags2)
union = tags1.union(tags2)
is_subset = tags1.issubset(tags2)
print("Intersection:", intersection)
print("Union:", union)
print("Is tags1 a subset of tags2?:", is_subset)

# %% Project 4: Inventory Mapping
# Difficulty: Advanced
# Description: Map frozen sets of items to inventory locations.
# Objective: Use frozen sets as dictionary keys for complex mappings.
# Tasks:
# - Create a dictionary with two frozen set keys (item groups) and location values.
# - Add a new mapping.
# - Access a value using an equivalent frozen set key.
# - Print the dictionary and accessed value.
inventory = {
    frozenset(["Laptop", "Smartphone"]): "Store A",
    frozenset(["Coffee Maker", "Blender"]): "Store B"
}
inventory[frozenset(["Mouse", "Keyboard"])] = "Store C"
equivalent_key = frozenset(["Smartphone", "Laptop"])  # Same elements, different order
location = inventory[equivalent_key]
print("Inventory:", inventory)
print("Location:", location)

# %% Project 5: Permission Validator
# Difficulty: Advanced
# Description: Validate permissions using frozen sets in a configuration.
# Objective: Use frozen sets for immutable permission groups and set operations.
# Tasks:
# - Create two frozen sets of permissions (allowed, required).
# - Check if required permissions are a subset of allowed.
# - Find permissions in allowed but not required (difference).
# - Print the results.
allowed = frozenset(["read", "write", "delete"])
required = frozenset(["read", "write"])
all_permitted = required.issubset(allowed)
extra_perms = allowed.difference(required)
print("Allowed:", allowed)
print("Required:", required)
print("All required permitted?:", all_permitted)
print("Extra permissions:", extra_perms)