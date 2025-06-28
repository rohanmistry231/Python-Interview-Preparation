# Python Dictionary DSA Patterns Interview Questions

This README provides **100 Python dictionary manipulation questions** designed for AI/ML students preparing for technical interviews. The questions focus on dictionary-specific problems, leveraging Python's dictionary data structure for efficient key-value operations and Data Structures and Algorithms (DSA) patterns such as hash tables, frequency counting, grouping, and dynamic programming. They are categorized into **Basic**, **Intermediate**, and **Advanced** levels, covering tasks like frequency analysis, key-value mapping, and complex dictionary-based algorithms. Each question includes a problem statement, with the solution hidden in a `<details>` tag to encourage users to attempt the problem before viewing the answer. This format supports hands-on practice and aligns with interview preparation for AI/ML roles, complementing the list and set-focused DSA questions.

## Basic Dictionary Questions

### 1. Count Frequency of Elements
**Problem**: Write a Python function to count the frequency of each element in a list using a dictionary.  
Example:  
```
Input: [1, 2, 2, 3, 1]  
Output: {1: 2, 2: 2, 3: 1}
```
<details>
<summary>Solution</summary>

```python
def count_frequency(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq
```

</details>

### 2. Check if Key Exists
**Problem**: Write a Python function to check if a key exists in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2}, key = 'a'  
Output: True
```
<details>
<summary>Solution</summary>

```python
def key_exists(d, key):
    return key in d
```

</details>

### 3. Merge Two Dictionaries
**Problem**: Write a Python function to merge two dictionaries, keeping the values from the second dictionary for duplicate keys.  
Example:  
```
Input: d1 = {'a': 1, 'b': 2}, d2 = {'b': 3, 'c': 4}  
Output: {'a': 1, 'b': 3, 'c': 4}
```
<details>
<summary>Solution</summary>

```python
def merge_dicts(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result
```

</details>

### 4. Find Key with Maximum Value
**Problem**: Write a Python function to find the key with the maximum value in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 3, 'c': 2}  
Output: 'b'
```
<details>
<summary>Solution</summary>

```python
def max_value_key(d):
    return max(d, key=d.get) if d else None
```

</details>

### 5. Find Key with Minimum Value
**Problem**: Write a Python function to find the key with the minimum value in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 3, 'c': 2}  
Output: 'a'
```
<details>
<summary>Solution</summary>

```python
def min_value_key(d):
    return min(d, key=d.get) if d else None
```

</details>

### 6. Invert Dictionary
**Problem**: Write a Python function to invert a dictionary, mapping values to keys. Assume unique values.  
Example:  
```
Input: {'a': 1, 'b': 2, 'c': 3}  
Output: {1: 'a', 2: 'b', 3: 'c'}
```
<details>
<summary>Solution</summary>

```python
def invert_dict(d):
    return {v: k for k, v in d.items()}
```

</details>

### 7. Group Elements by Value
**Problem**: Write a Python function to group list elements by their values using a dictionary.  
Example:  
```
Input: [1, 2, 1, 3, 2]  
Output: {1: [1, 1], 2: [2, 2], 3: [3]}
```
<details>
<summary>Solution</summary>

```python
def group_by_value(nums):
    result = {}
    for num in nums:
        result.setdefault(num, []).append(num)
    return result
```

</details>

### 8. Sum Values in Dictionary
**Problem**: Write a Python function to sum all values in a dictionary.  
Example:  
```
Input: {'a': 1, 'b': 2, 'c': 3}  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def sum_values(d):
    return sum(d.values())
```

</details>

### 9. Remove Key from Dictionary
**Problem**: Write a Python function to remove a specific key from a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, key = 'b'  
Output: {'a': 1, 'c': 3}
```
<details>
<summary>Solution</summary>

```python
def remove_key(d, key):
    result = d.copy()
    result.pop(key, None)
    return result
```

</details>

### 10. Check if Two Dictionaries are Equal
**Problem**: Write a Python function to check if two dictionaries are equal.  
Example:  
```
Input: d1 = {'a': 1, 'b': 2}, d2 = {'b': 2, 'a': 1}  
Output: True
```
<details>
<summary>Solution</summary>

```python
def dicts_equal(d1, d2):
    return d1 == d2
```

</details>

### 11. Find Common Keys
**Problem**: Write a Python function to find common keys between two dictionaries.  
Example:  
```
Input: d1 = {'a': 1, 'b': 2}, d2 = {'b': 3, 'c': 4}  
Output: ['b']
```
<details>
<summary>Solution</summary>

```python
def common_keys(d1, d2):
    return list(set(d1.keys()) & set(d2.keys()))
```

</details>

### 12. Find Unique Keys
**Problem**: Write a Python function to find keys that are unique to one dictionary.  
Example:  
```
Input: d1 = {'a': 1, 'b': 2}, d2 = {'b': 3, 'c': 4}  
Output: ['a', 'c']
```
<details>
<summary>Solution</summary>

```python
def unique_keys(d1, d2):
    return list(set(d1.keys()) ^ set(d2.keys()))
```

</details>

### 13. Create Dictionary from Two Lists
**Problem**: Write a Python function to create a dictionary from two lists of equal length (keys and values).  
Example:  
```
Input: keys = ['a', 'b'], values = [1, 2]  
Output: {'a': 1, 'b': 2}
```
<details>
<summary>Solution</summary>

```python
def lists_to_dict(keys, values):
    return dict(zip(keys, values))
```

</details>

