# Raise Statement Projects
# Purpose: Apply Raise Statement exception handling through 5 projects.
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions use retail-themed examples and simulate user inputs with fixed values for reproducibility.

# %% Project 1: Negative Price Enforcer
# Difficulty: Basic
# Description: Enforce non-negative prices with explicit error raising.
# Objective: Practice raising ValueError for invalid conditions.
# Tasks:
# - Simulate a product price.
# - Use try-except to raise and catch ValueError if price is negative.
# - Print the price or error message.
# Expected Output: Error: Negative price not allowed
price = -50
try:
    if price < 0:
        raise ValueError("Negative price not allowed")
    print(f"Price: ${price:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# %% Project 2: Zero Stock Enforcer
# Difficulty: Basic
# Description: Enforce positive stock quantities in a product dictionary.
# Objective: Use raise with try-except for ValueError handling.
# Tasks:
# - Create a product dictionary with zero stock.
# - Use try-except to raise and catch ValueError if stock is zero.
# - Print the stock or error message.
# Expected Output: Error: Zero stock not allowed
product = {"name": "Blender", "stock": 0}
try:
    if product["stock"] == 0:
        raise ValueError("Zero stock not allowed")
    print(f"Stock for {product['name']}: {product['stock']}")
except ValueError as e:
    print(f"Error: {e}")

# %% Project 3: Order Quantity Limiter
# Difficulty: Intermediate
# Description: Limit order quantities to a maximum value.
# Objective: Raise ValueError for excessive quantities in a retail context.
# Tasks:
# - Create an order dictionary with name, quantity, and price.
# - Use try-except to raise and catch ValueError if quantity > 100.
# - Print the order total or error message.
# Expected Output: Order total for Smartphone: $1399.98
order = {"name": "Smartphone", "quantity": 2, "price": 699.99}
try:
    if order["quantity"] > 100:
        raise ValueError("Quantity exceeds maximum limit")
    total = order["quantity"] * order["price"]
    print(f"Order total for {order['name']}: ${total:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# %% Project 4: Price Type Validator
# Difficulty: Intermediate
# Description: Enforce numeric price types in a product list.
# Objective: Raise TypeError for non-numeric prices.
# Tasks:
# - Create a list of products with mixed price types.
# - Use try-except to raise and catch TypeError for non-numeric prices.
# - Print valid prices or error message.
# Expected Output: Error: Price must be numeric
products = [{"name": "Mouse", "price": "abc"}]
try:
    for p in products:
        if not isinstance(p["price"], (int, float)):
            raise TypeError("Price must be numeric")
        print(f"Price for {p['name']}: ${p['price']:.2f}")
except TypeError as e:
    print(f"Error: {e}")

# %% Project 5: Complex Order Validator
# Difficulty: Advanced
# Description: Validate order data with multiple business rules.
# Objective: Combine raise for ValueError and TypeError in a retail context.
# Tasks:
# - Create an order dictionary with potential invalid data.
# - Use try-except to raise and catch ValueError (negative price) and TypeError (non-integer quantity).
# - Print the order total or error message.
# Expected Output: Error: Quantity must be an integer
order = {"name": "Tablet", "quantity": "5", "price": 499.99}
try:
    if not isinstance(order["quantity"], int):
        raise TypeError("Quantity must be an integer")
    if order["price"] < 0:
        raise ValueError("Negative price not allowed")
    total = order["quantity"] * order["price"]
    print(f"Order total for {order['name']}: ${total:.2f}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")