# Else Clause Projects
# Purpose: Apply Else Clause in try-except through 5 projects.
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions use retail-themed examples and simulate user inputs with fixed values for reproducibility.

# %% Project 1: Stock Input Validator
# Difficulty: Basic
# Description: Validate user-entered stock quantity with success confirmation.
# Objective: Practice try-except-else for ValueError handling.
# Tasks:
# - Simulate user input for stock quantity.
# - Use try-except-else to catch ValueError and confirm valid input in else.
# - Print the stock or an error message.
# Expected Output: Valid stock: 50
simulated_input = "50"  # Simulating valid input
try:
    stock = int(simulated_input)
except ValueError:
    print("Error: Invalid stock format")
else:
    print(f"Valid stock: {stock}")

# %% Project 2: Product Value Calculator
# Difficulty: Basic
# Description: Calculate total value of a product with valid data.
# Objective: Use try-except-else to handle KeyError and ValueError.
# Tasks:
# - Create a product dictionary with price and stock.
# - Use try-except-else to validate data and calculate total in else.
# - Print the total or an error message.
# Expected Output: Total value: $1999.98
product = {"name": "Laptop", "price": "999.99", "stock": "2"}
try:
    price = float(product["price"])
    stock = int(product["stock"])
except (ValueError, KeyError):
    print("Error: Invalid or missing data")
else:
    total = price * stock
    print(f"Total value: ${total:.2f}")

# %% Project 3: Order Processor
# Difficulty: Intermediate
# Description: Process an order list and confirm valid data.
# Objective: Use try-except-else for IndexError and ValueError in a retail context.
# Tasks:
# - Create an order list with name, quantity, and price.
# - Use try-except-else to validate and process total in else.
# - Print the total or an error message.
# Expected Output: Order total for Mouse: $149.95
order = ["Mouse", "5", "29.99"]
try:
    quantity = int(order[1])
    price = float(order[2])
except ValueError:
    print("Error: Invalid quantity or price")
except IndexError:
    print("Error: Incomplete order data")
else:
    total = quantity * price
    print(f"Order total for {order[0]}: ${total:.2f}")

# %% Project 4: Price Parser
# Difficulty: Intermediate
# Description: Parse and sum prices from a list with success confirmation.
# Objective: Use try-except-else to handle ValueError and TypeError.
# Tasks:
# - Create a list of prices with potential invalid entries.
# - Use try-except-else to sum valid prices in else.
# - Print the total or an error message.
# Expected Output: Error: Invalid price format
prices = [100, "abc", 300]
try:
    total = sum(float(price) for price in prices)
except (ValueError, TypeError):
    print("Error: Invalid price format")
else:
    print(f"Total price: ${total:.2f}")

# %% Project 5: Inventory Checker
# Difficulty: Advanced
# Description: Check inventory data and confirm valid calculations.
# Objective: Combine try-except-else for multiple exceptions in a retail context.
# Tasks:
# - Create a product dictionary with price, stock, and name.
# - Use try-except-else to handle ValueError, KeyError, and ZeroDivisionError, calculating price per unit in else.
# - Print the result or an error message.
# Expected Output: Error: Missing stock information
product = {"name": "Tablet", "price": "499.99"}
try:
    price = float(product["price"])
    stock = int(product["stock"])
    price_per_unit = price / stock
except ValueError:
    print("Error: Invalid price or stock format")
except KeyError:
    print("Error: Missing stock information")
except ZeroDivisionError:
    print("Error: Stock cannot be zero")
else:
    print(f"Price per unit for {product['name']}: ${price_per_unit:.2f}")