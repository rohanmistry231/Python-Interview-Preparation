# Classes and Objects Projects
# Purpose: Apply Classes and Objects through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Basic Product Creator
# Difficulty: Basic
# Description: Create a Product class with name and price attributes.
# Objective: Practice defining a class and creating an object.
# Tasks:
# - Define a Product class with name and price in __init__.
# - Create one product object.
# - Print the product’s name and price.
# Expected Output: Product: Mouse, Price: $29.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Mouse", 29.99)
print(f"Product: {product.name}, Price: ${product.price:.2f}")

# %% Project 2: Order Initializer
# Difficulty: Basic
# Description: Define an Order class to store order details.
# Objective: Practice initializing objects with multiple attributes.
# Tasks:
# - Create an Order class with order_id and total attributes.
# - Instantiate an order object.
# - Print the order details.
# Expected Output: Order ID: 101, Total: $1999.98
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

order = Order(101, 1999.98)
print(f"Order ID: {order.order_id}, Total: ${order.total:.2f}")

# %% Project 3: Customer Profile
# Difficulty: Basic
# Description: Model a customer with name and email attributes.
# Objective: Practice class creation for a retail entity.
# Tasks:
# - Define a Customer class with name and email.
# - Create a customer object.
# - Print the customer’s details.
# Expected Output: Customer: Alice, Email: alice@example.com
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

customer = Customer("Alice", "alice@example.com")
print(f"Customer: {customer.name}, Email: {customer.email}")

# %% Project 4: Product Category
# Difficulty: Intermediate
# Description: Create a Product class with a category attribute.
# Objective: Extend class attributes for categorization.
# Tasks:
# - Define a Product class with name, price, and category.
# - Create two product objects with different categories.
# - Print their details.
# Expected Output: Product: Blender, Category: Appliances
#                 Product: Keyboard, Category: Electronics
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

blender = Product("Blender", 39.99, "Appliances")
keyboard = Product("Keyboard", 59.99, "Electronics")
print(f"Product: {blender.name}, Category: {blender.category}")
print(f"Product: {keyboard.name}, Category: {keyboard.category}")

# %% Project 5: Inventory Item
# Difficulty: Intermediate
# Description: Model an inventory item with stock tracking.
# Objective: Use classes to manage retail inventory.
# Tasks:
# - Create an InventoryItem class with name, price, and stock.
# - Instantiate an item.
# - Print the item’s details.
# Expected Output: Item: Coffee Maker, Price: $49.99, Stock: 30
class InventoryItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

item = InventoryItem("Coffee Maker", 49.99, 30)
print(f"Item: {item.name}, Price: ${item.price:.2f}, Stock: {item.stock}")

# %% Project 6: Cart Item
# Difficulty: Intermediate
# Description: Define a class for items in a shopping cart.
# Objective: Practice classes for cart management.
# Tasks:
# - Create a CartItem class with product_name, quantity, and unit_price.
# - Create a cart item object.
# - Print the item’s details.
# Expected Output: Cart Item: Smartphone, Quantity: 2, Unit Price: $699.99
class CartItem:
    def __init__(self, product_name, quantity, unit_price):
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

cart_item = CartItem("Smartphone", 2, 699.99)
print(f"Cart Item: {cart_item.product_name}, Quantity: {cart_item.quantity}, Unit Price: ${cart_item.unit_price:.2f}")

# %% Project 7: Store Branch
# Difficulty: Intermediate
# Description: Model a retail store branch with location and manager.
# Objective: Apply classes to store management.
# Tasks:
# - Define a StoreBranch class with location and manager_name.
# - Create a branch object.
# - Print the branch details.
# Expected Output: Branch: Downtown, Manager: Bob
class StoreBranch:
    def __init__(self, location, manager_name):
        self.location = location
        self.manager_name = manager_name

branch = StoreBranch("Downtown", "Bob")
print(f"Branch: {branch.location}, Manager: {branch.manager_name}")

# %% Project 8: Promotion Record
# Difficulty: Advanced
# Description: Create a class to track product promotions.
# Objective: Use classes for promotional data.
# Tasks:
# - Define a Promotion class with product_name, discount_rate, and start_date.
# - Instantiate a promotion.
# - Print the promotion details.
# Expected Output: Promotion: Laptop, Discount: 15%, Start Date: 2025-05-01
class Promotion:
    def __init__(self, product_name, discount_rate, start_date):
        self.product_name = product_name
        self.discount_rate = discount_rate
        self.start_date = start_date

promotion = Promotion("Laptop", 0.15, "2025-05-01")
print(f"Promotion: {promotion.product_name}, Discount: {promotion.discount_rate:.0%}, Start Date: {promotion.start_date}")

# %% Project 9: Supplier Contact
# Difficulty: Advanced
# Description: Model a supplier with contact information.
# Objective: Practice complex class initialization.
# Tasks:
# - Create a Supplier class with name, contact_email, and phone.
# - Create a supplier object.
# - Print the supplier’s details.
# Expected Output: Supplier: TechCorp, Email: contact@techcorp.com, Phone: 555-1234
class Supplier:
    def __init__(self, name, contact_email, phone):
        self.name = name
        self.contact_email = contact_email
        self.phone = phone

supplier = Supplier("TechCorp", "contact@techcorp.com", "555-1234")
print(f"Supplier: {supplier.name}, Email: {supplier.contact_email}, Phone: {supplier.phone}")

# %% Project 10: Transaction Log
# Difficulty: Advanced
# Description: Define a class to log retail transactions.
# Objective: Use classes for transaction tracking.
# Tasks:
# - Create a Transaction class with transaction_id, amount, and date.
# - Instantiate a transaction.
# - Print the transaction details.
# Expected Output: Transaction ID: 1001, Amount: $999.99, Date: 2025-04-25
class Transaction:
    def __init__(self, transaction_id, amount, date):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date

transaction = Transaction(1001, 999.99, "2025-04-25")
print(f"Transaction ID: {transaction.transaction_id}, Amount: ${transaction.amount:.2f}, Date: {transaction.date}")