# Python Control Flow: Break Statement

# Purpose: Break statement exits a loop immediately.
# Key Features: Terminates loop execution based on a condition.

# 1. Break in For Loop
# Explanation: Exit a for loop when a condition is met.
# Example:
prices = [100, 200, 999.99, 50, 300]
for price in prices:
    if price > 500:
        print(f"Found expensive item: {price}, stopping")
        break
    print(f"Price: {price}")
# Output: Price: 100, Price: 200, Found expensive item: 999.99, stopping

# 2. Break in While Loop
# Explanation: Exit a while loop to prevent infinite or unwanted iterations.
# Example:
stock = 100
while stock > 0:
    if stock < 50:
        print(f"Stock too low: {stock}, stopping")
        break
    stock -= 20
    print(f"Stock: {stock}")
# Output: Stock: 80, Stock: 60, Stock too low: 40, stopping

# 3. Break in Nested Loops
# Explanation: Break exits only the innermost loop.
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker"]
categories = ["Electronics", "Appliances"]
for product in products:
    for category in categories:
        if product == "Coffee Maker" and category == "Appliances":
            print(f"Found {product} in {category}, stopping")
            break
        print(f"Checking {product} in {category}")
# Output: Checking Laptop in Electronics, Checking Laptop in Appliances, ...
#         Found Coffee Maker in Appliances, stopping

# Exercise 1: Stop a for loop over a list of quantities when a quantity exceeds 10.
# Solution:
# quantities = [5, 8, 12, 3]
# for qty in quantities:
#     if qty > 10:
#         print("Exercise 1 - High quantity found:", qty)
#         break
#     print("Exercise 1 - Quantity:", qty)
# # Output: Quantity: 5, Quantity: 8, High quantity found: 12

# Exercise 2: Use break in a while loop to stop when price falls below 300.
# Solution:
# price = 500
# while price > 0:
#     if price < 300:
#         print("Exercise 2 - Price below 300:", price)
#         break
#     price -= 50
#     print("Exercise 2 - Price:", price)
# # Output: Price: 450, Price: 400, Price: 350, Price below 300: 250

# Exercise 3: Break a nested loop when a product’s price and stock meet criteria (price > 700, stock < 50).
# Solution:
# items = [{"name": "Laptop", "price": 999.99, "stock": 30}, 
#          {"name": "Smartphone", "price": 699.99, "stock": 100}]
# for item in items:
#     for key, value in item.items():
#         if item["price"] > 700 and item["stock"] < 50:
#             print("Exercise 3 - Criteria met for", item["name"])
#             break
#         print("Exercise 3 - Checking", key, value)
# # Output: Checking name Laptop, ..., Criteria met for Laptop

# Notes:
# - Break only exits the innermost loop; use multiple breaks or flags for outer loops.
# - Use in ML for early stopping (e.g., training loops) or web apps for search termination.
# - Combine with conditionals for precise control.