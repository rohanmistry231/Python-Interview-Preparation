# Python Control Flow: Nested Conditionals
# Purpose: Learn Nested Conditionals to handle conditions within conditions for complex logic.
# Key Features: Hierarchical decision-making for detailed rules.

# %% 1. Basic Nested If
# Explanation: Place if statements inside another if or else block for sequential checks.
# Useful for multi-level decisions (e.g., product prioritization).
price = 999.99
stock = 50
if price > 500:
    if stock < 100:
        print("1.1 High-value, low-stock product")
    else:
        print("1.1 High-value, well-stocked product")
else:
    print("1.1 Budget product")
# Example with boolean
is_active = True
if is_active:
    if stock > 0:
        print("1.2 Product available")
    else:
        print("1.2 Product out of stock")
else:
    print("1.2 Product discontinued")

# Mini-Exercise: Check if a product is on sale (price < 300) and in stock (> 0).
sale_price = 250
sale_stock = 10
if sale_price < 300:
    if sale_stock > 0:
        print("1.3 Mini-Exercise: On sale and in stock")
    else:
        print("1.3 Mini-Exercise: On sale but out of stock")
else:
    print("1.3 Mini-Exercise: Not on sale")

# %% 2. Nested If-Elif
# Explanation: Combine nested if with elif for multiple inner conditions.
# Common in category-based processing.
category = "Electronics"
price = 699.99
if category == "Electronics":
    if price > 1000:
        print("2.1 Premium Electronics")
    elif price > 500:
        print("2.1 Mid-range Electronics")
    else:
        print("2.1 Budget Electronics")
else:
    print("2.1 Non-Electronics product")
# Example with multiple categories
if category in ["Electronics", "Appliances"]:
    if price > 700:
        print("2.2 High-end tech")
    else:
        print("2.2 Standard tech")
else:
    print("2.2 Non-tech")

# Mini-Exercise: Check if a product is "Appliances" and price > 200.
app_category = "Appliances"
app_price = 250
if app_category == "Appliances":
    if app_price > 200:
        print("2.3 Mini-Exercise: Expensive Appliance")
    else:
        print("2.3 Mini-Exercise: Affordable Appliance")
else:
    print("2.3 Mini-Exercise: Not an Appliance")

# %% 3. Deep Nesting
# Explanation: Handle multiple levels of conditions, but use sparingly to maintain readability.
# Useful for complex business rules.
product = {"category": "Appliances", "price": 49.99, "stock": 20}
if product["category"] in ["Electronics", "Appliances"]:
    if product["price"] > 100:
        if product["stock"] < 50:
            print("3.1 High-price, low-stock tech")
        else:
            print("3.1 High-price, sufficient stock")
    else:
        print("3.1 Low-price tech")
else:
    print("3.1 Non-tech product")
# Example with three levels
if product["stock"] > 0:
    if product["price"] < 100:
        if product["category"] == "Appliances":
            print("3.2 Affordable, in-stock Appliance")
        else:
            print("3.2 Affordable, in-stock non-Appliance")
    else:
        print("3.2 Expensive product")
else:
    print("3.2 Out of stock")

# Mini-Exercise: Check if a product is in stock (> 0), cheap (< 50), and Electronics.
mini_product = {"category": "Electronics", "price": 40, "stock": 5}
if mini_product["stock"] > 0:
    if mini_product["price"] < 50:
        if mini_product["category"] == "Electronics":
            print("3.3 Mini-Exercise: Cheap Electronics in stock")
        else:
            print("3.3 Mini-Exercise: Cheap non-Electronics")
    else:
        print("3.3 Mini-Exercise: Expensive product")
else:
    print("3.3 Mini-Exercise: Out of stock")

# %% 4. Exercises for Practice
# Exercise 1: Check if a product is expensive (> 500) and low-stock (< 30), printing appropriate status.
price = 600
stock = 25
if price > 500:
    if stock < 30:
        print("4.1 Exercise 1 - Expensive and low-stock")
    else:
        print("4.1 Exercise 1 - Expensive but sufficient stock")
else:
    print("4.1 Exercise 1 - Not expensive")

# Exercise 2: Nest conditions to categorize a product by category (Electronics/Other) and price (High > 700, Low <= 700).
category = "Electronics"
price = 650
if category == "Electronics":
    if price > 700:
        print("4.2 Exercise 2 - High-price Electronics")
    else:
        print("4.2 Exercise 2 - Low-price Electronics")
else:
    print("4.2 Exercise 2 - Other category")

# Exercise 3: Use nested conditionals to check if a product is in stock (> 0), affordable (<= 500), and in Electronics.
stock = 10
price = 400
category = "Electronics"
if stock > 0:
    if price <= 500:
        if category == "Electronics":
            print("4.3 Exercise 3 - Affordable Electronics in stock")
        else:
            print("4.3 Exercise 3 - Affordable non-Electronics")
    else:
        print("4.3 Exercise 3 - Expensive product")
else:
    print("4.3 Exercise 3 - Out of stock")

# Exercise 4: Check if a product is in a tech category, low-stock (< 20), and high-price (> 800).
tech_product = {"category": "Electronics", "stock": 15, "price": 900}
if tech_product["category"] in ["Electronics", "Appliances"]:
    if tech_product["stock"] < 20:
        if tech_product["price"] > 800:
            print("4.4 Exercise 4 - High-price, low-stock tech")
        else:
            print("4.4 Exercise 4 - Low-price, low-stock tech")
    else:
        print("4.4 Exercise 4 - Sufficient stock tech")
else:
    print("4.4 Exercise 4 - Non-tech product")

# %% 5. Notes for Further Learning
# - Nested conditionals enable complex logic but can reduce readability; limit to 2-3 levels.
# - Refactor deep nesting with functions, logical operators, or dictionaries for clarity.
# - Use in ML for feature engineering (e.g., nested rules for classification) or web apps for permissions.
# - Test nested conditions thoroughly to ensure all paths are covered.
# - Try the projects below to apply these concepts!