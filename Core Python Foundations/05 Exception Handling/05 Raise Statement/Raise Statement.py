# %% Purpose
# Python Exception Handling: Raise Statement
# Purpose: Raise statement triggers an exception explicitly to enforce conditions.
# Key Features: Custom error handling, program control.

# %% 1. Basic Raise
# Explanation: Raise an exception with raise ExceptionType("message").
# Example:
price = -50
if price < 0:
    raise ValueError("Price cannot be negative")
# Output: ValueError: Price cannot be negative (program stops unless caught)

# %% 2. Raise with Try-Except
# Explanation: Raise an exception and handle it in a try-except block.
# Example:
try:
    stock = 0
    if stock <= 0:
        raise ValueError("Stock must be positive")
    print(f"Stock: {stock}")
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Stock must be positive

# %% 3. Retail Scenario with Raise
# Explanation: Enforce business rules in a retail context.
# Example:
order = {"name": "Laptop", "quantity": 2, "price": 999.99}
try:
    if order["quantity"] > 100:
        raise ValueError("Quantity exceeds maximum limit")
    if order["price"] < 0:
        raise ValueError("Negative price not allowed")
    total = order["quantity"] * order["price"]
    print(f"Order total for {order['name']}: ${total:.2f}")
except ValueError as e:
    print(f"Order error: {e}")
# Output: Order total for Laptop: $1999.98

# %% Notes
# Notes:
# - Use raise to enforce business rules in ML (e.g., invalid model parameters) or web apps (e.g., API validation).
# - Combine with try-except to handle raised exceptions gracefully.
# - Include descriptive error messages for debugging.