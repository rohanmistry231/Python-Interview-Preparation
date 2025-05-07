# Finally Clause Projects
# Purpose: Apply Finally Clause in try-except through 5 projects.
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions use retail-themed examples and simulate user inputs with fixed values for reproducibility.

# %% Project 1: Price Input Logger
# Difficulty: Basic
# Description: Process user-entered price with logging.
# Objective: Practice try-except-finally for ValueError handling with cleanup.
# Tasks:
# - Simulate user input for a price.
# - Use try-except-finally to catch ValueError and log completion.
# - Print the price, error, and log message.
# Expected Output: Error: Invalid price format, Price processing logged
simulated_input = "abc"  # Simulating invalid input
try:
    price = float(simulated_input)
    print(f"Price: ${price:.2f}")
except ValueError:
    print("Error: Invalid price format")
finally:
    print("Price processing logged")

# %% Project 2: Product Data Logger
# Difficulty: Basic
# Description: Access product data with logging regardless of errors.
# Objective: Use try-except-finally for KeyError handling.
# Tasks:
# - Create a product dictionary without stock.
# - Use try-except-finally to catch KeyError and log processing.
# - Print the stock, error, and log message.
# Expected Output: Error: Missing stock information, Product processing logged
product = {"name": "Smartphone", "price": "699.99"}
try:
    stock = product["stock"]
    print(f"Stock for {product['name']}: {stock}")
except KeyError:
    print("Error: Missing stock information")
finally:
    print("Product processing logged")

# %% Project 3: Order Processor Logger
# Difficulty: Intermediate
# Description: Process an order list with logging for all outcomes.
# Objective: Use try-except-finally for ValueError and IndexError in a retail context.
# Tasks:
# - Create an order list with name, quantity, and price.
# - Use try-except-finally to process total and log completion.
# - Print the total, error, and log message.
# Expected Output: Order total for Mouse: $149.95, Order processing logged
order = ["Mouse", "5", "29.99"]
try:
    quantity = int(order[1])
    price = float(order[2])
    total = quantity * price
    print(f"Order total for {order[0]}: ${total:.2f}")
except (ValueError, IndexError):
    print("Error: Invalid or incomplete order")
finally:
    print("Order processing logged")

# %% Project 4: Stock Validator Logger
# Difficulty: Intermediate
# Description: Validate stock quantities with logging.
# Objective: Use try-except-finally for ValueError and TypeError.
# Tasks:
# - Create a list of stock quantities with invalid entries.
# - Use try-except-finally to sum quantities and log processing.
# - Print the total, error, and log message.
# Expected Output: Error: Invalid stock format, Stock processing logged
stock = [10, "20", 30]
try:
    total = sum(int(qty) for qty in stock)
    print(f"Total stock: {total}")
except (ValueError, TypeError):
    print("Error: Invalid stock format")
finally:
    print("Stock processing logged")

# %% Project 5: Inventory Analysis Logger
# Difficulty: Advanced
# Description: Analyze inventory with logging for all scenarios.
# Objective: Combine try-except-finally for multiple exceptions.
# Tasks:
# - Create a product dictionary with potential invalid data.
# - Use try-except-finally to handle ValueError, KeyError, and ZeroDivisionError, logging completion.
# - Print the price per unit, error, and log message.
# Expected Output: Error: Stock cannot be zero, Inventory processing logged
product = {"name": "Blender", "price": "39.99", "stock": "0"}
try:
    price = float(product["price"])
    stock = int(product["stock"])
    price_per_unit = price / stock
    print(f"Price per unit for {product['name']}: ${price_per_unit:.2f}")
except ValueError:
    print("Error: Invalid price or stock format")
except KeyError:
    print("Error: Missing stock information")
except ZeroDivisionError:
    print("Error: Stock cannot be zero")
finally:
    print("Inventory processing logged")