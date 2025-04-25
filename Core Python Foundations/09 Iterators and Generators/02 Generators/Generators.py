# %% Purpose
# Python Iterators and Generators: Generators
# Purpose: Generators are iterators created with functions using 'yield', producing values lazily.
# Key Features: Memory-efficient, simplifies iterator creation, one-time iteration.

# %% 1. Basic Generator Function
# Explanation: Use 'yield' to produce values one at a time.
# Example:
def product_generator(products):
    for product in products:
        yield product

products = ["Laptop", "Smartphone", "Coffee Maker"]
gen = product_generator(products)
print("First product:", next(gen))
print("Second product:", next(gen))
# Output: First product: Laptop
#         Second product: Smartphone

# %% 2. Generator with Logic
# Explanation: Include logic to filter or transform values.
# Example:
def discount_generator(prices, discount_rate):
    for price in prices:
        yield price * (1 - discount_rate)

prices = [999.99, 699.99, 49.99]
discounted_prices = discount_generator(prices, 0.1)
for price in discounted_prices:
    print(f"Discounted price: ${price:.2f}")
# Output: Discounted price: $899.99
#         Discounted price: $629.99
#         Discounted price: $44.99

# %% 3. Retail Scenario with Generators
# Explanation: Generate retail order IDs incrementally.
# Example:
def order_id_generator(start_id, count):
    for i in range(count):
        yield start_id + i

order_ids = order_id_generator(1001, 3)
orders = [{"order_id": order_id, "total": 1000.00} for order_id in order_ids]
for order in orders:
    print(f"Order {order['order_id']}: ${order['total']:.2f}")
# Output: Order 1001: $1000.00
#         Order 1002: $1000.00
#         Order 1003: $1000.00

# %% Notes
# Notes:
# - Generators are ideal for large datasets in ML (e.g., streaming data) or web apps (e.g., lazy API responses).
# - Generators can only be iterated once; store results in a list if needed.
# - Use 'yield' to pause and resume function execution.