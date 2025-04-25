# Generators Projects
# Purpose: Apply generator concepts through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Product Name Generator
# Difficulty: Basic
# Description: Generate product names one at a time.
# Objective: Practice basic generator creation.
# Tasks:
# - Define a generator function for a list of products.
# - Print the first two products.
# Expected Output: Product 1: Laptop
#                 Product 2: Smartphone
def product_generator(products):
    for product in products:
        yield product

products = ["Laptop", "Smartphone", "Coffee Maker"]
gen = product_generator(products)
print("Product 1:", next(gen))
print("Product 2:", next(gen))

# %% Project 2: Category Generator Loop
# Difficulty: Basic
# Description: Generate categories using a for loop.
# Objective: Practice using generators in loops.
# Tasks:
# - Define a generator for categories and iterate over it.
# - Print each category.
# Expected Output: Category: Electronics
#                 Category: Appliances
#                 Category: Clothing
def category_generator(categories):
    for category in categories:
        yield category

categories = ["Electronics", "Appliances", "Clothing"]
for category in category_generator(categories):
    print(f"Category: {category}")

# %% Project 3: Low Stock Generator
# Difficulty: Basic
# Description: Generate stock levels below 50.
# Objective: Practice filtering in generators.
# Tasks:
# - Define a generator to yield stock levels < 50.
# - Print low stock levels.
# Expected Output: Low stock: [30, 20]
def low_stock_generator(stocks):
    for stock in stocks:
        if stock < 50:
            yield stock

stocks = [30, 60, 20, 100]
print("Low stock:", [stock for stock in low_stock_generator(stocks)])

# %% Project 4: Discounted Price Generator
# Difficulty: Intermediate
# Description: Generate prices with a 15% discount.
# Objective: Practice transforming data in generators.
# Tasks:
# - Define a generator to apply a 15% discount to prices.
# - Print discounted prices.
# Expected Output: Discounted prices: [849.99, 594.99]
def discount_generator(prices):
    for price in prices:
        yield round(price * 0.85, 2)

prices = [999.99, 699.99]
print("Discounted prices:", [price for price in discount_generator(prices)])

# %% Project 5: Order ID Sequence Generator
# Difficulty: Intermediate
# Description: Generate a sequence of order IDs.
# Objective: Practice generating sequential values.
# Tasks:
# - Define a generator for order IDs from 2001 to 2003.
# - Print order IDs.
# Expected Output: Order IDs: [2001, 2002, 2003]
def order_id_generator(start, count):
    for i in range(count):
        yield start + i

print("Order IDs:", [id for id in order_id_generator(2001, 3)])

# %% Project 6: Expensive Order Generator
# Difficulty: Intermediate
# Description: Generate orders with total > $500.
# Objective: Practice complex filtering.
# Tasks:
# - Define a generator to yield expensive orders.
# - Print order details.
# Expected Output: Expensive orders: [{'order_id': 101, 'total': 1999.98}, {'order_id': 103, 'total': 699.99}]
def expensive_order_generator(orders):
    for order in orders:
        if order["total"] > 500:
            yield order

orders = [
    {"order_id": 101, "total": 1999.98},
    {"order_id": 102, "total": 49.99},
    {"order_id": 103, "total": 699.99}
]
print("Expensive orders:", [order for order in expensive_order_generator(orders)])

# %% Project 7: Customer Name Generator
# Difficulty: Intermediate
# Description: Generate names of customers with > 2 orders.
# Objective: Practice filtering based on conditions.
# Tasks:
# - Define a generator to yield high-order customer names.
# - Print customer names.
# Expected Output: High-order customers: ['Alice']
def customer_name_generator(customers):
    for customer in customers:
        if customer["orders"] > 2:
            yield customer["name"]

customers = [
    {"name": "Alice", "orders": 3},
    {"name": "Bob", "orders": 1}
]
print("High-order customers:", [name for name in customer_name_generator(customers)])

# %% Project 8: Incremental Price Generator
# Difficulty: Advanced
# Description: Generate prices with incremental increases.
# Objective: Practice dynamic value generation.
# Tasks:
# - Define a generator to yield prices increasing by $10.
# - Print generated prices.
# Expected Output: Prices: [100.00, 110.00, 120.00]
def price_generator(start, step, count):
    current = start
    for _ in range(count):
        yield current
        current += step

print("Prices:", [price for price in price_generator(100.00, 10.00, 3)])

# %% Project 9: Even Stock Generator
# Difficulty: Advanced
# Description: Generate even stock levels.
# Objective: Practice advanced filtering logic.
# Tasks:
# - Define a generator to yield even stock levels.
# - Print even stock levels.
# Expected Output: Even stock: [30, 20, 100]
def even_stock_generator(stocks):
    for stock in stocks:
        if stock % 2 == 0:
            yield stock

stocks = [30, 45, 20, 100]
print("Even stock:", [stock for stock in even_stock_generator(stocks)])

# %% Project 10: Comprehensive Retail Generator
# Difficulty: Advanced
# Description: Generate recent high-value orders.
# Objective: Practice combining generator features.
# Tasks:
# - Define a generator to yield orders with total > $100 and recent date.
# - Print order details.
# Expected Output: Recent high-value orders: [{'order_id': 101, 'total': 1999.98}]
from datetime import datetime, timedelta

def retail_order_generator(orders):
    recent_threshold = datetime.now() - timedelta(days=30)
    for order in orders:
        order_date = datetime.strptime(order["date"], "%Y-%m-%d")
        if order["total"] > 100 and order_date >= recent_threshold:
            yield order

orders = [
    {"order_id": 101, "total": 1999.98, "date": "2025-04-20"},
    {"order_id": 102, "total": 49.99, "date": "2025-04-20"},
    {"order_id": 103, "total": 699.99, "date": "2025-03-01"}
]
print("Recent high-value orders:", [order for order in retail_order_generator(orders)])