# Try-Except Projects
# Purpose: Apply Try-Except exception handling through 5 projects.
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions use retail-themed examples and simulate user inputs with fixed values for reproducibility.

# %% Project 1: Price Input Validator
# Difficulty: Basic
# Description: Handle invalid user-entered price inputs.
# Objective: Practice basic try-except for ValueError handling.
# Tasks:
# - Simulate user input for a product price.
# - Use try-except to catch ValueError for invalid inputs.
# - Print the valid price or an error message.
# Expected Output: Error: Invalid price format
simulated_input = "abc"  # Simulating invalid input
try:
    price = float(simulated_input)
    print(f"Valid price: ${price:.2f}")
except ValueError:
    print("Error: Invalid price format")

# %% Project 2: Stock List Summarizer
# Difficulty: Basic
# Description: Sum stock quantities from a list with potential invalid entries.
# Objective: Use try-except to handle TypeError in list summation.
# Tasks:
# - Create a list of stock quantities with mixed types.
# - Use try-except to catch TypeError when summing.
# - Print the total or an error message.
# Expected Output: Error: Invalid stock data type
stock = [10, 20, "30", 40]
try:
    total = sum(stock)
    print(f"Total stock: {total}")
except TypeError:
    print("Error: Invalid stock data type")

# %% Project 3: Product Data Accessor
# Difficulty: Intermediate
# Description: Access product stock from a dictionary with missing keys.
# Objective: Practice try-except for KeyError handling.
# Tasks:
# - Create a product dictionary without a stock key.
# - Use try-except to catch KeyError when accessing stock.
# - Print the stock or an error message.
# Expected Output: Error: Stock key not found for Smartphone
product = {"name": "Smartphone", "price": 699.99}
try:
    stock = product["stock"]
    print(f"Stock for {product['name']}: {stock}")
except KeyError:
    print(f"Error: Stock key not found for {product['name']}")

# %% Project 4: Order Price Parser
# Difficulty: Intermediate
# Description: Parse prices from an order list with potential invalid formats.
# Objective: Use try-except to handle ValueError in a retail context.
# Tasks:
# - Create an order list with product names and prices (some invalid).
# - Use try-except to convert prices to float and sum valid ones.
# - Print the total or an error message.
# Expected Output: Error: Invalid price format in order
order = ["Laptop", "999.99", "Mouse", "abc"]
try:
    total = sum(float(price) for price in order[1::2])
    print(f"Order total: ${total:.2f}")
except ValueError:
    print("Error: Invalid price format in order")

# %% Project 5: Inventory Division Calculator
# Difficulty: Advanced
# Description: Calculate price per stock unit with multiple error possibilities.
# Objective: Combine try-except for ValueError and ZeroDivisionError.
# Tasks:
# - Create a product dictionary with price and stock.
# - Use try-except to handle ValueError (invalid price) and ZeroDivisionError (zero stock).
# - Print the price per unit or an error message.
# Expected Output: Error: Stock cannot be zero
product = {"name": "Blender", "price": "39.99", "stock": 0}
try:
    price = float(product["price"])
    stock = int(product["stock"])
    price_per_unit = price / stock
    print(f"Price per unit for {product['name']}: ${price_per_unit:.2f}")
except ValueError:
    print("Error: Invalid price or stock format")
except ZeroDivisionError:
    print("Error: Stock cannot be zero")