# Python Tuple DSA Patterns Interview Questions

This README provides **100 Python tuple manipulation questions** designed for AI/ML students preparing for technical interviews. The questions focus on tuple-specific problems, leveraging Python's tuple data structure for immutable sequence operations and Data Structures and Algorithms (DSA) patterns such as sorting, searching, grouping, and combinatorial problems. They are categorized into **Basic**, **Intermediate**, and **Advanced** levels, covering tasks like tuple comparisons, subsequence checks, and complex tuple-based algorithms. Each question includes a problem statement, with the solution hidden in a `<details>` tag to encourage users to attempt the problem before viewing the answer. This format supports hands-on practice and aligns with interview preparation for AI/ML roles, complementing the list, set, and dictionary-focused DSA questions.

## Basic Tuple Questions

### 1. Check if Two Tuples are Equal
**Problem**: Write a Python function to check if two tuples are equal.  
Example:  
```
Input: t1 = (1, 2, 3), t2 = (1, 2, 3)  
Output: True
```
<details>
<summary>Solution</summary>

```python
def are_tuples_equal(t1, t2):
    return t1 == t2
```

</details>

### 2. Find Length of a Tuple
**Problem**: Write a Python function to find the length of a tuple.  
Example:  
```
Input: t = (1, 2, 3)  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def tuple_length(t):
    return len(t)
```

</details>

### 3. Get Element at Index
**Problem**: Write a Python function to get the element at a specific index in a tuple.  
Example:  
```
Input: t = (1, 2, 3), index = 1  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def get_element(t, index):
    return t[index] if 0 <= index < len(t) else None
```

</details>

### 4. Count Occurrences in a Tuple
**Problem**: Write a Python function to count the occurrences of an element in a tuple.  
Example:  
```
Input: t = (1, 2, 1, 3), element = 1  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def count_element(t, element):
    return t.count(element)
```

</details>

### 5. Find Index of Element
**Problem**: Write a Python function to find the first index of an element in a tuple.  
Example:  
```
Input: t = (1, 2, 3, 1), element = 1  
Output: 0
```
<details>
<summary>Solution</summary>

```python
def find_index(t, element):
    try:
        return t.index(element)
    except ValueError:
        return -1
```

</details>

### 6. Concatenate Two Tuples
**Problem**: Write a Python function to concatenate two tuples.  
Example:  
```
Input: t1 = (1, 2), t2 = (3, 4)  
Output: (1, 2, 3, 4)
```
<details>
<summary>Solution</summary>

```python
def concatenate_tuples(t1, t2):
    return t1 + t2
```

</details>

### 7. Check if Element Exists in Tuple
**Problem**: Write a Python function to check if an element exists in a tuple.  
Example:  
```
Input: t = (1, 2, 3), element = 2  
Output: True
```
<details>
<summary>Solution</summary>

```python
def element_exists(t, element):
    return element in t
```

</details>

### 8. Slice a Tuple
**Problem**: Write a Python function to slice a tuple between given start and end indices.  
Example:  
```
Input: t = (1, 2, 3, 4), start = 1, end = 3  
Output: (2, 3)
```
<details>
<summary>Solution</summary>

```python
def slice_tuple(t, start, end):
    return t[start:end]
```

</details>

### 9. Convert List to Tuple
**Problem**: Write a Python function to convert a list to a tuple.  
Example:  
```
Input: lst = [1, 2, 3]  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def list_to_tuple(lst):
    return tuple(lst)
```

</details>

### 10. Convert Tuple to List
**Problem**: Write a Python function to convert a tuple to a list.  
Example:  
```
Input: t = (1, 2, 3)  
Output: [1, 2, 3]
```
<details>
<summary>Solution</summary>

```python
def tuple_to_list(t):
    return list(t)
```

</details>

### 11. Find Maximum Element in Tuple
**Problem**: Write a Python function to find the maximum element in a tuple.  
Example:  
```
Input: t = (1, 3, 2)  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def max_element(t):
    return max(t) if t else None
```

</details>

### 12. Find Minimum Element in Tuple
**Problem**: Write a Python function to find the minimum element in a tuple.  
Example:  
```
Input: t = (1, 3, 2)  
Output: 1
```
<details>
<summary>Solution</summary>

```python
def min_element(t):
    return min(t) if t else None
```

</details>

### 13. Sum Elements in Tuple
**Problem**: Write a Python function to sum all elements in a tuple.  
Example:  
```
Input: t = (1, 2, 3)  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def sum_elements(t):
    return sum(t)
```

</details>

### 14. Check if Tuple is Sorted
**Problem**: Write a Python function to check if a tuple is sorted in ascending order.  
Example:  
```
Input: t = (1, 2, 3)  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_sorted(t):
    return all(t[i] <= t[i + 1] for i in range(len(t) - 1))
```

</details>

### 15. Reverse a Tuple
**Problem**: Write a Python function to reverse a tuple.  
Example:  
```
Input: t = (1, 2, 3)  
Output: (3, 2, 1)
```
<details>
<summary>Solution</summary>

```python
def reverse_tuple(t):
    return t[::-1]
```

</details>

