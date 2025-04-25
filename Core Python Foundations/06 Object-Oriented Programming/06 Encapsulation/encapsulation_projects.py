# Encapsulation Projects
# Purpose: Apply Encapsulation through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Protected Price Accessor
# Difficulty: Basic
# Description: Use a protected price attribute with a getter.
# Objective: Practice single underscore protection.
# Tasks:
# - Define a Product class with a protected _price attribute and get_price method.
# - Create a product and print the price via getter.
# Expected Output: Price: $29.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    def get_price(self):
        return self._price

product = Product("Mouse", 29.99)
print(f"Price: ${product.get_price():.2f}")

# %% Project 2: Private Order Total
# Difficulty: Basic
# Description: Protect an order’s total with getter/setter methods.
# Objective: Practice double underscore encapsulation.
# Tasks:
# - Create an Order class with a private __total attribute and getter/setter.
# - Update the total and print it.
# Expected Output: Updated total: $999.99
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.__total = total
    def get_total(self):
        return self.__total
    def set_total(self, total):
        self.__total = total

order = Order(101, 799.99)
order.set_total(999.99)
print(f"Updated total: ${order.get_total():.2f}")

# %% Project 3: Customer Email Protector
# Difficulty: Basic
# Description: Protect customer email with encapsulation.
# Objective: Practice private attributes with validation.
# Tasks:
# - Define a Customer class with a private __email attribute and getter/setter.
# - Update the email and print it.
# Expected Output: Email: bob@new.com
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.__email = email
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

customer = Customer("Bob", "bob@example.com")
customer.set_email("bob@new.com")
print(f"Email: {customer.get_email()}")

# %% Project 4: Stock Level Protector
# Difficulty: Intermediate
# Description: Protect stock levels with getter/setter methods.
# Objective: Practice encapsulation for inventory.
# Tasks:
# - Create an InventoryItem class with a private __stock attribute and getter/setter.
# - Update the stock and print it.
# Expected Output: Updated stock: 50
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock
    def get_stock(self):
        return self.__stock
    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            raise ValueError("Stock cannot be negative")

item = InventoryItem("Blender", 30)
item.set_stock(50)
print(f"Updated stock: {item.get_stock()}")

# %% Project 5: Product Discount Lock
# Difficulty: Intermediate
# Description: Protect a discount rate with validation.
# Objective: Practice encapsulation with setters.
# Tasks:
# - Define a Product class with a private __discount_rate attribute and getter/setter.
# - Set a valid discount and print it.
# Expected Output: Discount rate: 0.15
class Product:
    def __init__(self, name, discount_rate):
        self.name = name
        self.__discount_rate = discount_rate
    def get_discount_rate(self):
        return self.__discount_rate
    def set_discount_rate(self, rate):
        if 0 <= rate <= 1:
            self.__discount_rate = rate
        else:
            raise ValueError("Discount rate must be between 0 and 1")

product = Product("Laptop", 0.1)
product.set_discount_rate(0.15)
print(f"Discount rate: {product.get_discount_rate()}")

# %% Project 6: Supplier Contact Security
# Difficulty: Intermediate
# Description: Protect supplier contact details.
# Objective: Practice encapsulation for sensitive data.
# Tasks:
# - Create a Supplier class with a private __phone attribute and getter/setter.
# - Update the phone and print it.
# Expected Output: Phone: 555-5678
class Supplier:
    def __init__(self, name, phone):
        self.name = name
        self.__phone = phone
    def get_phone(self):
        return self.__phone
    def set_phone(self, phone):
        self.__phone = phone

supplier = Supplier("TechCorp", "555-1234")
supplier.set_phone("555-5678")
print(f"Phone: {supplier.get_phone()}")

# %% Project 7: Cart Total Security
# Difficulty: Intermediate
# Description: Protect the total cost of a cart.
# Objective: Practice encapsulation with validation.
# Tasks:
# - Define a Cart class with a private __total attribute and getter/setter.
# - Update the total and print it.
# Expected Output: Cart total: $1299.98
class Cart:
    def __init__(self, total):
        self.__total = total
    def get_total(self):
        return self.__total
    def set_total(self, total):
        if total >= 0:
            self.__total = total
        else:
            raise ValueError("Total cannot be negative")

cart = Cart(999.99)
cart.set_total(1299.98)
print(f"Cart total: ${cart.get_total():.2f}")

# %% Project 8: Transaction ID Lock
# Difficulty: Advanced
# Description: Protect a transaction ID with strict encapsulation.
# Objective: Practice advanced encapsulation.
# Tasks:
# - Create a Transaction class with a private __transaction_id attribute and getter.
# - Create a transaction and print the ID.
# Expected Output: Transaction ID: 1001
class Transaction:
    def __init__(self, transaction_id):
        self.__transaction_id = transaction_id
    def get_transaction_id(self):
        return self.__transaction_id

transaction = Transaction(1001)
print(f"Transaction ID: {transaction.get_transaction_id()}")

# %% Project 9: Promotion Rate Validator
# Difficulty: Advanced
# Description: Protect a promotion’s discount rate with validation.
# Objective: Practice encapsulation with complex setters.
# Tasks:
# - Define a Promotion class with a private __discount_rate attribute and getter/setter.
# - Attempt to set an invalid rate and print the result.
# Expected Output: Error: Discount rate must be between 0 and 1
class Promotion:
    def __init__(self, discount_rate):
        self.__discount_rate = discount_rate
    def get_discount_rate(self):
        return self.__discount_rate
    def set_discount_rate(self, rate):
        if 0 <= rate <= 1:
            self.__discount_rate = rate
        else:
            raise ValueError("Discount rate must be between 0 and 1")

promotion = Promotion(0.1)
try:
    promotion.set_discount_rate(1.5)
    print(f"Discount rate: {promotion.get_discount_rate()}")
except ValueError as e:
    print(f"Error: {e}")

# %% Project 10: Secure Inventory Tracker
# Difficulty: Advanced
# Description: Protect inventory data with multiple private attributes.
# Objective: Practice comprehensive encapsulation.
# Tasks:
# - Create an InventoryItem class with private __stock and __price attributes and getter/setter.
# - Update both and print the details.
# Expected Output: Item: Smartphone, Stock: 25, Price: $699.99
class InventoryItem:
    def __init__(self, name, stock, price):
        self.name = name
        self.__stock = stock
        self.__price = price
    def get_stock(self):
        return self.__stock
    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            raise ValueError("Stock cannot be negative")
    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Price cannot be negative")

item = InventoryItem("Smartphone", 20, 649.99)
item.set_stock(25)
item.set_price(699.99)
print(f"Item: {item.name}, Stock: {item.get_stock()}, Price: ${item.get_price():.2f}")