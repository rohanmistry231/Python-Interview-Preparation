# Dictionary Comprehensions Projects
# Purpose: Apply Dictionary Comprehensions through 10 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions cover Basic, Conditional, and Transforming Keys/Values Dictionary Comprehensions using retail-themed examples.

# %% Project 1: Product Index Mapper
# Difficulty: Basic
# Description: Create a dictionary mapping product names to their index positions.
# Objective: Practice basic dictionary comprehension for simple key-value mapping.
# Tasks:
# - Create a list of product names.
# - Use a dictionary comprehension to map each product to its index (starting from 1).
# - Print the product-index dictionary.
products = ["Mouse", "Keyboard", "Monitor"]
product_indices = {name: idx + 1 for idx, name in enumerate(products)}
print("Project 1 - Product indices:", product_indices)
# Output: Product indices: {'Mouse': 1, 'Keyboard': 2, 'Monitor': 3}

# %% Project 2: Price Formatter
# Difficulty: Basic
# Description: Map product names to their formatted prices (rounded to 2 decimals).
# Objective: Use basic dictionary comprehension for value transformation.
# Tasks:
# - Create a dictionary of products and their prices.
# - Use a dictionary comprehension to format prices to 2 decimal places.
# - Print the formatted price dictionary.
prices = {"Laptop": 999.99, "Smartphone": 699.99, "Blender": 49.99}
formatted_prices = {name: round(price, 2) for name, price in prices.items()}
print("Project 2 - Formatted prices:", formatted_prices)
# Output: Formatted prices: {'Laptop': 999.99, 'Smartphone': 699.99, 'Blender': 49.99}

# %% Project 3: Low Stock Filter
# Difficulty: Basic
# Description: Filter products with stock levels below 30.
# Objective: Practice dictionary comprehension with a condition.
# Tasks:
# - Create a dictionary of products and their stock levels.
# - Use a dictionary comprehension to include only products with stock < 30.
# - Print the low stock dictionary.
stock_levels = {"Mouse": 25, "Keyboard": 50, "Tablet": 10}
low_stock = {name: qty for name, qty in stock_levels.items() if qty < 30}
print("Project 3 - Low stock:", low_stock)
# Output: Low stock: {'Mouse': 25, 'Tablet': 10}

# %% Project 4: Expensive Product Filter
# Difficulty: Intermediate
# Description: Filter products with prices above 500 and adjust keys.
# Objective: Use conditional dictionary comprehension with key transformation.
# Tasks:
# - Create a dictionary of products and their prices.
# - Use a dictionary comprehension to include products with prices > 500, prefixing keys with "premium_".
# - Print the filtered dictionary.
prices = {"Laptop": 999.99, "Smartphone": 699.99, "Blender": 49.99}
premium_products = {f"premium_{name}": price for name, price in prices.items() if price > 500}
print("Project 4 - Premium products:", premium_products)
# Output: Premium products: {'premium_Laptop': 999.99, 'premium_Smartphone': 699.99}

# %% Project 5: Stock Status Tagger
# Difficulty: Intermediate
# Description: Map products to their stock status based on quantity.
# Objective: Use dictionary comprehension with conditional expressions for value transformation.
# Tasks:
# - Create a dictionary of products and their stock levels.
# - Use a dictionary comprehension to tag products as "Low" (< 20) or "Sufficient" (>= 20).
# - Print the stock status dictionary.
stock = {"Laptop": 15, "Mouse": 50, "Tablet": 5}
stock_status = {name: "Low" if qty < 20 else "Sufficient" for name, qty in stock.items()}
print("Project 5 - Stock status:", stock_status)
# Output: Stock status: {'Laptop': 'Low', 'Mouse': 'Sufficient', 'Tablet': 'Low'}

