# Python Functions Projects
# Purpose: Apply Python Functions knowledge through 10 projects (Basic to Advanced).
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions cover Defining Functions, Positional/Keyword Arguments, Default Parameters,
#       Variable-Length Arguments, Lambda Expressions, Recursion, and Function Annotations.
#       Retail-themed examples mimic real-world scenarios.

# %% Project 1: Basic Price Calculator
# Difficulty: Basic
# Description: Calculate the total price of an order using a simple function.
# Objective: Practice defining functions with positional arguments.
# Tasks:
# - Define a function that takes quantity and unit price as inputs.
# - Calculate and return the total price (quantity * price).
# - Print the result for a sample order.
def calculate_total_price(quantity: int, price: float) -> float:
    """Calculate total price for a given quantity and price."""
    return quantity * price

order_total = calculate_total_price(5, 99.99)
print("Project 1 - Order total:", order_total)
# Output: Order total: 499.95

# %% Project 2: Product Order Formatter
# Difficulty: Basic
# Description: Format order details using positional arguments.
# Objective: Use positional arguments to create readable order details.
# Tasks:
# - Define a function that takes product name and quantity.
# - Return a formatted string with order details.
# - Print the result for a sample product.
def format_order(product: str, quantity: int) -> str:
    """Return formatted order details with product and quantity."""
    return f"Order: {quantity} units of {product}"

order_details = format_order("Smartphone", 3)
print("Project 2 - Order details:", order_details)
# Output: Order details: Order: 3 units of Smartphone

# %% Project 3: Tax Calculator with Keyword Arguments
# Difficulty: Basic
# Description: Calculate tax for an order using keyword arguments.
# Objective: Practice keyword arguments for flexible parameter passing.
# Tasks:
# - Define a function that takes subtotal and tax rate as keyword arguments.
# - Calculate and return the tax amount (subtotal * tax_rate).
# - Print the result using keyword arguments.
def calculate_tax(subtotal: float, tax_rate: float) -> float:
    """Calculate tax for a subtotal and tax rate."""
    return subtotal * tax_rate

tax_amount = calculate_tax(tax_rate=0.07, subtotal=499.99)
print("Project 3 - Tax amount:", tax_amount)
# Output: Tax amount: 34.9993

# %% Project 4: Discount with Default Parameter
# Difficulty: Intermediate
# Description: Apply a discount to a price with a default discount rate.
# Objective: Use default parameters to simplify function calls.
# Tasks:
# - Define a function that takes price and an optional discount rate (default 5%).
# - Calculate and return the discounted price.
# - Print results for default and custom discount rates.
def apply_default_discount(price: float, discount_rate: float = 0.05) -> float:
    """Apply discount with a default rate of 5%."""
    return price * (1 - discount_rate)

default_discount = apply_default_discount(999.99)
custom_discount = apply_default_discount(999.99, discount_rate=0.15)
print("Project 4 - Default discount:", default_discount)
print("Project 4 - Custom discount:", custom_discount)
# Output: Default discount: 949.9905
#         Custom discount: 849.9915

# %% Project 5: Total Order Cost with Variable-Length Arguments
# Difficulty: Intermediate
# Description: Calculate total order cost including multiple prices and fees.
# Objective: Use *args for prices and **kwargs for fees.
# Tasks:
# - Define a function that accepts variable prices (*args) and fees (**kwargs).
# - Sum prices and fees, then return the total.
# - Print the result for a sample order.
def total_order_cost(*prices: float, **fees: float) -> float:
    """Calculate total cost including prices and fees."""
    total = sum(prices)
    total += sum(fees.values())
    return total

order_cost = total_order_cost(499.99, 29.99, shipping=15.0, tax=39.99)
print("Project 5 - Total order cost:", order_cost)
# Output: Total order cost: 584.97

