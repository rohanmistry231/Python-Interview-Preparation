# If-Else Projects
# Purpose: Apply If-Else statements through 5 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Price Tier Classifier
# Difficulty: Basic
# Description: Classify a product based on its price tier.
# Objective: Practice basic if-else with comparison operators.
# Tasks:
# - Create a variable for product price.
# - If price > 1000, classify as "Luxury"; otherwise, "Budget".
# - Print the classification.
price = 1200
if price > 1000:
    classification = "Luxury"
else:
    classification = "Budget"
print("Classification:", classification)

# %% Project 2: Stock Alert System
# Difficulty: Basic
# Description: Generate an alert based on stock level.
# Objective: Use if-else with a single condition.
# Tasks:
# - Create a variable for stock quantity.
# - If stock < 10, print "Critical stock"; otherwise, "Stock OK".
# - Print the alert.
stock = 5
if stock < 10:
    alert = "Critical stock"
else:
    alert = "Stock OK"
print("Alert:", alert)

# %% Project 3: Order Validator
# Difficulty: Intermediate
# Description: Validate an order based on price and quantity.
# Objective: Use if-else with logical operators (and).
# Tasks:
# - Create variables for order price and quantity.
# - If price > 500 and quantity > 0, print "Valid order"; otherwise, "Invalid order".
# - Print the validation result.
order_price = 600
order_quantity = 2
if order_price > 500 and order_quantity > 0:
    validation = "Valid order"
else:
    validation = "Invalid order"
print("Validation:", validation)

# %% Project 4: Category-Based Pricing
# Difficulty: Intermediate
# Description: Adjust pricing based on product category.
# Objective: Use if-else with dictionary data and string comparison.
# Tasks:
# - Create a dictionary with product name, price, and category.
# - If category is "Electronics", increase price by 10%; otherwise, keep original.
# - Print the product with updated price.
product = {"name": "Laptop", "price": 1000, "category": "Electronics"}
if product["category"] == "Electronics":
    product["price"] *= 1.1
print("Updated product:", product)

# %% Project 5: Shipping Cost Calculator
# Difficulty: Advanced
# Description: Calculate shipping cost based on order details.
# Objective: Use if-else with multiple conditions and data processing.
# Tasks:
# - Create a dictionary with order weight, total, and express shipping flag.
# - If weight > 5 or total > 1000, set base cost to $20; otherwise, $10.
# - If express is True, add $15 to cost.
# - Print the shipping cost.
order = {"weight": 6, "total": 800, "express": True}
if order["weight"] > 5 or order["total"] > 1000:
    cost = 20
else:
    cost = 10
if order["express"]:
    cost += 15
print("Shipping cost:", cost)