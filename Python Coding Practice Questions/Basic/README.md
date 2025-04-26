# Basic Python Coding Exercises

This file contains 34 basic Python coding exercises for interview preparation, focusing on fundamental concepts like syntax, loops, conditionals, and simple data structures. Retail-themed examples are included where applicable. Each exercise includes a problem statement, example, and a solution hidden in a collapsible section.

## Exercise 1: Print "Hello, World!"
**Description**: Write a function to print "Hello, World!".
**Example**:
```
Output: Hello, World!
```
<details>
<summary>Click to expand solution</summary>

```python
def print_hello():
    print("Hello, World!")

print_hello()
```

**Explanation**: The function uses the `print()` function to output the string "Hello, World!" to the console.
</details>

## Exercise 2: Check if a Number is Even
**Description**: Write a function to check if a given number is even.
**Example**:
```
Input: 4
Output: True
Input: 5
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_even(num):
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False
```

**Explanation**: The function uses the modulo operator (`%`) to check if the number is divisible by 2 with no remainder.
</details>

## Exercise 3: Concatenate Two Strings
**Description**: Write a function to concatenate two strings.
**Example**:
```
Input: "Hello, ", "World!"
Output: Hello, World!
```
<details>
<summary>Click to expand solution</summary>

```python
def concatenate_strings(str1, str2):
    return str1 + str2

print(concatenate_strings("Hello, ", "World!"))  # Hello, World!
```

**Explanation**: The function uses the `+` operator to concatenate the two input strings.
</details>

## Exercise 4: Find Maximum of Three Numbers
**Description**: Write a function to find the maximum of three numbers.
**Example**:
```
Input: 1, 2, 3
Output: 3
```
<details>
<summary>Click to expand solution</summary>

```python
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(1, 2, 3))  # 3
```

**Explanation**: The built-in `max()` function compares the three numbers and returns the largest.
</details>

## Exercise 5: Count Vowels in a String
**Description**: Write a function to count the number of vowels in a string.
**Example**:
```
Input: "hello"
Output: 2
```
<details>
<summary>Click to expand solution</summary>

```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("hello"))  # 2
```

**Explanation**: The function uses a generator expression to count characters in the string that are in the vowels set.
</details>

## Exercise 6: Calculate Factorial
**Description**: Write a function to calculate the factorial of a non-negative integer.
**Example**:
```
Input: 5
Output: 120
```
<details>
<summary>Click to expand solution</summary>

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

**Explanation**: The recursive function returns 1 for inputs 0 or 1 and multiplies `n` by the factorial of `n-1` for others.
</details>

## Exercise 7: Convert String to Integer
**Description**: Write a function to convert a string to an integer.
**Example**:
```
Input: "123"
Output: 123
```
<details>
<summary>Click to expand solution</summary>

```python
def str_to_int(s):
    return int(s)

print(str_to_int("123"))  # 123
```

**Explanation**: The built-in `int()` function converts a string to an integer, assuming the string represents a valid number.
</details>

## Exercise 8: Calculate Area of Rectangle
**Description**: Write a function to calculate the area of a rectangle given its length and width.
**Example**:
```
Input: length=5, width=10
Output: 50
```
<details>
<summary>Click to expand solution</summary>

```python
def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 10))  # 50
```

**Explanation**: The function multiplies the length and width to compute the area.
</details>

## Exercise 9: Reverse a String
**Description**: Write a function to reverse a given string.
**Example**:
```
Input: "hello"
Output: "olleh"
```
<details>
<summary>Click to expand solution</summary>

```python
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # olleh
```

**Explanation**: The function uses string slicing with a step of `-1` to reverse the string efficiently.
</details>

## Exercise 10: Check Palindrome
**Description**: Write a function to check if a string is a palindrome.
**Example**:
```
Input: "radar"
Output: True
Input: "hello"
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
```

**Explanation**: The function normalizes the string by converting to lowercase and removing spaces, then checks if it equals its reverse.
</details>

## Exercise 11: Find Sum of List
**Description**: Write a function to calculate the sum of all elements in a list.
**Example**:
```
Input: [1, 2, 3, 4]
Output: 10
```
<details>
<summary>Click to expand solution</summary>

```python
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4]))  # 10
```

**Explanation**: The built-in `sum()` function adds all elements in the list.
</details>

## Exercise 12: Swap Two Variables
**Description**: Write a function to swap two variables without using a temporary variable.
**Example**:
```
Input: a=5, b=10
Output: a=10, b=5
```
<details>
<summary>Click to expand solution</summary>

```python
def swap(a, b):
    a, b = b, a
    return a, b

a, b = 5, 10
a, b = swap(a, b)
print(f"a: {a}, b: {b}")  # a: 10, b: 5
```