### 14. Find Keys with Specific Value
**Problem**: Write a Python function to find all keys with a specific value in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 1}, value = 1  
Output: ['a', 'c']
```
<details>
<summary>Solution</summary>

```python
def keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]
```

</details>

### 15. Sort Dictionary by Value
**Problem**: Write a Python function to sort a dictionary by value in ascending order.  
Example:  
```
Input: {'a': 3, 'b': 1, 'c': 2}  
Output: {'b': 1, 'c': 2, 'a': 3}
```
<details>
<summary>Solution</summary>

```python
def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))
```

</details>

### 16. Count Characters in String
**Problem**: Write a Python function to count the frequency of each character in a string using a dictionary.  
Example:  
```
Input: "hello"  
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
<details>
<summary>Solution</summary>

```python
def count_characters(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
```

</details>

### 17. Find First Non-Repeating Character
**Problem**: Write a Python function to find the first non-repeating character in a string using a dictionary.  
Example:  
```
Input: "leetcode"  
Output: 'l'
```
<details>
<summary>Solution</summary>

```python
def first_non_repeating(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None
```

</details>

### 18. Group Anagrams
**Problem**: Write a Python function to group anagrams in a list of strings using a dictionary.  
Example:  
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]  
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```
<details>
<summary>Solution</summary>

```python
def group_anagrams(strs):
    result = {}
    for s in strs:
        key = tuple(sorted(s))
        result.setdefault(key, []).append(s)
    return list(result.values())
```

</details>

### 19. Check if Dictionary is Subset
**Problem**: Write a Python function to check if one dictionary is a subset of another.  
Example:  
```
Input: d1 = {'a': 1, 'b': 2}, d2 = {'a': 1, 'b': 2, 'c': 3}  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_dict_subset(d1, d2):
    return all(k in d2 and d2[k] == v for k, v in d1.items())
```

</details>

### 20. Sum of Values for Specific Keys
**Problem**: Write a Python function to sum the values of specific keys in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, keys = ['a', 'c']  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def sum_specific_keys(d, keys):
    return sum(d.get(key, 0) for key in keys)
```

</details>

## Intermediate Dictionary Questions

### 21. Find Two Sum
**Problem**: Write a Python function to find indices of two numbers in a list that sum to a target using a dictionary.  
Example:  
```
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]
```
<details>
<summary>Solution</summary>

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

</details>

### 22. Find Subarray with Sum K
**Problem**: Write a Python function to find the start and end indices of a subarray with sum k using a dictionary.  
Example:  
```
Input: nums = [1, 4, -2, 3], k = 5  
Output: [0, 3]
```
<details>
<summary>Solution</summary>

```python
def subarray_sum(nums, k):
    curr_sum = 0
    sums = {0: -1}
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - k in sums:
            return [sums[curr_sum - k] + 1, i]
        sums[curr_sum] = i
    return []
```

</details>

### 23. Find Longest Substring Without Repeating Characters
**Problem**: Write a Python function to find the length of the longest substring without repeating characters using a dictionary.  
Example:  
```
Input: "abcabcbb"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def longest_substring_no_repeat(s):
    seen = {}
    max_len = 0
    left = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        else:
            max_len = max(max_len, right - left + 1)
        seen[char] = right
    return max_len
```

</details>

### 24. Find All Anagrams in a String
**Problem**: Write a Python function to find all starting indices of anagrams of a pattern in a string using a dictionary.  
Example:  
```
Input: s = "cbaebabacd", p = "abc"  
Output: [0, 6]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def find_anagrams(s, p):
    p_count = Counter(p)
    window = Counter()
    result = []
    k = len(p)
    for i in range(len(s)):
        window[s[i]] += 1
        if i >= k:
            window[s[i - k]] -= 1
            if window[s[i - k]] == 0:
                del window[s[i - k]]
        if window == p_count:
            result.append(i - k + 1)
    return result
```

</details>

### 25. Find Minimum Window Substring
**Problem**: Write a Python function to find the minimum window substring that contains all characters of a pattern using a dictionary.  
Example:  
```
Input: s = "ADOBECODEBANC", t = "ABC"  
Output: "BANC"
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def min_window(s, t):
    t_count = Counter(t)
    required = len(t_count)
    window = {}
    formed = 0
    left = right = 0
    min_len = float('inf')
    min_window_sub = ""
    while right < len(s):
        window[s[right]] = window.get(s[right], 0) + 1
        if s[right] in t_count and window[s[right]] == t_count[s[right]]:
            formed += 1
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_sub = s[left:right + 1]
            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                formed -= 1
            left += 1
        right += 1
    return min_window_sub
```

</details>

### 26. Check if String is Isomorphic
**Problem**: Write a Python function to check if two strings are isomorphic using a dictionary.  
Example:  
```
Input: s = "egg", t = "add"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_to_s = {}
    for c1, c2 in zip(s, t):
        if c1 not in s_to_t and c2 not in t_to_s:
            s_to_t[c1] = c2
            t_to_s[c2] = c1
        elif s_to_t.get(c1) != c2 or t_to_s.get(c2) != c1:
            return False
    return True
```

</details>

### 27. Find First Unique Character in String
**Problem**: Write a Python function to find the index of the first unique character in a string using a dictionary.  
Example:  
```
Input: "leetcode"  
Output: 0
```
<details>
<summary>Solution</summary>

```python
def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1
```

</details>

### 28. Group Elements by Sum
**Problem**: Write a Python function to group list elements by their sum using a dictionary.  
Example:  
```
Input: [[1, 2], [2, 1], [3, 0]]  
Output: {3: [[1, 2], [2, 1]], 3: [[3, 0]]}
```
<details>
<summary>Solution</summary>

```python
def group_by_sum(arrs):
    result = {}
    for arr in arrs:
        s = sum(arr)
        result.setdefault(s, []).append(arr)
    return result
```

</details>

