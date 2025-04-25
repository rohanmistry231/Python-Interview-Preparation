# Methods Projects
# Purpose: Apply Methods through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Product Discount Applier
# Difficulty: Basic
# Description: Apply a discount to a product’s price.
# Objective: Practice defining and calling instance methods.
# Tasks:
# - Create a Product class with name, price, and an apply_discount method.
# - Apply a 10% discount and print the new price.
# Expected Output: Discounted price: $26.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, discount):
        self.price *= (1 - discount)
        return self.price

product = Product("Mouse", 29.99)
new_price = product.apply_discount(0.1)
print(f"Discounted price: ${new_price:.2f}")

# %% Project 2: Order Details Display
# Difficulty: Basic
# Description: Display order details using a method.
# Objective: Practice methods that return formatted strings.
# Tasks:
# - Define an Order class with order_id, total, and a display method.
# - Call display and print the result.
# Expected Output: Order 101: $999.99
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def display(self):
        return f"Order {self.order_id}: ${self.total:.2f}"

order = Order(101, 999.99)
print(order.display())

# %% Project 3: Customer Info Getter
# Difficulty: Basic
# Description: Retrieve customer information via a method.
# Objective: Practice methods accessing instance attributes.
# Tasks:
# - Create a Customer class with name, email, and a get_info method.
# - Call get_info and print the result.
# Expected Output: Customer: Alice, Email: alice@example.com
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def get_info(self):
        return f"Customer: {self.name}, Email: {self.email}"

customer = Customer("Alice", "alice@example.com")
print(customer.get_info())

# %% Project 4: Inventory Restock
# Difficulty: Intermediate
# Description: Restock inventory using a method.
# Objective: Practice methods that modify instance attributes.
# Tasks:
# - Define an InventoryItem class with name, stock, and a restock method.
# - Restock by 20 units and print the new stock.
# Expected Output: New stock: 50
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def restock(self, amount):
        self.stock += amount
        return self.stock

item = InventoryItem("Blender", 30)
new_stock = item.restock(20)
print(f"New stock: {new_stock}")

# %% Project 5: Cart Total Calculator
# Difficulty: Intermediate
# Description: Calculate the total cost of cart items.
# Objective: Practice methods with parameters.
# Tasks:
# - Create a Cart class with items and a calculate_total method.
# - Calculate the total for given quantities and print it.
# Expected Output: Cart Total: $1499.97
class Cart:
    def __init__(self, items):
        self.items = items
    def calculate_total(self, quantities):
        total = sum(item["price"] * qty for item, qty in zip(self.items, quantities))
        return total

cart = Cart([{"price": 699.99}, {"price": 99.99}])
total = cart.calculate_total([2, 1])
print(f"Cart Total: ${total:.2f}")

# %% Project 6: Product Tax Calculator
# Difficulty: Intermediate
# Description: Calculate tax for a product.
# Objective: Practice methods returning computed values.
# Tasks:
# - Define a Product class with price and a calculate_tax method (10% rate).
# - Compute and print the tax.
# Expected Output: Tax: $69.99
class Product:
    def __init__(self, price):
        self.price = price
    def calculate_tax(self):
        return self.price * 0.1

product = Product(699.99)
tax = product.calculate_tax()
print(f"Tax: ${tax:.2f}")

# %% Project 7: Supplier Contact Formatter
# Difficulty: Intermediate
# Description: Format supplier contact details.
# Objective: Practice methods for string formatting.
# Tasks:
# - Create a Supplier class with name, email, and a format_contact method.
# - Call format_contact and print the result.
# Expected Output: Supplier: TechCorp, Contact: contact@techcorp.com
class Supplier:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def format_contact(self):
        return f"Supplier: {self.name}, Contact: {self.email}"

supplier = Supplier("TechCorp", "contact@techcorp.com")
print(supplier.format_contact())

# %% Project 8: Promotion Discount Checker
# Difficulty: Advanced
# Description: Check if a promotion discount is valid.
# Objective: Practice methods with conditional logic.
# Tasks:
# - Define a Promotion class with discount_rate and a is_valid_discount method.
# - Check if the discount is between 0 and 1, and print the result.
# Expected Output: Discount valid: False
class Promotion:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate
    def is_valid_discount(self):
        return 0 <= self.discount_rate <= 1

promotion = Promotion(1.5)
print(f"Discount valid: {promotion.is_valid_discount()}")

# %% Project 9: Transaction Fee Adder
# Difficulty: Advanced
# Description: Add a transaction fee to an order total.
# Objective: Practice methods combining attributes and parameters.
# Tasks:
# - Create an Order class with total and an add_fee method.
# - Add a $5 fee and print the new total.
# Expected Output: Total with fee: $1004.99
class Order:
    def __init__(self, total):
        self.total = total
    def add_fee(self, fee):
        self.total += fee
        return self.total

order = Order(999.99)
new_total = order.add_fee(5.00)
print(f"Total with fee: ${new_total:.2f}")

# %% Project 10: Stock Availability Checker
# Difficulty: Advanced
# Description: Check stock availability for an order.
# Objective: Practice methods with complex logic.
# Tasks:
# - Define an InventoryItem class with stock and a check_availability method.
# - Check if a requested quantity is available and print the result.
# Expected Output: Stock available for 15 units: False
class InventoryItem:
    def __init__(self, stock):
        self.stock = stock
    def check_availability(self, quantity):
        return self.stock >= quantity

item = InventoryItem(10)
available = item.check_availability(15)
print(f"Stock available for 15 units: {available}")