# %% Project 6: Sort Products by Price with Lambda
# Difficulty: Intermediate
# Description: Sort a list of products by price using a lambda function.
# Objective: Practice lambda expressions for sorting.
# Tasks:
# - Define a list of product dictionaries with name and price.
# - Use sorted() with a lambda function to sort by price.
# - Print the sorted products.
products = [
    {"name": "Tablet", "price": 299.99},
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 19.99}
]
sorted_products = sorted(products, key=lambda x: x["price"])
print("Project 6 - Sorted products:", sorted_products)
# Output: Sorted products: [{'name': 'Mouse', 'price': 19.99},
#                          {'name': 'Tablet', 'price': 299.99},
#                          {'name': 'Laptop', 'price': 999.99}]

# %% Project 7: Recursive Order Quantity Sum
# Difficulty: Intermediate
# Description: Sum order quantities recursively.
# Objective: Practice recursion for processing lists.
# Tasks:
# - Define a recursive function to sum quantities in a list.
# - Pass the list and an index (default 0) to track progress.
# - Print the total quantity for a sample list.
def sum_quantities(quantities: list, index: int = 0) -> int:
    """Sum quantities recursively."""
    if index >= len(quantities):
        return 0
    return quantities[index] + sum_quantities(quantities, index + 1)

order_quantities = [4, 2, 6]
total_quantity = sum_quantities(order_quantities)
print("Project 7 - Total quantity:", total_quantity)
# Output: Total quantity: 12

# %% Project 8: Stock Value with Annotations
# Difficulty: Intermediate
# Description: Calculate total stock value with type annotations.
# Objective: Use function annotations for clarity and IDE support.
# Tasks:
# - Define an annotated function that takes quantity and unit price.
# - Calculate and return the stock value (quantity * unit_price).
# - Print the result for a sample stock.
def calculate_stock_value(quantity: int, unit_price: float) -> float:
    """Calculate total stock value with annotations."""
    return quantity * unit_price

stock_value = calculate_stock_value(100, 49.99)
print("Project 8 - Stock value:", stock_value)
# Output: Stock value: 4999.0

# %% Project 9: Complex Order Processor
# Difficulty: Advanced
# Description: Process an order with multiple function features.
# Objective: Combine default parameters, variable-length arguments, and annotations.
# Tasks:
# - Define a function that takes customer name, discount rate (default 0%), and variable items (*items).
# - Calculate total price from items (list of dictionaries with price and quantity).
# - Apply discount and return a formatted result with annotations.
# - Print the result for a sample order.
def process_complex_order(customer: str, *items: dict, discount_rate: float = 0.0) -> dict:
    """Process order with customer, items, and optional discount."""
    total = sum(item["price"] * item["quantity"] for item in items)
    discounted_total = total * (1 - discount_rate)
    return {
        "customer": customer,
        "items": items,
        "total": total,
        "discounted_total": discounted_total
    }

order = process_complex_order(
    "Alice",
    {"name": "Laptop", "price": 999.99, "quantity": 1},
    {"name": "Mouse", "price": 29.99, "quantity": 2},
    discount_rate=0.1
)
print("Project 9 - Order details:", order)
# Output: Order details: {'customer': 'Alice',
#                        'items': ({'name': 'Laptop', 'price': 999.99, 'quantity': 1},
#                                  {'name': 'Mouse', 'price': 29.99, 'quantity': 2}),
#                        'total': 1059.97,
#                        'discounted_total': 953.973}

# %% Project 10: Recursive Inventory Counter with Lambda Filter
# Difficulty: Advanced
# Description: Count high-value inventory items recursively, filtering with lambda.
# Objective: Combine recursion, lambda expressions, and annotations.
# Tasks:
# - Define a recursive function to count items with price > 500 using a lambda filter.
# - Use annotations and pass the inventory list and index (default 0).
# - Print the count for a sample inventory.
def count_high_value_items(inventory: list, index: int = 0) -> int:
    """Count high-value items (price > 500) recursively."""
    if index >= len(inventory):
        return 0
    filtered = list(filter(lambda x: x["price"] > 500, [inventory[index]]))
    return len(filtered) + count_high_value_items(inventory, index + 1)

inventory = [
    {"name": "Mouse", "price": 29.99},
    {"name": "Laptop", "price": 999.99},
    {"name": "Tablet", "price": 599.99}
]
high_value_count = count_high_value_items(inventory)
print("Project 10 - High-value item count:", high_value_count)
# Output: High-value item count: 2