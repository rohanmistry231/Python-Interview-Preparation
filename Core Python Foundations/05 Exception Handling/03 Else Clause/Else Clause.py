# %% Purpose
# Python Exception Handling: Else Clause
# Purpose: Else clause in try-except runs if no exception occurs in the try block.
# Key Features: Separates success logic from error handling.

# %% 1. Basic Try-Except-Else
# Explanation: Execute else block only if try block succeeds.
# Example:
try:
    price = float(input("Enter price: "))  # Simulating input (e.g., "49.99")
except ValueError:
    print("Error: Invalid price format")
else:
    print(f"Valid price: ${price:.2f}")
# Output (if input is "49.99"): Valid price: $49.99
# Output (if input is "abc"): Error: Invalid price format

# %% 2. Else with Multiple Exceptions
# Explanation: Combine with multiple except blocks for robust handling.
# Example:
product = {"name": "Laptop", "price": "999.99"}
try:
    price = float(product["price"])
    stock = product["stock"]
except ValueError:
    print("Error: Invalid price format")
except KeyError:
    print("Error: Missing stock information")
else:
    print(f"Product {product['name']}: Price ${price:.2f}, Stock {stock}")
# Output: Error: Missing stock information

# %% 3. Retail Scenario with Else
# Explanation: Use else to process valid data in a retail context.
# Example:
order = ["Smartphone", "2", "699.99"]
try:
    quantity = int(order[1])
    price = float(order[2])
except ValueError:
    print("Error: Invalid quantity or price")
except IndexError:
    print("Error: Incomplete order data")
else:
    total = quantity * price
    print(f"Order for {order[0]}: Total ${total:.2f}")
# Output: Order for Smartphone: Total $1399.98

# %% Notes
# Notes:
# - Else clause keeps success logic separate, improving code clarity.
# - Use in ML for data validation (e.g., ensuring clean features) or web apps for user input processing.
# - Else runs only if no exception is raised in try block.