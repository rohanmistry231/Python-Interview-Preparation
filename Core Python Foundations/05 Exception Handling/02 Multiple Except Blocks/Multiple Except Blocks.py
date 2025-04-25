# %% Purpose
# Python Exception Handling: Multiple Except Blocks
# Purpose: Multiple except blocks handle different exception types for specific error handling.
# Key Features: Targeted error management, improved debugging.

# %% 1. Basic Multiple Except Blocks
# Explanation: Define separate except blocks for each expected exception type.
# Example:
try:
    price = float(input("Enter price: "))  # Simulating input (e.g., "abc" or "-10")
    if price < 0:
        raise ValueError("Negative price not allowed")
    print(f"Price: ${price:.2f}")
except ValueError:
    print("Invalid input or negative price")
except TypeError:
    print("Type error occurred")
# Output (if input is "abc"): Invalid input or negative price
# Output (if input is "-10"): Invalid input or negative price

# %% 2. Handling Multiple Exceptions
# Explanation: Catch multiple exception types with specific actions.
# Example:
product = {"name": "Coffee Maker", "price": "49.99"}
try:
    stock = product["stock"]  # Missing key
    price = float(product["price"])
    result = price / stock  # Potential ZeroDivisionError
    print(f"Price per unit: ${result:.2f}")
except KeyError:
    print("Error: Missing stock information")
except ValueError:
    print("Error: Invalid price format")
except ZeroDivisionError:
    print("Error: Stock cannot be zero")
# Output: Error: Missing stock information

# %% 3. Combining with Retail Logic
# Explanation: Handle errors in a retail context with multiple exception types.
# Example:
order = ["Laptop", 2, "999.99"]
try:
    product_name = order[0]
    quantity = int(order[1])
    price = float(order[2])
    total = quantity * price
    print(f"Order total for {product_name}: ${total:.2f}")
except IndexError:
    print("Error: Incomplete order data")
except ValueError:
    print("Error: Invalid quantity or price")
except TypeError:
    print("Error: Invalid data type")
# Output: Order total for Laptop: $1999.98

# %% Notes
# Notes:
# - Order except blocks from specific to general (e.g., ValueError before Exception).
# - Use in ML for robust data validation (e.g., handling missing features) or web apps for API error handling.
# - Log exceptions for debugging in production systems.