# Python Control Flow: Break Statement
# Purpose: Learn Break Statement to exit a loop immediately.
# Key Features: Terminates loop execution based on a condition, enables early stopping.

# %% 1. Break in For Loop
# Explanation: Exit a for loop when a condition is met, skipping remaining iterations.
# Useful for searching or thresholding.
prices = [100, 200, 999.99, 50, 300]
for price in prices:
    if price > 500:
        print(f"1.1 Found expensive item: {price}, stopping")
        break
    print(f"1.1 Price: {price}")
# Example with list
items = ["Mouse", "Keyboard", "Monitor"]
for item in items:
    if item == "Keyboard":
        print(f"1.2 Found {item}, stopping")
        break
    print(f"1.2 Checking: {item}")

# Mini-Exercise: Stop a for loop when a number exceeds 5.
numbers = [2, 4, 6, 8]
for num in numbers:
    if num > 5:
        print("1.3 Mini-Exercise: Number too large:", num)
        break
    print("1.3 Mini-Exercise: Number:", num)

# %% 2. Break in While Loop
# Explanation: Exit a while loop to prevent infinite or unwanted iterations.
# Common in dynamic processes.
stock = 100
while stock > 0:
    if stock < 50:
        print(f"2.1 Stock too low: {stock}, stopping")
        break
    stock -= 20
    print(f"2.1 Stock: {stock}")
# Example with counter
count = 0
while count < 10:
    count += 1
    if count == 5:
        print(f"2.2 Stopping at count: {count}")
        break
    print(f"2.2 Count: {count}")

# Mini-Exercise: Break a while loop when a price falls below 200.
price = 300
while price > 100:
    if price < 200:
        print("2.3 Mini-Exercise: Price too low:", price)
        break
    price -= 50
    print("2.3 Mini-Exercise: Price:", price)

# %% 3. Break in Nested Loops
# Explanation: Break exits only the innermost loop; outer loops continue.
# Useful for multi-level searches.
products = ["Laptop", "Smartphone", "Coffee Maker"]
categories = ["Electronics", "Appliances"]
for product in products:
    for category in categories:
        if product == "Coffee Maker" and category == "Appliances":
            print(f"3.1 Found {product} in {category}, stopping")
            break
        print(f"3.1 Checking {product} in {category}")
# Example with dictionary
items = [{"name": "Laptop", "price": 999}, {"name": "Mouse", "price": 25}]
for item in items:
    for key, value in item.items():
        if item["price"] > 500:
            print(f"3.2 Expensive item: {item['name']}, stopping")
            break
        print(f"3.2 Checking {key}: {value}")

# Mini-Exercise: Break a nested loop when a value exceeds 10.
outer = [1, 2]
inner = [5, 15, 20]
for x in outer:
    for y in inner:
        if y > 10:
            print("3.3 Mini-Exercise: Value too large:", y)
            break
        print("3.3 Mini-Exercise: Value:", y)

# %% 4. Exercises for Practice
# Exercise 1: Stop a for loop over a list of quantities when a quantity exceeds 10.
quantities = [5, 8, 12, 3]
for qty in quantities:
    if qty > 10:
        print("4.1 Exercise 1 - High quantity found:", qty)
        break
    print("4.1 Exercise 1 - Quantity:", qty)

# Exercise 2: Use break in a while loop to stop when price falls below 300.
price = 500
while price > 0:
    if price < 300:
        print("4.2 Exercise 2 - Price below 300:", price)
        break
    price -= 50
    print("4.2 Exercise 2 - Price:", price)

# Exercise 3: Break a nested loop when a product’s price and stock meet criteria (price > 700, stock < 50).
items = [{"name": "Laptop", "price": 999.99, "stock": 30}, 
         {"name": "Smartphone", "price": 699.99, "stock": 100}]
for item in items:
    for key, value in item.items():
        if item["price"] > 700 and item["stock"] < 50:
            print("4.3 Exercise 3 - Criteria met for", item["name"])
            break
        print("4.3 Exercise 3 - Checking", key, value)

# Exercise 4: Break a for loop when a string contains "phone".
words = ["Laptop", "Smartphone", "Tablet"]
for word in words:
    if "phone" in word.lower():
        print("4.4 Exercise 4 - Found phone in:", word)
        break
    print("4.4 Exercise 4 - Checking:", word)

# %% 5. Notes for Further Learning
# - Break exits only the innermost loop; use flags or multiple breaks for outer loops.
# - Use in ML for early stopping (e.g., training loops) or web apps for search termination.
# - Combine with conditionals for precise control, but avoid overuse to maintain clarity.
# - Test break conditions to ensure loops terminate as expected.
# - Try the projects below to apply these concepts!