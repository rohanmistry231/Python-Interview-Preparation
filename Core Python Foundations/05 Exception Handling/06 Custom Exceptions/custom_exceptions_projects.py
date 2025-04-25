# Custom Exceptions Projects
# Purpose: Apply Custom Exceptions through 5 projects.
# Structure: Each project is separated by %% and includes description, tasks, and best solution.
# Note: Solutions use retail-themed examples and simulate user inputs with fixed values for reproducibility.

# %% Project 1: Low Stock Exception
# Difficulty: Basic
# Description: Define and raise a custom exception for low stock levels.
# Objective: Practice defining and using a basic custom exception.
# Tasks:
# - Define a custom LowStockError.
# - Raise it if stock is below 10.
# - Print the stock or error message.
# Expected Output: Error: Stock too low
class LowStockError(Exception):
    pass

stock = 5
try:
    if stock < 10:
        raise LowStockError("Stock too low")
    print(f"Stock: {stock}")
except LowStockError as e:
    print(f"Error: {e}")

# %% Project 2: Negative Price Exception
# Difficulty: Basic
# Description: Create a custom exception with a price attribute for negative prices.
# Objective: Use custom exception with attributes for detailed error reporting.
# Tasks:
# - Define a NegativePriceError with a price attribute.
# - Raise it if price is negative.
# - Print the error and price value.
# Expected Output: Error: Negative price not allowed, Price: -20
class NegativePriceError(Exception):
    def __init__(self, message, price):
        super().__init__(message)
        self.price = price

price = -20
try:
    if price < 0:
        raise NegativePriceError("Negative price not allowed", price)
    print(f"Price: ${price:.2f}")
except NegativePriceError as e:
    print(f"Error: {e}, Price: {e.price}")

# %% Project 3: Invalid Order Exception
# Difficulty: Intermediate
# Description: Define a custom exception for invalid order quantities.
# Objective: Use custom exception in a retail context with order details.
# Tasks:
# - Define an InvalidOrderError with order details.
# - Raise it if quantity is zero.
# - Print the error and order details.
# Expected Output: Error: Quantity cannot be zero, Order: {'name': 'Mouse', 'quantity': 0, 'price': 29.99}
class InvalidOrderError(Exception):
    def __init__(self, message, order):
        super().__init__(message)
        self.order = order

order = {"name": "Mouse", "quantity": 0, "price": 29.99}
try:
    if order["quantity"] == 0:
        raise InvalidOrderError("Quantity cannot be zero", order)
    total = order["quantity"] * order["price"]
    print(f"Order total for {order['name']}: ${total:.2f}")
except InvalidOrderError as e:
    print(f"Error: {e}, Order: {e.order}")

# %% Project 4: Stock Format Exception
# Difficulty: Intermediate
# Description: Create a custom exception for invalid stock formats in a list.
# Objective: Combine custom exception with try-except for TypeError handling.
# Tasks:
# - Define a StockFormatError.
# - Raise it for non-numeric stock entries in a list.
# - Print the error message.
# Expected Output: Error: Invalid stock format
class StockFormatError(Exception):
    pass

stock = [10, "20", 30]
try:
    for qty in stock:
        if not isinstance(qty, (int, float)):
            raise StockFormatError("Invalid stock format")
    total = sum(stock)
    print(f"Total stock: {total}")
except StockFormatError as e:
    print(f"Error: {e}")

# %% Project 5: Complex Order Validator
# Difficulty: Advanced
# Description: Validate orders with multiple custom exceptions.
# Objective: Use multiple custom exceptions for comprehensive validation.
# Tasks:
# - Define NegativePriceError and InvalidOrderError.
# - Raise them for negative prices or excessive quantities.
# - Print the error and relevant details.
# Expected Output: Error: Quantity exceeds maximum limit, Order: {'name': 'Laptop', 'quantity': 200, 'price': 999.99}
class NegativePriceError(Exception):
    def __init__(self, message, price):
        super().__init__(message)
        self.price = price

class InvalidOrderError(Exception):
    def __init__(self, message, order):
        super().__init__(message)
        self.order = order

order = {"name": "Laptop", "quantity": 200, "price": 999.99}
try:
    if order["price"] < 0:
        raise NegativePriceError("Negative price not allowed", order["price"])
    if order["quantity"] > 100:
        raise InvalidOrderError("Quantity exceeds maximum limit", order)
    total = order["quantity"] * order["price"]
    print(f"Order total for {order['name']}: ${total:.2f}")
except NegativePriceError as e:
    print(f"Error: {e}, Price: {e.price}")
except InvalidOrderError as e:
    print(f"Error: {e}, Order: {e.order}")