# Python Control Flow: If-Else Statements
# Purpose: Learn If-Else statements to execute code blocks based on conditions.
# Key Features: Conditional branching for binary decision-making, foundational for control flow.

# %% 1. Basic If-Else
# Explanation: If the condition evaluates to True, execute the if-block; otherwise, execute the else-block.
# Use for simple decisions (e.g., thresholding values).
price = 999.99
if price > 500:
    print("1.1 Premium product")
else:
    print("1.1 Standard product")
# Example with boolean
is_available = True
if is_available:
    print("1.2 Product in stock")
else:
    print("1.2 Out of stock")

# Mini-Exercise: Check if a quantity is positive and print "Valid quantity" or "Invalid quantity".
quantity = 10
if quantity > 0:
    print("1.3 Mini-Exercise: Valid quantity")
else:
    print("1.3 Mini-Exercise: Invalid quantity")

# %% 2. Multiple Conditions
# Explanation: Combine conditions using logical operators: and (both true), or (either true), not (inverts).
# Useful for complex decision rules (e.g., filtering items).
stock = 50
if price > 500 and stock < 100:
    print("2.1 High-value, low-stock item")
else:
    print("2.1 Regular item")
# Example with or
category = "Electronics"
if price > 1000 or category == "Electronics":
    print("2.2 Special handling required")
else:
    print("2.2 Standard handling")

# Mini-Exercise: Check if quantity is between 5 and 20 (inclusive) and print "Moderate stock" or "Check stock".
if 5 <= quantity <= 20:
    print("2.3 Mini-Exercise: Moderate stock")
else:
    print("2.3 Mini-Exercise: Check stock")

# %% 3. Using If-Else with Data
# Explanation: Apply if-else to process structured data (e.g., dictionaries, lists) for real-world tasks.
# Common in data processing or user input validation.
product = {"name": "Laptop Pro", "price": 999.99, "category": "Electronics"}
if product["price"] >= 700:
    product["status"] = "Premium"
else:
    product["status"] = "Standard"
print("3.1 Product with status:", product)
# Example with list
prices = [200, 1200, 600]
if max(prices) > 1000:
    print("3.2 Contains high-end item")
else:
    print("3.2 All standard items")

# Mini-Exercise: Add a "Low Stock" flag to product if stock < 30, else "Sufficient".
product["stock"] = 25
if product["stock"] < 30:
    product["low_stock"] = True
else:
    product["low_stock"] = False
print("3.3 Mini-Exercise: Updated product:", product)

# %% 4. Exercises for Practice
# Exercise 1: Check if a product’s stock is below 20 and print "Restock needed" or "Stock sufficient".
stock_quantity = 15
if stock_quantity < 20:
    print("4.1 Exercise 1 - Restock needed")
else:
    print("4.1 Exercise 1 - Stock sufficient")

# Exercise 2: Assign a discount (10% if price > 1000, 5% otherwise) and print the discounted price.
item_price = 1200
if item_price > 1000:
    discount = 0.1
else:
    discount = 0.05
discounted_price = item_price * (1 - discount)
print("4.2 Exercise 2 - Discounted price:", discounted_price)

# Exercise 3: Check if a product is in the "Electronics" category and print "Tech item" or "Non-tech item".
product_category = "Appliances"
if product_category == "Electronics":
    print("4.3 Exercise 3 - Tech item")
else:
    print("4.3 Exercise 3 - Non-tech item")

# Exercise 4: Check if a product’s price is between 500 and 1000 and stock > 10, print "Good deal" or "Check offer".
price_check = 800
stock_check = 15
if 500 <= price_check <= 1000 and stock_check > 10:
    print("4.4 Exercise 4 - Good deal")
else:
    print("4.4 Exercise 4 - Check offer")

# %% 5. Notes for Further Learning
# - Conditions must evaluate to True/False (e.g., ==, >, <, and, or, not).
# - If-Else is ideal for binary decisions in ML (e.g., feature thresholding) or web apps (e.g., user role checks).
# - Avoid deep nesting for readability; use elif or nested conditionals when needed.
# - Use clear variable names and comments to document decision logic.
# - Try the projects below to apply these concepts!