# Generator Expressions Projects
# Purpose: Apply Generator Expressions through 10 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions cover Basic, Conditional, and Using Generators in Loops using retail-themed examples.

# %% Project 1: Discounted Price Generator
# Difficulty: Basic
# Description: Yield discounted prices for a list of products.
# Objective: Practice basic generator expression for simple transformations.
# Tasks:
# - Create a list of product prices.
# - Use a generator expression to yield prices with a 10% discount.
# - Convert to list and print the discounted prices.
prices = [100, 250, 500, 750]
discounted_gen = (price * 0.9 for price in prices)
discounted_prices = list(discounted_gen)
print("Project 1 - Discounted prices:", discounted_prices)
# Output: Discounted prices: [90.0, 225.0, 450.0, 675.0]

# %% Project 2: Stock Multiplier Generator
# Difficulty: Basic
# Description: Yield doubled stock quantities for inventory planning.
# Objective: Use basic generator expression to transform quantities.
# Tasks:
# - Create a list of stock quantities.
# - Use a generator expression to yield doubled quantities.
# - Convert to list and print the doubled quantities.
stock = [10, 20, 30, 40]
doubled_gen = (qty * 2 for qty in stock)
doubled_stock = list(doubled_gen)
print("Project 2 - Doubled stock:", doubled_stock)
# Output: Doubled stock: [20, 40, 60, 80]

# %% Project 3: Expensive Product Name Generator
# Difficulty: Basic
# Description: Yield names of products with prices above 200.
# Objective: Practice generator expression with a condition.
# Tasks:
# - Create a list of tuples with product names and prices.
# - Use a generator expression to yield names of products with prices > 200.
# - Convert to list and print the product names.
product_prices = [("Laptop", 999.99), ("Mouse", 29.99), ("Smartphone", 699.99), ("Blender", 149.99)]
expensive_gen = (name for name, price in product_prices if price > 200)
expensive_products = list(expensive_gen)
print("Project 3 - Expensive products:", expensive_products)
# Output: Expensive products: ['Laptop', 'Smartphone']

# %% Project 4: Electronics Product Generator
# Difficulty: Intermediate
# Description: Yield product names from the Electronics category.
# Objective: Use conditional generator expression with dictionary data.
# Tasks:
# - Create a list of dictionaries with product name and category.
# - Use a generator expression to yield names of Electronics products.
# - Convert to list and print the product names.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Blender", "category": "Appliances"},
    {"name": "Smartphone", "category": "Electronics"},
    {"name": "Toaster", "category": "Appliances"}
]
electronics_gen = (p["name"] for p in products if p["category"] == "Electronics")
electronics_products = list(electronics_gen)
print("Project 4 - Electronics products:", electronics_products)
# Output: Electronics products: ['Laptop', 'Smartphone']

# %% Project 5: Formatted Order ID Generator
# Difficulty: Intermediate
# Description: Yield formatted order IDs with a prefix.
# Objective: Use generator expression for string formatting.
# Tasks:
# - Create a list of order numbers.
# - Use a generator expression to yield IDs formatted as "ORD-XXX" (zero-padded).
# - Convert to list and print the formatted order IDs.
order_numbers = [1, 15, 100, 999]
order_id_gen = (f"ORD-{num:03d}" for num in order_numbers)
formatted_orders = list(order_id_gen)
print("Project 5 - Formatted order IDs:", formatted_orders)
# Output: Formatted order IDs: ['ORD-001', 'ORD-015', 'ORD-100', 'ORD-999']

# %% Project 6: High Stock Generator in Loop
# Difficulty: Intermediate
# Description: Yield stock quantities above 50 for direct iteration.
# Objective: Practice using generator expression in a loop.
# Tasks:
# - Create a list of stock quantities.
# - Use a generator expression to yield quantities > 50.
# - Iterate over the generator and print each quantity.
stock_quantities = [10, 60, 20, 75, 30]
high_stock_gen = (qty for qty in stock_quantities if qty > 50)
for qty in high_stock_gen:
    print(f"Project 6 - High stock quantity: {qty}")
