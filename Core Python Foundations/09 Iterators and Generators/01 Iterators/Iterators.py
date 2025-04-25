# %% Purpose
# Python Iterators and Generators: Iterators
# Purpose: Iterators allow sequential access to elements in a collection, implementing __iter__() and __next__().
# Key Features: Memory-efficient iteration, supports for loops, custom iteration logic.

# %% 1. Using Built-in Iterators
# Explanation: Lists, tuples, etc., are iterable; use iter() and next() for manual iteration.
# Example:
products = ["Laptop", "Smartphone", "Coffee Maker"]
iterator = iter(products)
print("First product:", next(iterator))
print("Second product:", next(iterator))
# Output: First product: Laptop
#         Second product: Smartphone

# %% 2. Creating a Custom Iterator
# Explanation: Define a class with __iter__() and __next__() methods.
# Example:
class ProductInventory:
    def __init__(self, products):
        self.products = products
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration

inventory = ProductInventory(["Mouse", "Keyboard", "Monitor"])
for product in inventory:
    print(f"Inventory item: {product}")
# Output: Inventory item: Mouse
#         Inventory item: Keyboard
#         Inventory item: Monitor

# %% 3. Retail Scenario with Iterators
# Explanation: Iterate over retail orders with custom logic (e.g., filter expensive orders).
# Example:
class OrderIterator:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.orders):
            order = self.orders[self.index]
            self.index += 1
            if order["total"] > 500:  # Only return expensive orders
                return order
        raise StopIteration

orders = [
    {"order_id": 101, "total": 1999.98},
    {"order_id": 102, "total": 49.99},
    {"order_id": 103, "total": 699.99}
]
expensive_orders = OrderIterator(orders)
for order in expensive_orders:
    print(f"Expensive order {order['order_id']}: ${order['total']:.2f}")
# Output: Expensive order 101: $1999.98
#         Expensive order 103: $699.99

# %% Notes
# Notes:
# - Iterators are memory-efficient for large datasets in ML (e.g., batch processing) or web apps (e.g., streaming API responses).
# - StopIteration signals the end of iteration; handle in custom iterators.
# - All iterables (e.g., lists) can be converted to iterators using iter().