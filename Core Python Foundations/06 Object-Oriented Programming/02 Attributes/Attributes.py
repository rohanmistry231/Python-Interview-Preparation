# %% Purpose
# Python Object-Oriented Programming: Attributes
# Purpose: Attributes are variables that belong to a class or object, storing data.
# Key Features: Instance attributes (per object), class attributes (shared).

# %% 1. Instance Attributes
# Explanation: Defined in __init__, unique to each object.
# Example:
class Product:
    def __init__(self, name, price):
        self.name = name  # Instance attribute
        self.price = price  # Instance attribute

laptop = Product("Laptop Pro", 999.99)
smartphone = Product("Smartphone X", 699.99)
print(f"Laptop: {laptop.name}, ${laptop.price:.2f}")
print(f"Smartphone: {smartphone.name}, ${smartphone.price:.2f}")
# Output: Laptop: Laptop Pro, $999.99
#         Smartphone: Smartphone X, $699.99

# %% 2. Class Attributes
# Explanation: Defined outside __init__, shared across all objects.
# Example:
class Product:
    store_name = "Tech Retail"  # Class attribute
    def __init__(self, name, price):
        self.name = name
        self.price = price

laptop = Product("Laptop", 999.99)
print(f"Store: {Product.store_name}, Product: {laptop.name}")
print(f"Store from object: {laptop.store_name}")
# Output: Store: Tech Retail, Product: Laptop
#         Store from object: Tech Retail

# %% 3. Modifying Attributes
# Explanation: Update instance or class attributes dynamically.
# Example:
class Product:
    tax_rate = 0.1  # Class attribute
    def __init__(self, name, price):
        self.name = name
        self.price = price

blender = Product("Blender", 39.99)
blender.price = 35.99  # Update instance attribute
Product.tax_rate = 0.15  # Update class attribute
print(f"Updated price: ${blender.price:.2f}, New tax rate: {Product.tax_rate}")
# Output: Updated price: $35.99, New tax rate: 0.15

# %% Notes
# Notes:
# - Instance attributes are unique; class attributes are shared.
# - Use in ML for model parameters (e.g., weights) or web apps for shared configs (e.g., API keys).
# - Access attributes via dot notation (object.attribute).