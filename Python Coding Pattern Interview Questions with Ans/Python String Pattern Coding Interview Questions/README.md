# Python String Patterns Interview Questions

This README provides **100 Python string manipulation questions** designed for AI/ML students preparing for technical interviews. The questions focus on string-related problems (e.g., transformations, validations, substring searches) commonly asked in Python coding interviews. They are categorized into **Basic**, **Intermediate**, and **Advanced** levels, covering a range of string operations like reversals, anagrams, substring searches, and complex algorithms. Each question includes a problem statement, with the solution hidden in a `<details>` tag to encourage users to attempt the problem before viewing the answer. This format supports hands-on practice and aligns with interview preparation for AI/ML roles.

## Basic String Questions

### 1. String Compression
**Problem**: Write a Python function to compress a string by counting consecutive character occurrences.  
Example:  
```
Input: "aabbcccadd"  
Output: "a2b2c3a1d2"
```
<details>
<summary>Solution</summary>

```python
def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    result.append(current_char + str(count))
    return "".join(result)
```

</details>

### 2. Reverse String
**Problem**: Write a Python function to reverse a string.  
Example:  
```
Input: "hello"  
Output: "olleh"
```
<details>
<summary>Solution</summary>

```python
def reverse_string(s):
    return s[::-1]
```

</details>

### 3. Check Palindrome
**Problem**: Write a Python function to check if a string is a palindrome, ignoring non-alphanumeric characters and case.  
Example:  
```
Input: "A man, a plan, a canal: Panama"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

</details>

### 4. First Unique Character
**Problem**: Write a Python function to find the index of the first non-repeating character in a string. Return -1 if none exists.  
Example:  
```
Input: "leetcode"  
Output: 0
```
<details>
<summary>Solution</summary>

```python
def first_unique_char(s):
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    for i, c in enumerate(s):
        if char_count[c] == 1:
            return i
    return -1
```

</details>

### 5. Valid Anagram
**Problem**: Write a Python function to check if two strings are anagrams of each other.  
Example:  
```
Input: s = "anagram", t = "nagaram"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    for c in t:
        char_count[c] = char_count.get(c, 0) - 1
        if char_count[c] < 0:
            return False
    return all(count == 0 for count in char_count.values())
```

</details>

### 6. String to Integer (atoi)
**Problem**: Write a Python function to convert a string to a 32-bit signed integer, handling spaces, signs, and overflow.  
Example:  
```
Input: "   -42"  
Output: -42
```
<details>
<summary>Solution</summary>

```python
def atoi(s):
    s = s.strip()
    if not s:
        return 0
    sign = 1
    start = 0
    if s[0] in "+-":
        sign = -1 if s[0] == "-" else 1
        start = 1
    result = 0
    for i in range(start, len(s)):
        if not s[i].isdigit():
            break
        result = result * 10 + int(s[i])
    result *= sign
    return max(min(result, 2**31 - 1), -2**31)
```

</details>

### 7. Count Vowels
**Problem**: Write a Python function to count the number of vowels in a string.  
Example:  
```
Input: "hello"  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for c in s if c in vowels)
```

</details>

### 8. Check if String Contains Only Digits
**Problem**: Write a Python function to check if a string contains only digits.  
Example:  
```
Input: "12345"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_digit_only(s):
    return s.isdigit()
```

</details>

### 9. Capitalize First Letter
**Problem**: Write a Python function to capitalize the first letter of each word in a string.  
Example:  
```
Input: "hello world"  
Output: "Hello World"
```
<details>
<summary>Solution</summary>

```python
def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())
```

</details>

### 10. Remove Spaces
**Problem**: Write a Python function to remove all spaces from a string.  
Example:  
```
Input: "  hello   world  "  
Output: "helloworld"
```
<details>
<summary>Solution</summary>

```python
def remove_spaces(s):
    return "".join(s.split())
```

</details>

### 11. Check Substring
**Problem**: Write a Python function to check if a string contains a specific substring.  
Example:  
```
Input: s = "hello world", substr = "world"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def contains_substring(s, substr):
    return substr in s
```

</details>

### 12. Reverse Words in a String
**Problem**: Write a Python function to reverse the order of words in a string, removing extra spaces.  
Example:  
```
Input: "  hello   world  "  
Output: "world hello"
```
<details>
<summary>Solution</summary>

```python
def reverse_words(s):
    words = [w for w in s.split() if w]
    return " ".join(words[::-1])
```

</details>

### 13. Count Character Frequency
**Problem**: Write a Python function to count the frequency of each character in a string.  
Example:  
```
Input: "hello"  
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
<details>
<summary>Solution</summary>

```python
def char_frequency(s):
    return {c: s.count(c) for c in s}
```

</details>

### 14. Check if Strings are Equal Ignoring Case
**Problem**: Write a Python function to check if two strings are equal, ignoring case.  
Example:  
```
Input: s1 = "Hello", s2 = "hello"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def are_equal_ignore_case(s1, s2):
    return s1.lower() == s2.lower()
```

</details>

