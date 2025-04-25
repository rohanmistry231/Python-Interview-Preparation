# Creating Modules Projects
# Purpose: Apply Creating Modules through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions simulate module content in comments and handle ImportError, as actual .py files can't be created here.

# %% Project 1: Price Formatter Module
# Difficulty: Basic
# Description: Create a module to format retail prices.
# Objective: Practice creating a simple module with a function.
# Tasks:
# - Create a module price_utils.py with a format_price function.
# - Import the module and format a price.
# - Print the formatted price.
# Expected Output: Formatted price: $49.99
"""
# price_utils.py
def format_price(price):
    return f"${price:.2f}"
"""
# Simulate module import
def format_price(price):  # Inline for demo
    return f"${price:.2f}"

try:
    price = 49.99
    formatted = format_price(price)
    print(f"Formatted price: {formatted}")
except ImportError:
    print("Error: price_utils module not found (simulated)")

# %% Project 2: Order Class Module
# Difficulty: Basic
# Description: Create a module with an Order class for retail orders.
# Objective: Practice creating a module with a class.
# Tasks:
# - Create a module order_utils.py with an Order class.
# - Import the module and create an order object.
# - Print the order details.
# Expected Output: Order: 101, Total: $999.99
"""
# order_utils.py
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def display(self):
        return f"Order: {self.order_id}, Total: ${self.total:.2f}"
"""
# Simulate module import
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def display(self):
        return f"Order: {self.order_id}, Total: ${self.total:.2f}"

try:
    order = Order(101, 999.99)
    print(order.display())
except ImportError:
    print("Error: order_utils module not found (simulated)")

# %% Project 3: Stock Validator Module
# Difficulty: Basic
# Description: Create a module to validate inventory stock levels.
# Objective: Practice creating a module for validation logic.
# Tasks:
# - Create a module stock_utils.py with a validate_stock function.
# - Import the module and validate a stock level.
# - Print the validation result.
# Expected Output: Stock valid: True
"""
# stock_utils.py
def validate_stock(stock):
    return stock >= 0
"""
# Simulate module import
def validate_stock(stock):
    return stock >= 0

try:
    stock = 20
    valid = validate_stock(stock)
    print(f"Stock valid: {valid}")
except ImportError:
    print("Error: stock_utils module not found (simulated)")

# %% Project 4: Discount Calculator Module
# Difficulty: Intermediate
# Description: Create a module to calculate discounts for retail products.
# Objective: Practice creating a module with computational logic.
# Tasks:
# - Create a module discount_utils.py with a calculate_discount function.
# - Import the module and calculate a 10% discount.
# - Print the discounted price.
# Expected Output: Discounted price: $629.99
"""
# discount_utils.py
def calculate_discount(price, rate):
    return price * (1 - rate)
"""
# Simulate module import
def calculate_discount(price, rate):
    return price * (1 - rate)

try:
    price = 699.99
    discounted = calculate_discount(price, 0.1)
    print(f"Discounted price: ${discounted:.2f}")
except ImportError:
    print("Error: discount_utils module not found (simulated)")

# %% Project 5: Customer Formatter Module
# Difficulty: Intermediate
# Description: Create a module to format customer information.
# Objective: Practice creating a module for string formatting.
# Tasks:
# - Create a module customer_utils.py with a format_customer function.
# - Import the module and format customer data.
# - Print the formatted customer info.
# Expected Output: Customer: Alice, Email: alice@example.com
"""
# customer_utils.py
def format_customer(name, email):
    return f"Customer: {name}, Email: {email}"
"""
# Simulate module import
def format_customer(name, email):
    return f"Customer: {name}, Email: {email}"

try:
    formatted = format_customer("Alice", "alice@example.com")
    print(formatted)
except ImportError:
    print("Error: customer_utils module not found (simulated)")

