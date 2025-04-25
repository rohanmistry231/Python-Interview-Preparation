# Inheritance Projects
# Purpose: Apply Inheritance through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Basic Electronics Product
# Difficulty: Basic
# Description: Create an Electronics class inheriting from Product.
# Objective: Practice basic inheritance.
# Tasks:
# - Define a Product class with name and price.
# - Create an Electronics child class.
# - Instantiate and print details.
# Expected Output: Electronics: Mouse, Price: $29.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    pass

electronics = Electronics("Mouse", 29.99)
print(f"Electronics: {electronics.name}, Price: ${electronics.price:.2f}")

# %% Project 2: Online Order Extension
# Difficulty: Basic
# Description: Extend an Order class with an online version.
# Objective: Practice adding attributes in a child class.
# Tasks:
# - Define an Order class with order_id and total.
# - Create an OnlineOrder class with a delivery_fee attribute.
# - Print the order details.
# Expected Output: Online Order: 101, Delivery Fee: $10.00
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

class OnlineOrder(Order):
    def __init__(self, order_id, total, delivery_fee):
        super().__init__(order_id, total)
        self.delivery_fee = delivery_fee

order = OnlineOrder(101, 999.99, 10.00)
print(f"Online Order: {order.order_id}, Delivery Fee: ${order.delivery_fee:.2f}")

# %% Project 3: Furniture Product
# Difficulty: Basic
# Description: Create a Furniture class inheriting from Product.
# Objective: Practice inheritance with additional attributes.
# Tasks:
# - Define a Product class with name and price.
# - Create a Furniture class with a material attribute.
# - Print the furniture details.
# Expected Output: Furniture: Chair, Material: Wood
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Furniture(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

furniture = Furniture("Chair", 99.99, "Wood")
print(f"Furniture: {furniture.name}, Material: {furniture.material}")

# %% Project 4: Appliance Power Display
# Difficulty: Intermediate
# Description: Extend Product with an Appliance class and override display.
# Objective: Practice method overriding.
# Tasks:
# - Define a Product class with a display method.
# - Create an Appliance class with a power attribute and overridden display.
# - Print the appliance details.
# Expected Output: Appliance: Blender, Price: $39.99, Power: 500W
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return f"{self.name}: ${self.price:.2f}"

class Appliance(Product):
    def __init__(self, name, price, power):
        super().__init__(name, price)
        self.power = power
    def display(self):
        return f"Appliance: {self.name}, Price: ${self.price:.2f}, Power: {self.power}W"

appliance = Appliance("Blender", 39.99, 500)
print(appliance.display())

# %% Project 5: Premium Customer
# Difficulty: Intermediate
# Description: Create a PremiumCustomer class inheriting from Customer.
# Objective: Practice inheritance with additional functionality.
# Tasks:
# - Define a Customer class with name and email.
# - Create a PremiumCustomer class with a membership_level attribute.
# - Print the customer details.
# Expected Output: Premium Customer: Alice, Membership: Gold
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class PremiumCustomer(Customer):
    def __init__(self, name, email, membership_level):
        super().__init__(name, email)
        self.membership_level = membership_level

customer = PremiumCustomer("Alice", "alice@example.com", "Gold")
print(f"Premium Customer: {customer.name}, Membership: {customer.membership_level}")

# %% Project 6: Discounted Product
# Difficulty: Intermediate
# Description: Extend Product with a DiscountedProduct class.
# Objective: Practice method extension.
# Tasks:
# - Define a Product class with a price attribute.
# - Create a DiscountedProduct class with a discount_rate attribute.
# - Print the discounted price.
# Expected Output: Discounted price: $89.99
class Product:
    def __init__(self, price):
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, price, discount_rate):
        super().__init__(price)
        self.discount_rate = discount_rate
    def get_discounted_price(self):
        return self.price * (1 - self.discount_rate)

product = DiscountedProduct(99.99, 0.1)
print(f"Discounted price: ${product.get_discounted_price():.2f}")

# %% Project 7: Shippable Order
# Difficulty: Intermediate
# Description: Create a ShippableOrder class inheriting from Order.
# Objective: Practice inheritance for order processing.
# Tasks:
# - Define an Order class with total.
# - Create a ShippableOrder class with a shipping_status attribute.
# - Print the order details.
# Expected Output: Shippable Order: 102, Status: Shipped
class Order:
    def __init__(self, total):
        self.total = total

class ShippableOrder(Order):
    def __init__(self, total, shipping_status):
        super().__init__(total)
        self.shipping_status = shipping_status

order = ShippableOrder(499.99, "Shipped")
print(f"Shippable Order: 102, Status: {order.shipping_status}")

# %% Project 8: Electronics Warranty Checker
# Difficulty: Advanced
# Description: Extend Electronics with a warranty checker method.
# Objective: Practice complex inheritance.
# Tasks:
# - Define a Product class with name and price.
# - Create an Electronics class with a warranty attribute and a check_warranty method.
# - Print the warranty status.
# Expected Output: Warranty for Smartphone: 2 years
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
    def check_warranty(self):
        return f"Warranty for {self.name}: {self.warranty} years"

electronics = Electronics("Smartphone", 699.99, 2)
print(electronics.check_warranty())

# %% Project 9: Luxury Furniture
# Difficulty: Advanced
# Description: Create a LuxuryFurniture class with premium features.
# Objective: Practice deep inheritance customization.
# Tasks:
# - Define a Product class and a Furniture class.
# - Create a LuxuryFurniture class with a brand attribute.
# - Print the luxury furniture details.
# Expected Output: Luxury Furniture: Sofa, Brand: EliteDesign
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Furniture(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

class LuxuryFurniture(Furniture):
    def __init__(self, name, price, material, brand):
        super().__init__(name, price, material)
        self.brand = brand

furniture = LuxuryFurniture("Sofa", 999.99, "Leather", "EliteDesign")
print(f"Luxury Furniture: {furniture.name}, Brand: {furniture.brand}")

# %% Project 10: Bulk Order Processor
# Difficulty: Advanced
# Description: Extend Order with a BulkOrder class for large orders.
# Objective: Practice inheritance with complex logic.
# Tasks:
# - Define an Order class with total.
# - Create a BulkOrder class with a quantity attribute and a calculate_total method.
# - Print the bulk order total.
# Expected Output: Bulk Order Total: $4999.95
class Order:
    def __init__(self, total):
        self.total = total

class BulkOrder(Order):
    def __init__(self, total, quantity):
        super().__init__(total)
        self.quantity = quantity
    def calculate_total(self):
        return self.total * self.quantity

order = BulkOrder(999.99, 5)
print(f"Bulk Order Total: ${order.calculate_total():.2f}")