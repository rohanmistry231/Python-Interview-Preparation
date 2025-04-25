# Multiple Inheritance Projects
# Purpose: Apply Multiple Inheritance through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Discounted Electronics
# Difficulty: Basic
# Description: Create an Electronics class inheriting from Product and Discountable.
# Objective: Practice basic multiple inheritance.
# Tasks:
# - Define Product and Discountable classes.
# - Create an Electronics class inheriting both.
# - Apply a discount and print the price.
# Expected Output: Electronics: Mouse, Price: $26.99
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discountable:
    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Electronics(Product, Discountable):
    pass

electronics = Electronics("Mouse", 29.99)
electronics.apply_discount(0.1)
print(f"Electronics: {electronics.name}, Price: ${electronics.price:.2f}")

# %% Project 2: Promotable Order
# Difficulty: Basic
# Description: Combine Order and Promotable classes.
# Objective: Practice combining multiple parent classes.
# Tasks:
# - Define Order and Promotable classes.
# - Create a PromotableOrder class inheriting both.
# - Print the order and promotion details.
# Expected Output: Order: 101, Promotion: Free Shipping
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

class Promotable:
    def __init__(self, promotion):
        self.promotion = promotion

class PromotableOrder(Order, Promotable):
    def __init__(self, order_id, total, promotion):
        Order.__init__(self, order_id, total)
        Promotable.__init__(self, promotion)

order = PromotableOrder(101, 999.99, "Free Shipping")
print(f"Order: {order.order_id}, Promotion: {order.promotion}")

# %% Project 3: Warranted Appliance
# Difficulty: Basic
# Description: Create an Appliance class with Product and Warranty parents.
# Objective: Practice multiple inheritance with attributes.
# Tasks:
# - Define Product and Warranty classes.
# - Create an Appliance class inheriting both.
# - Print the appliance details.
# Expected Output: Appliance: Blender, Warranty: 1 year
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Warranty:
    def __init__(self, warranty_years):
        self.warranty_years = warranty_years

class Appliance(Product, Warranty):
    def __init__(self, name, price, warranty_years):
        Product.__init__(self, name, price)
        Warranty.__init__(self, warranty_years)

appliance = Appliance("Blender", 39.99, 1)
print(f"Appliance: {appliance.name}, Warranty: {appliance.warranty_years} year")

# %% Project 4: Shippable Discounted Product
# Difficulty: Intermediate
# Description: Combine Product, Discountable, and Shippable classes.
# Objective: Practice multiple inheritance with methods.
# Tasks:
# - Define Product, Discountable, and Shippable classes.
# - Create a ShippableProduct class inheriting all three.
# - Apply a discount and print the shipping status.
# Expected Output: Product: Smartphone, Discounted Price: $629.99, Status: Shipped
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discountable:
    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Shippable:
    def __init__(self, status):
        self.status = status

class ShippableProduct(Product, Discountable, Shippable):
    def __init__(self, name, price, status):
        Product.__init__(self, name, price)
        Shippable.__init__(self, status)

product = ShippableProduct("Smartphone", 699.99, "Shipped")
product.apply_discount(0.1)
print(f"Product: {product.name}, Discounted Price: ${product.price:.2f}, Status: {product.status}")

# %% Project 5: Promotable Customer
# Difficulty: Intermediate
# Description: Create a Customer class inheriting from Customer and Promotable.
# Objective: Practice multiple inheritance for customer data.
# Tasks:
# - Define Customer and Promotable classes.
# - Create a PromotableCustomer class inheriting both.
# - Print the customer and promotion details.
# Expected Output: Customer: Bob, Promotion: 10% off
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Promotable:
    def __init__(self, promotion):
        self.promotion = promotion

class PromotableCustomer(Customer, Promotable):
    def __init__(self, name, email, promotion):
        Customer.__init__(self, name, email)
        Promotable.__init__(self, promotion)

customer = PromotableCustomer("Bob", "bob@example.com", "10% off")
print(f"Customer: {customer.name}, Promotion: {customer.promotion}")

# %% Project 6: MRO Checker
# Difficulty: Intermediate
# Description: Check the Method Resolution Order for a multiply-inherited class.
# Objective: Practice understanding MRO.
# Tasks:
# - Define two parent classes with conflicting display methods.
# - Create a child class inheriting both.
# - Print the MRO and display result.
# Expected Output: MRO: [<class 'Item'>, <class 'Product'>, <class 'Category'>, <class 'object'>]
#                 Display: Product display
class Product:
    def display(self):
        return "Product display"

