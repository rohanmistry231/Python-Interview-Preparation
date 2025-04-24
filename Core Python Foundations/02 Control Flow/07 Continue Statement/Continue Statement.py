# Python Control Flow: Continue Statement

# Purpose: Continue statement skips the rest of the current loop iteration and moves to the next.
# Key Features: Selective iteration control.

# 1. Continue in For Loop
# Explanation: Skip iteration when a condition is met, continue with next item.
# Example:
prices = [100, 999.99, 50, 700, 25]
for price in prices:
    if price < 100:
        continue
    print(f"Price above 100: {price}")
# Output: Price above 100: 100, Price above 100: 999.99, Price above 100: 700

# 2. Continue in While Loop
# Explanation: Skip iteration in while loop, re-evaluate condition.
# Example:
stock = 100
while stock > 0:
    stock -= 20
    if stock % 40 == 0:
        continue
    print(f"Stock level: {stock}")
# Output: Stock level: 80, Stock level: 60, Stock level: 20

# 3. Continue in Nested Loops
# Explanation: Skips only the innermost loop’s current iteration.
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker"]
categories = ["Electronics", "Appliances"]
for product in products:
    for category in categories:
        if category == "Appliances":
            continue
        print(f"Checking {product} in {category}")
# Output: Checking Laptop in Electronics, Checking Smartphone in Electronics, ...

# Exercise 1: Skip prices below 200 in a for loop over a list of prices.
# Solution:
# prices = [150, 300, 50, 400]
# for price in prices:
#     if price < 200:
#         continue
#     print("Exercise 1 - Price:", price)
# # Output: Price: 300, Price: 400

# Exercise 2: Use continue in a while loop to skip stock levels that are even.
# Solution:
# stock = 50
# while stock > 0:
#     stock -= 10
#     if stock % 2 == 0:
#         continue
#     print("Exercise 2 - Odd stock level:", stock)
# # Output: Odd stock level: 30, Odd stock level: 10

# Exercise 3: Skip non-Electronics products in a nested loop over products and attributes.
# Solution:
# items = [{"name": "Laptop", "category": "Electronics"}, 
#          {"name": "Blender", "category": "Appliances"}]
# for item in items:
#     for key, value in item.items():
#         if item["category"] != "Electronics":
#             continue
#         print("Exercise 3 - Electronics attribute:", key, value)
# # Output: Electronics attribute: name Laptop, Electronics attribute: category Electronics

# Notes:
# - Continue skips to the next iteration without exiting the loop.
# - Use in ML for filtering data during preprocessing or web apps for selective processing.
# - Avoid overusing continue to maintain code clarity.