### 29. Find All Pairs with Sum K
**Problem**: Write a Python function to find all pairs in a list that sum to k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 5  
Output: [[1, 4], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
def find_pairs(nums, k):
    freq = {}
    result = []
    for num in nums:
        if k - num in freq:
            for _ in range(freq[k - num]):
                result.append([num, k - num])
        freq[num] = freq.get(num, 0) + 1
    return result
```

</details>

### 30. Check for Valid Anagram
**Problem**: Write a Python function to check if two strings are anagrams using a dictionary.  
Example:  
```
Input: s = "listen", t = "silent"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in t:
        freq[c] = freq.get(c, 0) - 1
        if freq[c] == 0:
            del freq[c]
    return not freq
```

</details>

### 31. Find Longest Subarray with Sum K
**Problem**: Write a Python function to find the length of the longest subarray with sum k using a dictionary.  
Example:  
```
Input: nums = [1, -1, 5, -2, 3], k = 3  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def longest_subarray_sum_k(nums, k):
    curr_sum = 0
    max_len = 0
    sums = {0: -1}
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - k in sums:
            max_len = max(max_len, i - sums[curr_sum - k])
        if curr_sum not in sums:
            sums[curr_sum] = i
    return max_len
```

</details>

### 32. Find All Subarrays with Sum K
**Problem**: Write a Python function to find all subarrays with sum k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, -3, 3], k = 3  
Output: [[1, 2], [3], [3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_sum_k(nums, k):
    curr_sum = 0
    sums = {0: [-1]}
    result = []
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - k in sums:
            for start in sums[curr_sum - k]:
                result.append(nums[start + 1:i + 1])
        sums[curr_sum] = sums.get(curr_sum, []) + [i]
    return result
```

</details>

### 33. Find Maximum Length Substring with K Distinct Characters
**Problem**: Write a Python function to find the maximum length substring with at most k distinct characters using a dictionary.  
Example:  
```
Input: s = "eceba", k = 2  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_substring_k_distinct(s, k):
    freq = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 34. Find All Substrings with K Distinct Characters
**Problem**: Write a Python function to find all substrings with exactly k distinct characters using a dictionary.  
Example:  
```
Input: s = "pqpqs", k = 2  
Output: ["pqp", "pqs"]
```
<details>
<summary>Solution</summary>

```python
def substrings_with_k_distinct(s, k):
    result = []
    for i in range(len(s)):
        freq = {}
        distinct = 0
        for j in range(i, len(s)):
            if s[j] not in freq:
                distinct += 1
            freq[s[j]] = freq.get(s[j], 0) + 1
            if distinct == k:
                result.append(s[i:j + 1])
            elif distinct > k:
                break
    return result
```

</details>

### 35. Find Maximum Value Sum with Unique Keys
**Problem**: Write a Python function to find the maximum sum of values from a list of key-value pairs with unique keys using a dictionary.  
Example:  
```
Input: pairs = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]  
Output: 7
```
<details>
<summary>Solution</summary>

```python
def max_sum_unique_keys(pairs):
    d = {}
    for key, value in pairs:
        d[key] = max(d.get(key, 0), value)
    return sum(d.values())
