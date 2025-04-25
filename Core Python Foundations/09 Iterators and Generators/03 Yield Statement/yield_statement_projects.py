# Yield Statement Projects
# Purpose: Apply yield statement concepts through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Basic Product Yielder
# Difficulty: Basic
# Description: Use yield to generate product names.
# Objective: Practice basic yield usage.
# Tasks:
# - Define a function to yield three product names.
# - Print the first two products.
# Expected Output: Product 1: Laptop
#                 Product 2: Smartphone
def product_yielder():
    yield "Laptop"
    yield "Smartphone"
    yield "Coffee Maker"

gen = product_yielder()
print("Product 1:", next(gen))
print("Product 2:", next(gen))

# %% Project 2: Category Yielder Loop
# Difficulty: Basic
# Description: Yield categories for iteration in a loop.
# Objective: Practice yielding in loops.
# Tasks:
# - Define a function to yield categories.
# - Print each category in a for loop.
# Expected Output: Category: Electronics
#                 Category: Appliances
#                 Category: Clothing
def category_yielder():
    for category in ["Electronics", "Appliances", "Clothing"]:
        yield category

for category in category_yielder():
    print(f"Category: {category}")

# %% Project 3: Low Stock Yielder
# Difficulty: Basic
# Description: Yield low stock alerts for products with stock < 50.
# Objective: Practice conditional yielding.
# Tasks:
# - Define a function to yield low stock alerts.
# - Print alerts.
# Expected Output: Alerts: ['Low stock: Mouse (30 units)', 'Low stock: Monitor (20 units)']
def stock_yielder(products):
    for product in products:
        if product["stock"] < 50:
            yield f"Low stock: {product['name']} ({product['stock']} units)"

products = [
    {"name": "Mouse", "stock": 30},
    {"name": "Keyboard", "stock": 60},
    {"name": "Monitor", "stock": 20}
]
print("Alerts:", [alert for alert in stock_yielder(products)])

# %% Project 4: Discounted Price Yielder
# Difficulty: Intermediate
# Description: Yield prices with a 10% discount.
# Objective: Practice transforming data with yield.
# Tasks:
# - Define a function to yield discounted prices.
# - Print discounted prices.
# Expected Output: Discounted prices: [899.99, 629.99]
def discount_yielder(prices):
    for price in prices:
        yield round(price * 0.9, 2)

prices = [999.99, 699.99]
print("Discounted prices:", [price for price in discount_yielder(prices)])

# %% Project 5: Order ID Yielder
# Difficulty: Intermediate
# Description: Yield a sequence of order IDs.
# Objective: Practice generating sequential values.
# Tasks:
# - Define a function to yield order IDs from 3001 to 3003.
# - Print order IDs.
# Expected Output: Order IDs: [3001, 3002, 3003]
def order_id_yielder(start, count):
    for i in range(count):
        yield start + i

print("Order IDs:", [id for id in order_id_yielder(3001, 3)])

# %% Project 6: Expensive Order Yielder
# Difficulty: Intermediate
# Description: Yield orders with total > $500.
# Objective: Practice filtering with yield.
# Tasks:
# - Define a function to yield expensive orders.
# - Print order details.
# Expected Output: Expensive orders: [{'order_id': 101, 'total': 1999.98}, {'order_id': 103, 'total': 699.99}]
def expensive_order_yielder(orders):
    for order in orders:
        if order["total"] > 500:
            yield order

orders = [
    {"order_id": 101, "total": 1999.98},
    {"order_id": 102, "total": 49.99},
    {"order_id": 103, "total": 699.99}
]
print("Expensive orders:", [order for order in expensive_order_yielder(orders)])

# %% Project 7: Customer Priority Yielder
# Difficulty: Intermediate
# Description: Yield names of customers with > 2 orders.
# Objective: Practice complex conditional yielding.
# Tasks:
# - Define a function to yield high-order customer names.
# - Print customer names.
# Expected Output: Priority customers: ['Alice']
def priority_customer_yielder(customers):
    for customer in customers:
        if customer["orders"] > 2:
            yield customer["name"]

customers = [
    {"name": "Alice", "orders": 3},
    {"name": "Bob", "orders": 1}
]
print("Priority customers:", [name for name in priority_customer_yielder(customers)])

# %% Project 8: Price Increment Yielder
# Difficulty: Advanced
# Description: Yield prices with incremental increases.
# Objective: Practice dynamic yielding.
# Tasks:
# - Define a function to yield prices increasing by $10.
# - Print generated prices.
# Expected Output: Prices: [100.00, 110.00, 120.00]
def price_yielder(start, step, count):
    current = start
    for _ in range(count):
        yield current
        current += step

print("Prices:", [price for price in price_yielder(100.00, 10.00, 3)])

# %% Project 9: Even Stock Yielder
# Difficulty: Advanced
# Description: Yield even stock levels.
# Objective: Practice advanced filtering with yield.
# Tasks:
# - Define a function to yield even stock levels.
# - Print even stock levels.
# Expected Output: Even stock: [30, 20, 100]
def even_stock_yielder(stocks):
    for stock in stocks:
        if stock % 2 == 0:
            yield stock

stocks = [30, 45, 20, 100]
print("Even stock:", [stock for stock in even_stock_yielder(stocks)])

# %% Project 10: Comprehensive Retail Yielder
# Difficulty: Advanced
# Description: Yield recent high-value orders.
# Objective: Practice combining yield features.
# Tasks:
# - Define a function to yield orders with total > $100 and recent date.
# - Print order details.
# Expected Output: Recent high-value orders: [{'order_id': 101, 'total': 1999.98}]
from datetime import datetime, timedelta

def retail_yielder(orders):
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
print("Recent high-value orders:", [order for order in retail_yielder(orders)])