# %% Project 6: Tax Calculator Module
# Difficulty: Intermediate
# Description: Create a module to calculate sales tax for retail orders.
# Objective: Practice creating a module for financial calculations.
# Tasks:
# - Create a module tax_utils.py with a calculate_tax function (10% rate).
# - Import the module and calculate tax for a price.
# - Print the tax amount.
# Expected Output: Tax: $69.99
"""
# tax_utils.py
def calculate_tax(price):
    return price * 0.1
"""
# Simulate module import
def calculate_tax(price):
    return price * 0.1

try:
    price = 699.99
    tax = calculate_tax(price)
    print(f"Tax: ${tax:.2f}")
except ImportError:
    print("Error: tax_utils module not found (simulated)")

# %% Project 7: Inventory Manager Module
# Difficulty: Intermediate
# Description: Create a module with a class to manage inventory items.
# Objective: Practice creating a module with a complex class.
# Tasks:
# - Create a module inventory_utils.py with an InventoryItem class.
# - Import the module and create an inventory item.
# - Print the item details.
# Expected Output: Item: Coffee Maker, Stock: 30
"""
# inventory_utils.py
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def display(self):
        return f"Item: {self.name}, Stock: {self.stock}"
"""
# Simulate module import
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def display(self):
        return f"Item: {self.name}, Stock: {self.stock}"

try:
    item = InventoryItem("Coffee Maker", 30)
    print(item.display())
except ImportError:
    print("Error: inventory_utils module not found (simulated)")

# %% Project 8: Transaction Logger Module
# Difficulty: Advanced
# Description: Create a module to log retail transactions.
# Objective: Practice creating a module for logging.
# Tasks:
# - Create a module transaction_utils.py with a log_transaction function.
# - Import the module and log a transaction.
# - Print the transaction log.
# Expected Output: Transaction logged: ID 1001, Amount: $999.99
"""
# transaction_utils.py
def log_transaction(transaction_id, amount):
    return f"Transaction logged: ID {transaction_id}, Amount: ${amount:.2f}"
"""
# Simulate module import
def log_transaction(transaction_id, amount):
    return f"Transaction logged: ID {transaction_id}, Amount: ${amount:.2f}"

try:
    log = log_transaction(1001, 999.99)
    print(log)
except ImportError:
    print("Error: transaction_utils module not found (simulated)")

# %% Project 9: Promotion Validator Module
# Difficulty: Advanced
# Description: Create a module to validate retail promotion rates.
# Objective: Practice creating a module with validation logic.
# Tasks:
# - Create a module promotion_utils.py with a validate_promo_rate function.
# - Import the module and validate a promotion rate.
# - Print the validation result.
# Expected Output: Valid promotion rate: True
"""
# promotion_utils.py
def validate_promo_rate(rate):
    return 0 <= rate <= 1
"""
# Simulate module import
def validate_promo_rate(rate):
    return 0 <= rate <= 1

try:
    valid = validate_promo_rate(0.15)
    print(f"Valid promotion rate: {valid}")
except ImportError:
    print("Error: promotion_utils module not found (simulated)")

# %% Project 10: Comprehensive Retail Utilities Module
# Difficulty: Advanced
# Description: Create a module with multiple utilities for retail operations.
# Objective: Practice creating a complex module with functions and classes.
# Tasks:
# - Create a module retail_utils.py with a Product class and calculate_discount function.
# - Import the module, create a product, and calculate a discount.
# - Print the product and discounted price.
# Expected Output: Product: Smartphone, Price: $699.99
#                 Discounted price: $594.99
"""
# retail_utils.py
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

def calculate_discount(price, rate):
    return price * (1 - rate)
"""
# Simulate module import
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

def calculate_discount(price, rate):
    return price * (1 - rate)

try:
    product = Product("Smartphone", 699.99)
    discounted = calculate_discount(product.price, 0.15)
    print(product.display())
    print(f"Discounted price: ${discounted:.2f}")
except ImportError:
    print("Error: retail_utils module not found (simulated)")