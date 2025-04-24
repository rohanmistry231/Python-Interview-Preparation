# Python Control Flow: Nested Conditionals

# Purpose: Nested conditionals allow conditions within conditions for complex logic.
# Key Features: Hierarchical decision-making.

# 1. Basic Nested If
# Explanation: Place if statements inside another if or else block.
# Example:
price = 999.99
stock = 50
if price > 500:
    if stock < 100:
        print("High-value, low-stock product")
    else:
        print("High-value, well-stocked product")
else:
    print("Budget product")
# Output: High-value, low-stock product

# 2. Nested If-Elif
# Explanation: Combine nested if with elif for multiple inner conditions.
# Example:
category = "Electronics"
price = 699.99
if category == "Electronics":
    if price > 1000:
        print("Premium Electronics")
    elif price > 500:
        print("Mid-range Electronics")
    else:
        print("Budget Electronics")
else:
    print("Non-Electronics product")
# Output: Mid-range Electronics

# 3. Deep Nesting
# Explanation: Handle multiple levels of conditions (use sparingly for readability).
# Example:
product = {"category": "Appliances", "price": 49.99, "stock": 20}
if product["category"] in ["Electronics", "Appliances"]:
    if product["price"] > 100:
        if product["stock"] < 50:
            print("High-price, low-stock tech")
        else:
            print("High-price, sufficient stock")
    else:
        print("Low-price tech")
else:
    print("Non-tech product")
# Output: Low-price tech

# Exercise 1: Check if a product is expensive (> 500) and low-stock (< 30), printing appropriate status.
# Solution:
# price = 600
# stock = 25
# if price > 500:
#     if stock < 30:
#         print("Expensive and low-stock")
#     else:
#         print("Expensive but sufficient stock")
# else:
#     print("Not expensive")
# # Output: Expensive and low-stock

# Exercise 2: Nest conditions to categorize a product by category (Electronics/Other) and price (High > 700, Low <= 700).
# Solution:
# category = "Electronics"
# price = 650
# if category == "Electronics":
#     if price > 700:
#         print("High-price Electronics")
#     else:
#         print("Low-price Electronics")
# else:
#     print("Other category")
# # Output: Low-price Electronics

# Exercise 3: Use nested conditionals to check if a product is in stock (> 0), affordable (<= 500), and in Electronics.
# Solution:
# stock = 10
# price = 400
# category = "Electronics"
# if stock > 0:
#     if price <= 500:
#         if category == "Electronics":
#             print("Affordable Electronics in stock")
#         else:
#             print("Affordable non-Electronics")
#     else:
#         print("Expensive product")
# else:
#     print("Out of stock")
# # Output: Affordable Electronics in stock

# Notes:
# - Nested conditionals are powerful but can reduce readability; consider refactoring with functions or logical operators.
# - Use in ML for complex feature engineering (e.g., nested rules for classification) or web apps for user permissions.
# - Limit nesting depth to 2-3 levels for maintainability.