# %% Purpose
# Python Iterators and Generators: Yield Statement
# Purpose: The 'yield' statement produces values in generators, pausing function execution.
# Key Features: Lazy evaluation, state preservation, enables generator functions.

# %% 1. Basic Yield Usage
# Explanation: 'yield' returns a value and pauses the function, resuming on next call.
# Example:
def product_yielder():
    yield "Laptop"
    yield "Smartphone"
    yield "Coffee Maker"

gen = product_yielder()
print("First yield:", next(gen))
print("Second yield:", next(gen))
# Output: First yield: Laptop
#         Second yield: Smartphone

# %% 2. Yield with Dynamic Data
# Explanation: Use 'yield' in loops to generate values dynamically.
# Example:
def price_incrementer(start_price, step, count):
    current_price = start_price
    for _ in range(count):
        yield current_price
        current_price += step

prices = price_incrementer(100.00, 10.00, 4)
for price in prices:
    print(f"Price: ${price:.2f}")
# Output: Price: $100.00
#         Price: $110.00
#         Price: $120.00
#         Price: $130.00

# %% 3. Retail Scenario with Yield
# Explanation: Generate stock alerts for low inventory using 'yield'.
# Example:
def stock_alert(products):
    for product in products:
        if product["stock"] < 50:
            yield f"Low stock alert: {product['name']} ({product['stock']} units)"

inventory = [
    {"name": "Mouse", "stock": 30},
    {"name": "Keyboard", "stock": 60},
    {"name": "Monitor", "stock": 20}
]
alerts = stock_alert(inventory)
for alert in alerts:
    print(alert)
# Output: Low stock alert: Mouse (30 units)
#         Low stock alert: Monitor (20 units)

# %% Notes
# Notes:
# - 'yield' enables lazy evaluation, ideal for ML (e.g., batch processing) or web apps (e.g., streaming data).
# - Functions with 'yield' become generators; they maintain state between calls.
# - Combine with try-except to handle StopIteration for robustness.