```

</details>

### 36. Find All Keys with Frequency K
**Problem**: Write a Python function to find all keys in a dictionary with a specific frequency in a list.  
Example:  
```
Input: nums = [1, 2, 1, 3], k = 2  
Output: [1]
```
<details>
<summary>Solution</summary>

```python
def keys_with_frequency(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return [key for key, count in freq.items() if count == k]
```

</details>

### 37. Find All Pairs with Difference K
**Problem**: Write a Python function to find all pairs in a list with difference k using a dictionary.  
Example:  
```
Input: nums = [3, 1, 4, 1, 5], k = 2  
Output: [[1, 3], [3, 5]]
```
<details>
<summary>Solution</summary>

```python
def pairs_with_difference(nums, k):
    freq = {}
    result = []
    for num in nums:
        if num + k in freq:
            for _ in range(freq[num + k]):
                result.append([num, num + k])
        if num - k in freq:
            for _ in range(freq[num - k]):
                result.append([num - k, num])
        freq[num] = freq.get(num, 0) + 1
    return result
```

</details>

### 38. Find Longest Consecutive Sequence
**Problem**: Write a Python function to find the length of the longest consecutive sequence in a list using a dictionary.  
Example:  
```
Input: [100, 4, 200, 1, 3, 2]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def longest_consecutive(nums):
    num_dict = {num: True for num in nums}
    max_len = 0
    for num in num_dict:
        if num - 1 not in num_dict:
            curr_num = num
            curr_len = 1
            while curr_num + 1 in num_dict:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len
```

</details>

### 39. Find All Subarrays with Zero Sum
**Problem**: Write a Python function to find all subarrays with sum zero using a dictionary.  
Example:  
```
Input: [4, 2, -2, 1, -1]  
Output: [[2, -2], [2, -2, 1, -1]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_with_zero_sum(nums):
    curr_sum = 0
    sums = {0: [-1]}
    result = []
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum in sums:
            for start in sums[curr_sum]:
                result.append(nums[start + 1:i + 1])
        sums[curr_sum] = sums.get(curr_sum, []) + [i]
    return result
```

</details>

### 40. Find Maximum Length Subarray with Equal 0s and 1s
**Problem**: Write a Python function to find the maximum length subarray with an equal number of 0s and 1s using a dictionary.  
Example:  
```
Input: [0, 1, 0, 1]  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_len_equal_0s_1s(nums):
    curr_sum = 0
    max_len = 0
    sums = {0: -1}
    for i, num in enumerate(nums):
        curr_sum += 1 if num == 1 else -1
        if curr_sum in sums:
            max_len = max(max_len, i - sums[curr_sum])
        else:
            sums[curr_sum] = i
    return max_len
```

</details>

## Advanced Dictionary Questions

### 41. Find All Subarrays with K Distinct Elements
**Problem**: Write a Python function to find all subarrays with exactly k distinct elements using a dictionary.  
Example:  
```
Input: nums = [1, 2, 1, 2, 3], k = 2  
Output: [[1, 2], [2, 1], [1, 2, 1], [2, 1, 2], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def subarrays_with_k_distinct(nums, k):
    result = []
    for i in range(len(nums)):
        freq = Counter()
        distinct = 0
        for j in range(i, len(nums)):
            if freq[nums[j]] == 0:
                distinct += 1
            freq[nums[j]] += 1
            if distinct == k:
                result.append(nums[i:j + 1])
            elif distinct > k:
                break
    return result
```

</details>

### 42. Find Maximum Sum Subarray with K Distinct Elements
**Problem**: Write a Python function to find the maximum sum subarray with at most k distinct elements using a dictionary.  
Example:  
```
Input: nums = [1, 5, 4, 2, 9], k = 2  
Output: 12
```
<details>
<summary>Solution</summary>

```python
def max_sum_subarray_k_distinct(nums, k):
    freq = {}
    curr_sum = 0
    max_sum = 0
    left = 0
    for right in range(len(nums)):
        freq[nums[right]] = freq.get(nums[right], 0) + 1
        curr_sum += nums[right]
        while len(freq) > k:
            freq[nums[left]] -= 1
            curr_sum -= nums[left]
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

</details>

### 43. Find All Anagrams in a List
**Problem**: Write a Python function to find all starting indices of anagrams of a pattern in a list using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 1, 2, 3, 4], pattern = [1, 2, 3]  
Output: [0, 3]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def find_anagrams_list(nums, pattern):
    p_count = Counter(pattern)
    window = Counter()
    result = []
    k = len(pattern)
    for i in range(len(nums)):
        window[nums[i]] += 1
        if i >= k:
            window[nums[i - k]] -= 1
            if window[nums[i - k]] == 0:
                del window[nums[i - k]]
        if window == p_count:
            result.append(i - k + 1)
    return result
```

</details>

### 44. Find Maximum Frequency Element
**Problem**: Write a Python function to find the element with the maximum frequency in a list using a dictionary.  
Example:  
```
Input: [1, 2, 2, 3, 3, 3]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_frequency_element(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get) if freq else None
```

</details>

### 45. Find All Subarrays with Product Less Than K
**Problem**: Write a Python function to find all subarrays with product less than k using a dictionary to track indices.  
Example:  
```
Input: nums = [1, 2, 3], k = 6  
Output: [[1], [2], [3], [1, 2], [1, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_product_less_than_k(nums, k):
    result = []
    for i in range(len(nums)):
        curr_prod = 1
        for j in range(i, len(nums)):
            curr_prod *= nums[j]
            if curr_prod < k:
                result.append(nums[i:j + 1])
            else:
                break
    return result
```

</details>

### 46. Find Maximum Length Subarray with Sum Less Than K
**Problem**: Write a Python function to find the maximum length subarray with sum less than k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 8  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_subarray_sum_less_k(nums, k):
    curr_sum = 0
    max_len = 0
    sums = {0: -1}
    for i, num in enumerate(nums):
        curr_sum += num
        for s in sums:
            if curr_sum - s < k:
                max_len = max(max_len, i - sums[s])
        sums[curr_sum] = i
    return max_len
```

</details>

### 47. Find All Keys with Values in Range
**Problem**: Write a Python function to find all keys in a dictionary whose values are within a given range.  
Example:  
```
Input: d = {'a': 1, 'b': 5, 'c': 3}, low = 2, high = 4  
Output: ['c']
```
<details>
<summary>Solution</summary>

```python
def keys_in_range(d, low, high):
    return [k for k, v in d.items() if low <= v <= high]
```

</details>

### 48. Find All Subarrays with Distinct Elements
**Problem**: Write a Python function to find all subarrays with distinct elements using a dictionary.  
Example:  
```
Input: [1, 2, 3, 1]  
Output: [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_distinct(nums):
    result = []
    for i in range(len(nums)):
        freq = {}
        for j in range(i, len(nums)):
            if nums[j] in freq:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 49. Find Maximum Sum of Values with Unique Keys
**Problem**: Write a Python function to find the maximum sum of values from a list of key-value pairs, ensuring unique keys, using a dictionary.  
Example:  
```
Input: pairs = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]  
Output: 7
```
<details>
<summary>Solution</summary>

```python
def max_sum_unique_keys_pairs(pairs):
    d = {}
    for key, value in pairs:
        d[key] = max(d.get(key, 0), value)
    return sum(d.values())
```

</details>

### 50. Find All Substrings with No Repeating Characters
**Problem**: Write a Python function to find all substrings with no repeating characters using a dictionary.  
Example:  
```
Input: "abcabcbb"  
Output: ["a", "b", "c", "ab", "bc", "abc"]
```
<details>
<summary>Solution</summary>

```python
def substrings_no_repeat(s):
    result = []
    for i in range(len(s)):
        freq = {}
        for j in range(i, len(s)):
            if s[j] in freq:
                break
            freq[s[j]] = 1
            result.append(s[i:j + 1])
    return result
```

</details>

### 51. Find Maximum Length Subarray with K Distinct Elements
**Problem**: Write a Python function to find the maximum length subarray with at most k distinct elements using a dictionary.  
Example:  
```
Input: nums = [1, 2, 1, 2, 3], k = 2  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_subarray_k_distinct(nums, k):
    freq = {}
    left = 0
    max_len = 0
    for right in range(len(nums)):
        freq[nums[right]] = freq.get(nums[right], 0) + 1
        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 52. Find All Keys with Top K Values
**Problem**: Write a Python function to find the keys with the top k values in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 3, 'c': 2, 'd': 4}, k = 2  
Output: ['d', 'b']
```
<details>
<summary>Solution</summary>

```python
def top_k_keys(d, k):
    return [k for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]
```

</details>

### 53. Find All Subarrays with Sum in Range
**Problem**: Write a Python function to find all subarrays with sum in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], low = 3, high = 5  
Output: [[1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_sum_in_range(nums, low, high):
    result = []
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if low <= curr_sum <= high:
                result.append(nums[i:j + 1])
    return result
```

</details>

### 54. Find All Keys with Values Greater Than Average
**Problem**: Write a Python function to find all keys whose values are greater than the average value in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 3, 'c': 5}  
Output: ['b', 'c']
```
<details>
<summary>Solution</summary>

```python
def keys_above_average(d):
    if not d:
        return []
    avg = sum(d.values()) / len(d)
    return [k for k, v in d.items() if v > avg]
```

</details>

### 55. Find All Substrings with K Distinct Characters
**Problem**: Write a Python function to find all substrings with exactly k distinct characters using a dictionary and sliding window.  
Example:  
```
Input: s = "pqpqs", k = 2  
Output: ["pqp", "pqs"]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def substrings_k_distinct(s, k):
    result = []
    for i in range(len(s)):
        freq = Counter()
        distinct = 0
        for j in range(i, len(s)):
            if freq[s[j]] == 0:
                distinct += 1
            freq[s[j]] += 1
            if distinct == k:
                result.append(s[i:j + 1])
            elif distinct > k:
                break
    return result
```

</details>

### 56. Find Maximum Sum of Values with Keys in Subset
**Problem**: Write a Python function to find the maximum sum of values for a subset of keys using a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, keys = ['a', 'b']  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_sum_subset_keys(d, keys):
    return sum(d.get(key, 0) for key in keys)
```

</details>

### 57. Find All Pairs with Product K
**Problem**: Write a Python function to find all pairs in a list with product k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 8  
Output: [[2, 4]]
```
<details>
<summary>Solution</summary>

```python
def pairs_with_product(nums, k):
    freq = {}
    result = []
    for num in nums:
        if k % num == 0 and k // num in freq:
            for _ in range(freq[k // num]):
                result.append([num, k // num])
        freq[num] = freq.get(num, 0) + 1
    return result
```

</details>

### 58. Find All Subarrays with No Duplicates
**Problem**: Write a Python function to find all subarrays with no duplicate elements using a dictionary.  
Example:  
```
Input: [1, 2, 3, 1]  
Output: [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_duplicates(nums):
    result = []
    for i in range(len(nums)):
        freq = {}
        for j in range(i, len(nums)):
            if nums[j] in freq:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 59. Find Maximum Length Subarray with No Duplicates
**Problem**: Write a Python function to find the maximum length subarray with no duplicate elements using a dictionary.  
Example:  
```
Input: [1, 2, 3, 1, 2]  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_no_duplicates(nums):
    freq = {}
    left = 0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] in freq and freq[nums[right]] >= left:
            left = freq[nums[right]] + 1
        freq[nums[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 60. Find All Keys with Values in Top K Percentile
**Problem**: Write a Python function to find all keys whose values are in the top k percentile of a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}, k = 50  
Output: ['c', 'd']
```
<details>
<summary>Solution</summary>

```python
def keys_top_k_percentile(d, k):
    if not d:
        return []
    values = sorted(d.values(), reverse=True)
    threshold_idx = int(len(values) * (1 - k / 100))
    threshold = values[threshold_idx] if threshold_idx < len(values) else values[-1]
    return [key for key, val in d.items() if val >= threshold]
```

</details>

### 61. Find All Subarrays with Sum Divisible by K
**Problem**: Write a Python function to find all subarrays with sum divisible by k using a dictionary.  
Example:  
```
Input: nums = [4, 5, 0, -2, -3, 1], k = 5  
Output: [[4, 5, 0, -2, -3, 1], [5], [5, 0], [0], [-2, -3, 1]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_sum_divisible_k(nums, k):
    curr_sum = 0
    sums = {0: [-1]}
    result = []
    for i, num in enumerate(nums):
        curr_sum += num
        rem = ((curr_sum % k) + k) % k
        if rem in sums:
            for start in sums[rem]:
                result.append(nums[start + 1:i + 1])
        sums[rem] = sums.get(rem, []) + [i]
    return result
```

</details>

### 62. Find Maximum Length Subarray with Sum Divisible by K
**Problem**: Write a Python function to find the maximum length subarray with sum divisible by k using a dictionary.  
Example:  
```
Input: nums = [4, 5, 0, -2, -3, 1], k = 5  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def max_len_sum_divisible_k(nums, k):
    curr_sum = 0
    max_len = 0
    sums = {0: -1}
    for i, num in enumerate(nums):
        curr_sum += num
        rem = ((curr_sum % k) + k) % k
        if rem in sums:
            max_len = max(max_len, i - sums[rem])
        if rem not in sums:
            sums[rem] = i
    return max_len
```

</details>

### 63. Find All Keys with Values Equal to Sum of Others
**Problem**: Write a Python function to find all keys whose values equal the sum of all other values in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}  
Output: ['c']
```
<details>
<summary>Solution</summary>

```python
def keys_equal_sum_others(d):
    total = sum(d.values())
    return [k for k, v in d.items() if v == total - v]
```

</details>

### 64. Find All Subarrays with Product in Range
**Problem**: Write a Python function to find all subarrays with product in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], low = 2, high = 6  
Output: [[1, 2], [1, 3], [2], [3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_product_in_range(nums, low, high):
    result = []
    for i in range(len(nums)):
        curr_prod = 1
        for j in range(i, len(nums)):
            curr_prod *= nums[j]
            if low <= curr_prod <= high:
                result.append(nums[i:j + 1])
            if curr_prod > high:
                break
    return result
```

</details>

### 65. Find Maximum Sum of Values with Keys in Pattern
**Problem**: Write a Python function to find the maximum sum of values for keys matching a pattern in a dictionary.  
Example:  
```
Input: d = {'abc': 1, 'abd': 2, 'xyz': 3}, pattern = "ab*"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
from fnmatch import fnmatch
def max_sum_pattern_keys(d, pattern):
    return sum(v for k, v in d.items() if fnmatch(k, pattern))
```

</details>

### 66. Find All Substrings with No Duplicate Characters
**Problem**: Write a Python function to find all substrings with no duplicate characters using a dictionary and sliding window.  
Example:  
```
Input: "abcabcbb"  
Output: ["a", "b", "c", "ab", "bc", "abc"]
```
<details>
<summary>Solution</summary>

```python
def substrings_no_duplicates(s):
    result = []
    for i in range(len(s)):
        freq = {}
        for j in range(i, len(s)):
            if s[j] in freq:
                break
            freq[s[j]] = 1
            result.append(s[i:j + 1])
    return result
```

</details>

### 67. Find Maximum Length Substring with No Duplicates
**Problem**: Write a Python function to find the maximum length substring with no duplicate characters using a dictionary.  
Example:  
```
Input: "abcabcbb"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_no_duplicates(s):
    freq = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in freq and freq[s[right]] >= left:
            left = freq[s[right]] + 1
        freq[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 68. Find All Keys with Values in Set
**Problem**: Write a Python function to find all keys whose values are in a given set using a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, values = {1, 3}  
Output: ['a', 'c']
```
<details>
<summary>Solution</summary>

```python
def keys_with_values_in_set(d, values):
    values = set(values)
    return [k for k, v in d.items() if v in values]
```

</details>

### 69. Find All Subarrays with Sum Equal to Average
**Problem**: Write a Python function to find all subarrays whose sum equals the average of the entire array using a dictionary.  
Example:  
```
Input: [1, 2, 3, 4]  
Output: [[2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_sum_equal_average(nums):
    avg = sum(nums) / len(nums)
    k = avg * len(nums)
    curr_sum = 0
    sums = {0: [-1]}
    result = []
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - k in sums:
            for start in sums[curr_sum - k]:
                sub = nums[start + 1:i + 1]
                if sub and sum(sub) / len(sub) == avg:
                    result.append(sub)
        sums[curr_sum] = sums.get(curr_sum, []) + [i]
    return result
```

</details>

### 70. Find Maximum Sum of Values with Keys Not in Set
**Problem**: Write a Python function to find the maximum sum of values for keys not in a given set using a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, forbidden = {'a'}  
Output: 5
```
<details>
<summary>Solution</summary>

```python
def max_sum_keys_not_in_set(d, forbidden):
    forbidden = set(forbidden)
    return sum(v for k, v in d.items() if k not in forbidden)
```

</details>

### 71. Find All Subarrays with K Distinct Elements in Range
**Problem**: Write a Python function to find all subarrays with exactly k distinct elements in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 1, 2, 3], k = 2, low = 2, high = 3  
Output: [[1, 2], [2, 1]]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def subarrays_k_distinct_in_range(nums, k, low, high):
    result = []
    for i in range(len(nums)):
        freq = Counter()
        distinct = 0
        for j in range(i, len(nums)):
            if freq[nums[j]] == 0:
                distinct += 1
            freq[nums[j]] += 1
            if distinct == k and low <= j - i + 1 <= high:
                result.append(nums[i:j + 1])
            elif distinct > k:
                break
    return result
```

</details>

### 72. Find All Keys with Values Divisible by K
**Problem**: Write a Python function to find all keys whose values are divisible by k in a dictionary.  
Example:  
```
Input: d = {'a': 2, 'b': 3, 'c': 4}, k = 2  
Output: ['a', 'c']
```
<details>
<summary>Solution</summary>

```python
def keys_values_divisible_k(d, k):
    return [k for k, v in d.items() if v % k == 0]
```

</details>

### 73. Find Maximum Length Subarray with Sum in Range
**Problem**: Write a Python function to find the maximum length subarray with sum in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], low = 3, high = 5  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_len_sum_in_range(nums, low, high):
    curr_sum = 0
    max_len = 0
    sums = {0: -1}
    for i, num in enumerate(nums):
        curr_sum += num
        for s in sums:
            if low <= curr_sum - s <= high:
                max_len = max(max_len, i - sums[s])
        sums[curr_sum] = i
    return max_len
```

</details>

### 74. Find All Substrings with Sum of Character Values K
**Problem**: Write a Python function to find all substrings whose character values sum to k using a dictionary.  
Example:  
```
Input: s = "abc", k = 6 (assume a=1, b=2, c=3)  
Output: ["abc"]
```
<details>
<summary>Solution</summary>

```python
def substrings_char_sum_k(s, k):
    char_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
    result = []
    for i in range(len(s)):
        curr_sum = 0
        for j in range(i, len(s)):
            curr_sum += char_values[s[j]]
            if curr_sum == k:
                result.append(s[i:j + 1])
    return result
```

</details>

### 75. Find Maximum Sum of Values with Keys in Graph
**Problem**: Write a Python function to find the maximum sum of values for keys in a connected component of a graph using a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, edges = [['a', 'b'], ['b', 'c']]  
Output: 6
```
<details>
<summary>Solution</summary>

```python
from collections import defaultdict
def max_sum_connected_component(d, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(node):
        visited.add(node)
        total = d.get(node, 0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                total += dfs(neighbor)
        return total
    max_sum = 0
    for node in d:
        if node not in visited:
            max_sum = max(max_sum, dfs(node))
    return max_sum
```

</details>

### 76. Find All Subarrays with No Pair Sum K
**Problem**: Write a Python function to find all subarrays where no pair sums to k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], k = 5  
Output: [[1], [2], [3], [1, 2], [1, 3], [2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_sum_k(nums, k):
    result = []
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                if num + nums[j] == k:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 77. Find Maximum Length Subarray with No Pair Sum K
**Problem**: Write a Python function to find the maximum length subarray where no pair sums to k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 7  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_no_pair_sum_k(nums, k):
    max_len = 0
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                if num + nums[j] == k:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            max_len = max(max_len, j - i + 1)
    return max_len
```

</details>

### 78. Find All Keys with Values in Top K
**Problem**: Write a Python function to find all keys with the top k values in a dictionary using a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 3, 'c': 2, 'd': 4}, k = 2  
Output: ['d', 'b']
```
<details>
<summary>Solution</summary>

```python
def top_k_keys_values(d, k):
    return [k for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]
```

</details>

### 79. Find All Subarrays with Sum Less Than Average
**Problem**: Write a Python function to find all subarrays with sum less than the average of the entire array using a dictionary.  
Example:  
```
Input: [1, 2, 3, 4]  
Output: [[1], [2], [1, 2]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_sum_less_average(nums):
    avg = sum(nums) / len(nums)
    result = []
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum < avg * (j - i + 1):
                result.append(nums[i:j + 1])
    return result
```

</details>

### 80. Find Maximum Sum of Values with Keys in Cycle
**Problem**: Write a Python function to find the maximum sum of values for keys in a cycle of a graph using a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, edges = [['a', 'b'], ['b', 'c'], ['c', 'a']]  
Output: 6
```
<details>
<summary>Solution</summary>

```python
from collections import defaultdict
def max_sum_cycle(d, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(node, parent, start):
        visited.add(node)
        total = d.get(node, 0)
        for neighbor in graph[node]:
            if neighbor == start and neighbor != parent:
                return total
            if neighbor not in visited:
                sub_total = dfs(neighbor, node, start)
                if sub_total > 0:
                    total += sub_total
        return total
    max_sum = 0
    for node in d:
        if node not in visited:
            total = dfs(node, None, node)
            if total > 0:
                max_sum = max(max_sum, total)
    return max_sum
```

</details>

### 81. Find All Subarrays with No Pair Product K
**Problem**: Write a Python function to find all subarrays where no pair’s product equals k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 6  
Output: [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_product_k(nums, k):
    result = []
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                if num * nums[j] == k:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 82. Find Maximum Length Subarray with No Pair Product K
**Problem**: Write a Python function to find the maximum length subarray where no pair’s product equals k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 6  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_no_pair_product_k(nums, k):
    max_len = 0
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                if num * nums[j] == k:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            max_len = max(max_len, j - i + 1)
    return max_len
```

</details>

### 83. Find All Keys with Values in Bottom K Percentile
**Problem**: Write a Python function to find all keys whose values are in the bottom k percentile of a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}, k = 50  
Output: ['a', 'b']
```
<details>
<summary>Solution</summary>

```python
def bottom_k_percentile_keys(d, k):
    if not d:
        return []
    values = sorted(d.values())
    threshold_idx = int(len(values) * k / 100)
    threshold = values[threshold_idx - 1] if threshold_idx > 0 else values[0]
    return [key for key, val in d.items() if val <= threshold]
```

</details>

### 84. Find All Subarrays with Sum Greater Than K
**Problem**: Write a Python function to find all subarrays with sum greater than k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], k = 3  
Output: [[1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_sum_greater_k(nums, k):
    result = []
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum > k:
                result.append(nums[i:j + 1])
    return result
```

</details>

### 85. Find Maximum Length Subarray with Sum Greater Than K
**Problem**: Write a Python function to find the maximum length subarray with sum greater than k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 5  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_sum_greater_k(nums, k):
    curr_sum = 0
    max_len = 0
    sums = {0: -1}
    for i, num in enumerate(nums):
        curr_sum += num
        for s in sums:
            if curr_sum - s > k:
                max_len = max(max_len, i - sums[s])
        sums[curr_sum] = i
    return max_len
```

</details>

### 86. Find All Keys with Values Equal to Product of Others
**Problem**: Write a Python function to find all keys whose values equal the product of all other values in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 2}  
Output: ['b', 'c']
```
<details>
<summary>Solution</summary>

```python
from math import prod
def keys_equal_product_others(d):
    total = prod(d.values())
    return [k for k, v in d.items() if v == total / v if v != 0 else False]
```

</details>

### 87. Find All Subarrays with No Pair Difference K
**Problem**: Write a Python function to find all subarrays where no pair’s absolute difference equals k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 1  
Output: [[1], [2], [3], [4]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_diff_k(nums, k):
    result = []
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                if abs(num - nums[j]) == k:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 88. Find Maximum Length Subarray with No Pair Difference K
**Problem**: Write a Python function to find the maximum length subarray where no pair’s absolute difference equals k using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], k = 1  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_len_no_pair_diff_k(nums, k):
    max_len = 0
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                if abs(num - nums[j]) == k:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            max_len = max(max_len, j - i + 1)
    return max_len
```

</details>

### 89. Find All Substrings with Sum of Character Values in Range
**Problem**: Write a Python function to find all substrings whose character values sum is in a given range using a dictionary.  
Example:  
```
Input: s = "abc", low = 3, high = 6 (assume a=1, b=2, c=3)  
Output: ["ab", "bc", "abc"]
```
<details>
<summary>Solution</summary>

```python
def substrings_char_sum_in_range(s, low, high):
    char_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
    result = []
    for i in range(len(s)):
        curr_sum = 0
        for j in range(i, len(s)):
            curr_sum += char_values[s[j]]
            if low <= curr_sum <= high:
                result.append(s[i:j + 1])
    return result
```

</details>

### 90. Find Maximum Sum of Values with Keys in Tree
**Problem**: Write a Python function to find the maximum sum of values for keys in a tree using a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3}, edges = [['a', 'b'], ['b', 'c']]  
Output: 6
```
<details>
<summary>Solution</summary>

```python
from collections import defaultdict
def max_sum_tree(d, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(node):
        visited.add(node)
        total = d.get(node, 0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                total += dfs(neighbor)
        return total
    max_sum = 0
    for node in d:
        if node not in visited:
            max_sum = max(max_sum, dfs(node))
    return max_sum
```

</details>

### 91. Find All Subarrays with No Pair Sum in Range
**Problem**: Write a Python function to find all subarrays where no pair’s sum is in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], low = 5, high = 7  
Output: [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_sum_in_range(nums, low, high):
    result = []
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                sum_val = num + nums[j]
                if low <= sum_val <= high:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 92. Find Maximum Length Subarray with No Pair Sum in Range
**Problem**: Write a Python function to find the maximum length subarray where no pair’s sum is in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], low = 7, high = 9  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def max_len_no_pair_sum_in_range(nums, low, high):
    max_len = 0
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                sum_val = num + nums[j]
                if low <= sum_val <= high:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            max_len = max(max_len, j - i + 1)
    return max_len
```

</details>

### 93. Find All Keys with Values Equal to Average of Others
**Problem**: Write a Python function to find all keys whose values equal the average of all other values in a dictionary.  
Example:  
```
Input: d = {'a': 1, 'b': 2, 'c': 3, 'd': 2}  
Output: ['b', 'd']
```
<details>
<summary>Solution</summary>

```python
def keys_equal_average_others(d):
    total = sum(d.values())
    n = len(d)
    return [k for k, v in d.items() if v == (total - v) / (n - 1) if n > 1 else False]
```

</details>

### 94. Find All Subarrays with No Pair Product in Range
**Problem**: Write a Python function to find all subarrays where no pair’s product is in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], low = 6, high = 9  
Output: [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_product_in_range(nums, low, high):
    result = []
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                prod = num * nums[j]
                if low <= prod <= high:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 95. Find Maximum Length Subarray with No Pair Product in Range
**Problem**: Write a Python function to find the maximum length subarray where no pair’s product is in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], low = 6, high = 9  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_no_pair_product_in_range(nums, low, high):
    max_len = 0
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                prod = num * nums[j]
                if low <= prod <= high:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            max_len = max(max_len, j - i + 1)
    return max_len
```

</details>

### 96. Find All Subarrays with No Pair Difference in Range
**Problem**: Write a Python function to find all subarrays where no pair’s absolute difference is in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], low = 2, high = 3  
Output: [[1], [2], [3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_diff_in_range(nums, low, high):
    result = []
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                diff = abs(num - nums[j])
                if low <= diff <= high:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>

### 97. Find Maximum Length Subarray with No Pair Difference in Range
**Problem**: Write a Python function to find the maximum length subarray where no pair’s absolute difference is in a given range using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3, 4], low = 2, high = 3  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def max_len_no_pair_diff_in_range(nums, low, high):
    max_len = 0
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                diff = abs(num - nums[j])
                if low <= diff <= high:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            max_len = max(max_len, j - i + 1)
    return max_len
```

</details>

### 98. Find All Substrings with Character Frequency K
**Problem**: Write a Python function to find all substrings where each character appears exactly k times using a dictionary.  
Example:  
```
Input: s = "aabbcc", k = 2  
Output: ["aabb", "bbcc", "aabbcc"]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def substrings_with_char_freq_k(s, k):
    result = []
    for i in range(len(s)):
        freq = Counter()
        for j in range(i, len(s)):
            freq[s[j]] += 1
            if all(count == k for count in freq.values()):
                result.append(s[i:j + 1])
            elif any(count > k for count in freq.values()):
                break
    return result
```

</details>

### 99. Find Maximum Length Substring with No Pair Sum in Forbidden Dictionary
**Problem**: Write a Python function to find the maximum length substring where no pair of characters’ ASCII values sum to any value in a forbidden dictionary using a dictionary.  
Example:  
```
Input: s = "abcd", forbidden = {'a': 97, 'b': 98}  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_len_no_pair_sum_forbidden(s, forbidden):
    max_len = 0
    for i in range(len(s)):
        freq = {}
        valid = True
        for j in range(i, len(s)):
            for char in freq:
                if ord(char) + ord(s[j]) in forbidden.values():
                    valid = False
                    break
            if not valid:
                break
            freq[s[j]] = 1
            max_len = max(max_len, j - i + 1)
    return max_len
```

</details>

### 100. Find All Subarrays with No Pair XOR in Forbidden Dictionary
**Problem**: Write a Python function to find all subarrays where no pair’s XOR equals any value in a forbidden dictionary using a dictionary.  
Example:  
```
Input: nums = [1, 2, 3], forbidden = {'a': 1, 'b': 2}  
Output: [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```
<details>
<summary>Solution</summary>

```python
def subarrays_no_pair_xor_forbidden(nums, forbidden):
    forbidden_values = set(forbidden.values())
    result = []
    for i in range(len(nums)):
        freq = {}
        valid = True
        for j in range(i, len(nums)):
            for num in freq:
                if (num ^ nums[j]) in forbidden_values:
                    valid = False
                    break
            if not valid:
                break
            freq[nums[j]] = 1
            result.append(nums[i:j + 1])
    return result
```

</details>