# Python Control Flow: If-Else Statements

# Purpose: If-Else statements execute code blocks based on a condition’s truth value.
# Key Features: Conditional branching for decision-making.

# 1. Basic If-Else
# Explanation: If condition is True, execute if-block; otherwise, execute else-block.
# Example:
price = 999.99
if price > 500:
    print("Premium product")
else:
    print("Standard product")
# Output: Premium product

# 2. Multiple Conditions
# Explanation: Combine conditions using and, or, not operators.
# Example:
stock = 50
if price > 500 and stock < 100:
    print("High-value, low-stock item")
else:
    print("Regular item")
# Output: High-value, low-stock item

# 3. Using If-Else with Data
# Explanation: Apply if-else to process real-world data (e.g., product categorization).
# Example:
product = {"name": "Laptop Pro", "price": 999.99, "category": "Electronics"}
if product["price"] >= 700:
    product["status"] = "Premium"
else:
    product["status"] = "Standard"
print("Product with status:", product)
# Output: {'name': 'Laptop Pro', 'price': 999.99, 'category': 'Electronics', 'status': 'Premium'}

# Exercise 1: Check if a product’s stock is below 20 and print "Restock needed" or "Stock sufficient".
# Solution:
# stock_quantity = 15
# if stock_quantity < 20:
#     print("Restock needed")
# else:
#     print("Stock sufficient")
# # Output: Restock needed

# Exercise 2: Assign a discount (10% if price > 1000, 5% otherwise) and print the discounted price.
# Solution:
# item_price = 1200
# if item_price > 1000:
#     discount = 0.1
# else:
#     discount = 0.05
# discounted_price = item_price * (1 - discount)
# print("Exercise 2 - Discounted price:", discounted_price)
# # Output: 1080.0

# Exercise 3: Check if a product is in the "Electronics" category and print "Tech item" or "Non-tech item".
# Solution:
# product_category = "Appliances"
# if product_category == "Electronics":
#     print("Tech item")
# else:
#     print("Non-tech item")
# # Output: Non-tech item

# Notes:
# - Conditions must evaluate to True/False (e.g., comparisons, boolean operations).
# - Use if-else for simple binary decisions in ML (e.g., feature thresholding) or web apps (e.g., user role checks).
# - Avoid deep nesting for readability (see Nested Conditionals).