### 16. Check if Tuple Contains Duplicates
**Problem**: Write a Python function to check if a tuple contains duplicate elements.  
Example:  
```
Input: t = (1, 2, 1)  
Output: True
```
<details>
<summary>Solution</summary>

```python
def has_duplicates(t):
    return len(t) != len(set(t))
```

</details>

### 17. Find All Indices of Element
**Problem**: Write a Python function to find all indices of an element in a tuple.  
Example:  
```
Input: t = (1, 2, 1, 3), element = 1  
Output: [0, 2]
```
<details>
<summary>Solution</summary>

```python
def all_indices(t, element):
    return [i for i, x in enumerate(t) if x == element]
```

</details>

### 18. Create Tuple from Range
**Problem**: Write a Python function to create a tuple from a range of numbers.  
Example:  
```
Input: start = 1, end = 4  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def range_to_tuple(start, end):
    return tuple(range(start, end))
```

</details>

### 19. Check if Tuple is Subset of Another
**Problem**: Write a Python function to check if one tuple is a subset of another.  
Example:  
```
Input: t1 = (1, 2), t2 = (1, 2, 3)  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_subset(t1, t2):
    return set(t1).issubset(set(t2))
```

</details>

### 20. Find Common Elements in Two Tuples
**Problem**: Write a Python function to find common elements between two tuples.  
Example:  
```
Input: t1 = (1, 2, 3), t2 = (2, 3, 4)  
Output: (2, 3)
```
<details>
<summary>Solution</summary>

```python
def common_elements(t1, t2):
    return tuple(set(t1) & set(t2))
```

</details>

## Intermediate Tuple Questions

### 21. Find Pair with Sum K
**Problem**: Write a Python function to find a pair in a tuple that sums to k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 5  
Output: (1, 4)
```
<details>
<summary>Solution</summary>

```python
def find_pair_sum_k(t, k):
    seen = set()
    for num in t:
        if k - num in seen:
            return (k - num, num)
        seen.add(num)
    return None
```

</details>

### 22. Find All Pairs with Sum K
**Problem**: Write a Python function to find all pairs in a tuple that sum to k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 5  
Output: [(1, 4), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def all_pairs_sum_k(t, k):
    freq = {}
    result = []
    for num in t:
        if k - num in freq:
            for _ in range(freq[k - num]):
                result.append((min(num, k - num), max(num, k - num)))
        freq[num] = freq.get(num, 0) + 1
    return sorted(result)
```

</details>

### 23. Find Subtuple with Sum K
**Problem**: Write a Python function to find a subtuple with sum k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 5  
Output: (2, 3)
```
<details>
<summary>Solution</summary>

```python
def subtuple_sum_k(t, k):
    curr_sum = 0
    sums = {0: -1}
    for i, num in enumerate(t):
        curr_sum += num
        if curr_sum - k in sums:
            return t[sums[curr_sum - k] + 1:i + 1]
        sums[curr_sum] = i
    return None
```

</details>

### 24. Find Longest Subtuple with Sum K
**Problem**: Write a Python function to find the longest subtuple with sum k.  
Example:  
```
Input: t = (1, 2, 3, -1, 2), k = 4  
Output: (1, 2, 3, -1, 2)
```
<details>
<summary>Solution</summary>

```python
def longest_subtuple_sum_k(t, k):
    curr_sum = 0
    max_len = 0
    result = None
    sums = {0: -1}
    for i, num in enumerate(t):
        curr_sum += num
        if curr_sum - k in sums:
            length = i - sums[curr_sum - k]
            if length > max_len:
                max_len = length
                result = t[sums[curr_sum - k] + 1:i + 1]
        if curr_sum not in sums:
            sums[curr_sum] = i
    return result
```

</details>

### 25. Find All Subtuples with Sum K
**Problem**: Write a Python function to find all subtuples with sum k.  
Example:  
```
Input: t = (1, 2, 3, -3, 3), k = 3  
Output: [(1, 2), (3,), (3,)]
```
<details>
<summary>Solution</summary>

```python
def all_subtuples_sum_k(t, k):
    curr_sum = 0
    sums = {0: [-1]}
    result = []
    for i, num in enumerate(t):
        curr_sum += num
        if curr_sum - k in sums:
            for start in sums[curr_sum - k]:
                result.append(t[start + 1:i + 1])
        sums[curr_sum] = sums.get(curr_sum, []) + [i]
    return result
```

</details>

### 26. Check if Tuple is Palindrome
**Problem**: Write a Python function to check if a tuple is a palindrome.  
Example:  
```
Input: t = (1, 2, 1)  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_palindrome(t):
    return t == t[::-1]
```

</details>

### 27. Find All Subtuples
**Problem**: Write a Python function to find all possible subtuples of a tuple.  
Example:  
```
Input: t = (1, 2)  
Output: [(), (1,), (2,), (1, 2)]
```
<details>
<summary>Solution</summary>

```python
def all_subtuples(t):
    result = [()]
    for i in range(1, 1 << len(t)):
        curr = []
        for j in range(len(t)):
            if i & (1 << j):
                curr.append(t[j])
        result.append(tuple(curr))
    return sorted(result, key=lambda x: (len(x), x))
