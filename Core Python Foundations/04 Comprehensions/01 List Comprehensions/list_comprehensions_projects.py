# List Comprehensions Projects
# Purpose: Apply List Comprehensions through 10 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions cover Basic, Conditional, and Nested List Comprehensions using retail-themed examples.

# %% Project 1: Price Formatter
# Difficulty: Basic
# Description: Format a list of prices with a 10% discount.
# Objective: Practice basic list comprehension for simple transformations.
# Tasks:
# - Create a list of product prices.
# - Use a list comprehension to apply a 10% discount to each price.
# - Print the discounted prices.
prices = [100, 250, 500, 750]
discounted_prices = [price * 0.9 for price in prices]
print("Project 1 - Discounted prices:", discounted_prices)
# Output: Discounted prices: [90.0, 225.0, 450.0, 675.0]

# %% Project 2: Stock Multiplier
# Difficulty: Basic
# Description: Double the stock quantities for inventory planning.
# Objective: Use basic list comprehension to transform quantities.
# Tasks:
# - Create a list of stock quantities.
# - Use a list comprehension to double each quantity.
# - Print the doubled quantities.
stock = [10, 20, 30, 40]
doubled_stock = [qty * 2 for qty in stock]
print("Project 2 - Doubled stock:", doubled_stock)
# Output: Doubled stock: [20, 40, 60, 80]

# %% Project 3: Expensive Product Filter
# Difficulty: Basic
# Description: Filter products with prices above 200.
# Objective: Practice list comprehension with a condition.
# Tasks:
# - Create a list of tuples with product names and prices.
# - Use a list comprehension to extract names of products with prices > 200.
# - Print the filtered product names.
product_prices = [("Laptop", 999.99), ("Mouse", 29.99), ("Smartphone", 699.99), ("Blender", 149.99)]
expensive_products = [name for name, price in product_prices if price > 200]
print("Project 3 - Expensive products:", expensive_products)
# Output: Expensive products: ['Laptop', 'Smartphone']

# %% Project 4: Electronics Category Filter
# Difficulty: Intermediate
# Description: Filter products belonging to the Electronics category.
# Objective: Use list comprehension with a condition on dictionary data.
# Tasks:
# - Create a list of dictionaries with product name and category.
# - Use a list comprehension to extract names of Electronics products.
# - Print the filtered product names.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Blender", "category": "Appliances"},
    {"name": "Smartphone", "category": "Electronics"},
    {"name": "Toaster", "category": "Appliances"}
]
electronics = [p["name"] for p in products if p["category"] == "Electronics"]
print("Project 4 - Electronics products:", electronics)
# Output: Electronics products: ['Laptop', 'Smartphone']

# %% Project 5: Formatted Order IDs
# Difficulty: Intermediate
# Description: Generate formatted order IDs with a prefix.
# Objective: Use list comprehension for string formatting.
# Tasks:
# - Create a list of order numbers.
# - Use a list comprehension to format each as "ORD-XXX" (zero-padded).
# - Print the formatted order IDs.
order_numbers = [1, 15, 100, 999]
formatted_orders = [f"ORD-{num:03d}" for num in order_numbers]
print("Project 5 - Formatted order IDs:", formatted_orders)
# Output: Formatted order IDs: ['ORD-001', 'ORD-015', 'ORD-100', 'ORD-999']

# %% Project 6: Nested Category Pairs
# Difficulty: Intermediate
# Description: Generate product-category pairs for specific categories.
# Objective: Practice nested list comprehension with conditions.
# Tasks:
# - Create lists of products and categories.
# - Use a nested list comprehension to pair products with Electronics or Appliances categories.
# - Print the product-category pairs.
products = ["Mouse", "Toaster", "Tablet"]
categories = ["Electronics", "Appliances", "Furniture"]
product_pairs = [f"{p} in {c}" for c in categories if c in ["Electronics", "Appliances"] for p in products]
print("Project 6 - Product-category pairs:", product_pairs)
# Output: Product-category pairs: ['Mouse in Electronics', 'Toaster in Electronics', 'Tablet in Electronics',
#                                'Mouse in Appliances', 'Toaster in Appliances', 'Tablet in Appliances']