class Category:
    def display(self):
        return "Category display"

class Item(Product, Category):
    pass

item = Item()
print(f"MRO: {Item.__mro__}")
print(f"Display: {item.display()}")

# %% Project 7: Discounted Warranted Electronics
# Difficulty: Intermediate
# Description: Combine Product, Discountable, and Warranty for electronics.
# Objective: Practice complex multiple inheritance.
# Tasks:
# - Define Product, Discountable, and Warranty classes.
# - Create an Electronics class inheriting all three.
# - Print the discounted price and warranty.
# Expected Output: Electronics: Laptop, Price: $899.99, Warranty: 2 years
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discountable:
    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Warranty:
    def __init__(self, warranty_years):
        self.warranty_years = warranty_years

class Electronics(Product, Discountable, Warranty):
    def __init__(self, name, price, warranty_years):
        Product.__init__(self, name, price)
        Warranty.__init__(self, warranty_years)

electronics = Electronics("Laptop", 999.99, 2)
electronics.apply_discount(0.1)
print(f"Electronics: {electronics.name}, Price: ${electronics.price:.2f}, Warranty: {electronics.warranty_years} years")

# %% Project 8: Promotable Shippable Order
# Difficulty: Advanced
# Description: Create an order class combining Order, Promotable, and Shippable.
# Objective: Practice advanced multiple inheritance.
# Tasks:
# - Define Order, Promotable, and Shippable classes.
# - Create a PromotableShippableOrder class inheriting all three.
# - Print the order, promotion, and shipping details.
# Expected Output: Order: 102, Promotion: 5% off, Status: Delivered
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

class Promotable:
    def __init__(self, promotion):
        self.promotion = promotion

class Shippable:
    def __init__(self, status):
        self.status = status

class PromotableShippableOrder(Order, Promotable, Shippable):
    def __init__(self, order_id, total, promotion, status):
        Order.__init__(self, order_id, total)
        Promotable.__init__(self, promotion)
        Shippable.__init__(self, status)

order = PromotableShippableOrder(102, 499.99, "5% off", "Delivered")
print(f"Order: {order.order_id}, Promotion: {order.promotion}, Status: {order.status}")

# %% Project 9: Luxury Discounted Furniture
# Difficulty: Advanced
# Description: Combine Furniture, Discountable, and Luxury classes.
# Objective: Practice multiple inheritance with complex attributes.
# Tasks:
# - Define Furniture, Discountable, and Luxury classes.
# - Create a LuxuryFurniture class inheriting all three.
# - Print the discounted price and luxury brand.
# Expected Output: Furniture: Sofa, Price: $899.99, Brand: EliteDesign
class Furniture:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discountable:
    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Luxury:
    def __init__(self, brand):
        self.brand = brand

class LuxuryFurniture(Furniture, Discountable, Luxury):
    def __init__(self, name, price, brand):
        Furniture.__init__(self, name, price)
        Luxury.__init__(self, brand)

furniture = LuxuryFurniture("Sofa", 999.99, "EliteDesign")
furniture.apply_discount(0.1)
print(f"Furniture: {furniture.name}, Price: ${furniture.price:.2f}, Brand: {furniture.brand}")

# %% Project 10: Multi-Feature Product
# Difficulty: Advanced
# Description: Create a product class with multiple inherited features.
# Objective: Practice combining multiple parents for a retail product.
# Tasks:
# - Define Product, Discountable, Warranted, and Promotable classes.
# - Create a MultiFeatureProduct class inheriting all four.
# - Print the price, warranty, and promotion.
# Expected Output: Product: Tablet, Price: $449.99, Warranty: 1 year, Promotion: Buy 1 Get 1 Free
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discountable:
    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Warranted:
    def __init__(self, warranty_years):
        self.warranty_years = warranty_years

class Promotable:
    def __init__(self, promotion):
        self.promotion = promotion

class MultiFeatureProduct(Product, Discountable, Warranted, Promotable):
    def __init__(self, name, price, warranty_years, promotion):
        Product.__init__(self, name, price)
        Warranted.__init__(self, warranty_years)
        Promotable.__init__(self, promotion)

product = MultiFeatureProduct("Tablet", 499.99, 1, "Buy 1 Get 1 Free")
product.apply_discount(0.1)
print(f"Product: {product.name}, Price: ${product.price:.2f}, Warranty: {product.warranty_years} year, Promotion: {product.promotion}")