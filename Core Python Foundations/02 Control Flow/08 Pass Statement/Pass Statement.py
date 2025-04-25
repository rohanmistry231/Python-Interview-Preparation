# Python Control Flow: Pass Statement
# Purpose: Learn Pass Statement as a placeholder that does nothing.
# Key Features: Enables empty blocks during development, ensures syntactical completeness.

# %% 1. Pass in Conditionals
# Explanation: Use pass when a block is required but no action is needed yet.
# Common during initial development or prototyping.
price = 999.99
if price > 1000:
    print("1.1 Luxury product")
else:
    pass  # Placeholder for future logic
# Example with multiple conditions
stock = 50
if stock < 20:
    print("1.2 Low stock")
else:
    pass  # To be implemented

# Mini-Exercise: Use pass for prices above 500.
test_price = 400
if test_price > 500:
    pass
else:
    print("1.3 Mini-Exercise: Price below 500:", test_price)

# %% 2. Pass in Loops
# Explanation: Use pass in loops to skip implementation temporarily.
# Useful for outlining loop structure.
products = ["Laptop", "Smartphone", "Coffee Maker"]
for product in products:
    if product == "Smartphone":
        pass  # Will add logic later
    else:
        print(f"2.1 Processing {product}")
# Example with while
count = 0
while count < 3:
    count += 1
    if count == 2:
        pass
    else:
        print(f"2.2 Count: {count}")

# Mini-Exercise: Use pass for odd numbers in a for loop.
numbers = [1, 2, 3]
for num in numbers:
    if num % 2 == 1:
        pass
    else:
        print("2.3 Mini-Exercise: Even number:", num)

# %% 3. Pass in Functions or Classes
# Explanation: Use pass for unimplemented functions or class methods.
# Common in API design or class scaffolding.
def calculate_discount(price):
    pass  # To be implemented later
class Product:
    def update_stock(self):
        pass  # Placeholder for method
product = Product()
print("3.1 Created Product object (no action)")
# Example with function
def process_order(order):
    pass
print("3.2 Placeholder function defined")

# Mini-Exercise: Define a placeholder class with a pass method.
class Order:
    def cancel(self):
        pass
order = Order()
print("3.3 Mini-Exercise: Order class defined")

# %% 4. Exercises for Practice
# Exercise 1: Use pass in an if-else block to skip budget products (< 100).
price = 50
if price < 100:
    pass
else:
    print("4.1 Exercise 1 - Non-budget price:", price)

# Exercise 2: Use pass in a for loop to skip a specific product.
items = ["Mouse", "Keyboard", "Monitor"]
for item in items:
    if item == "Keyboard":
        pass
    else:
        print("4.2 Exercise 2 - Processing:", item)

# Exercise 3: Define a placeholder function for stock checking with pass.
def check_stock(stock):
    pass
print("4.3 Exercise 3 - Placeholder function defined")

# Exercise 4: Use pass in a while loop for stock levels above 50.
stock = 70
while stock > 0:
    stock -= 10
    if stock > 50:
        pass
    else:
        print("4.4 Exercise 4 - Stock level:", stock)

# %% 5. Notes for Further Learning
# - Pass is a no-op, used to avoid syntax errors during development.
# - Common in ML for placeholder model training functions or web apps for API stubs.
# - Replace pass with actual logic as development progresses.
# - Use sparingly; excessive pass statements may indicate incomplete design.
# - Try the projects below to apply these concepts!