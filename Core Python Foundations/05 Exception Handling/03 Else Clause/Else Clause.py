# Python Exception Handling: Else Clause

# Purpose: Else clause in try-except runs if no exception occurs in the try block.
# Key Features: Separates success logic from error handling.

# 1. Basic Try-Except-Else
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

# 2. Else with Multiple Exceptions
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

# 3. Retail Scenario with Else
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

# Exercise 1: Use else to print a success message after converting a user-entered stock value.
# Solution:
# try:
#     stock = int(input("Enter stock: "))  # Simulating input (e.g., "50")
# except ValueError:
#     print("Exercise 1 - Error: Invalid stock format")
# else:
#     print("Exercise 1 - Stock recorded:", stock)
# # Output (if input is "50"): Stock recorded: 50

# Exercise 2: Use else to calculate total price if a product dictionary has valid data.
# Solution:
# product = {"name": "Blender", "price": "39.99", "stock": "20"}
# try:
#     price = float(product["price"])
#     stock = int(product["stock"])
# except (ValueError, KeyError):
#     print("Exercise 2 - Error: Invalid or missing data")
# else:
#     total = price * stock
#     print("Exercise 2 - Total value:", total)
# # Output: Total value: 799.8

# Exercise 3: Process an order list with else to confirm valid data.
# Solution:
# order = ["Mouse", "10", "29.99"]
# try:
#     qty = int(order[1])
#     price = float(order[2])
# except ValueError:
#     print("Exercise 3 - Error: Invalid format")
# except IndexError:
#     print("Exercise 3 - Error: Incomplete order")
# else:
#     print("Exercise 3 - Valid order: Quantity", qty, "Price", price)
# # Output: Valid order: Quantity 10 Price 29.99

# Notes:
# - Else clause keeps success logic separate, improving code clarity.
# - Use in ML for data validation (e.g., ensuring clean features) or web apps for user input processing.
# - Else runs only if no exception is raised in try block.