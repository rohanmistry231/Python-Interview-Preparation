# %% Purpose
# Python Exception Handling: Finally Clause
# Purpose: Finally clause runs regardless of whether an exception occurs, useful for cleanup.
# Key Features: Ensures execution of critical code (e.g., closing resources).

# %% 1. Basic Try-Except-Finally
# Explanation: Finally block executes after try and except, even if an exception occurs.
# Example:
try:
    price = float(input("Enter price: "))  # Simulating input (e.g., "49.99" or "abc")
    print(f"Price: ${price:.2f}")
except ValueError:
    print("Error: Invalid price format")
finally:
    print("Processing complete")
# Output (if input is "49.99"): Price: $49.99, Processing complete
# Output (if input is "abc"): Error: Invalid price format, Processing complete

# %% 2. Finally with Multiple Exceptions
# Explanation: Use finally with multiple except blocks for consistent cleanup.
# Example:
product = {"name": "Smartphone", "price": "699.99"}
try:
    price = float(product["price"])
    stock = product["stock"]
except ValueError:
    print("Error: Invalid price format")
except KeyError:
    print("Error: Missing stock information")
finally:
    print("Product processing finished")
# Output: Error: Missing stock information, Product processing finished

# %% 3. Retail Scenario with Finally
# Explanation: Use finally to log or clean up in a retail context.
# Example:
order = ["Laptop", "2", "999.99"]
try:
    quantity = int(order[1])
    price = float(order[2])
    total = quantity * price
    print(f"Order total: ${total:.2f}")
except (ValueError, IndexError):
    print("Error: Invalid or incomplete order")
finally:
    print("Order processing logged")
# Output: Order total: $1999.98, Order processing logged

# %% Notes
# Notes:
# - Finally is ideal for cleanup (e.g., closing files, releasing database connections) in ML or web apps.
# - Runs even if return or break statements are used in try/except.
# - Use for logging or resource management in production code.