### 15. Replace Substring
**Problem**: Write a Python function to replace all occurrences of a substring with another substring.  
Example:  
```
Input: s = "hello world", old = "world", new = "python"  
Output: "hello python"
```
<details>
<summary>Solution</summary>

```python
def replace_substring(s, old, new):
    return s.replace(old, new)
```

</details>

### 16. Longest Common Prefix
**Problem**: Write a Python function to find the longest common prefix among a list of strings.  
Example:  
```
Input: ["flower", "flow", "flight"]  
Output: "fl"
```
<details>
<summary>Solution</summary>

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, c in enumerate(shortest):
        for s in strs:
            if s[i] != c:
                return shortest[:i]
    return shortest
```

</details>

### 17. Check if String is Numeric
**Problem**: Write a Python function to check if a string represents a valid number (integer or float).  
Example:  
```
Input: "123.45"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
```

</details>

### 18. Swap Case
**Problem**: Write a Python function to swap the case of each character in a string.  
Example:  
```
Input: "Hello World"  
Output: "hELLO wORLD"
```
<details>
<summary>Solution</summary>

```python
def swap_case(s):
    return s.swapcase()
```

</details>

### 19. Count Words
**Problem**: Write a Python function to count the number of words in a string.  
Example:  
```
Input: "  hello   world  python  "  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def count_words(s):
    return len([w for w in s.split() if w])
```

</details>

### 20. Check if String is Alphanumeric
**Problem**: Write a Python function to check if a string contains only alphanumeric characters.  
Example:  
```
Input: "Hello123"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_alphanumeric(s):
    return s.isalnum()
```

</details>

### 21. Find First Occurrence
**Problem**: Write a Python function to find the index of the first occurrence of a character in a string.  
Example:  
```
Input: s = "hello", c = "l"  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def first_occurrence(s, c):
    return s.find(c)
```

</details>

### 22. Remove Duplicates
**Problem**: Write a Python function to remove duplicate characters from a string while maintaining order.  
Example:  
```
Input: "hello"  
Output: "helo"
```
<details>
<summary>Solution</summary>

```python
def remove_duplicates(s):
    seen = set()
    return "".join(c for c in s if not (c in seen or seen.add(c)))
```

</details>

### 23. Check if String is Empty
**Problem**: Write a Python function to check if a string is empty or contains only whitespace.  
Example:  
```
Input: "   "  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_empty(s):
    return not s.strip()
```

</details>

### 24. Split String by Delimiter
**Problem**: Write a Python function to split a string by a given delimiter.  
Example:  
```
Input: s = "a,b,c", delimiter = ","  
Output: ["a", "b", "c"]
```
<details>
<summary>Solution</summary>

```python
def split_string(s, delimiter):
    return s.split(delimiter)
```

</details>

### 25. Reverse Characters in Words
**Problem**: Write a Python function to reverse the characters in each word of a string.  
Example:  
```
Input: "hello world"  
Output: "olleh dlrow"
```
<details>
<summary>Solution</summary>

```python
def reverse_words_chars(s):
    return " ".join(word[::-1] for word in s.split())
```

</details>

### 26. Check if String Starts with Prefix
**Problem**: Write a Python function to check if a string starts with a given prefix.  
Example:  
```
Input: s = "hello world", prefix = "hello"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def starts_with(s, prefix):
    return s.startswith(prefix)
```

</details>

### 27. Check if String Ends with Suffix
**Problem**: Write a Python function to check if a string ends with a given suffix.  
Example:  
```
Input: s = "hello world", suffix = "world"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def ends_with(s, suffix):
    return s.endswith(suffix)
```

</details>

### 28. Convert String to Title Case
**Problem**: Write a Python function to convert a string to title case.  
Example:  
```
Input: "hello world"  
Output: "Hello World"
```
<details>
<summary>Solution</summary>

```python
def to_title_case(s):
    return s.title()
```

</details>

### 29. Find Last Occurrence
**Problem**: Write a Python function to find the index of the last occurrence of a character in a string.  
Example:  
```
Input: s = "hello", c = "l"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def last_occurrence(s, c):
    return s.rfind(c)
```

</details>

### 30. Remove Specific Character
**Problem**: Write a Python function to remove all occurrences of a specific character from a string.  
Example:  
```
Input: s = "hello", c = "l"  
Output: "heo"
```
<details>
<summary>Solution</summary>

```python
def remove_char(s, c):
    return s.replace(c, "")
```

</details>

### 31. Check if String is Uppercase
**Problem**: Write a Python function to check if a string is entirely uppercase.  
Example:  
```
Input: "HELLO"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_uppercase(s):
    return s.isupper()
```

</details>

### 32. Check if String is Lowercase
**Problem**: Write a Python function to check if a string is entirely lowercase.  
Example:  
```
Input: "hello"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_lowercase(s):
    return s.islower()
```

</details>

### 33. Trim Leading Whitespace
**Problem**: Write a Python function to remove leading whitespace from a string.  
Example:  
```
Input: "   hello"  
Output: "hello"
```
<details>
<summary>Solution</summary>

```python
def trim_leading(s):
    return s.lstrip()