```

</details>

### 28. Find Tuple with Maximum Sum
**Problem**: Write a Python function to find the tuple with the maximum sum from a list of tuples.  
Example:  
```
Input: tuples = [(1, 2), (3, 4), (1, 1)]  
Output: (3, 4)
```
<details>
<summary>Solution</summary>

```python
def max_sum_tuple(tuples):
    return max(tuples, key=sum, default=None)
```

</details>

### 29. Find Tuple with Minimum Sum
**Problem**: Write a Python function to find the tuple with the minimum sum from a list of tuples.  
Example:  
```
Input: tuples = [(1, 2), (3, 4), (1, 1)]  
Output: (1, 1)
```
<details>
<summary>Solution</summary>

```python
def min_sum_tuple(tuples):
    return min(tuples, key=sum, default=None)
```

</details>

### 30. Check if Tuple is Subsequence
**Problem**: Write a Python function to check if one tuple is a subsequence of another.  
Example:  
```
Input: t1 = (1, 2), t2 = (1, 2, 3)  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_subsequence(t1, t2):
    i = j = 0
    while i < len(t1) and j < len(t2):
        if t1[i] == t2[j]:
            i += 1
        j += 1
    return i == len(t1)
```

</details>

### 31. Find All Subsequences
**Problem**: Write a Python function to find all subsequences of a tuple.  
Example:  
```
Input: t = (1, 2)  
Output: [(), (1,), (2,), (1, 2)]
```
<details>
<summary>Solution</summary>

```python
def all_subsequences(t):
    result = [()]
    for i in range(1, 1 << len(t)):
        curr = []
        for j in range(len(t)):
            if i & (1 << j):
                curr.append(t[j])
        result.append(tuple(curr))
    return sorted(result, key=lambda x: (len(x), x))
