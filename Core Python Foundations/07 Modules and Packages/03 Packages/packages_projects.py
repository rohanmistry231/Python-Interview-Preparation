# Packages Projects
# Purpose: Apply Packages through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions simulate package structure in comments and handle ImportError, as actual package directories can't be created here.

# %% Project 1: Price Formatter Package
# Difficulty: Basic
# Description: Use a package module to format retail prices.
# Objective: Practice importing from a package.
# Tasks:
# - Create a retail_package with a utils.py module containing a format_price function.
# - Import the function and format a price.
# - Print the formatted price.
# Expected Output: Formatted price: $49.99
"""
# retail_package/utils.py
def format_price(price):
    return f"${price:.2f}"
"""
# Simulate package import
def format_price(price):
    return f"${price:.2f}"

try:
    price = 49.99
    formatted = format_price(price)
    print(f"Formatted price: {formatted}")
except ImportError:
    print("Error: retail_package.utils not found (simulated)")

# %% Project 2: Order Class Package
# Difficulty: Basic
# Description: Use a package module with an Order class for retail orders.
# Objective: Practice accessing classes from a package.
# Tasks:
# - Create a retail_package with an orders.py module containing an Order class.
# - Import the class and create an order object.
# - Print the order details.
# Expected Output: Order: 101, Total: $999.99
"""
# retail_package/orders.py
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def display(self):
        return f"Order: {self.order_id}, Total: ${self.total:.2f}"
"""
# Simulate package import
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
    print("Error: retail_package.orders not found (simulated)")

# %% Project 3: Stock Checker Package
# Difficulty: Basic
# Description: Use a package module to check inventory stock levels.
# Objective: Practice package module imports.
# Tasks:
# - Create a retail_package with a stock.py module containing a check_stock function.
# - Import the function and check a stock level.
# - Print the stock status.
# Expected Output: Stock status: Low
"""
# retail_package/stock.py
def check_stock(stock):
    return "Low" if stock < 50 else "Sufficient"
"""
# Simulate package import
def check_stock(stock):
    return "Low" if stock < 50 else "Sufficient"

try:
    stock = 30
    status = check_stock(stock)
    print(f"Stock status: {status}")
except ImportError:
    print("Error: retail_package.stock not found (simulated)")

# %% Project 4: Discount Calculator Package
# Difficulty: Intermediate
# Description: Use a package module to calculate discounts for retail products.
# Objective: Practice package imports for computations.
# Tasks:
# - Create a retail_package with a products.py module containing a calculate_discount function.
# - Import the function and calculate a 10% discount.
# - Print the discounted price.
# Expected Output: Discounted price: $629.99
"""
# retail_package/products.py
def calculate_discount(price, rate):
    return price * (1 - rate)
"""
# Simulate package import
def calculate_discount(price, rate):
    return price * (1 - rate)

try:
    price = 699.99
    discounted = calculate_discount(price, 0.1)
    print(f"Discounted price: ${discounted:.2f}")
except ImportError:
    print("Error: retail_package.products not found (simulated)")

# %% Project 5: Customer Manager Package
# Difficulty: Intermediate
# Description: Use a package module to manage customer data.
# Objective: Practice package imports for class-based operations.
# Tasks:
# - Create a retail_package with a customers.py module containing a Customer class.
# - Import the class and create a customer object.
# - Print the customer details.
# Expected Output: Customer: Alice, Email: alice@example.com
"""
# retail_package/customers.py
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display(self):
        return f"Customer: {self.name}, Email: {self.email}"
"""
# Simulate package import
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display(self):
        return f"Customer: {self.name}, Email: {self.email}"

try:
    customer = Customer("Alice", "alice@example.com")
    print(customer.display())
except ImportError:
    print("Error: retail_package.customers not found (simulated)")

# %% Project 6: Tax Calculator Package
# Difficulty: Intermediate
# Description: Use a package module to calculate sales tax for retail orders.
# Objective: Practice package imports for financial calculations.
# Tasks:
# - Create a retail_package with a tax.py module containing a calculate_tax function.
# - Import the function and calculate tax for a price.
# - Print the tax amount.
# Expected Output: Tax: $69.99
"""
# retail_package/tax.py
def calculate_tax(price):
    return price * 0.1
"""
# Simulate package import
def calculate_tax(price):
    return price * 0.1

try:
    price = 699.99
    tax = calculate_tax(price)
    print(f"Tax: ${tax:.2f}")
except ImportError:
    print("Error: retail_package.tax not found (simulated)")

# %% Project 7: Inventory Tracker Package
# Difficulty: Intermediate
# Description: Use a package module to track inventory items.
# Objective: Practice package imports for inventory management.
# Tasks:
# - Create a retail_package with an inventory.py module containing an InventoryItem class.
# - Import the class and create an inventory item.
# - Print the item details.
# Expected Output: Item: Coffee Maker, Stock: 30
"""
# retail_package/inventory.py
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def display(self):
        return f"Item: {self.name}, Stock: {self.stock}"
"""
# Simulate package import
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
    print("Error: retail_package.inventory not found (simulated)")

# %% Project 8: Transaction Logger Package
# Difficulty: Advanced
# Description: Use a package module to log retail transactions.
# Objective: Practice package imports for logging.
# Tasks:
# - Create a retail_package with a transactions.py module containing a log_transaction function.
# - Import the function and log a transaction.
# - Print the transaction log.
# Expected Output: Transaction logged: ID 1001, Amount: $999.99
"""
# retail_package/transactions.py
def log_transaction(transaction_id, amount):
    return f"Transaction logged: ID {transaction_id}, Amount: ${amount:.2f}"
"""
# Simulate package import
def log_transaction(transaction_id, amount):
    return f"Transaction logged: ID {transaction_id}, Amount: ${amount:.2f}"

try:
    log = log_transaction(1001, 999.99)
    print(log)
except ImportError:
    print("Error: retail_package.transactions not found (simulated)")

# %% Project 9: Promotion Manager Package
# Difficulty: Advanced
# Description: Use a package module to manage retail promotions.
# Objective: Practice package imports for complex operations.
# Tasks:
# - Create a retail_package with a promotions.py module containing a validate_promo_rate function.
# - Import the function and validate a promotion rate.
# - Print the validation result.
# Expected Output: Valid promotion rate: True
"""
# retail_package/promotions.py
def validate_promo_rate(rate):
    return 0 <= rate <= 1
"""
# Simulate package import
def validate_promo_rate(rate):
    return 0 <= rate <= 1

try:
    valid = validate_promo_rate(0.15)
    print(f"Valid promotion rate: {valid}")
except ImportError:
    print("Error: retail_package.promotions not found (simulated)")

# %% Project 10: Comprehensive Retail Package
# Difficulty: Advanced
# Description: Use multiple package modules for a retail operation.
# Objective: Practice integrating multiple package modules.
# Tasks:
# - Create a retail_package with products.py (calculate_discount) and orders.py (Order class).
# - Import both modules, create an order with a discounted price, and print the order details.
# Expected Output: Order 102: Total $594.99
"""
# retail_package/products.py
def calculate_discount(price, rate):
    return price * (1 - rate)
"""
"""
# retail_package/orders.py
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def display(self):
        return f"Order {self.order_id}: Total ${self.total:.2f}"
"""
# Simulate package import
def calculate_discount(price, rate):
    return price * (1 - rate)

class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def display(self):
        return f"Order {self.order_id}: Total ${self.total:.2f}"

try:
    price = 699.99
    discounted = calculate_discount(price, 0.15)
    order = Order(102, discounted)
    print(order.display())
except ImportError:
    print("Error: retail_package not found (simulated)")