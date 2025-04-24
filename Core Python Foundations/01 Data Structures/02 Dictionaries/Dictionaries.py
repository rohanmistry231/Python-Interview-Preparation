# Python Data Structures: Dictionaries
# Purpose: Learn Dictionaries, unordered, mutable collections of key-value pairs.
# Key Features: Fast lookups by key, unique keys, flexible values, order preserved (Python 3.7+).

# %% 1. Creating and Accessing Dictionaries
# Explanation: Dictionaries use curly braces {} with key-value pairs. Keys are unique and immutable (e.g., strings, numbers).
# Values can be any type. Access values using keys or get() for safe access.
product = {
    "id": 1,
    "name": "Laptop Pro",
    "price": 999.99,
    "category": "Electronics"
}
print("1.1 Dictionary:", product)
print("1.2 Name:", product["name"])  # Access by key (raises KeyError if key missing)
print("1.3 Price:", product.get("price"))  # Safe access with get()
print("1.4 Missing key:", product.get("stock", "Not found"))  # Default value for missing key

# Mini-Exercise: Create a dictionary for a book and print its title.
book = {"title": "1984", "author": "George Orwell", "year": 1949}
print("1.5 Mini-Exercise: Book title:", book["title"])

# %% 2. Modifying Dictionaries
# Explanation: Dictionaries are mutable. Add/update key-value pairs with assignment or update().
# Remove items with pop() or popitem(). Use del for specific keys.
product["stock"] = 50  # Add new key-value pair
print("2.1 After adding stock:", product)
product["price"] = 899.99  # Update existing key
print("2.2 After updating price:", product)
product.update({"category": "Premium Electronics", "warranty": "2 years"})  # Update multiple
print("2.3 After update:", product)
removed = product.pop("warranty")  # Remove specific key, return value
print("2.4 Removed:", removed, "Dictionary:", product)
del product["stock"]  # Remove key using del
print("2.5 After del stock:", product)

# Mini-Exercise: Add a rating to book, update year to 1950, and pop author.
book["rating"] = 4.8
book["year"] = 1950
popped_author = book.pop("author")
print("2.6 Mini-Exercise: Updated book:", book, "Popped author:", popped_author)

# %% 3. Dictionary Operations
# Explanation: Access keys, values, or items (key-value pairs). Check membership with 'in'.
# Use len() for size. Dictionaries support iteration over keys, values, or items.
print("3.1 Keys:", list(product.keys()))  # Get all keys
print("3.2 Values:", list(product.values()))  # Get all values
print("3.3 Items:", list(product.items()))  # Get key-value pairs
print("3.4 Is 'name' in keys?:", "name" in product)  # Check key existence
print("3.5 Dictionary size:", len(product))  # Number of key-value pairs

# Mini-Exercise: Print all items in book and check if 'title' exists.
print("3.6 Mini-Exercise: Book items:", list(book.items()))
print("3.7 Is 'title' in book?:", "title" in book)

# %% 4. Dictionary Methods
# Explanation: Methods like copy(), clear(), setdefault(), and fromkeys() enhance functionality.
# copy() creates a shallow copy, setdefault() adds a key with a default if absent.
product_copy = product.copy()  # Create a shallow copy
print("4.1 Copy:", product_copy)
product.setdefault("discount", 0.0)  # Add key if not exists
print("4.2 After setdefault discount:", product)
default_dict = dict.fromkeys(["id", "name"], "Unknown")  # Create dict with default values
print("4.3 Fromkeys example:", default_dict)
# product.clear()  # Clears all items (commented to preserve data)
# print("4.4 After clear:", product)

# Mini-Exercise: Create a copy of book, add a default key 'pages' with value 0, and print copy.
book_copy = book.copy()
book_copy.setdefault("pages", 0)
print("4.5 Mini-Exercise: Book copy with pages:", book_copy)

# %% 5. Exercises for Practice
# Exercise 1: Create a dictionary for a product, add a quantity key, update the price, and print all keys.
item = {"id": 2, "name": "Smartphone", "price": 699.99}
item["quantity"] = 100
item["price"] = 649.99
print("5.1 Exercise 1 - Keys:", list(item.keys()))

# Exercise 2: Use update() to add category and rating to a dictionary, then remove rating.
item = {"id": 3, "name": "Coffee Maker"}
item.update({"category": "Appliances", "rating": 4.5})
item.pop("rating")
print("5.2 Exercise 2 - Updated dictionary:", item)

# Exercise 3: Check if a key exists in a dictionary and print its value using get().
check_key = "category"
value = item.get(check_key, "Not found")
print(f"5.3 Exercise 3 - Value for {check_key}:", value)

# Exercise 4: Create a dictionary from a list of keys with a default value, then modify one value.
keys = ["name", "price", "stock"]
new_dict = dict.fromkeys(keys, "TBD")
new_dict["price"] = 299.99
print("5.4 Exercise 4 - Modified dictionary:", new_dict)

# %% 6. Notes for Further Learning
# - Dictionaries are ideal for fast key-based lookups (e.g., ML model configs, web app data).
# - Keys must be immutable (strings, numbers, tuples). Values can be any type.
# - Use dictionary comprehension for advanced operations (e.g., {k: v*2 for k, v in dict.items()}).
# - Common use cases: Storing user profiles, caching results, mapping data.
# - Try the projects below to apply these concepts!