```

</details>

### 34. Trim Trailing Whitespace
**Problem**: Write a Python function to remove trailing whitespace from a string.  
Example:  
```
Input: "hello   "  
Output: "hello"
```
<details>
<summary>Solution</summary>

```python
def trim_trailing(s):
    return s.rstrip()
```

</details>

## Intermediate String Questions

### 35. Longest Substring Without Repeating Characters
**Problem**: Write a Python function to find the length of the longest substring without repeating characters.  
Example:  
```
Input: "abcabcbb"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def length_of_longest_substring(s):
    seen = {}
    max_len = 0
    start = 0
    for end, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        else:
            max_len = max(max_len, end - start + 1)
        seen[c] = end
    return max_len
```

</details>

### 36. Group Anagrams
**Problem**: Write a Python function to group all anagrams in a list of strings.  
Example:  
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]  
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```
<details>
<summary>Solution</summary>

```python
def group_anagrams(strs):
    anagram_dict = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagram_dict.setdefault(sorted_s, []).append(s)
    return list(anagram_dict.values())
```

</details>

### 37. Valid Parentheses
**Problem**: Write a Python function to check if a string of parentheses is valid.  
Example:  
```
Input: "()[]{}"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_valid_parentheses(s):
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in brackets.values():
            stack.append(c)
        elif c in brackets:
            if not stack or stack.pop() != brackets[c]:
                return False
    return len(stack) == 0
```

</details>

### 38. Longest Palindromic Substring
**Problem**: Write a Python function to find the longest palindromic substring in a string.  
Example:  
```
Input: "babad"  
Output: "bab" or "aba"
```
<details>
<summary>Solution</summary>

```python
def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    start, end = 0, 0
    for i in range(len(s)):
        l1, r1 = expand_around_center(i, i)
        l2, r2 = expand_around_center(i, i + 1)
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end + 1]
```

</details>

### 39. Implement strStr()
**Problem**: Write a Python function to find the index of the first occurrence of needle in haystack, or -1 if not found.  
Example:  
```
Input: haystack = "hello", needle = "ll"  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def str_str(haystack, needle):
    if not needle:
        return 0
    n = len(needle)
    for i in range(len(haystack) - n + 1):
        if haystack[i:i+n] == needle:
            return i
    return -1
```

</details>

### 40. Count and Say
**Problem**: Write a Python function to generate the n-th term of the count-and-say sequence.  
Example:  
```
Input: n = 4  
Output: "1211"
```
<details>
<summary>Solution</summary>

```python
def count_and_say(n):
    if n == 1:
        return "1"
    s = "1"
    for _ in range(n - 1):
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                result.append(str(count) + s[i-1])
                count = 1
        result.append(str(count) + s[-1])
        s = "".join(result)
    return s
```

</details>

### 41. Add Binary
**Problem**: Write a Python function to add two binary strings and return the result as a binary string.  
Example:  
```
Input: a = "11", b = "1"  
Output: "100"
```
<details>
<summary>Solution</summary>

```python
def add_binary(a, b):
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2
    return "".join(result[::-1])
```

</details>

### 42. Minimum Window Substring
**Problem**: Write a Python function to find the smallest substring in s that contains all characters of t.  
Example:  
```
Input: s = "ADOBECODEBANC", t = "ABC"  
Output: "BANC"
```
<details>
<summary>Solution</summary>

```python
def min_window(s, t):
    if not t or not s:
        return ""
    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1
    required = len(t_count)
    formed = 0
    window_counts = {}
    left = right = 0
    min_len = float('inf')
    min_window_sub = ""
    
    while right < len(s):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        while left <= right and formed == required:
            c = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_sub = s[left:right + 1]
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            left += 1
        right += 1
    return min_window_sub
```

</details>

### 43. Valid Palindrome II
**Problem**: Write a Python function to check if a string can be a palindrome by removing at most one character.  
Example:  
```
Input: "aba"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def valid_palindrome_ii(s):
    def check_palindrome(left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return check_palindrome(left + 1, right, s) or check_palindrome(left, right - 1, s)
        left += 1
        right -= 1
    return True
```

</details>

### 44. Word Break
**Problem**: Write a Python function to check if a string can be segmented into words from a dictionary.  
Example:  
```
Input: s = "leetcode", wordDict = ["leet", "code"]  
Output: True
```
<details>
<summary>Solution</summary>

```python
def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    word_set = set(wordDict)
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]
```

</details>

### 45. Decode String
**Problem**: Write a Python function to decode a string with nested brackets, where k[str] means str repeated k times.  
Example:  
```
Input: "3[a]2[bc]"  
Output: "aaabcbc"
```
<details>
<summary>Solution</summary>

```python
def decode_string(s):
    stack = []
    curr_string = ""
    curr_number = 0
    
    for c in s:
        if c.isdigit():
            curr_number = curr_number * 10 + int(c)
        elif c == "[":
            stack.append((curr_string, curr_number))
            curr_string = ""
            curr_number = 0
        elif c == "]":
            prev_string, num = stack.pop()
            curr_string = prev_string + num * curr_string
        else:
            curr_string += c
    return curr_string
```

</details>

