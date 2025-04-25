# Set Comprehensions Projects
# Purpose: Apply Set Comprehensions through 10 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions cover Basic, Conditional, and Transforming Elements Set Comprehensions using retail-themed examples.

# %% Project 1: Unique Product Names
# Difficulty: Basic
# Description: Extract unique product names from a list with duplicates.
# Objective: Practice basic set comprehension for deduplication.
# Tasks:
# - Create a list of product names with duplicates.
# - Use a set comprehension to extract unique product names.
# - Print the unique product set.
products = ["Mouse", "Keyboard", "Mouse", "Monitor"]
unique_products = {product for product in products}
print("Project 1 - Unique products:", unique_products)
# Output: Unique products: {'Mouse', 'Keyboard', 'Monitor'}

# %% Project 2: Unique Order IDs
# Difficulty: Basic
# Description: Collect unique order IDs from a list with duplicates.
# Objective: Use basic set comprehension to ensure unique elements.
# Tasks:
# - Create a list of order IDs with duplicates.
# - Use a set comprehension to collect unique order IDs.
# - Print the unique order ID set.
order_ids = ["ORD-001", "ORD-002", "ORD-001", "ORD-003"]
unique_order_ids = {oid for oid in order_ids}
print("Project 2 - Unique order IDs:", unique_order_ids)
# Output: Unique order IDs: {'ORD-001', 'ORD-002', 'ORD-003'}

# %% Project 3: High Stock Filter
# Difficulty: Basic
# Description: Filter stock quantities above 50 from a list.
# Objective: Practice set comprehension with a condition.
# Tasks:
# - Create a list of stock quantities with duplicates.
# - Use a set comprehension to include quantities > 50.
# - Print the high stock set.
stock_quantities = [10, 60, 20, 75, 60]
high_stock = {qty for qty in stock_quantities if qty > 50}
print("Project 3 - High stock quantities:", high_stock)
# Output: High stock quantities: {60, 75}

# %% Project 4: Expensive Price Filter
# Difficulty: Intermediate
# Description: Filter prices above 500 from a list of product-price tuples.
# Objective: Use conditional set comprehension with tuple unpacking.
# Tasks:
# - Create a list of tuples with product names and prices.
# - Use a set comprehension to extract prices > 500.
# - Print the expensive price set.
product_prices = [("Laptop", 999.99), ("Mouse", 29.99), ("Smartphone", 699.99), ("Mouse", 29.99)]
expensive_prices = {price for _, price in product_prices if price > 500}
print("Project 4 - Expensive prices:", expensive_prices)
# Output: Expensive prices: {999.99, 699.99}

# %% Project 5: Uppercase Categories
# Difficulty: Intermediate
# Description: Convert category names to uppercase and remove duplicates.
# Objective: Use set comprehension with element transformation.
# Tasks:
# - Create a list of categories with duplicates.
# - Use a set comprehension to convert categories to uppercase.
# - Print the uppercase category set.
categories = ["Electronics", "Appliances", "Electronics", "Furniture"]
upper_categories = {cat.upper() for cat in categories}
print("Project 5 - Uppercase categories:", upper_categories)
# Output: Uppercase categories: {'ELECTRONICS', 'APPLIANCES', 'FURNITURE'}

# %% Project 6: Electronics Product Filter
# Difficulty: Intermediate
# Description: Extract unique product names from Electronics category.
# Objective: Use conditional set comprehension with dictionary data.
# Tasks:
# - Create a list of dictionaries with product name and category.
# - Use a set comprehension to extract names of Electronics products.
# - Print the Electronics product set.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Blender", "category": "Appliances"},
    {"name": "Smartphone", "category": "Electronics"},
    {"name": "Smartphone", "category": "Electronics"}
]
electronics_products = {p["name"] for p in products if p["category"] == "Electronics"}
print("Project 6 - Electronics products:", electronics_products)
# Output: Electronics products: {'Laptop', 'Smartphone'}

# %% Project 7: Formatted Price Tags
# Difficulty: Intermediate
# Description: Create unique price tags with currency formatting.
# Objective: Use set comprehension for string transformation.
# Tasks:
# - Create a list of prices with duplicates.
# - Use a set comprehension to format prices as "$X.XX".
# - Print the formatted price tag set.
prices = [29.99, 999.99, 29.99, 299.99]
price_tags = {f"${price:.2f}" for price in prices}
print("Project 7 - Price tags:", price_tags)
# Output: Price tags: {'$29.99', '$999.99', '$299.99'}

# %% Project 8: Unique Regions from Orders
# Difficulty: Advanced
# Description: Extract unique regions from a nested order structure.
# Objective: Use set comprehension with nested data iteration.
# Tasks:
# - Create a list of dictionaries with region and products.
# - Use a set comprehension to extract unique regions.
# - Print the unique region set.
orders = [
    {"region": "North", "products": ["Laptop", "Mouse"]},
    {"region": "South", "products": ["Tablet", "Keyboard"]},
    {"region": "North", "products": ["Monitor"]}
]
unique_regions = {o["region"] for o in orders}
print("Project 8 - Unique regions:", unique_regions)
# Output: Unique regions: {'North', 'South'}

# %% Project 9: Conditional Stock Status
# Difficulty: Advanced
# Description: Collect unique stock status labels based on quantity.
# Objective: Use set comprehension with conditional expressions.
# Tasks:
# - Create a list of dictionaries with product name and stock.
# - Use a set comprehension to collect status labels ("Low" for < 20, "Sufficient" for >= 20).
# - Print the status label set.
inventory = [
    {"name": "Laptop", "stock": 15},
    {"name": "Mouse", "stock": 50},
    {"name": "Tablet", "stock": 5},
    {"name": "Keyboard", "stock": 30}
]
stock_statuses = {"Low" if p["stock"] < 20 else "Sufficient" for p in inventory}
print("Project 9 - Stock statuses:", stock_statuses)
# Output: Stock statuses: {'Low', 'Sufficient'}

# %% Project 10: Dynamic Price Adjustments
# Difficulty: Advanced
# Description: Collect unique adjusted prices based on category and stock.
# Objective: Combine conditional transformations in a set comprehension.
# Tasks:
# - Create a list of dictionaries with product name, price, category, and stock.
# - Use a set comprehension to adjust Electronics prices by +10% if stock < 20, others by -5%.
# - Print the adjusted price set.
products = [
    {"name": "Laptop", "price": 1000, "category": "Electronics", "stock": 15},
    {"name": "Blender", "price": 100, "category": "Appliances", "stock": 30},
    {"name": "Tablet", "price": 500, "category": "Electronics", "stock": 10},
    {"name": "Toaster", "price": 50, "category": "Appliances", "stock": 25}
]
adjusted_prices = {
    p["price"] * 1.1 if p["category"] == "Electronics" and p["stock"] < 20 else p["price"] * 0.95
    for p in products
}
print("Project 10 - Adjusted prices:", adjusted_prices)
# Output: Adjusted prices: {1100.0, 95.0, 550.0, 47.5}