# Output: High stock quantity: 60
#         High stock quantity: 75

# %% Project 7: Stock Status Generator
# Difficulty: Intermediate
# Description: Yield stock status labels based on quantity.
# Objective: Use generator expression with conditional expressions.
# Tasks:
# - Create a list of dictionaries with product name and stock.
# - Use a generator expression to yield status labels ("Low" for < 20, "Sufficient" for >= 20).
# - Convert to list and print the status labels.
inventory = [
    {"name": "Laptop", "stock": 15},
    {"name": "Mouse", "stock": 50},
    {"name": "Tablet", "stock": 5},
    {"name": "Keyboard", "stock": 30}
]
status_gen = ("Low" if p["stock"] < 20 else "Sufficient" for p in inventory)
stock_statuses = list(status_gen)
print("Project 7 - Stock statuses:", stock_statuses)
# Output: Stock statuses: ['Low', 'Sufficient', 'Low', 'Sufficient']

# %% Project 8: Price Bucket Generator
# Difficulty: Advanced
# Description: Yield price bucket categories for products.
# Objective: Use generator expression with multiple conditional expressions.
# Tasks:
# - Create a list of dictionaries with product name and price.
# - Use a generator expression to yield categories ("Budget" for <= 100, "Mid-range" for 101-500, "Premium" for > 500).
# - Convert to list and print the categories.
products = [
    {"name": "Mouse", "price": 29.99},
    {"name": "Laptop", "price": 999.99},
    {"name": "Tablet", "price": 299.99}
]
bucket_gen = ("Budget" if p["price"] <= 100 else "Mid-range" if p["price"] <= 500 else "Premium" for p in products)
price_buckets = list(bucket_gen)
print("Project 8 - Price buckets:", price_buckets)
# Output: Price buckets: ['Budget', 'Premium', 'Mid-range']

# %% Project 9: Nested Order Summary Generator
# Difficulty: Advanced
# Description: Yield order summaries from a nested structure.
# Objective: Use generator expression with nested data iteration.
# Tasks:
# - Create a list of dictionaries with region and products (list of product names).
# - Use a generator expression to yield summaries like "Product in Region".
# - Convert to list and print the summaries.
orders = [
    {"region": "North", "products": ["Laptop", "Mouse"]},
    {"region": "South", "products": ["Tablet", "Keyboard"]}
]
summary_gen = (f"{p} in {o['region']}" for o in orders for p in o["products"])
order_summaries = list(summary_gen)
print("Project 9 - Order summaries:", order_summaries)
# Output: Order summaries: ['Laptop in North', 'Mouse in North', 'Tablet in South', 'Keyboard in South']

# %% Project 10: Dynamic Price Adjustment Generator
# Difficulty: Advanced
# Description: Yield adjusted prices based on category and stock.
# Objective: Combine conditional transformations in a generator expression.
# Tasks:
# - Create a list of dictionaries with product name, price, category, and stock.
# - Use a generator expression to yield Electronics prices +10% if stock < 20, others -5%.
# - Convert to list and print the adjusted prices.
products = [
    {"name": "Laptop", "price": 1000, "category": "Electronics", "stock": 15},
    {"name": "Blender", "price": 100, "category": "Appliances", "stock": 30},
    {"name": "Tablet", "price": 500, "category": "Electronics", "stock": 10},
    {"name": "Toaster", "price": 50, "category": "Appliances", "stock": 25}
]
price_gen = (
    p["price"] * 1.1 if p["category"] == "Electronics" and p["stock"] < 20 else p["price"] * 0.95
    for p in products
)
adjusted_prices = list(price_gen)
print("Project 10 - Adjusted prices:", adjusted_prices)
# Output: Adjusted prices: [1100.0, 95.0, 550.0, 47.5]