### 46. Longest Repeating Character Replacement
**Problem**: Write a Python function to find the length of the longest substring with at most k character replacements.  
Example:  
```
Input: s = "ABAB", k = 2  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def character_replacement(s, k):
    count = {}
    max_len = 0
    left = 0
    max_count = 0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        if right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 47. Group Shifted Strings
**Problem**: Write a Python function to group strings that are shifted versions of each other.  
Example:  
```
Input: ["abc", "bcd", "acef", "xyz", "az", "ba"]  
Output: [["abc", "bcd", "xyz"], ["az", "ba"], ["acef"]]
```
<details>
<summary>Solution</summary>

```python
def group_shifted_strings(strs):
    def get_shift_key(s):
        if not s:
            return ""
        key = []
        for i in range(1, len(s)):
            diff = (ord(s[i]) - ord(s[i-1])) % 26
            key.append(str(diff))
        return ",".join(key)
    
    groups = {}
    for s in strs:
        key = get_shift_key(s)
        groups.setdefault(key, []).append(s)
    return list(groups.values())
```

</details>

### 48. Is Subsequence
**Problem**: Write a Python function to check if s is a subsequence of t.  
Example:  
```
Input: s = "abc", t = "ahbgdc"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_subsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
```

</details>

### 49. Longest Common Subsequence
**Problem**: Write a Python function to find the length of the longest common subsequence between two strings.  
Example:  
```
Input: text1 = "abcde", text2 = "ace"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

</details>

### 50. Roman to Integer
**Problem**: Write a Python function to convert a Roman numeral string to an integer.  
Example:  
```
Input: "MCMXCIV"  
Output: 1994
```
<details>
<summary>Solution</summary>

```python
def roman_to_int(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    for c in s[::-1]:
        curr = roman[c]
        if curr >= prev:
            result += curr
        else:
            result -= curr
        prev = curr
    return result
```

</details>

### 51. Integer to Roman
**Problem**: Write a Python function to convert an integer to a Roman numeral string.  
Example:  
```
Input: 1994  
Output: "MCMXCIV"
```
<details>
<summary>Solution</summary>

```python
def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for v, s in zip(val, syms):
        while num >= v:
            result += s
            num -= v
    return result
```

</details>

### 52. Reverse Vowels
**Problem**: Write a Python function to reverse only the vowels in a string.  
Example:  
```
Input: "hello"  
Output: "holle"
```
<details>
<summary>Solution</summary>

```python
def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)
```

</details>

### 53. Valid Number
**Problem**: Write a Python function to check if a string is a valid number (including decimals and scientific notation).  
Example:  
```
Input: "2e10"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_valid_number(s):
    s = s.strip()
    try:
        float(s)
        return True
    except ValueError:
        return False
```

</details>

### 54. Longest Word in Dictionary
**Problem**: Write a Python function to find the longest word in a dictionary that can be formed by a string's characters.  
Example:  
```
Input: s = "abpcplea", d = ["ale", "apple", "monkey", "plea"]  
Output: "apple"
```
<details>
<summary>Solution</summary>

```python
def find_longest_word(s, d):
    def can_form(word, s_chars):
        s_iter = iter(s_chars)
        return all(c in s_iter for c in word)
    
    s_chars = list(s)
    max_word = ""
    for word in sorted(d, key=lambda x: (-len(x), x)):
        if len(word) <= len(s) and can_form(word, s_chars):
            return word
    return max_word
```

</details>

### 55. Compare Version Numbers
**Problem**: Write a Python function to compare two version numbers. Return 1 if version1 > version2, -1 if version1 < version2, else 0.  
Example:  
```
Input: version1 = "1.01", version2 = "1.001"  
Output: 0
```
<details>
<summary>Solution</summary>

```python
def compare_version(version1, version2):
    v1_parts = list(map(int, version1.split(".")))
    v2_parts = list(map(int, version2.split(".")))
    max_len = max(len(v1_parts), len(v2_parts))
    v1_parts += [0] * (max_len - len(v1_parts))
    v2_parts += [0] * (max_len - len(v2_parts))
    for i in range(max_len):
        if v1_parts[i] > v2_parts[i]:
            return 1
        elif v1_parts[i] < v2_parts[i]:
            return -1
    return 0
```

</details>

### 56. Simplify Path
**Problem**: Write a Python function to simplify a Unix-style file path.  
Example:  
```
Input: "/home//foo/"  
Output: "/home/foo"
```
<details>
<summary>Solution</summary>

```python
def simplify_path(path):
    stack = []
    for part in path.split("/"):
        if part == "." or not part:
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)
```

</details>

### 57. Longest Valid Parentheses
**Problem**: Write a Python function to find the length of the longest valid parentheses substring.  
Example:  
```
Input: "(()"  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len
```

</details>

### 58. Find All Anagrams in a String
**Problem**: Write a Python function to find all starting indices of anagrams of p in s.  
Example:  
```
Input: s = "cbaebabacd", p = "abc"  
Output: [0, 6]
```
<details>
<summary>Solution</summary>

