# Iterators Projects
# Purpose: Apply iterator concepts through 10 retail-themed projects.
# Structure: Each project is separated by %% and includes description, tasks, and solution code.
# Note: Solutions use simulated inputs for reproducibility and match the updated base file outputs.

# %% Project 1: Manual Product Iterator
# Difficulty: Basic
# Description: Use a built-in iterator to manually print the first two products.
# Objective: Practice using iter() and next().
# Tasks:
# - Create a list of products and use iter() to get an iterator.
# - Print the first two products using next().
# Expected Output: Product 1: Laptop
#                 Product 2: Smartphone
products = ["Laptop", "Smartphone", "Coffee Maker"]
iterator = iter(products)
print("Product 1:", next(iterator))
print("Product 2:", next(iterator))

# %% Project 2: Category Iterator Loop
# Difficulty: Basic
# Description: Iterate over a list of categories using a for loop.
# Objective: Practice using built-in iterators in loops.
# Tasks:
# - Create a list of categories and iterate using a for loop.
# - Print each category.
# Expected Output: Category: Electronics
#                 Category: Appliances
#                 Category: Clothing
categories = ["Electronics", "Appliances", "Clothing"]
for category in categories:
    print(f"Category: {category}")

# %% Project 3: Low Stock Iterator
# Difficulty: Basic
# Description: Create a custom iterator for stock levels below 50.
# Objective: Practice creating a simple custom iterator.
# Tasks:
# - Define a class to iterate over stock levels, returning only those < 50.
# - Print low stock levels.
# Expected Output: Low stock: [30, 20]
class StockIterator:
    def __init__(self, stocks):
        self.stocks = stocks
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.stocks):
            stock = self.stocks[self.index]
            self.index += 1
            if stock < 50:
                return stock
        raise StopIteration

stocks = [30, 60, 20, 100]
low_stock = StockIterator(stocks)
print("Low stock:", [stock for stock in low_stock])

# %% Project 4: Expensive Product Iterator
# Difficulty: Intermediate
# Description: Create an iterator for products with price > $500.
# Objective: Practice filtering in a custom iterator.
# Tasks:
# - Define a class to iterate over products, returning only expensive ones.
# - Print product names.
# Expected Output: Expensive products: ['Laptop', 'Smartphone']
class ExpensiveProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            if product["price"] > 500:
                return product["name"]
        raise StopIteration

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 699.99},
    {"name": "Coffee Maker", "price": 49.99}
]
expensive_products = ExpensiveProductIterator(products)
print("Expensive products:", [name for name in expensive_products])

# %% Project 5: Order ID Iterator
# Difficulty: Intermediate
# Description: Create an iterator for order IDs in a range.
# Objective: Practice generating sequential values.
# Tasks:
# - Define a class to iterate over order IDs from 1001 to 1003.
# - Print order IDs.
# Expected Output: Order IDs: [1001, 1002, 1003]
class OrderIDIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.end:
            order_id = self.current
            self.current += 1
            return order_id
        raise StopIteration

order_ids = OrderIDIterator(1001, 1003)
print("Order IDs:", [id for id in order_ids])

# %% Project 6: Discounted Price Iterator
# Difficulty: Intermediate
# Description: Create an iterator for discounted prices (10% off).
# Objective: Practice transforming data in an iterator.
# Tasks:
# - Define a class to iterate over prices, applying a 10% discount.
# - Print discounted prices.
# Expected Output: Discounted prices: [899.99, 629.99]
class DiscountedPriceIterator:
    def __init__(self, prices):
        self.prices = prices
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.prices):
            price = self.prices[self.index] * 0.9
            self.index += 1
            return round(price, 2)
        raise StopIteration

prices = [999.99, 699.99]
discounted_prices = DiscountedPriceIterator(prices)
print("Discounted prices:", [price for price in discounted_prices])

# %% Project 7: Customer Priority Iterator
# Difficulty: Intermediate
# Description: Create an iterator for high-priority customers (orders > 2).
# Objective: Practice complex filtering.
# Tasks:
# - Define a class to iterate over customers, returning those with > 2 orders.
# - Print customer names.
# Expected Output: Priority customers: ['Alice']
class PriorityCustomerIterator:
    def __init__(self, customers):
        self.customers = customers
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.customers):
            customer = self.customers[self.index]
            self.index += 1
            if customer["orders"] > 2:
                return customer["name"]
        raise StopIteration

customers = [
    {"name": "Alice", "orders": 3},
    {"name": "Bob", "orders": 1}
]
priority_customers = PriorityCustomerIterator(customers)
print("Priority customers:", [name for name in priority_customers])

# %% Project 8: Reverse Product Iterator
# Difficulty: Advanced
# Description: Create an iterator to return products in reverse order.
# Objective: Practice custom iteration order.
# Tasks:
# - Define a class to iterate over products in reverse.
# - Print products.
# Expected Output: Products: ['Monitor', 'Keyboard', 'Mouse']
class ReverseProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = len(products) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= 0:
            product = self.products[self.index]
            self.index -= 1
            return product
        raise StopIteration

products = ["Mouse", "Keyboard", "Monitor"]
reverse_products = ReverseProductIterator(products)
print("Products:", [product for product in reverse_products])

# %% Project 9: Even Order Iterator
# Difficulty: Advanced
# Description: Create an iterator for even-numbered order IDs.
# Objective: Practice advanced filtering logic.
# Tasks:
# - Define a class to iterate over orders, returning only even order IDs.
# - Print even order IDs.
# Expected Output: Even order IDs: [102, 104]
class EvenOrderIterator:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.orders):
            order = self.orders[self.index]
            self.index += 1
            if order["order_id"] % 2 == 0:
                return order["order_id"]
        raise StopIteration

orders = [
    {"order_id": 101, "total": 1999.98},
    {"order_id": 102, "total": 49.99},
    {"order_id": 103, "total": 699.99},
    {"order_id": 104, "total": 299.99}
]
even_orders = EvenOrderIterator(orders)
print("Even order IDs:", [id for id in even_orders])

# %% Project 10: Comprehensive Retail Iterator
# Difficulty: Advanced
# Description: Create an iterator for orders with multiple conditions (total > $100, recent).
# Objective: Practice combining iterator features.
# Tasks:
# - Define a class to iterate over orders, filtering by total and date.
# - Print order details.
# Expected Output: Filtered orders: [{'order_id': 101, 'total': 1999.98}]
from datetime import datetime, timedelta

class RetailOrderIterator:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0
        self.recent_threshold = datetime.now() - timedelta(days=30)
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.orders):
            order = self.orders[self.index]
            self.index += 1
            order_date = datetime.strptime(order["date"], "%Y-%m-%d")
            if order["total"] > 100 and order_date >= self.recent_threshold:
                return order
        raise StopIteration

orders = [
    {"order_id": 101, "total": 1999.98, "date": "2025-04-20"},
    {"order_id": 102, "total": 49.99, "date": "2025-04-20"},
    {"order_id": 103, "total": 699.99, "date": "2025-03-01"}
]
filtered_orders = RetailOrderIterator(orders)
print("Filtered orders:", [order for order in filtered_orders])