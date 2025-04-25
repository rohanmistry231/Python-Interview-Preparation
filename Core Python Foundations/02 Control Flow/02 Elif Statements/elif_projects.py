# Elif Projects
# Purpose: Apply Elif statements through 5 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions are designed for clarity, efficiency, and beginner learning.

# %% Project 1: Price Range Classifier
# Difficulty: Basic
# Description: Classify a product’s price into multiple ranges.
# Objective: Practice basic if-elif-else with multiple conditions.
# Tasks:
# - Create a variable for product price.
# - Classify as "Cheap" (< 100), "Moderate" (100-500), or "Expensive" (> 500).
# - Print the classification.
price = 250
if price < 100:
    classification = "Cheap"
elif price <= 500:
    classification = "Moderate"
else:
    classification = "Expensive"
print("Classification:", classification)

# %% Project 2: Stock Status Tagger
# Difficulty: Basic
# Description: Tag stock levels with descriptive statuses.
# Objective: Use multiple elif clauses for categorization.
# Tasks:
# - Create a variable for stock quantity.
# - Tag as "Critical" (< 10), "Low" (10-30), or "Sufficient" (> 30).
# - Print the status.
stock = 25
if stock < 10:
    status = "Critical"
elif stock <= 30:
    status = "Low"
else:
    status = "Sufficient"
print("Status:", status)

# %% Project 3: Category Price Adjuster
# Difficulty: Intermediate
# Description: Adjust price based on product category and price tier.
# Objective: Use elif with complex conditions and dictionary data.
# Tasks:
# - Create a dictionary with product name, price, and category.
# - If Electronics and price > 700, tag "Premium Tech"; elif Electronics, tag "Standard Tech"; else "Other".
# - Print the product with tag.
product = {"name": "Smartphone", "price": 800, "category": "Electronics"}
if product["category"] == "Electronics" and product["price"] > 700:
    product["tag"] = "Premium Tech"
elif product["category"] == "Electronics":
    product["tag"] = "Standard Tech"
else:
    product["tag"] = "Other"
print("Updated product:", product)

# %% Project 4: Order Size Evaluator
# Difficulty: Intermediate
# Description: Evaluate order size for processing priority.
# Objective: Use multiple elif clauses with ranges.
# Tasks:
# - Create a variable for order size (number of items).
# - Classify as "Small" (< 5), "Medium" (5-20), "Large" (21-50), or "Bulk" (> 50).
# - Print the classification.
order_size = 15
if order_size < 5:
    size = "Small"
elif order_size <= 20:
    size = "Medium"
elif order_size <= 50:
    size = "Large"
else:
    size = "Bulk"
print("Order size:", size)

# %% Project 5: Discount Tier System
# Difficulty: Advanced
# Description: Apply discounts based on order total and customer status.
# Objective: Use elif with logical operators and data processing.
# Tasks:
# - Create a dictionary with order total and VIP status (True/False).
# - If total > 2000 and VIP, discount 15%; elif total > 2000, 10%; elif total > 500, 5%; else 0%.
# - Print the discounted total.
order = {"total": 2000, "vip": True}
if order["total"] > 2000 and order["vip"]:
    discount = 0.15
elif order["total"] > 2000:
    discount = 0.1
elif order["total"] > 500:
    discount = 0.05
else:
    discount = 0
discounted_total = order["total"] * (1 - discount)
print("Discounted total:", discounted_total)