```python
def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    p_count = {}
    for c in p:
        p_count[c] = p_count.get(c, 0) + 1
    window_count = {}
    result = []
    for i in range(len(p)):
        window_count[s[i]] = window_count.get(s[i], 0) + 1
    if window_count == p_count:
        result.append(0)
    for i in range(len(p), len(s)):
        window_count[s[i]] = window_count.get(s[i], 0) + 1
        window_count[s[i - len(p)]] -= 1
        if window_count[s[i - len(p)]] == 0:
            del window_count[s[i - len(p)]]
        if window_count == p_count:
            result.append(i - len(p) + 1)
    return result
```

</details>

### 59. String to Integer (Binary)
**Problem**: Write a Python function to convert a binary string to an integer.  
Example:  
```
Input: "1010"  
Output: 10
```
<details>
<summary>Solution</summary>

```python
def binary_to_int(s):
    return int(s, 2)
```

</details>

### 60. String to Integer (Hex)
**Problem**: Write a Python function to convert a hexadecimal string to an integer.  
Example:  
```
Input: "1A"  
Output: 26
```
<details>
<summary>Solution</summary>

```python
def hex_to_int(s):
    return int(s, 16)
```

</details>

### 61. Check if String is Rotated
**Problem**: Write a Python function to check if one string is a rotation of another.  
Example:  
```
Input: s1 = "waterbottle", s2 = "erbottlewat"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)
```

</details>

### 62. Reverse String II
**Problem**: Write a Python function to reverse every k characters in a string.  
Example:  
```
Input: s = "abcdefg", k = 2  
Output: "bacdfeg"
```
<details>
<summary>Solution</summary>

```python
def reverse_str(s, k):
    s = list(s)
    for i in range(0, len(s), 2 * k):
        left, right = i, min(i + k - 1, len(s) - 1)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)
```

</details>

### 63. Longest Substring with At Least K Repeating Characters
**Problem**: Write a Python function to find the longest substring where every character appears at least k times.  
Example:  
```
Input: s = "ababbc", k = 2  
Output: 5
```
<details>
<summary>Solution</summary>

```python
def longest_substring_k_repeating(s, k):
    def check(s, k, start, end):
        count = {}
        for i in range(start, end):
            count[s[i]] = count.get(s[i], 0) + 1
        for i in range(start, end):
            if count[s[i]] < k:
                return max(check(s, k, start, i), check(s, k, i + 1, end))
        return end - start
    
    return check(s, k, 0, len(s))
```

</details>

### 64. Multiply Strings
**Problem**: Write a Python function to multiply two numbers given as strings.  
Example:  
```
Input: num1 = "123", num2 = "456"  
Output: "56088"
```
<details>
<summary>Solution</summary>

```python
def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10
    result = "".join(map(str, result)).lstrip("0")
    return result if result else "0"
```

</details>

### 65. Edit Distance
**Problem**: Write a Python function to find the minimum number of operations (insert, delete, replace) to convert one string to another.  
Example:  
```
Input: word1 = "horse", word2 = "ros"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    return dp[m][n]
```

</details>

### 66. Regular Expression Matching
**Problem**: Write a Python function to check if a string matches a regular expression pattern (supporting . and *).  
Example:  
```
Input: s = "aa", p = "a*"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_match(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    
    for j in range(2, len(p) + 1):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-2]
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == "*":
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))
            else:
                dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
    return dp[len(s)][len(p)]
```

</details>

## Advanced String Questions

### 67. Text Justification
**Problem**: Write a Python function to justify text by adding spaces to align words within a maximum width.  
Example:  
```
Input: words = ["This", "is", "an", "example"], maxWidth = 16  
Output: ["This    is    an", "example         "]
```
<details>
<summary>Solution</summary>

```python
def full_justify(words, maxWidth):
    result, curr_words, curr_len = [], [], 0
    for w in words:
        if curr_len + len(w) + len(curr_words) > maxWidth:
            if len(curr_words) == 1:
                result.append(curr_words[0] + " " * (maxWidth - curr_len))
            else:
                spaces = maxWidth - curr_len
                gaps = len(curr_words) - 1
                spaces_per_gap = spaces // gaps
                extra = spaces % gaps
                line = ""
                for i, word in enumerate(curr_words[:-1]):
                    line += word + " " * (spaces_per_gap + (1 if i < extra else 0))
                line += curr_words[-1]
                result.append(line)
            curr_words, curr_len = [], 0
        curr_words.append(w)
        curr_len += len(w)
    result.append(" ".join(curr_words) + " " * (maxWidth - curr_len - len(curr_words) + 1))
    return result
```

</details>

### 68. Minimum Genetic Mutation
**Problem**: Write a Python function to find the minimum number of mutations needed to change start to end using a bank.  
Example:  
```
Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]  
Output: 1
```
<details>
<summary>Solution</summary>

```python
from collections import deque
def min_mutation(start, end, bank):
    bank = set(bank)
    if end not in bank:
        return -1
    queue = deque([(start, 0)])
    seen = {start}
    chars = ['A', 'C', 'G', 'T']
    
    while queue:
        curr, steps = queue.popleft()
        if curr == end:
            return steps
        for i in range(len(curr)):
            for c in chars:
                new = curr[:i] + c + curr[i+1:]
                if new in bank and new not in seen:
                    seen.add(new)
                    queue.append((new, steps + 1))
    return -1
```

