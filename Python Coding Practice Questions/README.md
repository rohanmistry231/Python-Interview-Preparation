# Python Coding Practice: Interview Questions and Solutions

This markdown file contains a comprehensive set of Python coding interview exercises, ranging from beginner to advanced levels, designed to prepare you for technical interviews. Each exercise includes a problem statement and a solution hidden in a collapsible section, expandable by clicking "Click to expand solution". The exercises cover fundamental concepts, data structures, algorithms, and advanced Python features, ensuring thorough preparation.

## Table of Contents
- [Beginner Level](#beginner-level)
- [Intermediate Level](#intermediate-level)
- [Advanced Level](#advanced-level)

## Beginner Level

### Exercise 1: Print a Star Pattern
Print a right-angled triangle pattern of stars with 5 rows.

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

**Explanation**: The function iterates from 1 to 5, printing a string of stars (`*`) equal to the current row number. The `*` operator repeats the star character `i` times for each row.

</details>

### Exercise 2: Check if a Number is Even
Write a function to check if a given number is even.

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

**Explanation**: The function uses the modulo operator (`%`) to check if the number is divisible by 2 with no remainder. If true, the number is even.

</details>

### Exercise 3: Calculate Factorial
Write a function to calculate the factorial of a non-negative integer.

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

**Explanation**: The recursive function returns 1 for inputs 0 or 1. For other numbers, it multiplies `n` by the factorial of `n-1`.

</details>

### Exercise 4: Reverse a String
Write a function to reverse a given string.

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

**Explanation**: The solution uses string slicing with a step of `-1` to reverse the string efficiently.

</details>

### Exercise 5: Check Palindrome
Write a function to check if a string is a palindrome (reads the same forward and backward).

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
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
```

**Explanation**: The function converts the string to lowercase and compares it with its reverse using slicing.

</details>

### Exercise 6: Find Maximum in List
Write a function to find the largest element in a list of numbers.

**Example**:
```
Input: [3, 1, 4, 1, 5]
Output: 5
```

<details>
<summary>Click to expand solution</summary>

```python
def find_max(numbers):
    return max(numbers)

print(find_max([3, 1, 4, 1, 5]))  # 5
```

**Explanation**: The built-in `max()` function efficiently finds the largest element in the list.

</details>

### Exercise 7: Count Element Frequency
Write a function to count the frequency of each element in a list.

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

**Explanation**: The function uses a dictionary to track counts, incrementing the count for each element using `get()` to handle missing keys.

</details>

### Exercise 8: Check Prime Number
Write a function to check if a number is prime.

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

**Explanation**: The function checks divisibility up to the square root of `n` for efficiency. If no divisors are found, the number is prime.

</details>

### Exercise 9: Find Common Elements
Write a function to find common elements between two lists.

**Example**:
```
Input: [1, 2, 3], [2, 3, 4]
Output: [2, 3]
```

<details>
<summary>Click to expand solution</summary>

```python
def find_common(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(find_common([1, 2, 3], [2, 3, 4]))  # [2, 3]
```

**Explanation**: The function converts lists to sets and uses the `&` operator to find the intersection, then converts back to a list.

</details>

### Exercise 10: Bubble Sort
Write a function to sort a list using the bubble sort algorithm.

**Example**:
```
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]
```

<details>
<summary>Click to expand solution</summary>

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

**Explanation**: The function repeatedly compares adjacent elements and swaps them if they are in the wrong order, iterating until the list is sorted.

</details>

## Intermediate Level

### Exercise 11: Fibonacci Series
Write a function to generate the first `n` numbers in the Fibonacci series.

**Example**:
```
Input: 6
Output: [0, 1, 1, 2, 3, 5]
```

<details>
<summary>Click to expand solution</summary>

```python
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]
```

**Explanation**: The function initializes the series with `[0, 1]` and appends the sum of the last two numbers until the desired length is reached.

</details>

### Exercise 12: Remove Duplicates from List
Write a function to remove duplicates from a list while preserving order.

**Example**:
```
Input: [1, 2, 2, 3, 1]
Output: [1, 2, 3]
```

<details>
<summary>Click to expand solution</summary>

```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1]))  # [1, 2, 3]
```

**Explanation**: The function uses a set to track seen items and builds a new list, adding only the first occurrence of each item.

</details>

### Exercise 13: Find Second Largest Number
Write a function to find the second largest number in a list.

**Example**:
```
Input: [5, 2, 8, 1, 9]
Output: 8
```

<details>
<summary>Click to expand solution</summary>

```python
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