# %% Project 6: Discounted Price Mapper
# Difficulty: Intermediate
# Description: Map products to their prices after applying a category-based discount.
# Objective: Use dictionary comprehension with conditional value transformation.
# Tasks:
# - Create a list of dictionaries with product name, price, and category.
# - Use a dictionary comprehension to apply 10% discount for Electronics, 5% for others.
# - Print the discounted price dictionary.
products = [
    {"name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"name": "Blender", "price": 100, "category": "Appliances"},
    {"name": "Smartphone", "price": 699.99, "category": "Electronics"}
]
discounted_prices = {p["name"]: p["price"] * 0.9 if p["category"] == "Electronics" else p["price"] * 0.95 for p in products}
print("Project 6 - Discounted prices:", discounted_prices)
# Output: Discounted prices: {'Laptop': 899.991, 'Blender': 95.0, 'Smartphone': 629.991}

# %% Project 7: Category Indexer
# Difficulty: Intermediate
# Description: Map products to their category and index within a category.
# Objective: Use dictionary comprehension with enumeration and complex key creation.
# Tasks:
# - Create a list of dictionaries with product name and category.
# - Use a dictionary comprehension to map products to a string like "category_index".
# - Print the category index dictionary.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Smartphone", "category": "Electronics"},
    {"name": "Blender", "category": "Appliances"}
]
category_indices = {p["name"]: f"{p['category']}_{idx + 1}" for idx, p in enumerate(products)}
print("Project 7 - Category indices:", category_indices)
# Output: Category indices: {'Laptop': 'Electronics_1', 'Smartphone': 'Electronics_2', 'Blender': 'Appliances_3'}

# %% Project 8: Price Bucket Mapper
# Difficulty: Advanced
# Description: Map products to their price bucket categories.
# Objective: Use dictionary comprehension with multiple conditional expressions.
# Tasks:
# - Create a dictionary of products and their prices.
# - Use a dictionary comprehension to categorize prices as "Budget" (<= 100), "Mid-range" (101-500), or "Premium" (> 500).
# - Print the price bucket dictionary.
prices = {"Mouse": 29.99, "Laptop": 999.99, "Tablet": 299.99}
price_buckets = {name: "Budget" if price <= 100 else "Mid-range" if price <= 500 else "Premium" for name, price in prices.items()}
print("Project 8 - Price buckets:", price_buckets)
# Output: Price buckets: {'Mouse': 'Budget', 'Laptop': 'Premium', 'Tablet': 'Mid-range'}

# %% Project 9: Nested Order Counter
# Difficulty: Advanced
# Description: Count products per region from a nested order structure.
# Objective: Use dictionary comprehension with nested data iteration.
# Tasks:
# - Create a list of dictionaries with region and products (list of product names).
# - Use a dictionary comprehension to map regions to the count of their products.
# - Print the region product count dictionary.
orders = [
    {"region": "North", "products": ["Laptop", "Mouse"]},
    {"region": "South", "products": ["Tablet", "Keyboard"]}
]
region_counts = {o["region"]: len(o["products"]) for o in orders}
print("Project 9 - Region product counts:", region_counts)
# Output: Region product counts: {'North': 2, 'South': 2}

# %% Project 10: Dynamic Stock Adjuster
# Difficulty: Advanced
# Description: Adjust stock values based on category and price conditions.
# Objective: Combine conditional transformations in a dictionary comprehension.
# Tasks:
# - Create a list of dictionaries with product name, stock, category, and price.
# - Use a dictionary comprehension to increase Electronics stock by 10 if price > 500, decrease others by 5.
# - Print the adjusted stock dictionary.
products = [
    {"name": "Laptop", "stock": 15, "category": "Electronics", "price": 999.99},
    {"name": "Blender", "stock": 30, "category": "Appliances", "price": 100},
    {"name": "Tablet", "stock": 20, "category": "Electronics", "price": 299.99}
]
adjusted_stock = {
    p["name"]: p["stock"] + 10 if p["category"] == "Electronics" and p["price"] > 500 else p["stock"] - 5
    for p in products
}
print("Project 10 - Adjusted stock:", adjusted_stock)
# Output: Adjusted stock: {'Laptop': 25, 'Blender': 25, 'Tablet': 15}