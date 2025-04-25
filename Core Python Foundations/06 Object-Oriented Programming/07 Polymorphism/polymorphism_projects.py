# Polymorphism Projects
# Purpose: Apply Polymorphism through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Electronics Discount Override
# Difficulty: Basic
# Description: Override a discount method for electronics products.
# Objective: Practice method overriding for retail discounts.
# Tasks:
# - Define a Product class with an apply_discount method.
# - Create an Electronics class overriding apply_discount with a 15% discount.
# - Apply the discount and print the result.
# Expected Output: Electronics Discount: $25.49
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self):
        return self.price * 0.9

class Electronics(Product):
    def apply_discount(self):
        return self.price * 0.85

electronics = Electronics("Mouse", 29.99)
print(f"Electronics Discount: ${electronics.apply_discount():.2f}")

# %% Project 2: Order Display Override
# Difficulty: Basic
# Description: Override a display method for online orders.
# Objective: Practice polymorphic display methods.
# Tasks:
# - Define an Order class with a display method.
# - Create an OnlineOrder class overriding display.
# - Print the display result.
# Expected Output: Online Order 101: $999.99
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def display(self):
        return f"Order {self.order_id}: ${self.total:.2f}"

class OnlineOrder(Order):
    def display(self):
        return f"Online Order {self.order_id}: ${self.total:.2f}"

order = OnlineOrder(101, 999.99)
print(order.display())

