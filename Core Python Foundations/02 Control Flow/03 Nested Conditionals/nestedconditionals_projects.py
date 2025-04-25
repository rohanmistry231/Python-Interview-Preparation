# Nested Conditionals Projects
# Purpose: Apply Nested Conditionals through 5 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Stock Price Checker
# Difficulty: Basic
# Description: Check product price and stock for restocking needs.
# Objective: Practice basic nested if statements.
# Tasks:
# - Create variables for price and stock.
# - If price > 500, check if stock < 30; print "Restock expensive item" or "Sufficient stock".
# - Else print "Budget item".
# - Print the result.
price = 600
stock = 25
if price > 500:
    if stock < 30:
        result = "Restock expensive item"
    else:
        result = "Sufficient stock"
else:
    result = "Budget item"
print(result)

# %% Project 2: Category Stock Validator
# Difficulty: Basic
# Description: Validate stock for specific categories.
# Objective: Use nested if with string comparison.
# Tasks:
# - Create variables for category and stock.
# - If category is "Electronics", check if stock > 0; print "In stock" or "Out of stock".
# - Else print "Non-Electronics".
# - Print the result.
category = "Electronics"
stock = 10
if category == "Electronics":
    if stock > 0:
        result = "In stock"
    else:
        result = "Out of stock"
else:
    result = "Non-Electronics"
print(result)

# %% Project 3: Tech Product Pricer
# Difficulty: Intermediate
# Description: Price products based on category and stock.
# Objective: Use nested if-elif with dictionary data.
# Tasks:
# - Create a dictionary with category, price, and stock.
# - If category in ["Electronics", "Appliances"], check price > 500; if stock < 50, tag "Priority"; else "Standard".
# - Else tag "Non-Tech".
# - Print the product with tag.
product = {"category": "Electronics", "price": 600, "stock": 20}
if product["category"] in ["Electronics", "Appliances"]:
    if product["price"] > 500:
        if product["stock"] < 50:
            product["tag"] = "Priority"
        else:
            product["tag"] = "Standard"
    else:
        product["tag"] = "Standard"
else:
    product["tag"] = "Non-Tech"
print("Updated product:", product)

# %% Project 4: Order Approval System
# Difficulty: Intermediate
# Description: Approve orders based on multiple criteria.
# Objective: Use deep nesting with logical conditions.
# Tasks:
# - Create a dictionary with order total, items, and express flag.
# - If total > 1000, check items > 0; if express, approve "Express Order"; else "Standard Order".
# - Else print "Invalid Order".
# - Print the result.
order = {"total": 1500, "items": 3, "express": True}
if order["total"] > 1000:
    if order["items"] > 0:
        if order["express"]:
            result = "Express Order"
        else:
            result = "Standard Order"
    else:
        result = "Invalid Order"
else:
    result = "Invalid Order"
print(result)

# %% Project 5: Inventory Audit System
# Difficulty: Advanced
# Description: Audit inventory based on multiple conditions.
# Objective: Use deep nesting with complex data processing.
# Tasks:
# - Create a dictionary with category, price, stock, and is_tech flag.
# - If is_tech, check price > 700; if stock < 30, flag "Critical"; else "Monitor".
# - If not is_tech, check stock < 50; flag "Restock" or "Sufficient".
# - Print the audit result.
inventory = {"category": "Electronics", "price": 800, "stock": 25, "is_tech": True}
if inventory["is_tech"]:
    if inventory["price"] > 700:
        if inventory["stock"] < 30:
            audit_result = "Critical"
        else:
            audit_result = "Monitor"
    else:
        audit_result = "Monitor"
else:
    if inventory["stock"] < 50:
        audit_result = "Restock"
    else:
        audit_result = "Sufficient"
print("Audit result:", audit_result)