# Python Dictionary Pattern Coding Practice Questions

This file contains 100 practice questions for Python dictionary patterns, ranging from beginner to advanced levels. Each task is designed to enhance your understanding of dictionary operations and their applications in coding interviews.

## Beginner Level

1. **Print Value of Given Key**  
   Create a dictionary with keys: `name`, `IP`, `username`, `pwd` and values: `Router1`, `1.1.1.1`, `zframez`, `zframez`. Write a program to print the value of a user-specified key.

2. **Check and Add Key**  
   Given `network = {'name': 'Router1', 'ip': '1.1.1.1', 'username': 'zframez', 'pwd': 'zframez'}`, check if a user-specified key exists. If it exists, print its value; otherwise, add the key with a user-specified value.

3. **Create and Access Dictionary**  
   Create a dictionary with keys: `Interface`, `IP`, `status` and values for 4 entries (e.g., `Ethernet0`, `1.1.1.1`, `up`). Write a program to print the status of a given interface.

4. **Count Key-Value Pairs**  
   Write a program to count the number of key-value pairs in a given dictionary.

5. **Create Empty Dictionary**  
   Initialize an empty dictionary and add 3 key-value pairs based on user input.

6. **Access All Keys**  
   Given a dictionary, write a program to print all its keys.

7. **Access All Values**  
   Given a dictionary, write a program to print all its values.

8. **Update Value**  
   Given a dictionary, update the value of a user-specified key.

9. **Remove Key-Value Pair**  
   Write a program to remove a specified key from a dictionary.

10. **Check Dictionary Empty**  
    Write a program to check if a dictionary is empty.

11. **Copy Dictionary**  
    Create a program to create a copy of a given dictionary.

12. **Default Value for Missing Key**  
    Use `get()` to retrieve a key’s value, returning a default value if the key doesn’t exist.

13. **Merge Two Dictionaries**  
    Write a program to merge two dictionaries into one.

14. **Create Dictionary from Lists**  
    Given two lists (keys and values), create a dictionary from them.

15. **Sum of Numeric Values**  
    Write a program to calculate the sum of all numeric values in a dictionary.

16. **Find Maximum Value**  
    Write a program to find the maximum value in a dictionary.

17. **Find Minimum Value**  
    Write a program to find the minimum value in a dictionary (assume values are numeric).

18. **Dictionary Length**  
    Write a program to find the length of a dictionary.

19. **Clear Dictionary**  
    Write a program to clear all key-value pairs from a dictionary.

20. **Check Key Existence**  
    Write a program to check if a specific key exists in a dictionary.

## Intermediate Level

21. **Interface Status Check**  
    Given a dictionary with keys: `#`, `Interface`, `IP`, `status` (e.g., `#1`, `Ethernet0`, `1.1.1.1`, `up`), find the status of a user-specified interface.

22. **Filter Up Interfaces**  
    From the dictionary in Q21, find the interface and IP of all interfaces with status `up`.

23. **Count Ethernet Interfaces**  
    From the dictionary in Q21, count the number of Ethernet interfaces.

24. **Add New Entry**  
    From the dictionary in Q21, add a new entry with user-specified values.

25. **Nested Dictionary Creation**  
    Create a nested dictionary to store student details (name, roll_no, marks) for 3 students.

26. **Access Nested Dictionary**  
    From the nested dictionary in Q25, access the marks of a specific student.

27. **Update Nested Dictionary**  
    Update the marks of a specific student in the nested dictionary from Q25.

28. **Count Nested Keys**  
    Count the total number of keys in a nested dictionary (including nested levels).

29. **Dictionary to List**  
    Convert a dictionary’s key-value pairs into a list of tuples.

30. **Sort Dictionary by Keys**  
    Write a program to sort a dictionary by its keys.

31. **Sort Dictionary by Values**  
    Write a program to sort a dictionary by its values (assume values are comparable).

