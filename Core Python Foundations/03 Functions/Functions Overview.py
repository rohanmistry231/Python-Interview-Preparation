# Python Core Concepts: Functions Overview

# Purpose: Functions are reusable blocks of code that perform specific tasks, enhancing modularity and readability.
# Key Features: Defining functions, positional/keyword arguments, default parameters, variable-length arguments,
#               lambda expressions, recursion, and function annotations for type hints.
# Note: Functions are fundamental in Python, used in ML pipelines, web apps, and data processing.

# -----------------------------------
# 1. Defining Functions
# -----------------------------------
# Explanation: Functions are defined using 'def' to encapsulate reusable logic.
# Example: Calculate the total price of an order.
def calculate_total_price(quantity: int, price: float) -> float:
    """Calculate total price for a given quantity and price."""
    return quantity * price

order_total = calculate_total_price(5, 999.99)
print("1. Defining Functions - Order total:", order_total)
# Output: Order total: 4999.95

# Exercise 1: Define a function to calculate discounted price.
# Solution:
def apply_discount(price: float, discount_rate: float) -> float:
    """Apply discount to a price."""
    return price * (1 - discount_rate)

discounted_price = apply_discount(999.99, 0.1)
print("Exercise 1 - Discounted price:", discounted_price)
# Output: Discounted price: 899.991

# -----------------------------------
# 2. Positional Arguments
# -----------------------------------
# Explanation: Positional arguments are passed in the order defined by the function.
# Example: Process an order with product name and quantity.
def process_order(product: str, quantity: int) -> str:
    """Return order details with product and quantity."""
    return f"Order: {quantity} units of {product}"

order_details = process_order("Laptop", 2)
print("2. Positional Arguments - Order details:", order_details)
# Output: Order details: Order: 2 units of Laptop

# Exercise 2: Create a function with positional arguments for customer and total.
# Solution:
def generate_invoice(customer: str, total: float) -> str:
    """Generate invoice for customer and total."""
    return f"Invoice for {customer}: ${total:.2f}"

invoice = generate_invoice("Alice", 1999.98)
print("Exercise 2 - Invoice:", invoice)
# Output: Invoice: Invoice for Alice: $1999.98

# -----------------------------------
# 3. Keyword Arguments
# -----------------------------------
# Explanation: Keyword arguments are passed by name, allowing flexible order.
# Example: Calculate shipping cost with weight and rate.
def calculate_shipping(weight: float, rate: float = 2.5) -> float:
    """Calculate shipping cost based on weight and rate."""
    return weight * rate

shipping_cost = calculate_shipping(rate=3.0, weight=10.0)
print("3. Keyword Arguments - Shipping cost:", shipping_cost)
# Output: Shipping cost: 30.0

# Exercise 3: Create a function with keyword arguments for tax calculation.
# Solution:
def calculate_tax(subtotal: float, tax_rate: float) -> float:
    """Calculate tax for a subtotal and tax rate."""
    return subtotal * tax_rate

tax = calculate_tax(tax_rate=0.08, subtotal=999.99)
print("Exercise 3 - Tax:", tax)
# Output: Tax: 79.9992

# -----------------------------------
# 4. Default Parameters
# -----------------------------------
# Explanation: Default parameters provide fallback values if arguments are not passed.
# Example: Apply a default discount rate to products.
def apply_default_discount(price: float, discount_rate: float = 0.05) -> float:
    """Apply discount with a default rate of 5%."""
    return price * (1 - discount_rate)

price_with_default = apply_default_discount(699.99)
price_with_custom = apply_default_discount(699.99, 0.1)
print("4. Default Parameters - Default discount:", price_with_default)
print("Custom discount:", price_with_custom)
# Output: Default discount: 664.9905
#         Custom discount: 629.991

# Exercise 4: Create a function with a default shipping rate.
# Solution:
def calculate_default_shipping(weight: float, rate: float = 2.0) -> float:
    """Calculate shipping with a default rate of $2 per unit."""
    return weight * rate

shipping_default = calculate_default_shipping(5.0)
print("Exercise 4 - Default shipping:", shipping_default)
# Output: Default shipping: 10.0

# -----------------------------------
# 5. Variable-Length Arguments (*args, **kwargs)
# -----------------------------------
# Explanation: *args collects positional arguments as a tuple; **kwargs collects keyword arguments as a dict.
# Example: Sum multiple product prices with additional fees.
def total_order_cost(*prices: float, **fees: float) -> float:
    """Calculate total cost including prices and fees."""
    total = sum(prices)
    total += sum(fees.values())
    return total

