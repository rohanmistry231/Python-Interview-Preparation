# Python Data Structures: Strings
# Purpose: Learn Strings, immutable sequences of characters.
# Key Features: Text manipulation, formatting, versatile methods.

# %% 1. Creating and Accessing Strings
# Explanation: Strings are created with single ('') or double ("") quotes. Use triple quotes (''' or """) for multiline.
# Access characters via zero-based indexing or slicing. Negative indices count from the end.
product_name = "Laptop Pro"
print("1.1 String:", product_name)
print("1.2 First char (index 0):", product_name[0])  # Indexing
print("1.3 Last char (index -1):", product_name[-1])  # Negative indexing
print("1.4 Slice [0:6]:", product_name[0:6])  # Slicing
print("1.5 Length of string:", len(product_name))  # Get string length
multiline = """Line 1
Line 2"""
print("1.6 Multiline string:", multiline)

# Mini-Exercise: Create a string for a city name and print its first 3 characters.
city = "New York"
print("1.7 Mini-Exercise: First 3 chars of city:", city[:3])

# %% 2. String Operations
# Explanation: Strings support concatenation (+), repetition (*), and membership tests (in).
# Strings are immutable, so operations create new strings.
category = "Electronics"
combined = product_name + " - " + category  # Concatenation
print("2.1 Concatenated:", combined)
repeated = product_name * 2  # Repetition
print("2.2 Repeated:", repeated)
print("2.3 Is 'Pro' in string?:", "Pro" in product_name)  # Membership test
print("2.4 Is 'Tablet' in string?:", "Tablet" in product_name)  # Negative membership test
print("2.5 Length of combined:", len(combined))  # Length of new string

# Mini-Exercise: Concatenate city with " City" and check if "York" is in it.
city_combined = city + " City"
print("2.6 Mini-Exercise: Concatenated city:", city_combined, "Is 'York' in string?:", "York" in city_combined)

# %% 3. String Methods
# Explanation: String methods (e.g., upper(), lower(), strip(), replace()) return new strings.
# split() creates lists, join() combines lists into strings.
print("3.1 Uppercase:", product_name.upper())  # Convert to uppercase
print("3.2 Lowercase:", product_name.lower())  # Convert to lowercase
print("3.3 Stripped spaces:", "  Laptop  ".strip())  # Remove leading/trailing spaces
print("3.4 Replaced:", product_name.replace("Pro", "Elite"))  # Replace substring
print("3.5 Split:", product_name.split(" "))  # Split into list
items = ["Laptop", "Smartphone"]
print("3.6 Joined:", ", ".join(items))  # Join list into string
print("3.7 Starts with 'Lap'?:", product_name.startswith("Lap"))  # Check prefix
print("3.8 Ends with 'Pro'?:", product_name.endswith("Pro"))  # Check suffix

# Mini-Exercise: Convert city to lowercase and split it into words.
city_lower = city.lower()
city_words = city.split()
print("3.9 Mini-Exercise: Lowercase city:", city_lower, "Words:", city_words)

# %% 4. String Formatting
# Explanation: Format strings with % (old), .format() (Python 3), or f-strings (Python 3.6+, recommended).
# f-strings are concise and readable for embedding expressions.
price = 999.99
print("4.1 % formatting: Product: %s, Price: $%.2f" % (product_name, price))
print("4.2 .format(): Product: {}, Price: ${:.2f}".format(product_name, price))
print(f"4.3 f-string: Product: {product_name}, Price: ${price:.2f}")  # f-string
discount = 10
print("4.4 f-string with expression: Discounted: ${:.2f}".format(price * (1 - discount / 100)))

# Mini-Exercise: Format a string with city and a population using an f-string.
population = 8_400_000
print("4.5 Mini-Exercise: f-string: City: {city}, Population: {population:,}")

# %% 5. Exercises for Practice
# Exercise 1: Create a string for a product name, convert it to uppercase, and slice the first 3 characters.
name = "Smartphone X"
upper_name = name.upper()
first_three = name[:3]
print("5.1 Exercise 1 - Uppercase:", upper_name, "First 3 chars:", first_three)

# Exercise 2: Join a list of categories into a string and replace one word.
cats = ["Electronics", "Appliances"]
joined = ", ".join(cats)
replaced = joined.replace("Appliances", "Home Goods")
print("5.2 Exercise 2 - Joined and replaced:", replaced)

# Exercise 3: Format a string with product name and price using an f-string.
prod = "Coffee Maker"
cost = 49.99
formatted = f"Item: {prod}, Cost: ${cost:.2f}"
print("5.3 Exercise 3 - Formatted:", formatted)

# Exercise 4: Split a sentence into words, convert to title case, and join back.
sentence = "the quick brown fox"
words = sentence.split()
title_words = [word.title() for word in words]
joined_title = " ".join(title_words)
print("5.4 Exercise 4 - Title case sentence:", joined_title)

# %% 6. Notes for Further Learning
# - Strings are immutable; all methods return new strings, leaving the original unchanged.
# - f-strings (Python 3.6+) are the preferred formatting method for readability.
# - Common use cases: Text preprocessing in ML, user input validation in web apps, log processing.
# - Use strip(), split(), and join() for parsing data; use replace() for cleaning.
# - Advanced: Explore regular expressions (re module) for complex string patterns.
# - Try the projects below to apply these concepts!