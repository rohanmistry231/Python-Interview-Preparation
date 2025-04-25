# Multiple Except Blocks Projects
# Purpose: Apply Multiple Except Blocks exception handling through 5 projects.
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions use retail-themed examples and simulate user inputs with fixed values for reproducibility.

# %% Project 1: Quantity Input Processor
# Difficulty: Basic
# Description: Process user-entered quantity with multiple error types.
# Objective: Practice multiple except blocks for ValueError and TypeError.
# Tasks:
# - Simulate user input for a product quantity.
# - Use try-except to catch ValueError and TypeError.
# - Print the quantity or an appropriate error message.
# Expected Output: Error: Invalid quantity format
simulated_input = "abc"  # Simulating invalid input
try:
    quantity = int(simulated_input)
    print(f"Quantity: {quantity}")
except ValueError:
    print("Error: Invalid quantity format")
except TypeError:
    print("Error: Type mismatch")

# %% Project 2: Product Stock Divider
# Difficulty: Basic
# Description: Divide price by stock with missing or zero stock.
# Objective: Use multiple except blocks for KeyError and ZeroDivisionError.
# Tasks:
# - Create a product dictionary without stock.
# - Use try-except to catch KeyError and ZeroDivisionError.
# - Print the price per unit or an error message.
# Expected Output: Error: Missing stock information
product = {"name": "Coffee Maker", "price": "49.99"}
try:
    stock = product["stock"]
    price = float(product["price"])
    price_per_unit = price / stock
    print(f"Price per unit: ${price_per_unit:.2f}")
except KeyError:
    print("Error: Missing stock information")
except ZeroDivisionError:
    print("Error: Stock cannot be zero")

# %% Project 3: Order Data Validator
# Difficulty: Intermediate
# Description: Validate an order list with multiple potential errors.
# Objective: Handle IndexError, ValueError, and TypeError in a retail context.
# Tasks:
# - Create an incomplete order list.
# - Use try-except to catch IndexError, ValueError, and TypeError.
# - Print the order total or an error message.
# Expected Output: Error: Incomplete order data
order = ["Smartphone", "2"]
try:
    name = order[0]
    quantity = int(order[1])
    price = float(order[2])
    total = quantity * price
    print(f"Order total for {name}: ${total:.2f}")
except IndexError:
    print("Error: Incomplete order data")
except ValueError:
    print("Error: Invalid quantity or price")
except TypeError:
    print("Error: Invalid data type")

# %% Project 4: Price List Processor
# Difficulty: Intermediate
# Description: Process a list of prices with mixed types and invalid formats.
# Objective: Use multiple except blocks for ValueError and TypeError.
# Tasks:
# - Create a list of prices with invalid entries.
# - Use try-except to catch ValueError and TypeError while summing prices.
# - Print the total or an error message.
# Expected Output: Error: Invalid price format
prices = [100, "200", None, 400]
try:
    total = sum(float(price) for price in prices)
    print(f"Total price: ${total:.2f}")
except ValueError:
    print("Error: Invalid price format")
except TypeError:
    print("Error: Invalid price type")

# %% Project 5: Inventory Analysis
# Difficulty: Advanced
# Description: Analyze inventory data with multiple error scenarios.
# Objective: Combine multiple except blocks for ValueError, KeyError, and ZeroDivisionError.
# Tasks:
# - Create a product dictionary with potential invalid data.
# - Use try-except to handle ValueError, KeyError, and ZeroDivisionError.
# - Print the price per stock unit or an error message.
# Expected Output: Error: Invalid price format
product = {"name": "Tablet", "price": "abc"}
try:
    price = float(product["price"])
    stock = product["stock"]
    price_per_unit = price / stock
    print(f"Price per unit for {product['name']}: ${price_per_unit:.2f}")
except ValueError:
    print("Error: Invalid price format")
except KeyError:
    print("Error: Missing stock information")
except ZeroDivisionError:
    print("Error: Stock cannot be zero")