print(second_largest([5, 2, 8, 1, 9]))  # 8
```

**Explanation**: The function tracks the largest and second-largest numbers in a single pass, updating them as needed.

</details>

### Exercise 14: Merge Two Sorted Lists
Write a function to merge two sorted lists into a single sorted list.

**Example**:
```
Input: [1, 3, 5], [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
```

<details>
<summary>Click to expand solution</summary>

```python
def merge_sorted_lists(lst1, lst2):
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
```

**Explanation**: The function compares elements from both lists, appending the smaller one to the result, and adds remaining elements at the end.

</details>

### Exercise 15: Find First Non-Repeating Character
Write a function to find the first non-repeating character in a string.

**Example**:
```
Input: "swiss"
Output: "w"
```

<details>
<summary>Click to expand solution</summary>

```python
def first_non_repeating_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

print(first_non_repeating_char("swiss"))  # w
```

**Explanation**: The function counts character frequencies in a dictionary and returns the first character with a count of 1.

</details>

## Advanced Level

### Exercise 16: Longest Substring Without Repeating Characters
Write a function to find the length of the longest substring without repeating characters.

**Example**:
```
Input: "abcabcbb"
Output: 3
```

<details>
<summary>Click to expand solution</summary>

```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))  # 3
```

**Explanation**: The function uses a sliding window with a set to track unique characters, updating the maximum length as it moves.

</details>

### Exercise 17: Merge Intervals
Write a function to merge all overlapping intervals in a list of intervals.

**Example**:
```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

<details>
<summary>Click to expand solution</summary>

```python
def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
```

**Explanation**: The function sorts intervals by start time and merges overlapping intervals by updating the end time of the last interval.

</details>

### Exercise 18: Implement LRU Cache
Implement a Least Recently Used (LRU) cache with `get` and `put` operations.

**Example**:
```
LRUCache cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
```

<details>
<summary>Click to expand solution</summary>

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Example usage
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)
print(cache.get(2))  # -1
```

**Explanation**: The class uses an `OrderedDict` to maintain insertion order. `get` moves the accessed key to the end, and `put` evicts the least recently used item if the cache is full.

</details>

### Exercise 19: Metaclass Implementation
Write a metaclass that enforces a singleton pattern for a class.

**Example**:
```
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True
```

<details>
<summary>Click to expand solution</summary>

```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True
```

**Explanation**: The metaclass maintains a dictionary of instances and returns the existing instance if the class is already instantiated.

</details>

### Exercise 20: Multiprocessing Example
Write a function to parallelize a task using the `multiprocessing` module.

**Example**:
```
Input: [1, 2, 3, 4]
Output: [1, 4, 9, 16]  # Squares of input numbers
```

<details>
<summary>Click to expand solution</summary>

```python
from multiprocessing import Pool

def square(n):
    return n * n

def parallel_square(numbers):
    with Pool() as pool:
        results = pool.map(square, numbers)
    return results

print(parallel_square([1, 2, 3, 4]))  # [1, 4, 9, 16]
```

**Explanation**: The function uses `Pool` to parallelize the `square` function across multiple processes, mapping it to the input list.

</details>

## Credits
This collection is curated from reputable sources to aid Python interview preparation:
- [GeeksforGeeks Python Interview Questions](https://www.geeksforgeeks.org/python-interview-questions/)
- [Tanu-N-Prabhu GitHub Repository](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%2520Coding%2520Interview%2520Prep/Python%2520Coding%2520Interview%2520Questions%2520%28Beginner%2520to%2520Advanced%29.md)
- [InterviewBit Python Questions](https://www.interviewbit.com/python-interview-questions/)