# %% Project 3: Product Details Formatter
# Difficulty: Basic
# Description: Use polymorphism to format product details.
# Objective: Practice polymorphic behavior for retail products.
# Tasks:
# - Define a Product class and an Appliance class with get_details methods.
# - Create a list of products and print their details.
# Expected Output: Product: Mouse, Price: $29.99
#                 Appliance: Blender, Price: $39.99, Power: 500W
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_details(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

class Appliance(Product):
    def __init__(self, name, price, power):
        super().__init__(name, price)
        self.power = power
    def get_details(self):
        return f"Appliance: {self.name}, Price: ${self.price:.2f}, Power: {self.power}W"

products = [Product("Mouse", 29.99), Appliance("Blender", 39.99, 500)]
for product in products:
    print(product.get_details())

# %% Project 4: Customer Type Display
# Difficulty: Intermediate
# Description: Display different customer types polymorphically.
# Objective: Practice method overriding for customer data.
# Tasks:
# - Define a Customer class with a get_info method.
# - Create a PremiumCustomer class overriding get_info.
# - Print the customer info.
# Expected Output: Premium Customer: Alice, Membership: Gold
class Customer:
    def __init__(self, name):
        self.name = name
    def get_info(self):
        return f"Customer: {self.name}"

class PremiumCustomer(Customer):
    def __init__(self, name, membership):
        super().__init__(name)
        self.membership = membership
    def get_info(self):
        return f"Premium Customer: {self.name}, Membership: {self.membership}"

customer = PremiumCustomer("Alice", "Gold")
print(customer.get_info())

# %% Project 5: Inventory Stock Formatter
# Difficulty: Intermediate
# Description: Format stock details for different inventory types.
# Objective: Practice polymorphic methods for inventory.
# Tasks:
# - Define an InventoryItem class and an ElectronicsItem class with get_stock_info methods.
# - Create a list of items and print their stock info.
# Expected Output: Item: Coffee Maker, Stock: 30
#                 Electronics: Smartphone, Stock: 25, Warranty: 1 year
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def get_stock_info(self):
        return f"Item: {self.name}, Stock: {self.stock}"

class ElectronicsItem(InventoryItem):
    def __init__(self, name, stock, warranty):
        super().__init__(name, stock)
        self.warranty = warranty
    def get_stock_info(self):
        return f"Electronics: {self.name}, Stock: {self.stock}, Warranty: {self.warranty} year"

items = [InventoryItem("Coffee Maker", 30), ElectronicsItem("Smartphone", 25, 1)]
for item in items:
    print(item.get_stock_info())

# %% Project 6: Promotion Discount Override
# Difficulty: Intermediate
# Description: Override a discount method for promotional products.
# Objective: Practice polymorphism in retail discounts.
# Tasks:
# - Define a Product class with an apply_discount method (10% discount).
# - Create a PromotionalProduct class overriding apply_discount (20% discount).
# - Print the discounted price.
# Expected Output: Promotional Discount: $31.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self):
        return self.price * 0.9

class PromotionalProduct(Product):
    def apply_discount(self):
        return self.price * 0.8

product = PromotionalProduct("Blender", 39.99)
print(f"Promotional Discount: ${product.apply_discount():.2f}")

# %% Project 7: Order Processing Polymorphism
# Difficulty: Intermediate
# Description: Process orders differently based on type.
# Objective: Practice polymorphic order processing.
# Tasks:
# - Define an Order class and a BulkOrder class with process methods.
# - Create a list of orders and print their process results.
# Expected Output: Processing standard order: 101
#                 Processing bulk order: 102, Quantity: 50
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
    def process(self):
        return f"Processing standard order: {self.order_id}"

class BulkOrder(Order):
    def __init__(self, order_id, quantity):
        super().__init__(order_id)
        self.quantity = quantity
    def process(self):
        return f"Processing bulk order: {self.order_id}, Quantity: {self.quantity}"

orders = [Order(101), BulkOrder(102, 50)]
for order in orders:
    print(order.process())

# %% Project 8: Supplier Contact Polymorphism
# Difficulty: Advanced
# Description: Format supplier contacts differently based on type.
# Objective: Practice advanced polymorphic methods.
# Tasks:
# - Define a Supplier class and a PremiumSupplier class with get_contact methods.
# - Create a list of suppliers and print their contact info.
# Expected Output: Supplier: TechCorp, Email: contact@techcorp.com
#                 Premium Supplier: EliteCorp, Email: vip@elitecorp.com, Priority: High
class Supplier:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def get_contact(self):
        return f"Supplier: {self.name}, Email: {self.email}"

class PremiumSupplier(Supplier):
    def __init__(self, name, email, priority):
        super().__init__(name, email)
        self.priority = priority
    def get_contact(self):
        return f"Premium Supplier: {self.name}, Email: {self.email}, Priority: {self.priority}"

suppliers = [Supplier("TechCorp", "contact@techcorp.com"), PremiumSupplier("EliteCorp", "vip@elitecorp.com", "High")]
for supplier in suppliers:
    print(supplier.get_contact())

# %% Project 9: Cart Total Calculator
# Difficulty: Advanced
# Description: Calculate cart totals differently based on cart type.
# Objective: Practice polymorphism with complex calculations.
# Tasks:
# - Define a Cart class and a PremiumCart class with calculate_total methods.
# - Create a list of carts and print their totals.
# Expected Output: Standard Cart Total: $1499.97
#                 Premium Cart Total: $1350.00
class Cart:
    def __init__(self, items):
        self.items = items
    def calculate_total(self):
        return sum(item["price"] for item in self.items)

class PremiumCart(Cart):
    def calculate_total(self):
        return sum(item["price"] for item in self.items) * 0.9  # 10% discount

carts = [
    Cart([{"price": 699.99}, {"price": 799.98}]),
    PremiumCart([{"price": 699.99}, {"price": 799.98}])
]
for i, cart in enumerate(carts, 1):
    total = cart.calculate_total()
    cart_type = "Standard" if i == 1 else "Premium"
    print(f"{cart_type} Cart Total: ${total:.2f}")

# %% Project 10: Comprehensive Discount System
# Difficulty: Advanced
# Description: Apply different discount rules for various product types.
# Objective: Practice polymorphism in a retail discount system.
# Tasks:
# - Define a Product class and two subclasses (Electronics, Appliance) with apply_discount methods.
# - Create a list of products, apply discounts, and print the results.
# Expected Output: Electronics: Smartphone, Discounted Price: $594.99
#                 Appliance: Blender, Discounted Price: $33.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self):
        return self.price * 0.95

class Electronics(Product):
    def apply_discount(self):
        return self.price * 0.85

class Appliance(Product):
    def apply_discount(self):
        return self.price * 0.85

products = [Electronics("Smartphone", 699.99), Appliance("Blender", 39.99)]
for product in products:
    discounted_price = product.apply_discount()
    print(f"{product.__class__.__name__}: {product.name}, Discounted Price: ${discounted_price:.2f}")