32. **Invert Dictionary**  
    Write a program to invert a dictionary (swap keys and values, assuming values are unique).

33. **Count Frequency**  
    Given a list, create a dictionary to count the frequency of each element.

34. **Group by Key**  
    Given a list of tuples (e.g., `[('a', 1), ('b', 2), ('a', 3)]`), group values by keys in a dictionary.

35. **Dictionary Comprehension**  
    Use dictionary comprehension to create a dictionary of squares for numbers 1 to 10.

36. **Filter Dictionary**  
    Filter a dictionary to include only key-value pairs where values are greater than a user-specified threshold.

37. **Find Common Keys**  
    Write a program to find common keys between two dictionaries.

38. **Find Unique Keys**  
    Write a program to find keys that are unique to one dictionary compared to another.

39. **Dictionary from String**  
    Given a string, create a dictionary to store character frequencies.

40. **Merge Dictionaries with Sum**  
    Merge two dictionaries, summing values for common keys.

## Advanced Level

41. **Find All Up Interfaces**  
    From a dictionary with multiple interface entries, return a new dictionary with only `up` interfaces.

42. **Dynamic Nested Dictionary**  
    Create a nested dictionary from a list of tuples representing hierarchical data (e.g., department > team > employee).

43. **Deep Nested Access**  
    Access a value in a deeply nested dictionary using a list of keys (e.g., `['dept', 'team', 'emp']`).

44. **Flatten Nested Dictionary**  
    Write a program to flatten a nested dictionary into a single-level dictionary with concatenated keys.

45. **Dictionary as Lookup Table**  
    Create a dictionary as a lookup table for mapping country codes to country names and retrieve a name by code.

46. **Count Nested Values**  
    Count the total number of values in a nested dictionary (including all levels).

47. **Dictionary Path Finder**  
    Given a nested dictionary, find all paths (as lists of keys) leading to a specific value.

48. **Dictionary Difference**  
    Write a program to find the difference between two dictionaries (keys and values that differ).

49. **Validate Dictionary Structure**  
    Validate if a dictionary follows a specific structure (e.g., all values are integers).

50. **Dictionary to JSON**  
    Convert a dictionary to a JSON string using the `json` module.

51. **Dictionary from JSON**  
    Parse a JSON string into a dictionary using the `json` module.

52. **Group by Value Type**  
    Group dictionary values by their data type (e.g., int, str, list).

53. **Dynamic Key Generation**  
    Create a dictionary with dynamically generated keys based on a pattern (e.g., `key1`, `key2`, ...).

54. **Dictionary with Default Factory**  
    Use `collections.defaultdict` to create a dictionary with a default value for missing keys.

55. **Merge Nested Dictionaries**  
    Merge two nested dictionaries, preserving the structure and updating values for common keys.

56. **Dictionary Key Transformation**  
    Transform all keys in a dictionary to uppercase.

57. **Recursive Dictionary Update**  
    Write a recursive function to update values in a nested dictionary.

58. **Dictionary Key Validation**  
    Validate that all keys in a dictionary match a specific pattern (e.g., regex for IP addresses).

59. **Dictionary Aggregation**  
    Aggregate values in a dictionary (e.g., sum, average) based on a user-specified operation.

60. **Dictionary Subset**  
    Create a new dictionary with a subset of keys from an existing dictionary.

61. **Dictionary Key Renaming**  
    Rename specific keys in a dictionary based on a mapping.

62. **Dictionary Intersection**  
    Find the intersection of two dictionaries (common keys with same values).

63. **Dictionary Union**  
    Create a union of two dictionaries, keeping all keys and their values.

64. **Dictionary to CSV**  
    Convert a dictionary to a CSV string where keys are headers and values are rows.

65. **Dictionary from CSV**  
    Parse a CSV string into a dictionary.

66. **Dictionary Key Sorting with Priority**  
    Sort a dictionary by keys, prioritizing a specific key to appear first.

