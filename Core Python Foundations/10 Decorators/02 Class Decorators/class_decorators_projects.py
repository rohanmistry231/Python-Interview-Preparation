# Class Decorators Projects
# Purpose: Apply class decorator concepts through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Class Name Decorator
# Difficulty: Basic
# Description: Create a class decorator to add a method to get the class name.
# Objective: Practice adding methods via decorators.
# Tasks:
# - Define a decorator to add a get_class_name method.
# - Apply to a Customer class and print the class name.
# Expected Output: Class name: Customer
def add_class_name_method(cls):
    def get_class_name(self):
        return self.__class__.__name__
    cls.get_class_name = get_class_name
    return cls

@add_class_name_method
class Customer:
    def __init__(self, name):
        self.name = name

customer = Customer("Alice")
print("Class name:", customer.get_class_name())

# %% Project 2: Tax Attribute Decorator
# Difficulty: Basic
# Description: Create a class decorator to add a tax attribute (8% of price).
# Objective: Practice modifying class attributes.
# Tasks:
# - Define a decorator to add a tax attribute based on price.
# - Apply to a Product class and print the tax.
# Expected Output: Tax: 56.00
def add_tax_attribute(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.tax = self.price * 0.08
    cls.__init__ = new_init
    return cls

@add_tax_attribute
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Smartphone", 699.99)
print("Tax:", round(product.tax, 2))

# %% Project 3: String Validation Decorator
# Difficulty: Basic
# Description: Create a class decorator to validate non-empty string attributes.
# Objective: Practice attribute validation.
# Tasks:
# - Define a decorator to check for non-empty strings.
# - Apply to an Order class and print customer name.
# Expected Output: Customer: Bob
def validate_string_attributes(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for attr, value in vars(self).items():
            if isinstance(value, str) and not value.strip():
                raise ValueError(f"{attr} must be non-empty")
    cls.__init__ = new_init
    return cls

@validate_string_attributes
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name

order = Order(102, "Bob")
print("Customer:", order.customer_name)

# %% Project 4: Display Method Decorator
# Difficulty: Basic
# Description: Create a class decorator to add a display method for attributes.
# Objective: Practice adding formatted output methods.
# Tasks:
# - Define a decorator to add a display method.
# - Apply to an Inventory class and print attributes.
# Expected Output: Inventory: {'name': 'Mouse', 'stock': 30}
def add_display_method(cls):
    def display(self):
        return f"{self.__class__.__name__}: {vars(self)}"
    cls.display = display
    return cls

@add_display_method
class Inventory:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

inventory = Inventory("Mouse", 30)
print(inventory.display())

# %% Project 5: Discount Attribute Decorator
# Difficulty: Intermediate
# Description: Create a class decorator to add a discounted price attribute.
# Objective: Practice decorators with arguments.
# Tasks:
# - Define a decorator factory for a 15% discount.
# - Apply to an Order class and print discounted price.
# Expected Output: Discounted price: 849.99
def add_discount(discount_rate):
    def decorator(cls):
        original_init = cls.__init__
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.discounted_price = self.price * (1 - discount_rate)
        cls.__init__ = new_init
        return cls
    return decorator

@add_discount(0.15)
class Order:
    def __init__(self, order_id, price):
        self.order_id = order_id
        self.price = price

order = Order(101, 999.99)
print("Discounted price:", round(order.discounted_price, 2))

# %% Project 6: Positive Attribute Decorator
# Difficulty: Intermediate
# Description: Create a class decorator to validate positive numerical attributes.
# Objective: Practice robust validation.
# Tasks:
# - Define a decorator to ensure non-negative numbers.
# - Apply to a Product class and print price.
# Expected Output: Price: 999.99
def validate_positive_attributes(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for attr, value in vars(self).items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"{attr} must be non-negative")
    cls.__init__ = new_init
    return cls

@validate_positive_attributes
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999.99)
print("Price:", product.price)

# %% Project 7: Timestamp Decorator
# Difficulty: Intermediate
# Description: Create a class decorator to add a creation timestamp.
# Objective: Practice adding dynamic attributes.
# Tasks:
# - Define a decorator to add a created_at timestamp.
# - Apply to an Order class and print timestamp.
# Expected Output: Created at: 2025-04-25 (approx)
from datetime import datetime

def add_timestamp(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.created_at = datetime.now().strftime("%Y-%m-%d")
    cls.__init__ = new_init
    return cls

@add_timestamp
class Order:
    def __init__(self, order_id):
        self.order_id = order_id

order = Order(101)
print("Created at:", order.created_at)

# %% Project 8: Method Counter Decorator
# Difficulty: Intermediate
# Description: Create a class decorator to count method calls.
# Objective: Practice tracking class behavior.
# Tasks:
# - Define a decorator to count calls to a specific method.
# - Apply to a Product class and print call count.
# Expected Output: Method calls: 2
def method_counter(cls):
    cls._call_count = 0
    original_method = cls.get_price
    def new_method(self):
        cls._call_count += 1
        return original_method(self)
    cls.get_price = new_method
    return cls

@method_counter
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price

product = Product("Mouse", 29.99)
product.get_price()
product.get_price()
print("Method calls:", product._call_count)

# %% Project 9: Attribute Logger Decorator
# Difficulty: Advanced
# Description: Create a class decorator to log attribute changes.
# Objective: Practice advanced metaprogramming.
# Tasks:
# - Define a decorator to log changes to price attribute.
# - Apply to a Product class and print logs.
# Expected Output: Price changed to: 999.99
def attribute_logger(cls):
    original_init = cls.__init__
    cls._logs = []
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        if hasattr(self, 'price'):
            cls._logs.append(f"Price changed to: {self.price}")
    cls.__init__ = new_init
    return cls

@attribute_logger
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999.99)
print(product._logs[0])

# %% Project 10: Comprehensive Retail Decorator
# Difficulty: Advanced
# Description: Create a class decorator to add validation, discount, and display.
# Objective: Practice combining class decorator features.
# Tasks:
# - Combine validation, discount, and display in one decorator.
# - Apply to an Inventory class and print details.
# Expected Output: Inventory: {'name': 'Mouse', 'stock': 30, 'price': 29.99, 'discounted_price': 25.49}
def comprehensive_decorator(cls):
    # Add validation
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for attr, value in vars(self).items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"{attr} must be non-negative")
        self.discounted_price = self.price * 0.85  # 15% discount
    cls.__init__ = new_init
    # Add display
    def display(self):
        return f"{self.__class__.__name__}: {vars(self)}"
    cls.display = display
    return cls

@comprehensive_decorator
class Inventory:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

inventory = Inventory("Mouse", 30, 29.99)
print(inventory.display())