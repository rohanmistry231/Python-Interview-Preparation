# Attributes Projects
# Purpose: Apply Attributes through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Product Price Updater
# Difficulty: Basic
# Description: Create a Product class and update its price.
# Objective: Practice instance attribute modification.
# Tasks:
# - Define a Product class with name and price attributes.
# - Create a product and update its price.
# - Print the updated price.
# Expected Output: Updated price: $25.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Mouse", 29.99)
product.price = 25.99
print(f"Updated price: ${product.price:.2f}")

# %% Project 2: Order Status Tracker
# Difficulty: Basic
# Description: Track order status using an instance attribute.
# Objective: Practice defining and accessing instance attributes.
# Tasks:
# - Create an Order class with order_id and status attributes.
# - Create an order and print its status.
# Expected Output: Order 102 Status: Pending
class Order:
    def __init__(self, order_id, status):
        self.order_id = order_id
        self.status = status

order = Order(102, "Pending")
print(f"Order {order.order_id} Status: {order.status}")

# %% Project 3: Store Name Shared Attribute
# Difficulty: Basic
# Description: Use a class attribute for store name across products.
# Objective: Practice class attributes.
# Tasks:
# - Define a Product class with a class attribute store_name and instance attribute name.
# - Create a product and print the store name.
# Expected Output: Store: RetailWorld
class Product:
    store_name = "RetailWorld"
    def __init__(self, name):
        self.name = name

product = Product("Keyboard")
print(f"Store: {Product.store_name}")

# %% Project 4: Customer Points System
# Difficulty: Intermediate
# Description: Track customer loyalty points as an instance attribute.
# Objective: Modify instance attributes dynamically.
# Tasks:
# - Create a Customer class with name and points attributes.
# - Update the points for a customer.
# - Print the updated points.
# Expected Output: Customer: Bob, Points: 150
class Customer:
    def __init__(self, name, points):
        self.name = name
        self.points = points

customer = Customer("Bob", 100)
customer.points = 150
print(f"Customer: {customer.name}, Points: {customer.points}")

# %% Project 5: Product Tax Rate
# Difficulty: Intermediate
# Description: Update a shared tax rate for all products.
# Objective: Practice modifying class attributes.
# Tasks:
# - Define a Product class with a class attribute tax_rate and instance attribute price.
# - Update the tax rate and print it.
# Expected Output: New tax rate: 0.2
class Product:
    tax_rate = 0.1
    def __init__(self, price):
        self.price = price

Product.tax_rate = 0.2
print(f"New tax rate: {Product.tax_rate}")

# %% Project 6: Inventory Stock Tracker
# Difficulty: Intermediate
# Description: Manage stock levels as an instance attribute.
# Objective: Use instance attributes for inventory.
# Tasks:
# - Create an InventoryItem class with name and stock attributes.
# - Update the stock and print it.
# Expected Output: Item: Smartphone, Stock: 25
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

item = InventoryItem("Smartphone", 20)
item.stock = 25
print(f"Item: {item.name}, Stock: {item.stock}")

# %% Project 7: Promotion Discount Rate
# Difficulty: Intermediate
# Description: Use a class attribute for a shared discount rate.
# Objective: Apply class attributes in a retail context.
# Tasks:
# - Define a Product class with a class attribute discount_rate and instance attribute name.
# - Create two products and print the discount rate.
# Expected Output: Discount rate: 0.15
class Product:
    discount_rate = 0.1
    def __init__(self, name):
        self.name = name

product1 = Product("Laptop")
product2 = Product("Mouse")
Product.discount_rate = 0.15
print(f"Discount rate: {Product.discount_rate}")

# %% Project 8: Supplier Rating
# Difficulty: Advanced
# Description: Track supplier ratings as an instance attribute.
# Objective: Manage complex instance attributes.
# Tasks:
# - Create a Supplier class with name and rating attributes.
# - Update the rating and print it.
# Expected Output: Supplier: TechCorp, Rating: 4.5
class Supplier:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

supplier = Supplier("TechCorp", 4.0)
supplier.rating = 4.5
print(f"Supplier: {supplier.name}, Rating: {supplier.rating}")

# %% Project 9: Transaction Fee
# Difficulty: Advanced
# Description: Apply a shared transaction fee across orders.
# Objective: Use class attributes for shared fees.
# Tasks:
# - Define an Order class with a class attribute transaction_fee and instance attribute total.
# - Update the fee and print it.
# Expected Output: Transaction fee: $5.00
class Order:
    transaction_fee = 2.50
    def __init__(self, total):
        self.total = total

Order.transaction_fee = 5.00
print(f"Transaction fee: ${Order.transaction_fee:.2f}")

# %% Project 10: Cart Total Accumulator
# Difficulty: Advanced
# Description: Accumulate total cost in a cart as an instance attribute.
# Objective: Combine instance attribute updates.
# Tasks:
# - Create a Cart class with items and total attributes.
# - Add an item’s cost to the total and print it.
# Expected Output: Cart Total: $1299.98
class Cart:
    def __init__(self, items, total):
        self.items = items
        self.total = total

cart = Cart(["Smartphone"], 599.99)
cart.total += 699.99
print(f"Cart Total: ${cart.total:.2f}")