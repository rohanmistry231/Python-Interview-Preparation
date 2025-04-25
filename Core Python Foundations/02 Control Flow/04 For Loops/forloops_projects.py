# For Loops Projects
# Purpose: Apply For Loops through 5 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Price Formatter
# Difficulty: Basic
# Description: Format a list of prices with a discount.
# Objective: Practice basic for loop over a list.
# Tasks:
# - Create a list of prices.
# - Loop over prices and print each with a 5% discount.
# - Print the discounted prices.
prices = [100, 200, 300]
for price in prices:
    discounted = price * 0.95
    print("Discounted price:", discounted)

# %% Project 2: Product Counter
# Difficulty: Basic
# Description: Count products in a category.
# Objective: Use for loop with conditionals.
# Tasks:
# - Create a list of product dictionaries with category.
# - Loop over products and count those in "Electronics".
# - Print the count.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Blender", "category": "Appliances"},
    {"name": "Smartphone", "category": "Electronics"}
]
count = 0
for product in products:
    if product["category"] == "Electronics":
        count += 1
print("Electronics count:", count)

# %% Project 3: Stock Summarizer
# Difficulty: Intermediate
# Description: Summarize stock levels across products.
# Objective: Use for loop with dictionary iteration.
# Tasks:
# - Create a list of product dictionaries with stock.
# - Loop over products and sum stock levels.
# - Print the total stock.
products = [
    {"name": "Laptop", "stock": 50},
    {"name": "Smartphone", "stock": 100},
    {"name": "Blender", "stock": 0}
]
total_stock = 0
for product in products:
    total_stock += product["stock"]
print("Total stock:", total_stock)

# %% Project 4: Price Range Filter
# Difficulty: Intermediate
# Description: Filter products by price range.
# Objective: Use for loop with conditionals and list creation.
# Tasks:
# - Create a list of product dictionaries with price.
# - Loop over products and collect those with price > 500.
# - Print the filtered products.
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 25},
    {"name": "Smartphone", "price": 699.99}
]
filtered = []
for product in products:
    if product["price"] > 500:
        filtered.append(product)
print("Filtered products:", filtered)

# %% Project 5: Order Report Generator
# Difficulty: Advanced
# Description: Generate a report for orders with dynamic formatting.
# Objective: Use for loop with enumerate and string formatting.
# Tasks:
# - Create a list of order dictionaries with total and status.
# - Loop over orders with enumerate to add index; format a report line for each.
# - Print the report.
orders = [
    {"total": 1000, "status": "Shipped"},
    {"total": 500, "status": "Pending"}
]
for index, order in enumerate(orders, 1):
    print(f"Order {index}: Total ${order['total']:.2f}, Status: {order['status']}")