67. **Dictionary Value Mapping**  
    Map dictionary values to new values using a provided function.

68. **Dictionary with Timestamps**  
    Add a timestamp to each value in a dictionary to track when it was added.

69. **Dictionary Key Hierarchy**  
    Create a dictionary with hierarchical keys (e.g., `dept.team.emp`) from a flat dictionary.

70. **Dictionary Value Validation**  
    Validate that all values in a dictionary meet a specific condition (e.g., positive numbers).

71. **Dictionary Key-Value Swap with Duplicates**  
    Swap keys and values in a dictionary, handling duplicate values by storing them in lists.

72. **Dictionary Grouping by Value**  
    Group dictionary keys by their values into a new dictionary.

73. **Dictionary Key Filtering**  
    Filter a dictionary to include only keys that satisfy a given condition.

74. **Dictionary Value Transformation**  
    Transform all values in a dictionary using a user-specified function.

75. **Dictionary to Tree Structure**  
    Convert a flat dictionary into a tree-like nested dictionary based on key patterns.

76. **Dictionary Key Path Validation**  
    Validate that a given key path exists in a nested dictionary.

77. **Dictionary Value Aggregation**  
    Aggregate dictionary values by a specific key in a nested dictionary.

78. **Dictionary Key Merging**  
    Merge keys with similar prefixes into a single key with a combined value.

79. **Dictionary Value Sorting**  
    Sort dictionary values and return a list of sorted values.

80. **Dictionary Key-Value Pair Filtering**  
    Filter key-value pairs based on both key and value conditions.

## Expert Level

81. **Dynamic Dictionary Schema**  
    Create a dictionary with a schema defined by user input (e.g., key types and value constraints).

82. **Dictionary Circular Reference Check**  
    Check if a nested dictionary contains circular references.

83. **Dictionary Query Language**  
    Implement a simple query language to retrieve values from a nested dictionary (e.g., `dept.team.emp`).

84. **Dictionary Diff with Paths**  
    Find differences between two nested dictionaries, returning paths to differing keys/values.

85. **Dictionary Compression**  
    Compress a dictionary by removing redundant values and storing them efficiently.

86. **Dictionary Key Normalization**  
    Normalize dictionary keys to a standard format (e.g., lowercase, no spaces).

87. **Dictionary Value Deduplication**  
    Deduplicate values in a dictionary, keeping only the first occurrence of each value.

88. **Dictionary Key-Value Dependency**  
    Enforce dependencies between keys and values (e.g., if key `A` exists, key `B` must exist).

89. **Dictionary to Graph**  
    Convert a dictionary representing edges (e.g., `{'A': 'B', 'B': 'C'}`) into a graph structure.

90. **Dictionary Path Aggregation**  
    Aggregate values along a specific path in a nested dictionary.

91. **Dictionary Key-Value Validation**  
    Validate that key-value pairs follow a specific schema (e.g., IP addresses as keys, integers as values).

92. **Dictionary Recursive Flattening**  
    Recursively flatten a nested dictionary with customizable key separators.

93. **Dictionary Key-Value Mapping**  
    Map both keys and values to new values using two separate functions.

94. **Dictionary Partial Match**  
    Find key-value pairs where keys partially match a given pattern.

95. **Dictionary Value Replacement**  
    Replace specific values in a nested dictionary with a new value.

96. **Dictionary Key-Value Transformation**  
    Transform both keys and values based on a user-specified rule.

97. **Dictionary to Adjacency List**  
    Convert a dictionary representing a graph into an adjacency list.

98. **Dictionary Key-Value Constraints**  
    Enforce constraints on key-value pairs (e.g., sum of values must equal 100).

99. **Dictionary Recursive Search**  
    Search for a value in a nested dictionary and return all paths leading to it.

100. **Dictionary Serialization**  
     Serialize a complex nested dictionary into a custom string format and deserialize it back.