</details>

### 69. Word Ladder
**Problem**: Write a Python function to find the shortest transformation sequence length from beginWord to endWord using a dictionary.  
Example:  
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]  
Output: 5
```
<details>
<summary>Solution</summary>

```python
from collections import deque
def ladder_length(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    queue = deque([(beginWord, 1)])
    seen = {beginWord}
    
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set and new_word not in seen:
                    seen.add(new_word)
                    queue.append((new_word, steps + 1))
    return 0
```

</details>

### 70. Longest Palindromic Subsequence
**Problem**: Write a Python function to find the length of the longest palindromic subsequence in a string.  
Example:  
```
Input: "bbbab"  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end] and length == 2:
                dp[start][end] = 2
            elif s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1] + 2
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    return dp[0][n-1]
```

</details>

### 71. Distinct Subsequences
**Problem**: Write a Python function to find the number of distinct subsequences of s that equal t.  
Example:  
```
Input: s = "rabbbit", t = "rabbit"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def num_distinct(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]
```

</details>

### 72. Wildcard Matching
**Problem**: Write a Python function to check if a string matches a pattern with wildcards (? and *).  
Example:  
```
Input: s = "adceb", p = "*a*b"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_wildcard_match(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    
    for j in range(1, len(p) + 1):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-1]
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == "*":
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] == "?" or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[len(s)][len(p)]
```

</details>

### 73. Longest Substring with K Distinct Characters
**Problem**: Write a Python function to find the length of the longest substring with at most k distinct characters.  
Example:  
```
Input: s = "eceba", k = 2  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    count = {}
    max_len = 0
    left = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 74. Minimum Remove to Make Valid Parentheses
**Problem**: Write a Python function to remove the minimum number of parentheses to make a string valid.  
Example:  
```
Input: "lee(t(c)o)de)"  
Output: "lee(t(c)o)de"
```
<details>
<summary>Solution</summary>

```python
def min_remove_valid_parentheses(s):
    s = list(s)
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                s[i] = ""
    for i in stack:
        s[i] = ""
    return "".join(s)
```

</details>

### 75. Scramble String
**Problem**: Write a Python function to check if one string is a scrambled version of another.  
Example:  
```
Input: s1 = "great", s2 = "rgeat"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_scramble(s1, s2):
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    n = len(s1)
    for i in range(1, n):
        if (is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])) or \
           (is_scramble(s1[:i], s2[n-i:]) and is_scramble(s1[i:], s2[:n-i])):
            return True
    return False
```

</details>

### 76. Longest Repeating Substring
**Problem**: Write a Python function to find the length of the longest repeating substring in a string.  
Example:  
```
Input: "abcd"  
Output: 0
```
<details>
<summary>Solution</summary>

```python
def longest_repeating_substring(s):
    def check(length):
        seen = set()
        for i in range(len(s) - length + 1):
            substr = s[i:i+length]
            if substr in seen:
                return True
            seen.add(substr)
        return False
    
    left, right = 1, len(s)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
```

</details>

### 77. String Compression II
**Problem**: Write a Python function to find the length of the shortest compressed string with at most k deletions.  
Example:  
```
Input: s = "aaabcccd", k = 2  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def get_length_of_optimal_compression(s, k):
    n = len(s)
    dp = [[9999] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(k + 1):
            cnt = 0
            del_count = 0
            for l in range(i, 0, -1):
                if s[l-1] == s[i-1]:
                    cnt += 1
                else:
                    del_count += 1
                if j - del_count >= 0:
                    compressed_len = 1 if cnt == 1 else (2 if cnt < 10 else (3 if cnt < 100 else 4))
                    dp[i][j] = min(dp[i][j], dp[l-1][j-del_count] + compressed_len)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
    return dp[n][k]
```

</details>

### 78. Longest Substring with At Most Two Distinct Characters
**Problem**: Write a Python function to find the length of the longest substring with at most two distinct characters.  
Example:  
```
Input: "eceba"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def length_of_longest_substring_two_distinct(s):
    count = {}
    max_len = 0
    left = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        while len(count) > 2:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 79. Backspace String Compare
**Problem**: Write a Python function to compare two strings with backspace characters (#).  
Example:  
```
Input: s = "ab#c", t = "ad#c"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def backspace_compare(s, t):
    def process_string(string):
        stack = []
        for c in string:
            if c != "#":
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)
    return process_string(s) == process_string(t)
```

</details>

### 80. Longest Substring with Same Letters after Replacement
**Problem**: Write a Python function to find the longest substring length with same letters after k replacements.  
Example:  
```
Input: s = "AABABBA", k = 1  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def longest_repeating_letter(s, k):
    count = {}
    max_len = 0
    left = 0
    max_count = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        if right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 81. Group Words by Length
**Problem**: Write a Python function to group words in a list by their length.  
Example:  
```
Input: ["cat", "dog", "rat", "bat"]  
Output: {3: ["cat", "dog", "rat", "bat"]}
```
<details>
<summary>Solution</summary>

```python
def group_by_length(words):
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups
```

</details>

