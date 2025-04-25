# While Loops Projects
# Purpose: Apply While Loops through 5 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Price Reducer
# Difficulty: Basic
# Description: Reduce a price until affordable.
# Objective: Practice basic while loop with decrement.
# Tasks:
# - Create a variable for price.
# - While price > 200, reduce by 50 and print.
# - Print the final price.
price = 500
while price > 200:
    price -= 50
    print("Reduced price:", price)
print("Final price:", price)

# %% Project 2: Stock Depletion Tracker
# Difficulty: Basic
# Description: Track stock depletion over time.
# Objective: Use while loop with conditionals.
# Tasks:
# - Create a variable for stock.
# - While stock > 0, reduce by 10 and print status.
# - Print final stock.
stock = 100
while stock > 0:
    stock -= 10
    print("Stock:", stock)
print("Final stock:", stock)

# %% Project 3: Order Accumulator
# Difficulty: Intermediate
# Description: Accumulate order totals until a threshold.
# Objective: Use while loop with list processing.
# Tasks:
# - Create a list of order amounts.
# - While total < 1000, add next amount and print running total.
# - Print final total.
orders = [300, 300, 500]
total = 0
index = 0
while total < 1000 and index < len(orders):
    total += orders[index]
    print("Running total:", total)
    index += 1
print("Final total:", total)

# %% Project 4: Discount Optimizer
# Difficulty: Intermediate
# Description: Optimize discounts to reach a target price.
# Objective: Use while loop with dynamic adjustments.
# Tasks:
# - Create variables for price and target.
# - While price > target, increase discount by 5% and print new price.
# - Print final discount.
price = 1000
target = 850
discount = 0
while price > target:
    discount += 0.05
    price = 1000 * (1 - discount)
    print("New price:", price)
print("Final discount:", f"{discount * 100}%")

# %% Project 5: Inventory Restock Simulator
# Difficulty: Advanced
# Description: Simulate restocking until sufficient.
# Objective: Use while loop with complex logic.
# Tasks:
# - Create a dictionary with stock and target.
# - While stock < target, add 10 units if stock < 50, else 5; track restocks.
# - Print restock count and final stock.
inventory = {"stock": 30, "target": 100}
restock_count = 0
while inventory["stock"] < inventory["target"]:
    if inventory["stock"] < 50:
        inventory["stock"] += 10
    else:
        inventory["stock"] += 5
    restock_count += 1
print("Restock count:", restock_count)
print("Final stock:", inventory["stock"])