```

</details>

### 32. Find Longest Increasing Subsequence
**Problem**: Write a Python function to find the longest increasing subsequence in a tuple.  
Example:  
```
Input: t = (3, 10, 2, 1, 20)  
Output: (3, 10, 20)
```
<details>
<summary>Solution</summary>

```python
def longest_increasing_subsequence(t):
    if not t:
        return ()
    dp = [1] * len(t)
    prev = [-1] * len(t)
    max_len = 1
    max_idx = 0
    for i in range(1, len(t)):
        for j in range(i):
            if t[i] > t[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i
    result = []
    while max_idx != -1:
        result.append(t[max_idx])
        max_idx = prev[max_idx]
    return tuple(reversed(result))
```

</details>

### 33. Find All Pairs with Difference K
**Problem**: Write a Python function to find all pairs in a tuple with difference k.  
Example:  
```
Input: t = (1, 3, 5, 4), k = 2  
Output: [(1, 3), (3, 5)]
```
<details>
<summary>Solution</summary>

```python
def pairs_with_difference_k(t, k):
    seen = set()
    result = []
    for num in t:
        if num + k in seen:
            result.append((num, num + k))
        if num - k in seen:
            result.append((num - k, num))
        seen.add(num)
    return sorted(result)
```

</details>

### 34. Find Longest Consecutive Sequence
**Problem**: Write a Python function to find the longest consecutive sequence in a tuple.  
Example:  
```
Input: t = (100, 4, 200, 1, 3, 2)  
Output: (1, 2, 3, 4)
```
<details>
<summary>Solution</summary>

```python
def longest_consecutive_sequence(t):
    num_set = set(t)
    max_seq = ()
    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_seq = [num]
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_seq.append(curr_num)
            if len(curr_seq) > len(max_seq):
                max_seq = tuple(curr_seq)
    return max_seq
```

</details>

### 35. Find All Subtuples with Product K
**Problem**: Write a Python function to find all subtuples with product k.  
Example:  
```
Input: t = (1, 2, 4, 8), k = 8  
Output: [(2, 4), (8,)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_product_k(t, k):
    result = []
    for i in range(1, 1 << len(t)):
        curr = []
        curr_prod = 1
        for j in range(len(t)):
            if i & (1 << j):
                curr.append(t[j])
                curr_prod *= t[j]
        if curr_prod == k:
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 36. Find Maximum Product Subtuple
**Problem**: Write a Python function to find the subtuple with the maximum product.  
Example:  
```
Input: t = (1, -2, 3, -4)  
Output: (-2, -4)
```
<details>
<summary>Solution</summary>

```python
def max_product_subtuple(t):
    max_prod = float('-inf')
    result = None
    for i in range(1, 1 << len(t)):
        curr = []
        curr_prod = 1
        for j in range(len(t)):
            if i & (1 << j):
                curr.append(t[j])
                curr_prod *= t[j]
        if curr_prod > max_prod:
            max_prod = curr_prod
            result = tuple(curr)
    return result
```

</details>

### 37. Find All Subtuples with No Duplicates
**Problem**: Write a Python function to find all subtuples with no duplicate elements.  
Example:  
```
Input: t = (1, 2, 1)  
Output: [(), (1,), (2,), (1, 2)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_duplicates(t):
    result = [()]
    for i in range(1, 1 << len(t)):
        curr = []
        for j in range(len(t)):
            if i & (1 << j):
                curr.append(t[j])
        if len(set(curr)) == len(curr):
            result.append(tuple(curr))
    return sorted(result, key=lambda x: (len(x), x))
```

</details>

### 38. Find Longest Subtuple with No Duplicates
**Problem**: Write a Python function to find the longest subtuple with no duplicate elements.  
Example:  
```
Input: t = (1, 2, 1, 3)  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def longest_subtuple_no_duplicates(t):
    seen = {}
    max_len = 0
    result = None
    left = 0
    for right in range(len(t)):
        if t[right] in seen and seen[t[right]] >= left:
            left = seen[t[right]] + 1
        else:
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                result = t[left:right + 1]
        seen[t[right]] = right
    return result
```

</details>

### 39. Find All Subtuples with Sum in Range
**Problem**: Write a Python function to find all subtuples with sum in a given range.  
Example:  
```
Input: t = (1, 2, 3), low = 3, high = 5  
Output: [(1, 2), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_sum_in_range(t, low, high):
    result = []
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if low <= curr_sum <= high:
                result.append(tuple(curr))
        curr = []
    return sorted(result)
```

</details>

### 40. Find Maximum Length Subtuple with Sum in Range
**Problem**: Write a Python function to find the maximum length subtuple with sum in a given range.  
Example:  
```
Input: t = (1, 2, 3, 4), low = 3, high = 5  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_sum_in_range(t, low, high):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if low <= curr_sum <= high and len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

## Advanced Tuple Questions

### 41. Find All Subtuples with K Distinct Elements
**Problem**: Write a Python function to find all subtuples with exactly k distinct elements.  
Example:  
```
Input: t = (1, 2, 1, 2, 3), k = 2  
Output: [(1, 2), (2, 1), (1, 2, 1), (2, 1, 2), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def subtuples_k_distinct(t, k):
    result = []
    for i in range(len(t)):
        freq = Counter()
        for j in range(i, len(t)):
            freq[t[j]] += 1
            if len(freq) == k:
                result.append(t[i:j + 1])
            elif len(freq) > k:
                break
    return sorted(set(result))
```

</details>

### 42. Find Maximum Length Subtuple with K Distinct Elements
**Problem**: Write a Python function to find the maximum length subtuple with at most k distinct elements.  
Example:  
```
Input: t = (1, 2, 1, 2, 3), k = 2  
Output: (1, 2, 1, 2)
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def max_len_subtuple_k_distinct(t, k):
    freq = Counter()
    left = 0
    max_len = 0
    result = None
    for right in range(len(t)):
        freq[t[right]] += 1
        while len(freq) > k:
            freq[t[left]] -= 1
            if freq[t[left]] == 0:
                del freq[t[left]]
            left += 1
        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len
            result = t[left:right + 1]
    return result
```

</details>

### 43. Find All Subtuples with No Pair Sum K
**Problem**: Write a Python function to find all subtuples where no pair sums to k.  
Example:  
```
Input: t = (1, 2, 3), k = 5  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_sum_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 44. Find Maximum Length Subtuple with No Pair Sum K
**Problem**: Write a Python function to find the maximum length subtuple where no pair sums to k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 7  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_sum_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 45. Find All Subtuples with Product in Range
**Problem**: Write a Python function to find all subtuples with product in a given range.  
Example:  
```
Input: t = (1, 2, 3), low = 2, high = 6  
Output: [(1, 2), (1, 3), (2,), (3,)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_product_in_range(t, low, high):
    result = []
    for i in range(len(t)):
        curr = []
        curr_prod = 1
        for j in range(i, len(t)):
            curr_prod *= t[j]
            curr.append(t[j])
            if low <= curr_prod <= high:
                result.append(tuple(curr))
            if curr_prod > high:
                break
    return sorted(result)
```

</details>

### 46. Find Maximum Length Subtuple with Product in Range
**Problem**: Write a Python function to find the maximum length subtuple with product in a given range.  
Example:  
```
Input: t = (1, 2, 3, 4), low = 2, high = 6  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_product_in_range(t, low, high):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        curr_prod = 1
        for j in range(i, len(t)):
            curr_prod *= t[j]
            curr.append(t[j])
            if low <= curr_prod <= high and len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
            if curr_prod > high:
                break
    return result
```

</details>

### 47. Find All Subtuples with No Pair Difference K
**Problem**: Write a Python function to find all subtuples where no pair’s absolute difference equals k.  
Example:  
```
Input: t = (1, 2, 3), k = 1  
Output: [(1,), (2,), (3,)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_diff_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 48. Find Maximum Length Subtuple with No Pair Difference K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s absolute difference equals k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 1  
Output: (1, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_diff_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 49. Find All Subtuples with Sum Divisible by K
**Problem**: Write a Python function to find all subtuples with sum divisible by k.  
Example:  
```
Input: t = (4, 5, 0, -2, -3, 1), k = 5  
Output: [(4, 5, 0, -2, -3, 1), (5,), (5, 0), (0,), (-2, -3, 1)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_sum_divisible_k(t, k):
    curr_sum = 0
    sums = {0: [-1]}
    result = []
    for i, num in enumerate(t):
        curr_sum += num
        rem = ((curr_sum % k) + k) % k
        if rem in sums:
            for start in sums[rem]:
                result.append(t[start + 1:i + 1])
        sums[rem] = sums.get(rem, []) + [i]
    return sorted(result)
```

</details>

### 50. Find Maximum Length Subtuple with Sum Divisible by K
**Problem**: Write a Python function to find the maximum length subtuple with sum divisible by k.  
Example:  
```
Input: t = (4, 5, 0, -2, -3, 1), k = 5  
Output: (4, 5, 0, -2, -3, 1)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_sum_divisible_k(t, k):
    curr_sum = 0
    max_len = 0
    result = None
    sums = {0: -1}
    for i, num in enumerate(t):
        curr_sum += num
        rem = ((curr_sum % k) + k) % k
        if rem in sums:
            length = i - sums[rem]
            if length > max_len:
                max_len = length
                result = t[sums[rem] + 1:i + 1]
        if rem not in sums:
            sums[rem] = i
    return result
```

</details>

### 51. Find All Subtuples with No Pair Product K
**Problem**: Write a Python function to find all subtuples where no pair’s product equals k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 6  
Output: [(1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_product_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num * t[j] == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 52. Find Maximum Length Subtuple with No Pair Product K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s product equals k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 6  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_product_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num * t[j] == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 53. Find All Subtuples with K Distinct Elements in Range
**Problem**: Write a Python function to find all subtuples with exactly k distinct elements in a given length range.  
Example:  
```
Input: t = (1, 2, 1, 2, 3), k = 2, low = 2, high = 3  
Output: [(1, 2), (2, 1), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
from collections import Counter
def subtuples_k_distinct_in_range(t, k, low, high):
    result = []
    for i in range(len(t)):
        freq = Counter()
        for j in range(i, len(t)):
            freq[t[j]] += 1
            length = j - i + 1
            if len(freq) == k and low <= length <= high:
                result.append(t[i:j + 1])
            elif len(freq) > k:
                break
    return sorted(set(result))
```

</details>

### 54. Find All Subtuples with Sum Greater Than K
**Problem**: Write a Python function to find all subtuples with sum greater than k.  
Example:  
```
Input: t = (1, 2, 3), k = 3  
Output: [(1, 2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_sum_greater_k(t, k):
    result = []
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if curr_sum > k:
                result.append(tuple(curr))
    return sorted(result)
```

</details>

### 55. Find Maximum Length Subtuple with Sum Greater Than K
**Problem**: Write a Python function to find the maximum length subtuple with sum greater than k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 5  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_sum_greater_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if curr_sum > k and len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 56. Find All Subtuples with No Pair Sum in Range
**Problem**: Write a Python function to find all subtuples where no pair’s sum is in a given range.  
Example:  
```
Input: t = (1, 2, 3), low = 5, high = 7  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_sum_in_range(t, low, high):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                sum_val = num + t[j]
                if low <= sum_val <= high:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 57. Find Maximum Length Subtuple with No Pair Sum in Range
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s sum is in a given range.  
Example:  
```
Input: t = (1, 2, 3, 4), low = 7, high = 9  
Output: (1, 2, 3, 4)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_sum_in_range(t, low, high):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                sum_val = num + t[j]
                if low <= sum_val <= high:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 58. Find All Subtuples with No Pair Product in Range
**Problem**: Write a Python function to find all subtuples where no pair’s product is in a given range.  
Example:  
```
Input: t = (1, 2, 3), low = 6, high = 9  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_product_in_range(t, low, high):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                prod = num * t[j]
                if low <= prod <= high:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 59. Find Maximum Length Subtuple with No Pair Product in Range
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s product is in a given range.  
Example:  
```
Input: t = (1, 2, 3, 4), low = 6, high = 9  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_product_in_range(t, low, high):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                prod = num * t[j]
                if low <= prod <= high:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 60. Find All Subtuples with No Pair Difference in Range
**Problem**: Write a Python function to find all subtuples where no pair’s absolute difference is in a given range.  
Example:  
```
Input: t = (1, 2, 3), low = 2, high = 3  
Output: [(1,), (2,), (3,)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_diff_in_range(t, low, high):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                diff = abs(num - t[j])
                if low <= diff <= high:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 61. Find Maximum Length Subtuple with No Pair Difference in Range
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s absolute difference is in a given range.  
Example:  
```
Input: t = (1, 2, 3, 4), low = 2, high = 3  
Output: (1, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_diff_in_range(t, low, high):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                diff = abs(num - t[j])
                if low <= diff <= high:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 62. Find All Subtuples with Sum Equal to Average
**Problem**: Write a Python function to find all subtuples whose sum equals the average of the entire tuple.  
Example:  
```
Input: t = (1, 2, 3, 4)  
Output: [(2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_sum_equal_average(t):
    avg = sum(t) / len(t)
    k = avg * len(t)
    curr_sum = 0
    sums = {0: [-1]}
    result = []
    for i, num in enumerate(t):
        curr_sum += num
        if curr_sum - k in sums:
            for start in sums[curr_sum - k]:
                sub = t[start + 1:i + 1]
                if sub and sum(sub) / len(sub) == avg:
                    result.append(sub)
        sums[curr_sum] = sums.get(curr_sum, []) + [i]
    return sorted(result)
```

</details>

### 63. Find Maximum Length Subtuple with Sum Equal to Average
**Problem**: Write a Python function to find the maximum length subtuple whose sum equals the average of the entire tuple.  
Example:  
```
Input: t = (1, 2, 3, 4)  
Output: (2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_sum_equal_average(t):
    avg = sum(t) / len(t)
    k = avg * len(t)
    curr_sum = 0
    max_len = 0
    result = None
    sums = {0: -1}
    for i, num in enumerate(t):
        curr_sum += num
        if curr_sum - k in sums:
            length = i - sums[curr_sum - k]
            sub = t[sums[curr_sum - k] + 1:i + 1]
            if sub and sum(sub) / len(sub) == avg and length > max_len:
                max_len = length
                result = sub
        sums[curr_sum] = i
    return result
```

</details>

### 64. Find All Subtuples with No Pair XOR K
**Problem**: Write a Python function to find all subtuples where no pair’s XOR equals k.  
Example:  
```
Input: t = (1, 2, 3), k = 3  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_xor_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num ^ t[j]) == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 65. Find Maximum Length Subtuple with No Pair XOR K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s XOR equals k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 7  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_xor_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num ^ t[j]) == k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 66. Find All Subtuples with Sum Less Than K
**Problem**: Write a Python function to find all subtuples with sum less than k.  
Example:  
```
Input: t = (1, 2, 3), k = 4  
Output: [(1,), (2,), (3,), (1, 2)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_sum_less_k(t, k):
    result = []
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if curr_sum < k:
                result.append(tuple(curr))
    return sorted(result)
```

</details>

### 67. Find Maximum Length Subtuple with Sum Less Than K
**Problem**: Write a Python function to find the maximum length subtuple with sum less than k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 6  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_sum_less_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if curr_sum < k and len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 68. Find All Subtuples with No Pair Sum Divisible by K
**Problem**: Write a Python function to find all subtuples where no pair’s sum is divisible by k.  
Example:  
```
Input: t = (1, 2, 3), k = 5  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_sum_divisible_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num + t[j]) % k == 0:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 69. Find Maximum Length Subtuple with No Pair Sum Divisible by K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s sum is divisible by k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 5  
Output: (1, 2, 3, 4)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_sum_divisible_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num + t[j]) % k == 0:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 70. Find All Subtuples with No Pair Difference Divisible by K
**Problem**: Write a Python function to find all subtuples where no pair’s absolute difference is divisible by k.  
Example:  
```
Input: t = (1, 2, 3), k = 2  
Output: [(1,), (2,), (3,)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_diff_divisible_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) % k == 0:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 71. Find Maximum Length Subtuple with No Pair Difference Divisible by K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s absolute difference is divisible by k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 2  
Output: (1, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_diff_divisible_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) % k == 0:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 72. Find All Subtuples with Sum Equal to Product
**Problem**: Write a Python function to find all subtuples where the sum equals the product.  
Example:  
```
Input: t = (1, 2, 2)  
Output: [(2, 2)]
```
<details>
<summary>Solution</summary>

```python
from math import prod
def subtuples_sum_equal_product(t):
    result = []
    for i in range(len(t)):
        curr = []
        curr_sum = 0
        curr_prod = 1
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr_prod *= t[j]
            curr.append(t[j])
            if curr_sum == curr_prod:
                result.append(tuple(curr))
    return sorted(result)
```

</details>

### 73. Find Maximum Length Subtuple with Sum Equal to Product
**Problem**: Write a Python function to find the maximum length subtuple where the sum equals the product.  
Example:  
```
Input: t = (1, 2, 2, 3)  
Output: (2, 2)
```
<details>
<summary>Solution</summary>

```python
from math import prod
def max_len_subtuple_sum_equal_product(t):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        curr_sum = 0
        curr_prod = 1
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr_prod *= t[j]
            curr.append(t[j])
            if curr_sum == curr_prod and len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 74. Find All Subtuples with No Pair Sum in Forbidden Set
**Problem**: Write a Python function to find all subtuples where no pair’s sum is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3), forbidden = {5, 7}  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_sum_forbidden(t, forbidden):
    forbidden = set(forbidden)
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 75. Find Maximum Length Subtuple with No Pair Sum in Forbidden Set
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s sum is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3, 4), forbidden = {7, 9}  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_sum_forbidden(t, forbidden):
    forbidden = set(forbidden)
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 76. Find All Subtuples with No Pair Product in Forbidden Set
**Problem**: Write a Python function to find all subtuples where no pair’s product is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3, 4), forbidden = {6, 8}  
Output: [(1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_product_forbidden(t, forbidden):
    forbidden = set(forbidden)
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num * t[j] in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 77. Find Maximum Length Subtuple with No Pair Product in Forbidden Set
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s product is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3, 4), forbidden = {6, 8}  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_product_forbidden(t, forbidden):
    forbidden = set(forbidden)
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num * t[j] in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 78. Find All Subtuples with No Pair XOR in Forbidden Set
**Problem**: Write a Python function to find all subtuples where no pair’s XOR is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3), forbidden = {3, 7}  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_xor_forbidden(t, forbidden):
    forbidden = set(forbidden)
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num ^ t[j]) in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 79. Find Maximum Length Subtuple with No Pair XOR in Forbidden Set
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s XOR is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3, 4), forbidden = {7, 9}  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_xor_forbidden(t, forbidden):
    forbidden = set(forbidden)
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num ^ t[j]) in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 80. Find All Subtuples with Sum in Top K Percentile
**Problem**: Write a Python function to find all subtuples whose sum is in the top k percentile of all possible subtuple sums.  
Example:  
```
Input: t = (1, 2, 3), k = 50  
Output: [(1, 2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_top_k_percentile(t, k):
    sums = []
    for i in range(len(t)):
        curr_sum = 0
        for j in range(i, len(t)):
            curr_sum += t[j]
            sums.append((curr_sum, t[i:j + 1]))
    sums.sort(reverse=True)
    threshold_idx = int(len(sums) * (1 - k / 100))
    threshold = sums[threshold_idx][0] if threshold_idx < len(sums) else sums[-1][0]
    return sorted([tup for s, tup in sums if s >= threshold])
```

</details>

### 81. Find Maximum Length Subtuple with Sum in Top K Percentile
**Problem**: Write a Python function to find the maximum length subtuple whose sum is in the top k percentile of all possible subtuple sums.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 50  
Output: (1, 2, 3, 4)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_top_k_percentile(t, k):
    sums = []
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            sums.append((curr_sum, tuple(curr)))
    sums.sort(reverse=True)
    threshold_idx = int(len(sums) * (1 - k / 100))
    threshold = sums[threshold_idx][0] if threshold_idx < len(sums) else sums[-1][0]
    max_len = 0
    result = None
    for s, tup in sums:
        if s >= threshold and len(tup) > max_len:
            max_len = len(tup)
            result = tup
    return result
```

</details>

### 82. Find All Subtuples with No Pair Sum Equal to Average
**Problem**: Write a Python function to find all subtuples where no pair’s sum equals the average of the entire tuple.  
Example:  
```
Input: t = (1, 2, 3)  
Output: [(1,), (2,), (3,), (1, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_sum_equal_average(t):
    avg = sum(t) / len(t)
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] == avg:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 83. Find Maximum Length Subtuple with No Pair Sum Equal to Average
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s sum equals the average of the entire tuple.  
Example:  
```
Input: t = (1, 2, 3, 4)  
Output: (1, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_sum_equal_average(t):
    avg = sum(t) / len(t)
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] == avg:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 84. Find All Subtuples with Sum Greater Than Average
**Problem**: Write a Python function to find all subtuples whose sum is greater than the average of the entire tuple.  
Example:  
```
Input: t = (1, 2, 3)  
Output: [(1, 2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_sum_greater_average(t):
    avg = sum(t) / len(t)
    result = []
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if curr_sum > avg * len(curr):
                result.append(tuple(curr))
    return sorted(result)
```

</details>

### 85. Find Maximum Length Subtuple with Sum Greater Than Average
**Problem**: Write a Python function to find the maximum length subtuple whose sum is greater than the average of the entire tuple.  
Example:  
```
Input: t = (1, 2, 3, 4)  
Output: (1, 2, 3, 4)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_sum_greater_average(t):
    avg = sum(t) / len(t)
    max_len = 0
    result = None
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            if curr_sum > avg * len(curr) and len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 86. Find All Subtuples with No Pair Product Divisible by K
**Problem**: Write a Python function to find all subtuples where no pair’s product is divisible by k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 6  
Output: [(1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_product_divisible_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num * t[j]) % k == 0:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 87. Find Maximum Length Subtuple with No Pair Product Divisible by K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s product is divisible by k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 6  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_product_divisible_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if (num * t[j]) % k == 0:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 88. Find All Subtuples with No Pair Difference in Forbidden Set
**Problem**: Write a Python function to find all subtuples where no pair’s absolute difference is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3), forbidden = {2, 3}  
Output: [(1,), (2,), (3,)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_diff_forbidden(t, forbidden):
    forbidden = set(forbidden)
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 89. Find Maximum Length Subtuple with No Pair Difference in Forbidden Set
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s absolute difference is in a forbidden set.  
Example:  
```
Input: t = (1, 2, 3, 4), forbidden = {2, 3}  
Output: (1, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_diff_forbidden(t, forbidden):
    forbidden = set(forbidden)
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 90. Find All Subtuples with Sum in Bottom K Percentile
**Problem**: Write a Python function to find all subtuples whose sum is in the bottom k percentile of all possible subtuple sums.  
Example:  
```
Input: t = (1, 2, 3), k = 50  
Output: [(1,), (2,), (3,), (1, 2)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_bottom_k_percentile(t, k):
    sums = []
    for i in range(len(t)):
        curr_sum = 0
        for j in range(i, len(t)):
            curr_sum += t[j]
            sums.append((curr_sum, t[i:j + 1]))
    sums.sort()
    threshold_idx = int(len(sums) * k / 100)
    threshold = sums[threshold_idx - 1][0] if threshold_idx > 0 else sums[0][0]
    return sorted([tup for s, tup in sums if s <= threshold])
```

</details>

### 91. Find Maximum Length Subtuple with Sum in Bottom K Percentile
**Problem**: Write a Python function to find the maximum length subtuple whose sum is in the bottom k percentile of all possible subtuple sums.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 50  
Output: (1, 2)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_bottom_k_percentile(t, k):
    sums = []
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            sums.append((curr_sum, tuple(curr)))
    sums.sort()
    threshold_idx = int(len(sums) * k / 100)
    threshold = sums[threshold_idx - 1][0] if threshold_idx > 0 else sums[0][0]
    max_len = 0
    result = None
    for s, tup in sums:
        if s <= threshold and len(tup) > max_len:
            max_len = len(tup)
            result = tup
    return result
```

</details>

### 92. Find All Subtuples with No Pair Sum Greater Than K
**Problem**: Write a Python function to find all subtuples where no pair’s sum is greater than k.  
Example:  
```
Input: t = (1, 2, 3), k = 4  
Output: [(1,), (2,), (3,), (1, 2)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_sum_greater_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] > k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 93. Find Maximum Length Subtuple with No Pair Sum Greater Than K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s sum is greater than k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 5  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_sum_greater_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] > k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 94. Find All Subtuples with No Pair Product Greater Than K
**Problem**: Write a Python function to find all subtuples where no pair’s product is greater than k.  
Example:  
```
Input: t = (1, 2, 3), k = 4  
Output: [(1,), (2,), (3,), (1, 2)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_product_greater_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num * t[j] > k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 95. Find Maximum Length Subtuple with No Pair Product Greater Than K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s product is greater than k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 6  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_product_greater_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num * t[j] > k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 96. Find All Subtuples with No Pair Difference Greater Than K
**Problem**: Write a Python function to find all subtuples where no pair’s absolute difference is greater than k.  
Example:  
```
Input: t = (1, 2, 3), k = 1  
Output: [(1,), (2,), (3,), (1, 2), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_diff_greater_k(t, k):
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) > k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>

### 97. Find Maximum Length Subtuple with No Pair Difference Greater Than K
**Problem**: Write a Python function to find the maximum length subtuple where no pair’s absolute difference is greater than k.  
Example:  
```
Input: t = (1, 2, 3, 4), k = 1  
Output: (1, 2)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_no_pair_diff_greater_k(t, k):
    max_len = 0
    result = None
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if abs(num - t[j]) > k:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            if len(curr) > max_len:
                max_len = len(curr)
                result = tuple(curr)
    return result
```

</details>

### 98. Find All Subtuples with Sum Equal to Median
**Problem**: Write a Python function to find all subtuples whose sum equals the median of all possible subtuple sums.  
Example:  
```
Input: t = (1, 2, 3)  
Output: [(1, 2), (3,)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_sum_equal_median(t):
    sums = []
    for i in range(len(t)):
        curr_sum = 0
        for j in range(i, len(t)):
            curr_sum += t[j]
            sums.append((curr_sum, t[i:j + 1]))
    sums.sort()
    median_idx = len(sums) // 2
    median = sums[median_idx][0]
    return sorted([tup for s, tup in sums if s == median])
```

</details>

### 99. Find Maximum Length Subtuple with Sum Equal to Median
**Problem**: Write a Python function to find the maximum length subtuple whose sum equals the median of all possible subtuple sums.  
Example:  
```
Input: t = (1, 2, 3, 4)  
Output: (1, 2, 3)
```
<details>
<summary>Solution</summary>

```python
def max_len_subtuple_sum_equal_median(t):
    sums = []
    for i in range(len(t)):
        curr_sum = 0
        curr = []
        for j in range(i, len(t)):
            curr_sum += t[j]
            curr.append(t[j])
            sums.append((curr_sum, tuple(curr)))
    sums.sort()
    median_idx = len(sums) // 2
    median = sums[median_idx][0]
    max_len = 0
    result = None
    for s, tup in sums:
        if s == median and len(tup) > max_len:
            max_len = len(tup)
            result = tup
    return result
```

</details>

### 100. Find All Subtuples with No Pair Sum in Forbidden Tuple
**Problem**: Write a Python function to find all subtuples where no pair’s sum is in a forbidden tuple.  
Example:  
```
Input: t = (1, 2, 3), forbidden = (5, 7)  
Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
```
<details>
<summary>Solution</summary>

```python
def subtuples_no_pair_sum_forbidden_tuple(t, forbidden):
    forbidden = set(forbidden)
    result = []
    for i in range(len(t)):
        curr = []
        valid = True
        for j in range(i, len(t)):
            for num in curr:
                if num + t[j] in forbidden:
                    valid = False
                    break
            if not valid:
                break
            curr.append(t[j])
            result.append(tuple(curr))
    return sorted(result)
```

</details>