# Python Object-Oriented Programming: Class Methods

# Purpose: Class methods operate on the class itself, taking 'cls' as first parameter.
# Key Features: Access class attributes, alternative constructors.

# 1. Defining a Class Method
# Explanation: Use @classmethod decorator, 'cls' refers to the class.
# Example:
class Product:
    store_name = "Tech Retail"
    @classmethod
    def get_store(cls):
        return cls.store_name

print(Product.get_store())
# Output: Tech Retail

# 2. Class Method as Alternative Constructor
# Explanation: Create objects from alternative data formats.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def from_string(cls, product_str):
        name, price = product_str.split(",")
        return cls(name, float(price))

laptop = Product.from_string("Laptop Pro,999.99")
print(f"Product: {laptop.name}, Price: ${laptop.price:.2f}")
# Output: Product: Laptop Pro, Price: $999.99

# 3. Retail Scenario with Class Method
# Explanation: Manage class-level data or create objects.
# Example:
class Product:
    discount_rate = 0.1
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def set_discount(cls, rate):
        cls.discount_rate = rate
    def apply_discount(self):
        return self.price * (1 - Product.discount_rate)

blender = Product("Blender", 39.99)
Product.set_discount(0.15)
print(f"Discounted price: ${blender.apply_discount():.2f}")
# Output: Discounted price: $33.99

# Exercise 1: Create a class method to get a class attribute category.
# Solution:
# class Product:
#     category = "Electronics"
#     @classmethod
#     def get_category(cls):
#         return cls.category
# print("Exercise 1 - Category:", Product.get_category())
# # Output: Category: Electronics

# Exercise 2: Define a class method as an alternative constructor from a dictionary.
# Solution:
# class Order:
#     def __init__(self, order_id, total):
#         self.order_id = order_id
#         self.total = total
#     @classmethod
#     def from_dict(cls, order_dict):
#         return cls(order_dict["id"], order_dict["total"])
# order = Order.from_dict({"id": 101, "total": 999.99})
# print("Exercise 2 - Order:", order.order_id, order.total)
# # Output: Order: 101 999.99

# Exercise 3: Use a class method to update a class attribute tax_rate.
# Solution:
# class Product:
#     tax_rate = 0.05
#     @classmethod
#     def set_tax(cls, rate):
#         cls.tax_rate = rate
# Product.set_tax(0.1)
# print("Exercise 3 - Tax rate:", Product.tax_rate)
# # Output: Tax rate: 0.1

# Notes:
# - Class methods operate on class state, used in ML for model configs or web apps for shared settings.
# - Use 'cls' to access class attributes or create objects.
# - Alternative constructors enhance flexibility.