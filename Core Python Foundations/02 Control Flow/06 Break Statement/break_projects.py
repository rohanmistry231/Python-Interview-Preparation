# Break Projects
# Purpose: Apply Break Statement through 5 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Price Threshold Stopper
# Difficulty: Basic
# Description: Stop processing prices when too high.
# Objective: Practice break in for loop.
# Tasks:
# - Create a list of prices.
# - Loop over prices; break if price > 1000.
# - Print processed prices.
prices = [200, 500, 1200, 300]
for price in prices:
    if price > 1000:
        print("Stopped at:", price)
        break
    print("Processed price:", price)

# %% Project 2: Stock Limit Checker
# Difficulty: Basic
# Description: Stop checking stock when too low.
# Objective: Use break in while loop.
# Tasks:
# - Create a variable for stock.
# - While stock > 0, reduce by 20; break if < 30.
# - Print final stock.
stock = 100
while stock > 0:
    stock -= 20
    print("Stock:", stock)
    if stock < 30:
        print("Stopped at:", stock)
        break

# %% Project 3: Product Searcher
# Difficulty: Intermediate
# Description: Search for a specific product in a list.
# Objective: Use break with for loop and conditionals.
# Tasks:
# - Create a list of product dictionaries.
# - Loop over products; break when Electronics with price > 500 is found.
# - Print found product or "Not found".
products = [
    {"name": "Mouse", "category": "Electronics", "price": 25},
    {"name": "Laptop", "category": "Electronics", "price": 999.99},
    {"name": "Blender", "category": "Appliances", "price": 100}
]
found = None
for product in products:
    if product["category"] == "Electronics" and product["price"] > 500:
        found = product
        break
print("Found product:", found if found else "Not found")

# %% Project 4: Order Scanner
# Difficulty: Intermediate
# Description: Scan orders until a large order is found.
# Objective: Use break with while loop and list.
# Tasks:
# - Create a list of order totals.
# - While iterating, break if total > 2000.
# - Print processed totals and stopping point.
orders = [500, 1000, 2500, 300]
index = 0
while index < len(orders):
    total = orders[index]
    if total > 2000:
        print("Stopped at:", total)
        break
    print("Processed total:", total)
    index += 1

# %% Project 5: Nested Product Filter
# Difficulty: Advanced
# Description: Filter products in nested loops with early stopping.
# Objective: Use break in nested loops with complex data.
# Tasks:
# - Create a list of product dictionaries with attributes.
# - Loop over products and attributes; break inner loop if price > 700 and stock < 50.
# - Print filtered products.
products = [
    {"name": "Laptop", "price": 999.99, "stock": 30},
    {"name": "Smartphone", "price": 699.99, "stock": 100}
]
filtered = []
for product in products:
    for key, value in product.items():
        if product["price"] > 700 and product["stock"] < 50:
            filtered.append(product)
            break
print("Filtered product:", filtered)