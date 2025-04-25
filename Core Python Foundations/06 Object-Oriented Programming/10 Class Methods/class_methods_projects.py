# Class Methods Projects
# Purpose: Apply Class Methods through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Store Name Accessor
# Difficulty: Basic
# Description: Retrieve a shared store name for retail products using a class method.
# Objective: Practice basic class methods for accessing class attributes.
# Tasks:
# - Define a Product class with a class attribute store_name and a get_store class method.
# - Call get_store and print the result.
# Expected Output: Store: RetailWorld
class Product:
    store_name = "RetailWorld"
    @classmethod
    def get_store(cls):
        return cls.store_name

print(f"Store: {Product.get_store()}")

# %% Project 2: Order Dictionary Constructor
# Difficulty: Basic
# Description: Create an order from a dictionary using a class method for retail orders.
# Objective: Practice class methods as alternative constructors.
# Tasks:
# - Create an Order class with a from_dict class method that creates an order from a dictionary.
# - Create an order from a dictionary and print its details.
# Expected Output: Order: 101, Total: $999.99
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    @classmethod
    def from_dict(cls, order_dict):
        return cls(order_dict["order_id"], order_dict["total"])
    def display(self):
        return f"Order: {self.order_id}, Total: ${self.total:.2f}"

order = Order.from_dict({"order_id": 101, "total": 999.99})
print(order.display())

# %% Project 3: Tax Rate Modifier
# Difficulty: Basic
# Description: Update a shared tax rate for retail products using a class method.
# Objective: Practice class methods for modifying class attributes.
# Tasks:
# - Define a Product class with a class attribute tax_rate and a set_tax class method.
# - Update the tax rate and print the new value.
# Expected Output: New tax rate: 0.15
class Product:
    tax_rate = 0.1
    @classmethod
    def set_tax(cls, rate):
        cls.tax_rate = rate

Product.set_tax(0.15)
print(f"New tax rate: {Product.tax_rate}")

# %% Project 4: Product String Constructor
# Difficulty: Intermediate
# Description: Create a product from a string input using a class method for retail inventory.
# Objective: Practice class methods for alternative object creation.
# Tasks:
# - Create a Product class with a from_string class method that parses "name,price".
# - Create a product from a string and print its details.
# Expected Output: Product: Smartphone, Price: $699.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def from_string(cls, product_str):
        name, price = product_str.split(",")
        return cls(name, float(price))
    def display(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

product = Product.from_string("Smartphone,699.99")
print(product.display())

# %% Project 5: Customer Category Updater
# Difficulty: Intermediate
# Description: Update a shared customer category for retail using a class method.
# Objective: Practice class methods for managing class-level data.
# Tasks:
# - Define a Customer class with a class attribute category and a set_category class method.
# - Update the category and print the new value.
# Expected Output: Customer category: Premium
class Customer:
    category = "Standard"
    @classmethod
    def set_category(cls, category):
        cls.category = category

Customer.set_category("Premium")
print(f"Customer category: {Customer.category}")

# %% Project 6: Inventory List Constructor
# Difficulty: Intermediate
# Description: Create an inventory item from a list using a class method for retail stock.
# Objective: Practice class methods for complex object creation.
# Tasks:
# - Create an InventoryItem class with a from_list class method that parses [name, price, stock].
# - Create an item from a list and print its details.
# Expected Output: Item: Coffee Maker, Stock: 30
class InventoryItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    @classmethod
    def from_list(cls, item_list):
        return cls(item_list[0], item_list[1], item_list[2])
    def display(self):
        return f"Item: {self.name}, Stock: {self.stock}"

item = InventoryItem.from_list(["Coffee Maker", 49.99, 30])
print(item.display())

# %% Project 6: Inventory List Constructor
# Difficulty: Intermediate
# Description: Create an inventory item from a list using a class method for retail stock.
# Objective: Practice class methods for complex object creation.
# Tasks:
# - Create an InventoryItem class with a from_list class method that parses [name, price, stock].
# - Create an item from a list and print its details.
# Expected Output: Item: Coffee Maker, Stock: 30
class InventoryItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    @classmethod
    def from_list(cls, item_list):
        return cls(item_list[0], item_list[1], item_list[2])
    def display(self):
        return f"Item: {self.name}, Stock: {self.stock}"

item = InventoryItem.from_list(["Coffee Maker", 49.99, 30])
print(item.display())

# %% Project 7: Discount Rate Modifier
# Difficulty: Intermediate
# Description: Update a shared discount rate for retail products using a class method.
# Objective: Practice class methods for retail settings.
# Tasks:
# - Define a Product class with a class attribute discount_rate and a set_discount class method.
# - Update the discount rate and print the new value.
# Expected Output: New discount rate: 0.2
class Product:
    discount_rate = 0.1
    @classmethod
    def set_discount(cls, rate):
        cls.discount_rate = rate

Product.set_discount(0.2)
print(f"New discount rate: {Product.discount_rate}")

# %% Project 8: Supplier Dictionary Constructor
# Difficulty: Advanced
# Description: Create a supplier from a dictionary using a class method for retail suppliers.
# Objective: Practice advanced class methods for object creation.
# Tasks:
# - Create a Supplier class with a from_dict class method that parses a dictionary with name and email.
# - Create a supplier from a dictionary and print its details.
# Expected Output: Supplier: TechCorp, Email: contact@techcorp.com
class Supplier:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    @classmethod
    def from_dict(cls, supplier_dict):
        return cls(supplier_dict["name"], supplier_dict["email"])
    def display(self):
        return f"Supplier: {self.name}, Email: {self.email}"

supplier = Supplier.from_dict({"name": "TechCorp", "email": "contact@techcorp.com"})
print(supplier.display())

# %% Project 9: Transaction Counter
# Difficulty: Advanced
# Description: Track the number of retail transactions using a class method.
# Objective: Practice class methods for managing class-level state.
# Tasks:
# - Create a Transaction class with a class attribute count and an increment_count class method.
# - Increment the count twice and print the result.
# Expected Output: Transaction count: 2
class Transaction:
    count = 0
    @classmethod
    def increment_count(cls):
        cls.count += 1

Transaction.increment_count()
Transaction.increment_count()
print(f"Transaction count: {Transaction.count}")

# %% Project 10: Cart Items Constructor
# Difficulty: Advanced
# Description: Create a shopping cart from a list of items using a class method for retail carts.
# Objective: Practice complex class methods for object creation.
# Tasks:
# - Create a Cart class with a from_items class method that parses a list of [name, price] pairs.
# - Create a cart from a list and print the total price.
# Expected Output: Cart total: $89.98
class Cart:
    def __init__(self, items):
        self.items = items
    @classmethod
    def from_items(cls, item_list):
        items = [{"name": name, "price": price} for name, price in item_list]
        return cls(items)
    def get_total(self):
        return sum(item["price"] for item in self.items)

cart = Cart.from_items([("Mouse", 29.99), ("Keyboard", 59.99)])
print(f"Cart total: ${cart.get_total():.2f}")