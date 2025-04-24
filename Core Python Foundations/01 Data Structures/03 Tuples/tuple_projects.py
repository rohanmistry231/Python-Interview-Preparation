# Python Tuple Projects
# Purpose: Apply Python Tuple knowledge through 10 optimized projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Order Record Manager
# Difficulty: Basic
# Description: Create a program to manage a single order record using a tuple.
# Objective: Practice creating, accessing, and slicing tuples.
# Tasks:
# - Initialize a tuple with 4 order details (id, product, quantity, price).
# - Access the product name and quantity.
# - Print a slice of the middle two items.
# - Print the tuple length.
order = (1, "Laptop", 2, 999.99)
product_name, quantity = order[1], order[2]  # Access specific items
middle_slice = order[1:3]  # Slice middle two items
print("Order:", order)
print("Product:", product_name, "Quantity:", quantity)
print("Middle slice:", middle_slice)
print("Length:", len(order))

# %% Project 2: Coordinate Storage
# Difficulty: Basic
# Description: Store and manipulate 2D coordinates in a tuple.
# Objective: Practice tuple creation and membership tests.
# Tasks:
# - Create a tuple of 3 coordinates (x, y, z).
# - Check if a specific value (e.g., 20) is in the tuple.
# - Concatenate with another tuple of 2 coordinates.
# - Print the combined tuple.
coords = (10, 20, 30)
is_present = 20 in coords  # Membership test
more_coords = (40, 50)
combined = coords + more_coords  # Concatenate
print("Coordinates:", coords)
print("Is 20 present?:", is_present)
print("Combined:", combined)

# %% Project 3: Item Catalog
# Difficulty: Basic
# Description: Manage a catalog of items using a tuple.
# Objective: Practice tuple repetition and methods.
# Tasks:
# - Create a tuple with 3 item names.
# - Repeat the tuple twice.
# - Count occurrences of one item.
# - Print the repeated tuple and count.
catalog = ("Pen", "Notebook", "Pencil")
repeated_catalog = catalog * 2  # Repeat tuple
pen_count = repeated_catalog.count("Pen")  # Count item
print("Repeated catalog:", repeated_catalog)
print("Count of Pen:", pen_count)

# %% Project 4: Employee Record System
# Difficulty: Intermediate
# Description: Store employee records in a tuple with nested tuples.
# Objective: Work with nested tuples and unpacking.
# Tasks:
# - Create a tuple of 3 employee records (id, (name, department)).
# - Unpack the second employee’s name and department.
# - Print all records and the unpacked details.
employees = ((1, ("Alice", "HR")), (2, ("Bob", "IT")), (3, ("Charlie", "Sales")))
_, (name, dept) = employees[1]  # Unpack second employee
print("Records:", employees)
print("Second employee: Name:", name, "Department:", dept)

# %% Project 5: Sales Data Analysis
# Difficulty: Intermediate
# Description: Analyze sales data stored in a tuple.
# Objective: Practice tuple methods and iteration.
# Tasks:
# - Create a tuple of 5 sales amounts.
# - Find the index of a specific amount.
# - Count occurrences of another amount.
# - Print the tuple, index, and count.
sales = (100, 200, 100, 300, 200)
index_300 = sales.index(300)  # Find index
count_100 = sales.count(100)  # Count occurrences
print("Sales:", sales)
print("Index of 300:", index_300)
print("Count of 100:", count_100)

# %% Project 6: Route Planner
# Difficulty: Intermediate
# Description: Store a route as a tuple of coordinates.
# Objective: Use concatenation and slicing for route manipulation.
# Tasks:
# - Create a tuple of 3 coordinates (x, y).
# - Concatenate with 2 more coordinates.
# - Extract a sub-route (middle 3 coordinates).
# - Print the full route and sub-route.
route = ((1, 2), (3, 4), (5, 6))
more_points = ((7, 8), (9, 10))
full_route = route + more_points  # Concatenate
sub_route = full_route[1:4]  # Middle 3 coordinates
print("Full route:", full_route)
print("Sub-route:", sub_route)

# %% Project 7: Inventory Lookup
# Difficulty: Advanced
# Description: Use tuples as dictionary keys for inventory lookup.
# Objective: Leverage tuple hashability for key-based storage.
# Tasks:
# - Create a dictionary with tuple keys (item, size) and quantity values.
# - Add a new item-size pair.
# - Print all items and total quantity.
inventory = {
    ("Shirt", "M"): 10,
    ("Shirt", "L"): 5
}
inventory[("Pants", "M")] = 8  # Add new item-size pair
total_quantity = sum(inventory.values())  # Sum quantities
print("Inventory:", inventory)
print("Total quantity:", total_quantity)

# %% Project 8: Event Log
# Difficulty: Advanced
# Description: Store event logs as a tuple of timestamped records.
# Objective: Manipulate nested tuples and analyze data.
# Tasks:
# - Create a tuple of 4 events (timestamp, action).
# - Extract actions using unpacking or iteration.
# - Print events and unique actions.
events = ((1, "login"), (2, "logout"), (3, "login"), (4, "update"))
actions = set(event[1] for event in events)  # Extract unique actions
print("Events:", events)
print("Unique actions:", actions)

# %% Project 9: Data Point Clustering
# Difficulty: Advanced
# Description: Group data points (tuples) by a specific attribute.
# Objective: Use tuples in sets and dictionaries for grouping.
# Tasks:
# - Create a tuple of 5 data points (x, y, label).
# - Group points by label using a dictionary.
# - Print the grouped points.
points = ((1, 2, "A"), (3, 4, "A"), (5, 6, "B"), (7, 8, "B"), (9, 10, "C"))
groups = {}
for x, y, label in points:
    if label not in groups:
        groups[label] = []
    groups[label].append((x, y))  # Group coordinates by label
print("Groups:", groups)

# %% Project 10: Function Return Analyzer
# Difficulty: Advanced
# Description: Analyze multiple return values from a function using tuples.
# Objective: Use tuples for function returns and unpacking.
# Tasks:
# - Define a function that returns a tuple (sum, count) for a list of numbers.
# - Call the function with a list and unpack the result.
# - Print the sum and count.
def analyze_numbers(numbers):
    return (sum(numbers), len(numbers))  # Return tuple
numbers = [1, 2, 3, 4]
total, count = analyze_numbers(numbers)  # Unpack result
print("Input:", numbers)
print("Sum:", total, "Count:", count)