### 82. Find and Replace Pattern
**Problem**: Write a Python function to find words that match a pattern based on character mappings.  
Example:  
```
Input: words = ["abc", "deq", "mee"], pattern = "abb"  
Output: ["mee"]
```
<details>
<summary>Solution</summary>

```python
def find_and_replace_pattern(words, pattern):
    def get_pattern(s):
        char_map = {}
        result = []
        next_id = 0
        for c in s:
            if c not in char_map:
                char_map[c] = next_id
                next_id += 1
            result.append(char_map[c])
        return tuple(result)
    
    pattern_key = get_pattern(pattern)
    return [w for w in words if get_pattern(w) == pattern_key]
```

</details>

### 83. Valid Word Abbreviation
**Problem**: Write a Python function to check if a word matches its abbreviation.  
Example:  
```
Input: word = "internationalization", abbr = "i12n"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def valid_word_abbreviation(word, abbr):
    i = j = 0
    while i < len(word) and j < len(abbr):
        if word[i] == abbr[j]:
            i += 1
            j += 1
        elif abbr[j].isdigit():
            if abbr[j] == "0":
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            return False
    return i == len(word) and j == len(abbr)
```

</details>

### 84. Count Binary Substrings
**Problem**: Write a Python function to count substrings with equal consecutive 0s and 1s.  
Example:  
```
Input: "00110011"  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def count_binary_substrings(s):
    prev_count = curr_count = 1
    total = 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            total += min(prev_count, curr_count)
            prev_count = curr_count
            curr_count = 1
        else:
            curr_count += 1
    return total + min(prev_count, curr_count)
```

</details>

### 85. Longest Uncommon Subsequence
**Problem**: Write a Python function to find the length of the longest uncommon subsequence between two strings.  
Example:  
```
Input: a = "aba", b = "cdc"  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def find_LUS_length(a, b):
    return max(len(a), len(b)) if a != b else -1
```

</details>

### 86. Shortest Palindrome
**Problem**: Write a Python function to form the shortest palindrome by adding characters to the front of a string.  
Example:  
```
Input: "aacecaaa"  
Output: "aaacecaaa"
```
<details>
<summary>Solution</summary>

```python
def shortest_palindrome(s):
    def kmp(s, rev):
        concat = s + "#" + rev
        k = [0] * len(concat)
        for i in range(1, len(concat)):
            j = k[i-1]
            while j > 0 and concat[i] != concat[j]:
                j = k[j-1]
            if concat[i] == concat[j]:
                j += 1
            k[i] = j
        return k[-1]
    
    return s[::-1][:-kmp(s, s[::-1])] + s
```

</details>

### 87. Repeated Substring Pattern
**Problem**: Write a Python function to check if a string can be formed by repeating a substring.  
Example:  
```
Input: "abab"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def repeated_substring_pattern(s):
    return s in (s + s)[1:-1]
```

</details>

### 88. Longest Substring with Unique Characters
**Problem**: Write a Python function to find the longest substring with all unique characters.  
Example:  
```
Input: "abcabcbb"  
Output: "abc"
```
<details>
<summary>Solution</summary>

```python
def longest_unique_substring(s):
    seen = {}
    max_len = 0
    start = 0
    max_sub = ""
    for end, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        else:
            if end - start + 1 > max_len:
                max_len = end - start + 1
                max_sub = s[start:end + 1]
        seen[c] = end
    return max_sub
```

</details>

### 89. Check if String is Valid Shuffle
**Problem**: Write a Python function to check if a string is a valid shuffle of two other strings.  
Example:  
```
Input: s1 = "abc", s2 = "def", shuffle = "dabcef"  
Output: True
```
<details>
<summary>Solution</summary>

```python
def is_valid_shuffle(s1, s2, shuffle):
    if len(shuffle) != len(s1) + len(s2):
        return False
    s1_count = {}
    s2_count = {}
    for c in s1:
        s1_count[c] = s1_count.get(c, 0) + 1
    for c in s2:
        s2_count[c] = s2_count.get(c, 0) + 1
    shuffle_count = {}
    for c in shuffle:
        shuffle_count[c] = shuffle_count.get(c, 0) + 1
    for c in shuffle_count:
        if s1_count.get(c, 0) + s2_count.get(c, 0) != shuffle_count[c]:
            return False
    return True
```

</details>

### 90. Longest Word with All Prefixes
**Problem**: Write a Python function to find the longest word in a list that has all its prefixes in the list.  
Example:  
```
Input: ["cat", "cats", "ca", "c"]  
Output: "cats"
```
<details>
<summary>Solution</summary>

```python
def longest_word_with_prefixes(words):
    words_set = set(words)
    result = ""
    for word in sorted(words, key=len, reverse=True):
        if all(word[:i] in words_set for i in range(1, len(word) + 1)):
            return word
    return result
```

</details>

### 91. Minimum Window Substring with All Characters
**Problem**: Write a Python function to find the minimum window substring containing all characters from a set.  
Example:  
```
Input: s = "ADOBECODEBANC", chars = {'A', 'B', 'C'}  
Output: "ABC"
```
<details>
<summary>Solution</summary>