order_cost = total_order_cost(999.99, 29.99, shipping=10.0, tax=79.99)
print("5. Variable-Length Arguments - Order cost:", order_cost)
# Output: Order cost: 1119.97

# Exercise 5: Create a function to list order items and metadata.
# Solution:
def list_order(*items: str, **metadata: str) -> dict:
    """List order items and metadata."""
    return {"items": list(items), "metadata": metadata}

order_info = list_order("Laptop", "Mouse", customer="Bob", date="2025-04-20")
print("Exercise 5 - Order info:", order_info)
# Output: Order info: {'items': ['Laptop', 'Mouse'], 'metadata': {'customer': 'Bob', 'date': '2025-04-20'}}

# -----------------------------------
# 6. Lambda Expressions
# -----------------------------------
# Explanation: Lambda expressions create anonymous functions for concise operations.
# Example: Sort products by price using a lambda function.
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 29.99},
    {"name": "Smartphone", "price": 699.99}
]
sorted_products = sorted(products, key=lambda x: x["price"])
print("6. Lambda Expressions - Sorted products:", sorted_products)
# Output: Sorted products: [{'name': 'Mouse', 'price': 29.99},
#                          {'name': 'Smartphone', 'price': 699.99},
#                          {'name': 'Laptop', 'price': 999.99}]

# Exercise 6: Use a lambda to filter high-rated products (rating > 4.0).
# Solution:
product_ratings = [
    {"name": "Laptop", "rating": 4.5},
    {"name": "Mouse", "rating": 3.5},
    {"name": "Smartphone", "rating": 4.2}
]
high_rated = list(filter(lambda x: x["rating"] > 4.0, product_ratings))
print("Exercise 6 - High-rated products:", high_rated)
# Output: High-rated products: [{'name': 'Laptop', 'rating': 4.5}, {'name': 'Smartphone', 'rating': 4.2}]

# -----------------------------------
# 7. Recursion
# -----------------------------------
# Explanation: Recursion solves problems by calling a function within itself.
# Example: Calculate factorial for inventory batch sizes.
def factorial(n: int) -> int:
    """Calculate factorial of n recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

batch_size_factorial = factorial(5)
print("7. Recursion - Factorial of 5:", batch_size_factorial)
# Output: Factorial of 5: 120

# Example: Retail scenario - Sum order quantities recursively.
def sum_quantities(quantities: list, index: int = 0) -> int:
    """Sum quantities recursively."""
    if index >= len(quantities):
        return 0
    return quantities[index] + sum_quantities(quantities, index + 1)

order_quantities = [2, 5, 3]
total_quantity = sum_quantities(order_quantities)
print("Total quantity:", total_quantity)
# Output: Total quantity: 10

# Exercise 7: Create a recursive function to count items in a nested order list.
# Solution:
def count_items(orders: list, index: int = 0) -> int:
    """Count items in a nested order list recursively."""
    if index >= len(orders):
        return 0
    return 1 + count_items(orders, index + 1)

nested_orders = [{"product": "Laptop"}, {"product": "Mouse"}]
item_count = count_items(nested_orders)
print("Exercise 7 - Item count:", item_count)
# Output: Item count: 2

# -----------------------------------
# 8. Function Annotations
# -----------------------------------
# Explanation: Function annotations provide type hints for better code readability and IDE support.
# Example: Annotate a function to calculate order revenue.
def calculate_revenue(quantity: int, price: float, tax_rate: float = 0.08) -> float:
    """Calculate revenue with annotations."""
    return quantity * price * (1 + tax_rate)

revenue = calculate_revenue(3, 699.99)
print("8. Function Annotations - Revenue:", revenue)
# Output: Revenue: 2267.9676

# Exercise 8: Create an annotated function to calculate stock value.
# Solution:
def calculate_stock_value(quantity: int, unit_price: float) -> float:
    """Calculate total stock value with annotations."""
    return quantity * unit_price

stock_value = calculate_stock_value(50, 29.99)
print("Exercise 8 - Stock value:", stock_value)
# Output: Stock value: 1499.5

# -----------------------------------
# Notes
# -----------------------------------
# - Functions are critical in ML for data preprocessing (e.g., lambda for feature mapping) and web apps for order processing.
# - Retail-themed functions mimic MySQL Workbench data operations (e.g., calculating totals from query results).
# - Use exception handling (Exception Handling module) for invalid inputs (e.g., negative quantities).
# - Save function outputs to files (File Handling module) for integration with ML pipelines or APIs.
# - Combine with NumPy/Pandas for numerical data, Scikit-learn for ML, or Collections for data structuring.
# - Decorators (Decorators module) can enhance functions (e.g., timing calculations).
# - Iterators and Generators can work with functions for large datasets (e.g., recursive data processing).