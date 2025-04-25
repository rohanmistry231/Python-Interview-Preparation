# %% Purpose
# Python Object-Oriented Programming: Abstract Classes
# Purpose: Abstract classes define methods that must be implemented by child classes.
# Key Features: Enforces interface, prevents instantiation.

# %% 1. Defining an Abstract Class
# Explanation: Use abc module, ABC class, and @abstractmethod decorator.
# Example:
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def display(self):
        pass

# Cannot instantiate Product
# product = Product()  # Error: Can't instantiate abstract class

# %% 2. Implementing Abstract Methods
# Explanation: Child class must implement all abstract methods.
# Example:
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def display(self):
        pass

class Electronics(Product):
    def display(self):
        return f"Electronics - {self.name}: ${self.price:.2f}"

laptop = Electronics("Laptop Pro", 999.99)
print(laptop.display())
# Output: Electronics - Laptop Pro: $999.99

# %% 3. Retail Scenario with Abstract Class
# Explanation: Enforce a discount policy across product types.
# Example:
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def apply_discount(self):
        pass

class Appliance(Product):
    def apply_discount(self):
        return self.price * 0.9

blender = Appliance("Blender", 39.99)
print(f"Discounted price: ${blender.apply_discount():.2f}")
# Output: Discounted price: $35.99

# %% Notes
# Notes:
# - Abstract classes ensure consistent interfaces in ML (e.g., model APIs) or web apps (e.g., entity handlers).
# - Use abc module to enforce abstraction.
# - Child classes must implement all abstract methods.