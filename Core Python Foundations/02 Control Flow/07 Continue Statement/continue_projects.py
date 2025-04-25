# Continue Projects
# Purpose: Apply Continue Statement through 5 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Price Filter
# Difficulty: Basic
# Description: Filter out low prices during processing.
# Objective: Practice continue in for loop.
# Tasks:
# - Create a list of prices.
# - Loop over prices; skip if price < 200.
# - Print valid prices.
prices = [150, 300, 50, 500]
for price in prices:
    if price < 200:
        continue
    print("Valid price:", price)

# %% Project 2: Stock Skip System
# Difficulty: Basic
# Description: Skip even stock levels during depletion.
# Objective: Use continue in while loop.
# Tasks:
# - Create a variable for stock.
# - While stock > 0, reduce by 10; skip even levels.
# - Print odd stock levels.
stock = 100
while stock > 0:
    stock -= 10
    if stock % 2 == 0:
        continue
    print("Odd stock level:", stock)

# %% Project 3: Category Processor
# Difficulty: Intermediate
# Description: Process only specific product categories.
# Objective: Use continue with for loop and dictionaries.
# Tasks:
# - Create a list of product dictionaries with category.
# - Loop over products; skip non-Electronics.
# - Print processed products.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Blender", "category": "Appliances"},
    {"name": "Smartphone", "category": "Electronics"}
]
for product in products:
    if product["category"] != "Electronics":
        continue
    print("Processed product:", product)

# %% Project 4: Order Skipper
# Difficulty: Intermediate
# Description: Skip small orders during processing.
# Objective: Use continue with while loop and list.
# Tasks:
# - Create a list of order totals.
# - While iterating, skip totals < 500.
# - Print processed totals.
orders = [200, 1000, 300, 2000]
index = 0
while index < len(orders):
    total = orders[index]
    if total < 500:
        index += 1
        continue
    print("Processed total:", total)
    index += 1

# %% Project 5: Nested Attribute Filter
# Difficulty: Advanced
# Description: Filter attributes in nested loops.
# Objective: Use continue in nested loops with complex data.
# Tasks:
# - Create a list of product dictionaries with attributes.
# - Loop over products and attributes; skip if category isn’t Electronics.
# - Print Electronics attributes.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Blender", "category": "Appliances"}
]
for product in products:
    for key, value in product.items():
        if product["category"] != "Electronics":
            continue
        print(f"Electronics attribute: {key} = {value}")