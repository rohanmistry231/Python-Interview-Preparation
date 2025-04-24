# Python Control Flow: Elif Statements

# Purpose: Elif statements allow multiple conditions to be checked sequentially.
# Key Features: Extends if-else for multi-way branching.

# 1. Basic If-Elif-Else
# Explanation: Check conditions in order; execute the first True block or else-block.
# Example:
price = 699.99
if price > 1000:
    print("Luxury product")
elif price > 500:
    print("Mid-range product")
else:
    print("Budget product")
# Output: Mid-range product

# 2. Multiple Elif Clauses
# Explanation: Use multiple elif clauses for granular conditions.
# Example:
stock = 30
if stock > 100:
    print("Overstocked")
elif stock > 50:
    print("Well-stocked")
elif stock > 20:
    print("Moderately stocked")
else:
    print("Low stock")
# Output: Moderately stocked

# 3. Elif with Complex Conditions
# Explanation: Combine with and/or for complex decision-making.
# Example:
product = {"name": "Smartphone", "price": 699.99, "stock": 100}
if product["price"] > 1000 and product["stock"] < 50:
    print("High-value, low-stock")
elif product["price"] > 500 and product["stock"] >= 50:
    print("High-value, sufficient stock")
elif product["price"] <= 500:
    print("Affordable product")
# Output: High-value, sufficient stock

# Exercise 1: Categorize a product price as "Cheap" (< 100), "Moderate" (100-500), or "Expensive" (> 500).
# Solution:
# price = 250
# if price < 100:
#     print("Cheap")
# elif price <= 500:
#     print("Moderate")
# else:
#     print("Expensive")
# # Output: Moderate

# Exercise 2: Assign a stock status: "Critical" (< 10), "Low" (10-30), "Normal" (31-100), or "High" (> 100).
# Solution:
# stock_level = 25
# if stock_level < 10:
#     print("Critical")
# elif stock_level <= 30:
#     print("Low")
# elif stock_level <= 100:
#     print("Normal")
# else:
#     print("High")
# # Output: Low

# Exercise 3: Check a product’s category and price to assign a tag: "Premium Tech" (Electronics, > 700), 
# "Standard Tech" (Electronics, <= 700), or "Non-Tech".
# Solution:
# category = "Electronics"
# price = 800
# if category == "Electronics" and price > 700:
#     print("Premium Tech")
# elif category == "Electronics":
#     print("Standard Tech")
# else:
#     print("Non-Tech")
# # Output: Premium Tech

# Notes:
# - Elif reduces nested if statements, improving readability.
# - Use in ML for feature categorization (e.g., binning values) or web apps for tiered pricing.
# - Only the first True condition’s block executes.