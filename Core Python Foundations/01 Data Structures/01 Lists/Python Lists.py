# Python Data Structures: Lists
# Purpose: Learn Lists, which are ordered, mutable collections that allow duplicate elements.
# Key Features: Indexing, slicing, appending, removing, sorting, and more.

# %% 1. Creating and Accessing Lists
# Explanation: Lists are defined with square brackets []. Elements can be of any type (strings, numbers, etc.).
# Lists are ordered, and you can access items using zero-based indexing or slicing.
products = ["Laptop", "Smartphone", "Coffee Maker", 999.99, 50]
print("1.1 Original List:", products)
print("1.2 First item (index 0):", products[0])  # Access first item
print("1.3 Last item (index -1):", products[-1])  # Negative indexing
print("1.4 Slice (items 1 to 2):", products[0:2])  # Slicing (excludes index 3)
print("1.5 Length of list:", len(products))  # Get list length

# Mini-Exercise: Create a list of 3 fruits and print the second fruit.
fruits = ["Apple", "Banana", "Orange"]
print("1.6 Mini-Exercise: Second fruit:", fruits[1])

# %% 2. Modifying Lists
# Explanation: Lists are mutable, meaning you can change their contents using methods like append(), remove(), or direct index assignment.
products.append("Blender")  # Add item to the end
print("2.1 After append:", products)
products[3] = 899.99  # Update price at index 3
print("2.2 After update:", products)
products.remove("Smartphone")  # Remove specific item
print("2.3 After remove:", products)
popped_item = products.pop()  # Remove and return last item
print("2.4 Popped item:", popped_item, "New list:", products)

# Mini-Exercise: Add a new item to fruits, update the first item, and pop the last item.
fruits.append("Mango")
fruits[0] = "Grape"
popped_fruit = fruits.pop()
print("2.5 Mini-Exercise: Updated fruits:", fruits, "Popped fruit:", popped_fruit)

# %% 3. List Operations
# Explanation: Lists support operations like concatenation (+), repetition (*), and in-place methods like sort() and reverse().
electronics = ["Mouse", "Keyboard"]
combined = products + electronics  # Combine two lists
print("3.1 Concatenated list:", combined)
repeated = electronics * 2  # Repeat list
print("3.2 Repeated list:", repeated)
numbers = [5, 2, 8, 1]
numbers.sort()  # Sort in ascending order
print("3.3 Sorted numbers:", numbers)
numbers.reverse()  # Reverse the list
print("3.4 Reversed numbers:", numbers)

# Mini-Exercise: Create a list of 4 numbers, sort it, and concatenate it with fruits.
numbers = [10, 3, 7, 1]
numbers.sort()
combined_with_fruits = numbers + fruits
print("3.5 Mini-Exercise: Sorted numbers + fruits:", combined_with_fruits)

# %% 4. Common List Methods
# Explanation: Lists have built-in methods for tasks like finding items, counting occurrences, or extending lists.
print("4.1 Index of 'Laptop':", products.index("Laptop"))  # Find index of item
print("4.2 Count of 'Coffee Maker':", products.count("Coffee Maker"))  # Count occurrences
products.extend(["Headphones", "Monitor"])  # Add multiple items
print("4.3 After extend:", products)
products.clear()  # Remove all items
print("4.4 After clear:", products)

# Mini-Exercise: Create a list, use extend() to add two items, and find the index of one item.
items = ["Pen", "Notebook"]
items.extend(["Pencil", "Eraser"])
print("4.5 Mini-Exercise: Extended list:", items, "Index of 'Pencil':", items.index("Pencil"))

# %% 5. Exercises for Practice
# Exercise 1: Create a list of 5 product prices, add a new price, update the second price, and sort the list.
prices = [499.99, 299.99, 49.99, 89.99, 199.99]
prices.append(399.99)
prices[1] = 349.99
prices.sort()
print("5.1 Exercise 1 - Sorted prices:", prices)

# Exercise 2: Create a list of categories, remove one category, and print the length of the final list.
categories = ["Electronics", "Appliances", "Furniture", "Clothing"]
categories.remove("Furniture")
print("5.2 Exercise 2 - Categories length:", len(categories))

# Exercise 3: Combine two lists (products and quantities), pop the last item, and reverse the combined list.
products = ["Laptop", "Coffee Maker"]  # Reset products for exercise
quantities = [10, 20, 30]
combined_list = products + quantities
combined_list.pop()
combined_list.reverse()
print("5.3 Exercise 3 - Reversed combined list:", combined_list)

# %% 6. Notes for Further Learning
# - Lists are versatile but can be slow for very large datasets (consider arrays or other structures later).
# - Indexing starts at 0; negative indices (-1 is last item) are useful.
# - Use list comprehension for advanced operations (covered later).
# - Common use cases: Storing data for ML models, managing app inventories, etc.
# Try the projects below to deepen your understanding!