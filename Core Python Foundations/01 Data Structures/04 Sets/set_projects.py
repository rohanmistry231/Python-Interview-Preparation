# Python Set Projects
# Purpose: Apply Python Set knowledge through 10 optimized projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Product Category Filter
# Difficulty: Basic
# Description: Manage product categories in a set to ensure uniqueness.
# Objective: Practice creating, adding, and removing set elements.
# Tasks:
# - Initialize a set with 3 product categories.
# - Add 2 new categories.
# - Remove 1 category using discard().
# - Print the set and its length.
categories = {"Electronics", "Appliances", "Furniture"}
categories.update(["Clothing", "Books"])  # Add multiple categories
categories.discard("Furniture")  # Remove category
print("Categories:", categories)
print("Length:", len(categories))

# %% Project 2: Unique IDs Generator
# Difficulty: Basic
# Description: Generate a set of unique product IDs.
# Objective: Practice set creation and membership testing.
# Tasks:
# - Create a set of 4 product IDs.
# - Add a new ID using add().
# - Check if an ID exists in the set.
# - Print the set and membership result.
product_ids = {1, 2, 3, 4}
product_ids.add(5)  # Add new ID
is_present = 3 in product_ids  # Check membership
print("Product IDs:", product_ids)
print("Is ID 3 present?:", is_present)

# %% Project 3: Tag Manager
# Difficulty: Basic
# Description: Manage tags for a blog post using a set.
# Objective: Practice update() and pop().
# Tasks:
# - Create a set with 3 tags.
# - Use update() to add 2 more tags.
# - Pop an arbitrary tag.
# - Print the updated set.
tags = {"python", "coding", "tech"}
tags.update(["tutorial", "programming"])  # Add tags
popped_tag = tags.pop()  # Remove arbitrary tag
print("Tags:", tags)

# %% Project 4: Common Items Finder
# Difficulty: Intermediate
# Description: Find common items between two inventories.
# Objective: Use set operations (intersection, union).
# Tasks:
# - Create two sets of inventory items.
# - Find their intersection and union.
# - Print both results.
inventory1 = {"Laptop", "Smartphone", "Tablet"}
inventory2 = {"Smartphone", "Tablet", "Headphones", "Charger"}
common_items = inventory1.intersection(inventory2)  # Common items
all_items = inventory1.union(inventory2)  # All unique items
print("Intersection:", common_items)
print("Union:", all_items)

# %% Project 5: Unique Word Extractor
# Difficulty: Intermediate
# Description: Extract unique words from a sentence.
# Objective: Convert lists to sets and use set operations.
# Tasks:
# - Take a sentence and split it into words.
# - Convert to a set to remove duplicates.
# - Print the unique words and their count.
sentence = "the cat and the dog and cat"
unique_words = set(sentence.split())  # Remove duplicates
print("Unique words:", unique_words)
print("Count:", len(unique_words))

# %% Project 6: Access Control
# Difficulty: Intermediate
# Description: Manage user roles with sets.
# Objective: Use set methods and subset checks.
# Tasks:
# - Create a set of user permissions.
# - Add new permissions using update().
# - Check if a specific set of permissions is a subset.
# - Print the permissions and subset result.
permissions = {"read", "write"}
permissions.update(["delete", "admin"])  # Add permissions
is_subset = {"read", "write"}.issubset(permissions)  # Check subset
print("Permissions:", permissions)
print("Is {'read', 'write'} a subset?:", is_subset)

# %% Project 7: Inventory Difference Analyzer
# Difficulty: Advanced
# Description: Compare inventories to find exclusive items.
# Objective: Use difference and symmetric difference.
# Tasks:
# - Create two sets of inventory items.
# - Find items unique to each inventory (difference).
# - Find items exclusive to one inventory (symmetric difference).
# - Print both results.
inv1 = {"Laptop", "Smartphone", "Tablet"}
inv2 = {"Smartphone", "Tablet", "Headphones"}
unique_to_inv1 = inv1.difference(inv2)  # Items only in inv1
exclusive_items = inv1.symmetric_difference(inv2)  # Items in one but not both
print("Unique to inventory 1:", unique_to_inv1)
print("Exclusive items:", exclusive_items)

# %% Project 8: Event Attendee Tracker
# Difficulty: Advanced
# Description: Track attendees across multiple events.
# Objective: Use set operations to analyze attendance.
# Tasks:
# - Create sets of attendees for 3 events.
# - Find attendees common to all events (intersection).
# - Find attendees who attended at least one event (union).
# - Print both results.
event1 = {"Alice", "Bob", "Charlie"}
event2 = {"Alice", "Charlie", "Dana"}
event3 = {"Alice", "Dana", "Eve"}
common_attendees = event1.intersection(event2, event3)  # Common to all
all_attendees = event1.union(event2, event3)  # At least one event
print("Common attendees:", common_attendees)
print("All attendees:", all_attendees)

# %% Project 9: Data Deduplication
# Difficulty: Advanced
# Description: Remove duplicates from a dataset using sets.
# Objective: Convert between sets and other structures.
# Tasks:
# - Create a list with duplicate data (e.g., IDs).
# - Convert to a set to remove duplicates.
# - Convert back to a sorted list.
# - Print the deduplicated list.
data = [1, 2, 2, 3, 3, 4, 5, 5]
deduplicated = sorted(set(data))  # Remove duplicates and sort
print("Deduplicated data:", deduplicated)

# %% Project 10: Permission Conflict Resolver
# Difficulty: Advanced
# Description: Resolve conflicting permissions between user roles.
# Objective: Use set operations to identify and resolve conflicts.
# Tasks:
# - Create two sets of permissions for different roles.
# - Find conflicting permissions (intersection).
# - Remove conflicts from one role using difference_update().
# - Print updated roles.
role1 = {"read", "write", "delete"}
role2 = {"write", "delete", "admin"}
conflicts = role1.intersection(role2)  # Find conflicts
role1.difference_update(conflicts)  # Remove conflicts from role1
print("Conflicts:", conflicts)
print("Updated role 1:", role1)
print("Role 2:", role2)