**Explanation**: Python’s multiple assignment unpacks the tuple `(b, a)` to swap the variables.
</details>

## Exercise 13: Find Length of String
**Description**: Write a function to find the length of a string without using `len()`.
**Example**:
```
Input: "hello"
Output: 5
```
<details>
<summary>Click to expand solution</summary>

```python
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

print(string_length("hello"))  # 5
```

**Explanation**: The function iterates over each character in the string, incrementing a counter.
</details>

## Exercise 14: Check Prime Number
**Description**: Write a function to check if a number is prime.
**Example**:
```
Input: 7
Output: True
Input: 4
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(4))  # False
```

**Explanation**: The function checks divisibility up to the square root of `n` for efficiency.
</details>

## Exercise 15: Calculate Retail Discount
**Description**: Write a function to apply a 10% discount to a retail price.
**Example**:
```
Input: 100.00
Output: 90.00
```
<details>
<summary>Click to expand solution</summary>

```python
def apply_discount(price):
    return round(price * 0.9, 2)

print(apply_discount(100.00))  # 90.00
```

**Explanation**: The function multiplies the price by 0.9 and rounds to two decimal places.
</details>

## Exercise 16: Find Minimum in List
**Description**: Write a function to find the smallest element in a list.
**Example**:
```
Input: [3, 1, 4, 1, 5]
Output: 1
```
<details>
<summary>Click to expand solution</summary>

```python
def find_min(numbers):
    return min(numbers)

print(find_min([3, 1, 4, 1, 5]))  # 1
```

**Explanation**: The built-in `min()` function returns the smallest element in the list.
</details>

## Exercise 17: Sum of Digits
**Description**: Write a function to calculate the sum of digits in a number.
**Example**:
```
Input: 123
Output: 6
```
<details>
<summary>Click to expand solution</summary>

```python
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(123))  # 6
```

**Explanation**: The function converts the number to a string, iterates over digits, and sums them.
</details>

## Exercise 18: Print Star Pattern
**Description**: Print a right-angled triangle pattern of stars with 5 rows.
**Example Output**:
```
*
**
***
****
*****
```
<details>
<summary>Click to expand solution</summary>

```python
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)

print_star_pattern(5)
```

**Explanation**: The function iterates from 1 to 5, printing a string of stars equal to the current row number.
</details>

## Exercise 19: Check Leap Year
**Description**: Write a function to check if a year is a leap year.
**Example**:
```
Input: 2024
Output: True
Input: 2023
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False
```

**Explanation**: A year is a leap year if divisible by 4, but not by 100 unless also divisible by 400.
</details>

## Exercise 20: Convert List to String
**Description**: Write a function to convert a list of strings into a single string with spaces.
**Example**:
```
Input: ["Hello", "World"]
Output: "Hello World"
```
<details>
<summary>Click to expand solution</summary>

```python
def list_to_string(lst):
    return " ".join(lst)

print(list_to_string(["Hello", "World"]))  # Hello World
```

**Explanation**: The `join()` method concatenates list elements with a space separator.
</details>

## Exercise 21: Find Power of Number
**Description**: Write a function to calculate the power of a number without using `**`.
**Example**:
```
Input: base=2, exp=3
Output: 8
```
<details>
<summary>Click to expand solution</summary>

```python
def power(base, exp):
    if exp == 0:
        return 1
    result = 1
    for _ in range(exp):
        result *= base
    return result

print(power(2, 3))  # 8
```

**Explanation**: The function multiplies the base by itself `exp` times to compute the power.
</details>

## Exercise 22: Check Armstrong Number
**Description**: Write a function to check if a number is an Armstrong number.
**Example**:
```
Input: 153
Output: True
Input: 123
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n

print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
```

**Explanation**: The function sums each digit raised to the power of the number of digits and checks if it equals the original number.
</details>

## Exercise 23: Find GCD
**Description**: Write a function to find the Greatest Common Divisor (GCD) of two numbers.
**Example**:
```
Input: 48, 18
Output: 6
```
<details>
<summary>Click to expand solution</summary>

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6
```

**Explanation**: The Euclidean algorithm uses repeated division to find the GCD.
</details>

## Exercise 24: Find LCM
**Description**: Write a function to find the Least Common Multiple (LCM) of two numbers.
**Example**:
```
Input: 12, 18
Output: 36
```
<details>
<summary>Click to expand solution</summary>

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(12, 18))  # 36
```

**Explanation**: The LCM is calculated using the formula `LCM(a, b) = |a * b| / GCD(a, b)`.
</details>

