# Python Exception Handling: Try-Except

# Purpose: Try-Except blocks handle exceptions (errors) to prevent program crashes.
# Key Features: Graceful error handling, improves robustness.

# 1. Basic Try-Except
# Explanation: Code in try block is executed; if an exception occurs, except block handles it.
# Example:
try:
    stock = int(input("Enter stock quantity: "))  # Simulating user input (e.g., "50")
    print(f"Stock recorded: {stock}")
except ValueError:
    print("Error: Please enter a valid integer")
# Output (if input is "50"): Stock recorded: 50
# Output (if input is "abc"): Error: Please enter a valid integer

# 2. Handling Specific Exceptions
# Explanation: Catch specific exceptions to handle different error types.
# Example:
prices = [100, 200, "300", 400]
try:
    total = sum(float(price) for price in prices)
    print(f"Total price: {total}")
except ValueError:
    print("Error: Invalid price format in list")
# Output: Error: Invalid price format in list

# 3. Try-Except with Retail Scenario
# Explanation: Handle errors in a retail context (e.g., processing product data).
# Example:
product = {"name": "Laptop", "price": "999.99"}  # Simulating database input
try:
    price = float(product["price"])
    if price < 0:
        print("Warning: Negative price detected")
    else:
        print(f"Valid price: ${price:.2f}")
except ValueError:
    print(f"Error: Invalid price for {product['name']}")
# Output: Valid price: $999.99

# Exercise 1: Handle a ValueError when converting a user-entered price to float.
# Solution:
# try:
#     price = float(input("Enter product price: "))  # Simulating input (e.g., "49.99")
#     print("Exercise 1 - Price:", price)
# except ValueError:
#     print("Exercise 1 - Error: Invalid price format")
# # Output (if input is "49.99"): Price: 49.99
# # Output (if input is "abc"): Error: Invalid price format

# Exercise 2: Catch a TypeError when summing a list with mixed types.
# Solution:
# items = [10, 20, "30", 40]
# try:
#     total = sum(items)
#     print("Exercise 2 - Total:", total)
# except TypeError:
#     print("Exercise 2 - Error: Mixed types in list")
# # Output: Error: Mixed types in list

# Exercise 3: Handle a KeyError when accessing a missing key in a product dictionary.
# Solution:
# product = {"name": "Smartphone", "price": 699.99}
# try:
#     stock = product["stock"]
#     print("Exercise 3 - Stock:", stock)
# except KeyError:
#     print("Exercise 3 - Error: Stock key not found")
# # Output: Error: Stock key not found

# Notes:
# - Use try-except for operations prone to errors (e.g., user input, data parsing) in ML (data cleaning) or web apps (API handling).
# - Catch specific exceptions to avoid masking unrelated errors.
# - Avoid bare except clauses (e.g., except:) to prevent catching unintended exceptions.