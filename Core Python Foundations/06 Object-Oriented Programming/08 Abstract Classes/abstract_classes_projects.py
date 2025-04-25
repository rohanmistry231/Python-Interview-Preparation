# Abstract Classes Projects
# Purpose: Apply Abstract Classes through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Product Display Enforcer
# Difficulty: Basic
# Description: Define an abstract Product class to enforce a display method for retail products.
# Objective: Practice creating an abstract class and implementing its method.
# Tasks:
# - Create an abstract Product class with an abstract display method.
# - Define a concrete Electronics class that implements display.
# - Instantiate an Electronics object and print its display output.
# Expected Output: Electronics: Mouse, Price: $29.99
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def display(self):
        pass

class Electronics(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"Electronics: {self.name}, Price: ${self.price:.2f}"

electronics = Electronics("Mouse", 29.99)
print(electronics.display())

# %% Project 2: Order Processing Interface
# Difficulty: Basic
# Description: Create an abstract Order class to enforce order processing logic.
# Objective: Practice defining and implementing abstract methods.
# Tasks:
# - Define an abstract Order class with an abstract process method.
# - Create a concrete OnlineOrder class that implements process.
# - Instantiate an OnlineOrder and print the process result.
# Expected Output: Processing online order: 101
from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process(self):
        pass

class OnlineOrder(Order):
    def __init__(self, order_id):
        self.order_id = order_id
    def process(self):
        return f"Processing online order: {self.order_id}"

order = OnlineOrder(101)
print(order.process())

# %% Project 3: Inventory Stock Interface
# Difficulty: Basic
# Description: Enforce stock tracking with an abstract InventoryItem class.
# Objective: Practice abstract method implementation for inventory.
# Tasks:
# - Create an abstract InventoryItem class with an abstract get_stock method.
# - Define a concrete ProductItem class that implements get_stock.
# - Instantiate a ProductItem and print its stock.
# Expected Output: Stock for Coffee Maker: 30
from abc import ABC, abstractmethod

class InventoryItem(ABC):
    @abstractmethod
    def get_stock(self):
        pass

class ProductItem(InventoryItem):
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def get_stock(self):
        return f"Stock for {self.name}: {self.stock}"

item = ProductItem("Coffee Maker", 30)
print(item.get_stock())

# %% Project 4: Discount Policy Enforcer
# Difficulty: Intermediate
# Description: Use an abstract class to enforce a discount policy for retail products.
# Objective: Practice abstract methods for discount calculations.
# Tasks:
# - Define an abstract Product class with an abstract apply_discount method.
# - Create a concrete Appliance class that implements apply_discount (10% discount).
# - Instantiate an Appliance and print the discounted price.
# Expected Output: Discounted price: $35.99
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def apply_discount(self):
        pass

class Appliance(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self):
        return self.price * 0.9

appliance = Appliance("Blender", 39.99)
print(f"Discounted price: ${appliance.apply_discount():.2f}")

# %% Project 5: Customer Information Interface
# Difficulty: Intermediate
# Description: Enforce a consistent customer information interface with an abstract class.
# Objective: Practice abstract classes for customer data.
# Tasks:
# - Create an abstract Customer class with an abstract get_info method.
# - Define a concrete PremiumCustomer class that implements get_info.
# - Instantiate a PremiumCustomer and print its info.
# Expected Output: Premium Customer: Alice, Membership: Gold
from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def get_info(self):
        pass

class PremiumCustomer(Customer):
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership
    def get_info(self):
        return f"Premium Customer: {self.name}, Membership: {self.membership}"

customer = PremiumCustomer("Alice", "Gold")
print(customer.get_info())

# %% Project 6: Promotion Details Enforcer
# Difficulty: Intermediate
# Description: Use an abstract class to enforce promotion details for retail campaigns.
# Objective: Practice abstract methods for promotions.
# Tasks:
# - Create an abstract Promotion class with an abstract get_promo_details method.
# - Define a concrete DiscountPromotion class that implements get_promo_details.
# - Instantiate a DiscountPromotion and print its details.
# Expected Output: Promotion: 10% off
from abc import ABC, abstractmethod

class Promotion(ABC):
    @abstractmethod
    def get_promo_details(self):
        pass

class DiscountPromotion(Promotion):
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate
    def get_promo_details(self):
        return f"Promotion: {self.discount_rate:.0%} off"

promotion = DiscountPromotion(0.1)
print(promotion.get_promo_details())

# %% Project 7: Supplier Contact Interface
# Difficulty: Intermediate
# Description: Enforce supplier contact information with an abstract class.
# Objective: Practice abstract classes for supplier data.
# Tasks:
# - Create an abstract Supplier class with an abstract get_contact method.
# - Define a concrete TechSupplier class that implements get_contact.
# - Instantiate a TechSupplier and print its contact info.
# Expected Output: Supplier: TechCorp, Contact: contact@techcorp.com
from abc import ABC, abstractmethod

class Supplier(ABC):
    @abstractmethod
    def get_contact(self):
        pass

class TechSupplier(Supplier):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def get_contact(self):
        return f"Supplier: {self.name}, Contact: {self.email}"

supplier = TechSupplier("TechCorp", "contact@techcorp.com")
print(supplier.get_contact())

# %% Project 8: Transaction Logging Interface
# Difficulty: Advanced
# Description: Use an abstract class to enforce transaction logging in a retail system.
# Objective: Practice complex abstract method implementation.
# Tasks:
# - Create an abstract Transaction class with an abstract log_transaction method.
# - Define a concrete OrderTransaction class that implements log_transaction.
# - Instantiate an OrderTransaction and print its log.
# Expected Output: Transaction logged: ID 1001, Amount: $999.99
from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def log_transaction(self):
        pass

class OrderTransaction(Transaction):
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount
    def log_transaction(self):
        return f"Transaction logged: ID {self.transaction_id}, Amount: ${self.amount:.2f}"

transaction = OrderTransaction(1001, 999.99)
print(transaction.log_transaction())

# %% Project 9: Cart Management Interface
# Difficulty: Advanced
# Description: Enforce cart management with an abstract class requiring multiple methods.
# Objective: Practice advanced abstract classes with multiple methods.
# Tasks:
# - Create an abstract Cart class with abstract add_item and get_total methods.
# - Define a concrete ShoppingCart class that implements both methods.
# - Add an item and print the cart total.
# Expected Output: Cart total: $1299.98
from abc import ABC, abstractmethod

class Cart(ABC):
    @abstractmethod
    def add_item(self, item):
        pass
    @abstractmethod
    def get_total(self):
        pass

class ShoppingCart(Cart):
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def get_total(self):
        return sum(item["price"] for item in self.items)

cart = ShoppingCart()
cart.add_item({"name": "Smartphone", "price": 699.99})
cart.add_item({"name": "Headphones", "price": 599.99})
print(f"Cart total: ${cart.get_total():.2f}")

# %% Project 10: Comprehensive Product Interface
# Difficulty: Advanced
# Description: Enforce a comprehensive product interface with multiple abstract methods.
# Objective: Practice complex abstract classes for retail products.
# Tasks:
# - Create an abstract Product class with abstract display and apply_discount methods.
# - Define a concrete Electronics class that implements both methods.
# - Instantiate an Electronics object, display it, and print its discounted price.
# Expected Output: Electronics: Smartphone, Price: $699.99
#                 Discounted price: $594.99
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def apply_discount(self):
        pass

class Electronics(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"Electronics: {self.name}, Price: ${self.price:.2f}"
    def apply_discount(self):
        return self.price * 0.85

electronics = Electronics("Smartphone", 699.99)
print(electronics.display())
print(f"Discounted price: ${electronics.apply_discount():.2f}")