## Exercise 25: Retail Stock Checker
**Description**: Write a function to check if a retail product’s stock is sufficient for an order.
**Example**:
```
Input: stock=50, order=30
Output: True
Input: stock=20, order=30
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def check_stock(stock, order):
    return stock >= order

print(check_stock(50, 30))  # True
print(check_stock(20, 30))  # False
```

**Explanation**: The function compares stock and order quantities, returning `True` if sufficient.
</details>

## Exercise 26: Find All Substrings
**Description**: Write a function to find all possible substrings of a string.
**Example**:
```
Input: "abc"
Output: ["a", "b", "c", "ab", "bc", "abc"]
```
<details>
<summary>Click to expand solution</summary>

```python
def find_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

print(find_substrings("abc"))  # ["a", "b", "c", "ab", "bc", "abc"]
```

**Explanation**: The function uses nested loops to generate all substrings by varying start and end indices.
</details>

## Exercise 27: Check Perfect Number
**Description**: Write a function to check if a number is perfect (sum of proper divisors equals the number).
**Example**:
```
Input: 6
Output: True
Input: 8
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

print(is_perfect(6))  # True
print(is_perfect(8))  # False
```

**Explanation**: The function sums all proper divisors and checks if the sum equals the number.
</details>

## Exercise 28: Find Unique Elements
**Description**: Write a function to find unique elements in a list while preserving order.
**Example**:
```
Input: [1, 2, 2, 3, 3, 4]
Output: [1, 2, 3, 4]
```
<details>
<summary>Click to expand solution</summary>

```python
def find_unique(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(find_unique([1, 2, 2, 3, 3, 4]))  # [1, 2, 3, 4]
```

**Explanation**: The function uses a set to track seen items, adding only the first occurrence to the result list.
</details>

## Exercise 29: Count Element Frequency
**Description**: Write a function to count the frequency of each element in a list.
**Example**:
```
Input: [1, 2, 2, 3, 1]
Output: {1: 2, 2: 2, 3: 1}
```
<details>
<summary>Click to expand solution</summary>

```python
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(count_frequency([1, 2, 2, 3, 1]))  # {1: 2, 2: 2, 3: 1}
```

**Explanation**: The function uses a dictionary to track counts, incrementing for each element.
</details>

## Exercise 30: Find Sum of Pairs
**Description**: Write a function to find all pairs in a list that sum to a target value.
**Example**:
```
Input: [1, 2, 3, 4], target=7
Output: [(3, 4)]
```
<details>
<summary>Click to expand solution</summary>

```python
def find_pairs_with_sum(nums, target):
    pairs = []
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    return pairs

print(find_pairs_with_sum([1, 2, 3, 4], 7))  # [(3, 4)]
```

**Explanation**: The function uses a set to track seen numbers, checking for complements to form pairs.
</details>

## Exercise 31: Check Anagram
**Description**: Write a function to check if two strings are anagrams.
**Example**:
```
Input: "listen", "silent"
Output: True
Input: "hello", "world"
Output: False
```
<details>
<summary>Click to expand solution</summary>

```python
def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False
```

**Explanation**: The function normalizes strings and compares their sorted characters.
</details>

## Exercise 32: Find Missing Number
**Description**: Write a function to find the missing number in a list of integers from 1 to `n`.
**Example**:
```
Input: [1, 2, 4, 5]
Output: 3
```
<details>
<summary>Click to expand solution</summary>

```python
def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(find_missing_number([1, 2, 4, 5]))  # 3
```

**Explanation**: The function uses the formula for the sum of the first `n` numbers to find the missing number.
</details>

## Exercise 33: Retail Order Total
**Description**: Write a function to calculate the total of retail orders with a 5% tax.
**Example**:
```
Input: [100.00, 50.00]
Output: 157.50
```
<details>
<summary>Click to expand solution</summary>

```python
def calculate_order_total(items):
    subtotal = sum(items)
    tax = subtotal * 0.05
    return round(subtotal + tax, 2)

print(calculate_order_total([100.00, 50.00]))  # 157.50
```

**Explanation**: The function sums the items, adds a 5% tax, and rounds to two decimal places.
</details>

## Exercise 34: Print Diamond Pattern
**Description**: Print a diamond pattern of stars with 5 rows.
**Example Output**:
```
  *
 ***
*****
 ***
  *
```
<details>
<summary>Click to expand solution</summary>

```python
def print_diamond(n):
    for i in range(n // 2 + 1):
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))
    for i in range(n // 2 - 1, -1, -1):
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))

print_diamond(5)
```

**Explanation**: The function prints the upper half of the diamond by increasing stars and decreasing spaces, then reverses for the lower half.
</details>