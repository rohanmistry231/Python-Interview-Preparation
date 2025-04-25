# Static Methods Projects
# Purpose: Apply Static Methods through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Price Formatter Utility
# Difficulty: Basic
# Description: Format product prices using a static method for retail display.
# Objective: Practice defining a static method for formatting.
# Tasks:
# - Define a Product class with a static format_price method that formats a price as $XX.XX.
# - Call format_price with a price and print the result.
# Expected Output: Formatted price: $29.99
class Product:
    @staticmethod
    def format_price(price):
        return f"${price:.2f}"

print(f"Formatted price: {Product.format_price(29.99)}")

# %% Project 2: Order ID Validator
# Difficulty: Basic
# Description: Validate retail order IDs using a static method.
# Objective: Practice static methods for input validation.
# Tasks:
# - Create an Order class with a static is_valid_id method to check if an ID is a positive integer.
# - Check an order ID and print the result.
# Expected Output: Valid ID: True
class Order:
    @staticmethod
    def is_valid_id(order_id):
        return isinstance(order_id, int) and order_id > 0

print(f"Valid ID: {Order.is_valid_id(101)}")

# %% Project 3: Stock Status Indicator
# Difficulty: Basic
# Description: Indicate stock status using a static method for inventory management.
# Objective: Practice static methods for status checks.
# Tasks:
# - Define an InventoryItem class with a static stock_status method that returns "Low" if stock < 50, else "Sufficient".
# - Call stock_status with a stock value and print the result.
# Expected Output: Stock status: Low
class InventoryItem:
    @staticmethod
    def stock_status(stock):
        return "Low" if stock < 50 else "Sufficient"

print(f"Stock status: {InventoryItem.stock_status(30)}")

# %% Project 4: Tax Calculator Utility
# Difficulty: Intermediate
# Description: Calculate sales tax for retail products using a static method.
# Objective: Practice static methods for computations.
# Tasks:
# - Create a Product class with a static calculate_tax method that applies a 10% tax rate.
# - Compute tax for a given price and print the result.
# Expected Output: Tax: $69.99
class Product:
    @staticmethod
    def calculate_tax(price):
        return price * 0.1

print(f"Tax: ${Product.calculate_tax(699.99):.2f}")

# %% Project 5: Discount Rate Validator
# Difficulty: Intermediate
# Description: Validate discount rates for retail promotions using a static method.
# Objective: Practice static methods for validation logic.
# Tasks:
# - Define a Promotion class with a static is_valid_discount method to check if a rate is between 0 and 1.
# - Check a discount rate and print the result.
# Expected Output: Valid discount: True
class Promotion:
    @staticmethod
    def is_valid_discount(rate):
        return 0 <= rate <= 1

print(f"Valid discount: {Promotion.is_valid_discount(0.15)}")

# %% Project 6: Email Address Formatter
# Difficulty: Intermediate
# Description: Format customer email addresses for retail communication using a static method.
# Objective: Practice static methods for string formatting.
# Tasks:
# - Create a Customer class with a static format_email method that ensures a lowercase email format.
# - Format an email address and print the result.
# Expected Output: Formatted email: alice@store.com
class Customer:
    @staticmethod
    def format_email(email):
        return email.lower()

print(f"Formatted email: {Customer.format_email('Alice@Store.com')}")

# %% Project 7: Total With Fee Calculator
# Difficulty: Intermediate
# Description: Calculate an order total including a transaction fee using a static method.
# Objective: Practice static methods for financial calculations.
# Tasks:
# - Define an Order class with a static total_with_fee method that adds a $5 fee to a total.
# - Compute the total with fee for a given amount and print the result.
# Expected Output: Total with fee: $1004.99
class Order:
    @staticmethod
    def total_with_fee(total):
        return total + 5.00

print(f"Total with fee: ${Order.total_with_fee(999.99):.2f}")

# %% Project 8: Stock Threshold Checker
# Difficulty: Advanced
# Description: Check if inventory stock meets a minimum threshold using a static method.
# Objective: Practice complex static methods for inventory control.
# Tasks:
# - Create an InventoryItem class with a static meets_threshold method that checks if stock is above a given threshold.
# - Check if a stock level meets a threshold of 50 and print the result.
# Expected Output: Meets threshold: False
class InventoryItem:
    @staticmethod
    def meets_threshold(stock, threshold):
        return stock >= threshold

print(f"Meets threshold: {InventoryItem.meets_threshold(30, 50)}")

# %% Project 9: Transaction ID Formatter
# Difficulty: Advanced
# Description: Format transaction IDs for retail records using a static method.
# Objective: Practice static methods for complex formatting.
# Tasks:
# - Define a Transaction class with a static format_id method that prefixes an ID with "TXN-".
# - Format a transaction ID and print the result.
# Expected Output: Transaction ID: TXN-1001
class Transaction:
    @staticmethod
    def format_id(transaction_id):
        return f"TXN-{transaction_id}"

print(f"Transaction ID: {Transaction.format_id(1001)}")

# %% Project 10: Price Range Validator
# Difficulty: Advanced
# Description: Validate product prices within an acceptable range for retail using a static method.
# Objective: Practice advanced static method logic for validation.
# Tasks:
# - Create a Product class with a static is_valid_price_range method that checks if a price is between $10 and $1000.
# - Check a price and print the result.
# Expected Output: Valid price range: True
class Product:
    @staticmethod
    def is_valid_price_range(price):
        return 10 <= price <= 1000

print(f"Valid price range: {Product.is_valid_price_range(699.99)}")