```python
def min_window_all_chars(s, chars):
    chars = set(chars)
    count = {}
    required = len(chars)
    formed = 0
    window_counts = {}
    left = right = 0
    min_len = float('inf')
    min_window_sub = ""
    
    while right < len(s):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        if c in chars and window_counts[c] == 1:
            formed += 1
        while left <= right and formed == required:
            c = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_sub = s[left:right + 1]
            window_counts[c] -= 1
            if c in chars and window_counts[c] == 0:
                formed -= 1
            left += 1
        right += 1
    return min_window_sub
```

</details>

### 92. Longest Substring with Balanced Parentheses
**Problem**: Write a Python function to find the longest substring with balanced parentheses.  
Example:  
```
Input: "((()))"  
Output: 6
```
<details>
<summary>Solution</summary>

```python
def longest_balanced_substring(s):
    stack = [-1]
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len
```

</details>

### 93. Find Kth Character in String Game
**Problem**: Write a Python function to find the k-th character in a string formed by concatenating "1" to "n" in binary.  
Example:  
```
Input: n = 2, k = 3  
Output: "0"
```
<details>
<summary>Solution</summary>

```python
def kth_character(n, k):
    s = ""
    for i in range(1, n + 1):
        s += bin(i)[2:]
    return s[k-1]
```

</details>

### 94. Longest Substring with Even Vowel Counts
**Problem**: Write a Python function to find the longest substring with an even count of vowels.  
Example:  
```
Input: "eleetminicoworoep"  
Output: 13
```
<details>
<summary>Solution</summary>

```python
def longest_even_vowel_substring(s):
    vowels = set('aeiou')
    state = 0
    seen = {0: -1}
    max_len = 0
    for i, c in enumerate(s):
        if c in vowels:
            state ^= 1 << "aeiou".index(c)
        if state in seen:
            max_len = max(max_len, i - seen[state])
        else:
            seen[state] = i
    return max_len
```

</details>

### 95. Longest Substring with Same Characters
**Problem**: Write a Python function to find the longest substring with all identical characters.  
Example:  
```
Input: "aabbbcccc"  
Output: 4
```
<details>
<summary>Solution</summary>

```python
def longest_same_char_substring(s):
    if not s:
        return 0
    max_len = 1
    curr_len = 1
    curr_char = s[0]
    for c in s[1:]:
        if c == curr_char:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_char = c
            curr_len = 1
    return max_len
```

</details>

### 96. Longest Substring Without Three Consecutive Same Characters
**Problem**: Write a Python function to find the longest substring without three consecutive identical characters.  
Example:  
```
Input: "aabbaaaa"  
Output: 7
```
<details>
<summary>Solution</summary>

```python
def longest_no_three_consecutive(s):
    if not s:
        return 0
    max_len = 0
    curr_len = 1
    curr_char = s[0]
    count = 1
    for c in s[1:]:
        if c == curr_char:
            count += 1
            if count <= 2:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 2
        else:
            curr_char = c
            count = 1
            curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len
```

</details>

### 97. Longest Substring with At Most K Vowels
**Problem**: Write a Python function to find the longest substring with at most k vowels.  
Example:  
```
Input: s = "aeiou", k = 2  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def longest_substring_k_vowels(s, k):
    vowels = set('aeiou')
    max_len = 0
    vowel_count = 0
    left = 0
    for right in range(len(s)):
        if s[right] in vowels:
            vowel_count += 1
        while vowel_count > k:
            if s[left] in vowels:
                vowel_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>

### 98. Longest Substring with No Repeating Substrings
**Problem**: Write a Python function to find the longest substring with no repeating substrings of length k.  
Example:  
```
Input: s = "abababab", k = 2  
Output: 2
```
<details>
<summary>Solution</summary>

```python
def longest_no_repeat_substring(s, k):
    def check(length):
        seen = set()
        for i in range(len(s) - length + 1):
            substr = s[i:i+length]
            if len(substr) == length and substr in seen:
                return False
            seen.add(substr)
        return True
    
    left, right = 1, len(s)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
```

</details>

### 99. Longest Substring with At Least One of Each Vowel
**Problem**: Write a Python function to find the longest substring containing at least one of each vowel.  
Example:  
```
Input: "aeiou"  
Output: 5
```
<details>
<summary>Solution</summary>

```python
def longest_all_vowels(s):
    vowels = set('aeiou')
    count = {}
    min_len = float('inf')
    left = 0
    formed = 0
    for right in range(len(s)):
        if s[right] in vowels:
            count[s[right]] = count.get(s[right], 0) + 1
            if count[s[right]] == 1:
                formed += 1
        while formed == len(vowels):
            min_len = min(min_len, right - left + 1)
            if s[left] in vowels:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    formed -= 1
            left += 1
    return min_len if min_len != float('inf') else 0
```

</details>

### 100. Longest Substring with No More Than K Distinct Characters
**Problem**: Write a Python function to find the longest substring with no more than k distinct characters.  
Example:  
```
Input: s = "eceba", k = 2  
Output: 3
```
<details>
<summary>Solution</summary>

```python
def longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    count = {}
    max_len = 0
    left = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

</details>