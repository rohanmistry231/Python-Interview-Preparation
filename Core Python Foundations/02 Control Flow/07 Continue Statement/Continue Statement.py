# Python Control Flow: Continue Statement
# Purpose: Learn Continue Statement to skip the rest of the current loop iteration.
# Key Features: Selective iteration control, skips to next iteration.

# %% 1. Continue in For Loop
# Explanation: Skip the current iteration when a condition is met, continue with next item.
# Useful for filtering during iteration.
prices = [100, 999.99, 50, 700, 25]
for price in prices:
    if price < 100:
        continue
    print(f"1.1 Price above 100: {price}")
# Example with strings
items = ["Mouse", "Keyboard", "Monitor"]
for item in items:
    if len(item) < 6:
        continue
    print(f"1.2 Long name: {item}")

# Mini-Exercise: Skip numbers less than 3 in a for loop.
numbers = [1, 3, 5]
for num in numbers:
    if num < 3:
        continue
    print("1.3 Mini-Exercise: Number:", num)

# %% 2. Continue in While Loop
# Explanation: Skip iteration in a while loop, re-evaluate the condition.
# Common in dynamic filtering.
stock = 100
while stock > 0:
    stock -= 20
    if stock % 40 == 0:
        continue
    print(f"2.1 Stock level: {stock}")
# Example with counter
count = 0
while count < 5:
    count += 1
    if count % 2 == 0:
        continue
    print(f"2.2 Odd count: {count}")

# Mini-Exercise: Skip stock levels divisible by 30 in a while loop.
stock = 90
while stock > 0:
    stock -= 10
    if stock % 30 == 0:
        continue
    print("2.3 Mini-Exercise: Stock:", stock)

# %% 3. Continue in Nested Loops
# Explanation: Skips only the innermost loop’s current iteration; outer loop continues.
# Useful for selective processing in multi-level loops.
products = ["Laptop", "Smartphone", "Coffee Maker"]
categories = ["Electronics", "Appliances"]
for product in products:
    for category in categories:
        if category == "Appliances":
            continue
        print(f"3.1 Checking {product} in {category}")
# Example with dictionary
items = [{"name": "Laptop", "category": "Electronics"}, 
         {"name": "Blender", "category": "Appliances"}]
for item in items:
    for key, value in item.items():
        if item["category"] != "Electronics":
            continue
        print(f"3.2 Electronics attribute: {key} = {value}")

# Mini-Exercise: Skip inner loop values less than 10 in a nested loop.
outer = [1, 2]
inner = [5, 15, 20]
for x in outer:
    for y in inner:
        if y < 10:
            continue
        print("3.3 Mini-Exercise: Value:", y)

# %% 4. Exercises for Practice
# Exercise 1: Skip prices below 200 in a for loop over a list of prices.
prices = [150, 300, 50, 400]
for price in prices:
    if price < 200:
        continue
    print("4.1 Exercise 1 - Price:", price)

# Exercise 2: Use continue in a while loop to skip stock levels that are even.
stock = 50
while stock > 0:
    stock -= 10
    if stock % 2 == 0:
        continue
    print("4.2 Exercise 2 - Odd stock level:", stock)

# Exercise 3: Skip non-Electronics products in a nested loop over products and attributes.
items = [{"name": "Laptop", "category": "Electronics"}, 
         {"name": "Blender", "category": "Appliances"}]
for item in items:
    for key, value in item.items():
        if item["category"] != "Electronics":
            continue
        print("4.3 Exercise 3 - Electronics attribute:", key, value)

# Exercise 4: Skip words shorter than 5 characters in a for loop.
words = ["Cat", "Mouse", "Keyboard"]
for word in words:
    if len(word) < 5:
        continue
    print("4.4 Exercise 4 - Long word:", word)

# %% 5. Notes for Further Learning
# - Continue skips to the next iteration without exiting the loop, useful for filtering.
# - Use in ML for data preprocessing (e.g., skipping invalid entries) or web apps for selective processing.
# - Avoid overusing continue to maintain code clarity; consider list comprehensions for simple filters.
# - Test continue conditions to ensure correct iterations are skipped.
# - Try the projects below to apply these concepts!