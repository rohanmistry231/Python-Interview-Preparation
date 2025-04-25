# Python Control Flow: Elif Statements
# Purpose: Learn Elif statements to check multiple conditions sequentially.
# Key Features: Extends if-else for multi-way branching, improves readability.

# %% 1. Basic If-Elif-Else
# Explanation: Check conditions in order; execute the first True block, or else-block if none are True.
# Ideal for categorizing data with multiple tiers.
price = 699.99
if price > 1000:
    print("1.1 Luxury product")
elif price > 500:
    print("1.1 Mid-range product")
else:
    print("1.1 Budget product")
# Example with boolean
stock_alert = 30
if stock_alert < 10:
    print("1.2 Critical alert")
elif stock_alert <= 50:
    print("1.2 Warning alert")
else:
    print("1.2 No alert")

# Mini-Exercise: Classify a score (0-100) as "Fail" (< 60), "Pass" (60-80), or "Excellent" (> 80).
score = 75
if score < 60:
    print("1.3 Mini-Exercise: Fail")
elif score <= 80:
    print("1.3 Mini-Exercise: Pass")
else:
    print("1.3 Mini-Exercise: Excellent")

# %% 2. Multiple Elif Clauses
# Explanation: Use multiple elif clauses for fine-grained conditions, stopping at the first True.
# Useful for tiered pricing or inventory management.
stock = 30
if stock > 100:
    print("2.1 Overstocked")
elif stock > 50:
    print("2.1 Well-stocked")
elif stock > 20:
    print("2.1 Moderately stocked")
else:
    print("2.1 Low stock")
# Example with ranges
price_level = 1200
if price_level > 2000:
    print("2.2 Ultra-premium")
elif price_level > 1000:
    print("2.2 Premium")
elif price_level > 500:
    print("2.2 Mid-tier")
else:
    print("2.2 Entry-level")

# Mini-Exercise: Categorize age as "Child" (< 13), "Teen" (13-19), "Adult" (20-64), or "Senior" (65+).
age = 25
if age < 13:
    print("2.3 Mini-Exercise: Child")
elif age <= 19:
    print("2.3 Mini-Exercise: Teen")
elif age <= 64:
    print("2.3 Mini-Exercise: Adult")
else:
    print("2.3 Mini-Exercise: Senior")

# %% 3. Elif with Complex Conditions
# Explanation: Combine elif with logical operators (and, or) for complex decision-making.
# Common in data filtering or business rules.
product = {"name": "Smartphone", "price": 699.99, "stock": 100}
if product["price"] > 1000 and product["stock"] < 50:
    print("3.1 High-value, low-stock")
elif product["price"] > 500 and product["stock"] >= 50:
    print("3.1 High-value, sufficient stock")
elif product["price"] <= 500:
    print("3.1 Affordable product")
# Example with or
if product["price"] > 1000 or product["stock"] < 20:
    print("3.2 Special monitoring")
else:
    print("3.2 Standard monitoring")

# Mini-Exercise: Tag a product as "Priority" (Electronics and stock < 30) or "Normal" (otherwise).
if product["stock"] < 30 and product["name"] == "Smartphone":
    print("3.3 Mini-Exercise: Priority")
else:
    print("3.3 Mini-Exercise: Normal")

# %% 4. Exercises for Practice
# Exercise 1: Categorize a product price as "Cheap" (< 100), "Moderate" (100-500), or "Expensive" (> 500).
price = 250
if price < 100:
    print("4.1 Exercise 1 - Cheap")
elif price <= 500:
    print("4.1 Exercise 1 - Moderate")
else:
    print("4.1 Exercise 1 - Expensive")

# Exercise 2: Assign a stock status: "Critical" (< 10), "Low" (10-30), "Normal" (31-100), or "High" (> 100).
stock_level = 25
if stock_level < 10:
    print("4.2 Exercise 2 - Critical")
elif stock_level <= 30:
    print("4.2 Exercise 2 - Low")
elif stock_level <= 100:
    print("4.2 Exercise 2 - Normal")
else:
    print("4.2 Exercise 2 - High")

# Exercise 3: Check a product’s category and price to assign a tag: "Premium Tech" (Electronics, > 700), 
# "Standard Tech" (Electronics, <= 700), or "Non-Tech".
category = "Electronics"
price = 800
if category == "Electronics" and price > 700:
    print("4.3 Exercise 3 - Premium Tech")
elif category == "Electronics":
    print("4.3 Exercise 3 - Standard Tech")
else:
    print("4.3 Exercise 3 - Non-Tech")

# Exercise 4: Categorize order size as "Small" (< 5 items), "Medium" (5-20), "Large" (21-50), or "Bulk" (> 50).
order_size = 15
if order_size < 5:
    print("4.4 Exercise 4 - Small")
elif order_size <= 20:
    print("4.4 Exercise 4 - Medium")
elif order_size <= 50:
    print("4.4 Exercise 4 - Large")
else:
    print("4.4 Exercise 4 - Bulk")

# %% 5. Notes for Further Learning
# - Elif statements reduce nested if-else, improving code readability.
# - Only the first True condition’s block executes; subsequent conditions are skipped.
# - Use in ML for feature categorization (e.g., binning values) or web apps for tiered pricing.
# - Combine with logical operators for complex rules, but keep conditions clear.
# - Try the projects below to apply these concepts!