# %% Project 7: Stock Status Tagger
# Difficulty: Intermediate
# Description: Tag products based on stock levels.
# Objective: Use list comprehension with conditional expressions.
# Tasks:
# - Create a list of dictionaries with product name and stock.
# - Use a list comprehension to tag products as "Low" (< 20) or "Sufficient" (>= 20).
# - Print the tagged products.
inventory = [
    {"name": "Laptop", "stock": 15},
    {"name": "Mouse", "stock": 50},
    {"name": "Tablet", "stock": 5},
    {"name": "Keyboard", "stock": 30}
]
stock_status = [f"{p['name']}: {'Low' if p['stock'] < 20 else 'Sufficient'}" for p in inventory]
print("Project 7 - Stock status:", stock_status)
# Output: Stock status: ['Laptop: Low', 'Mouse: Sufficient', 'Tablet: Low', 'Keyboard: Sufficient']

# %% Project 8: Price Range Buckets
# Difficulty: Advanced
# Description: Categorize products into price buckets.
# Objective: Use list comprehension with multiple conditions for categorization.
# Tasks:
# - Create a list of dictionaries with product name and price.
# - Use a list comprehension to categorize prices as "Budget" (<= 100), "Mid-range" (101-500), or "Premium" (> 500).
# - Print the categorized products.
products = [
    {"name": "Mouse", "price": 29.99},
    {"name": "Laptop", "price": 999.99},
    {"name": "Tablet", "price": 299.99},
    {"name": "Headphones", "price": 89.99}
]
price_buckets = [f"{p['name']}: {'Budget' if p['price'] <= 100 else 'Mid-range' if p['price'] <= 500 else 'Premium'}" for p in products]
print("Project 8 - Price buckets:", price_buckets)
# Output: Price buckets: ['Mouse: Budget', 'Laptop: Premium', 'Tablet: Mid-range', 'Headphones: Budget']

# %% Project 9: Nested Order Summary
# Difficulty: Advanced
# Description: Generate a summary of orders across regions and products.
# Objective: Use nested list comprehension with complex data structures.
# Tasks:
# - Create a list of dictionaries with region and products (list of product names).
# - Use a nested list comprehension to create summaries like "Product in Region".
# - Print the order summaries.
orders = [
    {"region": "North", "products": ["Laptop", "Mouse"]},
    {"region": "South", "products": ["Tablet", "Keyboard"]}
]
order_summaries = [f"{p} in {o['region']}" for o in orders for p in o["products"]]
print("Project 9 - Order summaries:", order_summaries)
# Output: Order summaries: ['Laptop in North', 'Mouse in North', 'Tablet in South', 'Keyboard in South']

# %% Project 10: Dynamic Price Adjustments
# Difficulty: Advanced
# Description: Adjust prices based on category and stock levels.
# Objective: Combine nested conditions and transformations in a list comprehension.
# Tasks:
# - Create a list of dictionaries with product name, price, category, and stock.
# - Use a list comprehension to increase Electronics prices by 10% if stock < 20, decrease others by 5%.
# - Print the adjusted prices.
products = [
    {"name": "Laptop", "price": 1000, "category": "Electronics", "stock": 15},
    {"name": "Blender", "price": 100, "category": "Appliances", "stock": 30},
    {"name": "Tablet", "price": 500, "category": "Electronics", "stock": 10},
    {"name": "Toaster", "price": 50, "category": "Appliances", "stock": 25}
]
adjusted_prices = [
    {"name": p["name"], "price": p["price"] * 1.1 if p["category"] == "Electronics" and p["stock"] < 20 else p["price"] * 0.95}
    for p in products
]
print("Project 10 - Adjusted prices:", adjusted_prices)
# Output: Adjusted prices: [{'name': 'Laptop', 'price': 1100.0}, {'name': 'Blender', 'price': 95.0},
#                          {'name': 'Tablet', 'price': 550.0}, {'name': 'Toaster', 'price': 47.5}]