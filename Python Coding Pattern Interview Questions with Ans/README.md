# Python Patterns Interview Questions

This README provides **100 Python pattern questions** designed for AI/ML students preparing for technical interviews. The questions focus on printing patterns (e.g., stars, numbers, characters) commonly asked in Python coding interviews. They are categorized into **Basic**, **Intermediate**, and **Advanced** levels, covering a range of pattern types like pyramids, triangles, diamonds, and more complex designs. Each question includes a problem statement, with the solution hidden in a `<details>` tag to encourage users to attempt the problem before viewing the answer. This format supports hands-on practice and aligns with interview preparation for AI/ML roles.

## Basic Patterns

### 1. Print a Right-Angle Triangle of Stars
**Problem**: Write a Python program to print a right-angle triangle of stars with 5 rows.  
Example:  
```
*  
**  
***  
****  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print("*" * i)
```

</details>

### 2. Print a Square of Stars
**Problem**: Write a Python program to print a 4x4 square of stars.  
Example:  
```
****  
****  
****  
****
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    print("*" * n)
```

</details>

### 3. Print a Number Sequence
**Problem**: Write a Python program to print numbers from 1 to 5 in each row for 5 rows.  
Example:  
```
12345  
12345  
12345  
12345  
12345
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print("".join(str(j) for j in range(1, n + 1)))
```

</details>

### 4. Print a Reverse Right-Angle Triangle
**Problem**: Write a Python program to print a reverse right-angle triangle of stars with 5 rows.  
Example:  
```
*****  
****  
***  
**  
*
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n, 0, -1):
    print("*" * i)
```

</details>

### 5. Print a Left-Aligned Triangle
**Problem**: Write a Python program to print a left-aligned triangle of stars with 5 rows.  
Example:  
```
    *  
   **  
  ***  
 ****  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
```

</details>

### 6. Print a Number Pyramid
**Problem**: Write a Python program to print a number pyramid with 5 rows.  
Example:  
```
    1  
   12  
  123  
 1234  
12345
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))
```

</details>

### 7. Print a Hollow Square
**Problem**: Write a Python program to print a hollow square of stars with side length 5.  
Example:  
```
*****  
*   *  
*   *  
*   *  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
```

</details>

### 8. Print a Character Sequence
**Problem**: Write a Python program to print characters A to E in each row for 5 rows.  
Example:  
```
ABCDE  
ABCDE  
ABCDE  
ABCDE  
ABCDE
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print("".join(chr(65 + j) for j in range(n)))
```

</details>

### 9. Print an Inverted Number Triangle
**Problem**: Write a Python program to print an inverted number triangle with 5 rows.  
Example:  
```
12345  
1234  
123  
12  
1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n, 0, -1):
    print("".join(str(j) for j in range(1, i + 1)))
```

</details>

### 10. Print a Star Border
**Problem**: Write a Python program to print a 5x5 star border.  
Example:  
```
*****  
*   *  
*   *  
*   *  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
```

</details>

### 11. Print a Right-Angle Number Triangle
**Problem**: Write a Python program to print a right-angle triangle of numbers with 5 rows.  
Example:  
```
1  
12  
123  
1234  
12345
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print("".join(str(j) for j in range(1, i + 1)))
```

</details>

### 12. Print a Star Rectangle
**Problem**: Write a Python program to print a 3x5 rectangle of stars.  
Example:  
```
*****  
*****  
*****
```
<details>
<summary>Solution</summary>

```python
rows = 3
cols = 5
for i in range(rows):
    print("*" * cols)
```

</details>

### 13. Print a Diagonal Star Pattern
**Problem**: Write a Python program to print a diagonal star pattern for 5 rows.  
Example:  
```
*    
 *   
  *  
   * 
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * i + "*")
```

</details>

### 14. Print a Reverse Diagonal Star Pattern
**Problem**: Write a Python program to print a reverse diagonal star pattern for 5 rows.  
Example:  
```
    *  
   *   
  *    
 *     
*
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*")
```

</details>

### 15. Print a Character Triangle
**Problem**: Write a Python program to print a character triangle with 5 rows.  
Example:  
```
    A  
   AB  
  ABC  
 ABCD  
ABCDE
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(chr(65 + j) for j in range(i)))
```

</details>

### 16. Print a Star Cross
**Problem**: Write a Python program to print a star cross for a 5x5 grid.  
Example:  
```
  *  
  *  
*****  
  *  
  *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == n // 2:
        print("*" * n)
    else:
        print(" " * (n // 2) + "*")
```

</details>

### 17. Print a Number Square
**Problem**: Write a Python program to print a 4x4 square of the number 5.  
Example:  
```
5555  
5555  
5555  
5555
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    print("5" * n)
```

</details>

### 18. Print a Hollow Triangle Border
**Problem**: Write a Python program to print a hollow triangle border with 5 rows.  
Example:  
```
    *  
   * *  
  *   *  
 *     *  
*********
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "*")
    elif i == n - 1:
        print("*" * (2 * n - 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
```

</details>

### 19. Print an Alternating Star Pattern
**Problem**: Write a Python program to print an alternating star pattern for 5 rows.  
Example:  
```
*  
**  
*  
**  
*
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print("*" * (1 if i % 2 == 0 else 2))
```

</details>

### 20. Print a Number Diagonal
**Problem**: Write a Python program to print a number diagonal for 5 rows.  
Example:  
```
1    
 2   
  3  
   4 
    5
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (i - 1) + str(i))
```

</details>

### 21. Print a Right-Angle Star Pattern with Spaces
**Problem**: Write a Python program to print a right-angle star pattern with spaces between stars for 5 rows.  
Example:  
```
*  
* *  
* * *  
* * * *  
* * * * *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" * " * i)
```

</details>

### 22. Print a Number Reverse Triangle
**Problem**: Write a Python program to print a reverse number triangle with 5 rows.  
Example:  
```
54321  
5432  
543  
54  
5
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n, 0, -1):
    print("".join(str(j) for j in range(5, 5 - i, -1)))
```

</details>

### 23. Print a Star Frame
**Problem**: Write a Python program to print a star frame for a 5x5 grid.  
Example:  
```
*****  
*   *  
*   *  
*   *  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
```

</details>

### 24. Print a Character Square
**Problem**: Write a Python program to print a 4x4 square of the character 'A'.  
Example:  
```
AAAA  
AAAA  
AAAA  
AAAA
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    print("A" * n)
```

</details>

### 25. Print a Star Ladder
**Problem**: Write a Python program to print a star ladder with 5 rows.  
Example:  
```
*  
 *  
  *  
   *  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * i + "*")
```

</details>

### 26. Print a Number Right Triangle
**Problem**: Write a Python program to print a right triangle of numbers with 5 rows.  
Example:  
```
1  
22  
333  
4444  
55555
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(str(i) * i)
```

</details>

### 27. Print a Hollow Rectangle
**Problem**: Write a Python program to print a hollow rectangle of 3x5 stars.  
Example:  
```
*****  
*   *  
*****
```
<details>
<summary>Solution</summary>

```python
rows = 3
cols = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * cols)
    else:
        print("*" + " " * (cols - 2) + "*")
```

</details>

### 28. Print a Star Zigzag
**Problem**: Write a Python program to print a star zigzag for 5 rows.  
Example:  
```
*    
 *   
  *  
 *   
*
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (i % 3) + "*")
```

</details>

### 29. Print a Number Frame
**Problem**: Write a Python program to print a 5x5 number frame with 1s.  
Example:  
```
11111  
1   1  
1   1  
1   1  
11111
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("1" * n)
    else:
        print("1" + " " * (n - 2) + "1")
```

</details>

### 30. Print a Character Diagonal
**Problem**: Write a Python program to print a character diagonal for 5 rows.  
Example:  
```
A    
 B   
  C  
   D 
    E
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * i + chr(65 + i))
```

</details>

### 31. Print a Star Plus
**Problem**: Write a Python program to print a star plus for a 5x5 grid.  
Example:  
```
  *  
  *  
*****  
  *  
  *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == n // 2:
        print("*" * n)
    else:
        print(" " * (n // 2) + "*")
```

</details>

### 32. Print a Number Ladder
**Problem**: Write a Python program to print a number ladder with 5 rows.  
Example:  
```
1  
 2  
  3  
   4  
    5
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (i - 1) + str(i))
```

</details>

### 33. Print a Star Outline
**Problem**: Write a Python program to print a star outline for a 5x5 grid.  
Example:  
```
*****  
*   *  
*   *  
*   *  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
```

</details>

## Intermediate Patterns

### 34. Print a Full Pyramid
**Problem**: Write a Python program to print a full pyramid of stars with 5 rows.  
Example:  
```
    *  
   ***  
  *****  
 *******  
*********
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 35. Print an Inverted Full Pyramid
**Problem**: Write a Python program to print an inverted full pyramid of stars with 5 rows.  
Example:  
```
*********  
 *******  
  *****  
   ***  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 36. Print a Diamond Pattern
**Problem**: Write a Python program to print a diamond pattern of stars with 5 rows on each half.  
Example:  
```
    *  
   ***  
  *****  
 *******  
*********  
 *******  
  *****  
   ***  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 37. Print a Hollow Pyramid
**Problem**: Write a Python program to print a hollow pyramid of stars with 5 rows.  
Example:  
```
    *  
   * *  
  *   *  
 *     *  
*********
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "*")
    elif i == n - 1:
        print("*" * (2 * n - 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
```

</details>

### 38. Print a Number Full Pyramid
**Problem**: Write a Python program to print a number full pyramid with 5 rows.  
Example:  
```
    1  
   123  
  12345  
 1234567  
123456789
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
```

</details>

### 39. Print a Pascal’s Triangle
**Problem**: Write a Python program to print Pascal’s triangle with 5 rows.  
Example:  
```
    1  
   1 1  
  1 2 1  
 1 3 3 1  
1 4 6 4 1
```
<details>
<summary>Solution</summary>

```python
n = 5
def binomial_coeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(binomial_coeff(i, j), end=" ")
    print()
```

</details>

### 40. Print a Hollow Diamond
**Problem**: Write a Python program to print a hollow diamond pattern with 5 rows on each half.  
Example:  
```
    *  
   * *  
  *   *  
 *     *  
*       *  
 *     *  
  *   *  
   * *  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + ("*" if i > 0 else ""))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + ("*" if i > 0 else ""))
```

</details>

### 41. Print a Character Full Pyramid
**Problem**: Write a Python program to print a character full pyramid with 5 rows.  
Example:  
```
    A  
   ABC  
  ABCDE  
 ABCDEFG  
ABCDEFGHI
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
```

</details>

### 42. Print a Half Diamond
**Problem**: Write a Python program to print a half diamond pattern with 5 rows.  
Example:  
```
*  
**  
***  
****  
*****  
****  
***  
**  
*
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)
```

</details>

### 43. Print a Number Diamond
**Problem**: Write a Python program to print a number diamond with 5 rows on each half.  
Example:  
```
    1  
   123  
  12345  
 1234567  
123456789  
 1234567  
  12345  
   123  
    1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
```

</details>

### 44. Print a Star Hourglass
**Problem**: Write a Python program to print a star hourglass with 5 rows on each half.  
Example:  
```
*********  
 *******  
  *****  
   ***  
    *  
   ***  
  *****  
 *******  
*********
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 45. Print a Hollow Inverted Pyramid
**Problem**: Write a Python program to print a hollow inverted pyramid with 5 rows.  
Example:  
```
*********  
 *     *  
  *   *  
   * *  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n - 1, -1, -1):
    if i == n - 1:
        print("*" * (2 * n - 1))
    elif i == 0:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
```

</details>

### 46. Print a Number Half Diamond
**Problem**: Write a Python program to print a number half diamond with 5 rows.  
Example:  
```
1  
12  
123  
1234  
12345  
1234  
123  
12  
1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print("".join(str(j) for j in range(1, i + 1)))
for i in range(n - 1, 0, -1):
    print("".join(str(j) for j in range(1, i + 1)))
```

</details>

### 47. Print a Character Hourglass
**Problem**: Write a Python program to print a character hourglass with 5 rows on each half.  
Example:  
```
ABCDEFGHI  
 ABCDEFG  
  ABCDE  
   ABC  
    A  
   ABC  
  ABCDE  
 ABCDEFG  
ABCDEFGHI
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
for i in range(1, n):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
```

</details>

### 48. Print a Star Butterfly
**Problem**: Write a Python program to print a star butterfly pattern with 5 rows on each half.  
Example:  
```
*        *  
**      **  
***    ***  
****  ****  
**********  
****  ****  
***    ***  
**      **  
*        *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
```

</details>

### 49. Print a Number Inverted Pyramid
**Problem**: Write a Python program to print a number inverted pyramid with 5 rows.  
Example:  
```
123456789  
 1234567  
  12345  
   123  
    1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
```

</details>

### 50. Print a Hollow Half Diamond
**Problem**: Write a Python program to print a hollow half diamond with 5 rows.  
Example:  
```
*  
* *  
*   *  
* *  
*
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n):
    if i == 1:
        print("*")
    else:
        print("*" + " " * (i - 2) + ("*" if i > 1 else ""))
for i in range(n - 2, 0, -1):
    if i == 1:
        print("*")
    else:
        print("*" + " " * (i - 2) + ("*" if i > 1 else ""))
```

</details>

### 51. Print a Star Wave
**Problem**: Write a Python program to print a star wave pattern with 5 rows.  
Example:  
```
*    
 **   
  ***  
 ****  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (i - 1) + "*" * i)
```

</details>

### 52. Print a Number Butterfly
**Problem**: Write a Python program to print a number butterfly pattern with 5 rows on each half.  
Example:  
```
1        1  
12      12  
123    123  
1234  1234  
1234512345  
1234  1234  
123    123  
12      12  
1        1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    left = "".join(str(j) for j in range(1, i + 1))
    print(left + " " * (2 * (n - i)) + left)
for i in range(n - 1, 0, -1):
    left = "".join(str(j) for j in range(1, i + 1))
    print(left + " " * (2 * (n - i)) + left)
```

</details>

### 53. Print a Character Half Diamond
**Problem**: Write a Python program to print a character half diamond with 5 rows.  
Example:  
```
A  
AB  
ABC  
ABCD  
ABCDE  
ABCD  
ABC  
AB  
A
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print("".join(chr(65 + j) for j in range(i)))
for i in range(n - 1, 0, -1):
    print("".join(chr(65 + j) for j in range(i)))
```

</details>

### 54. Print a Star Sandglass
**Problem**: Write a Python program to print a star sandglass with 5 rows on each half.  
Example:  
```
*********  
 *******  
  *****  
   ***  
    *  
   ***  
  *****  
 *******  
*********
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 55. Print a Number Wave
**Problem**: Write a Python program to print a number wave pattern with 5 rows.  
Example:  
```
1    
 12   
 123  
 1234  
12345
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (i - 1) + "".join(str(j) for j in range(1, i + 1)))
```

</details>

### 56. Print a Hollow Number Pyramid
**Problem**: Write a Python program to print a hollow number pyramid with 5 rows.  
Example:  
```
    1  
   1 2  
  1   3  
 1     4  
123456789
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "1")
    elif i == n - 1:
        print("".join(str(j) for j in range(1, 2 * n)))
    else:
        print(" " * (n - i - 1) + "1" + " " * (2 * i - 1) + str(i + 1))
```

</details>

### 57. Print a Star Spiral
**Problem**: Write a Python program to print a star spiral pattern with 5 rows.  
Example:  
```
*    
 **   
  ***  
   ****  
    *****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (i - 1) + "*" * i)
```

</details>

### 58. Print a Character Inverted Pyramid
**Problem**: Write a Python program to print a character inverted pyramid with 5 rows.  
Example:  
```
ABCDEFGHI  
 ABCDEFG  
  ABCDE  
   ABC  
    A
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
```

</details>

### 59. Print a Number Spiral
**Problem**: Write a Python program to print a number spiral pattern with 5 rows.  
Example:  
```
1    
 12   
 123  
 1234  
12345
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (i - 1) + "".join(str(j) for j in range(1, i + 1)))
```

</details>

### 60. Print a Hollow Character Pyramid
**Problem**: Write a Python program to print a hollow character pyramid with 5 rows.  
Example:  
```
    A  
   A B  
  A   C  
 A     D  
ABCDEFGHI
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "A")
    elif i == n - 1:
        print("".join(chr(65 + j) for j in range(2 * n - 1)))
    else:
        print(" " * (n - i - 1) + "A" + " " * (2 * i - 1) + chr(65 + i))
```

</details>

### 61. Print a Star Double Triangle
**Problem**: Write a Python program to print a star double triangle with 5 rows.  
Example:  
```
    *  
   * *  
  *   *  
 *     *  
* * * * *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == n - 1:
        print("* " * n)
    elif i == 0:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
```

</details>

### 62. Print a Number Double Pyramid
**Problem**: Write a Python program to print a number double pyramid with 5 rows.  
Example:  
```
    1  
   1 2  
  1   3  
 1     4  
123456789
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "1")
    elif i == n - 1:
        print("".join(str(j) for j in range(1, 2 * n)))
    else:
        print(" " * (n - i - 1) + "1" + " " * (2 * i - 1) + str(i + 1))
```

</details>

### 63. Print a Character Double Triangle
**Problem**: Write a Python program to print a character double triangle with 5 rows.  
Example:  
```
    A  
   A B  
  A   C  
 A     D  
ABCDEFGHI
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "A")
    elif i == n - 1:
        print("".join(chr(65 + j) for j in range(2 * n - 1)))
    else:
        print(" " * (n - i - 1) + "A" + " " * (2 * i - 1) + chr(65 + i))
```

</details>

### 64. Print a Star Zigzag Pyramid
**Problem**: Write a Python program to print a star zigzag pyramid with 5 rows.  
Example:  
```
    *  
   ***  
  *****  
   ***  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i < n // 2 + 1:
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (i) + "*" * (2 * (n - i - 1) + 1))
```

</details>

### 65. Print a Number Zigzag Pyramid
**Problem**: Write a Python program to print a number zigzag pyramid with 5 rows.  
Example:  
```
    1  
   123  
  12345  
   123  
    1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i < n // 2 + 1:
        print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
    else:
        print(" " * (i) + "".join(str(j) for j in range(1, 2 * (n - i))))
```

</details>

### 66. Print a Character Zigzag Pyramid
**Problem**: Write a Python program to print a character zigzag pyramid with 5 rows.  
Example:  
```
    A  
   ABC  
  ABCDE  
   ABC  
    A
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i < n // 2 + 1:
        print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
    else:
        print(" " * (i) + "".join(chr(65 + j) for j in range(2 * (n - i - 1) + 1)))
```

</details>

## Advanced Patterns

### 67. Print a Star Heart
**Problem**: Write a Python program to print a star heart pattern with 7 rows.  
Example:  
```
  ***   ***  
 **** ****  
***********  
 *********  
  *******  
   *****  
    ***
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    if i == 0:
        print("  ***   ***  ")
    elif i == 1:
        print(" **** **** ")
    else:
        print(" " * (i - 1) + "*" * (2 * (n - i + 1) + 1))
for i in range(n - 1, -1, -1):
    print(" " * (n - i) + "*" * (2 * i + 1))
```

</details>

### 68. Print a Number Spiral Matrix
**Problem**: Write a Python program to print a 4x4 number spiral matrix.  
Example:  
```
1  2  3  4  
12 13 14 5  
11 16 15 6  
10 9  8  7
```
<details>
<summary>Solution</summary>

```python
n = 4
matrix = [[0] * n for _ in range(n)]
num, row, col = 1, 0, 0
top, bottom, left, right = 0, n - 1, 0, n - 1
while num <= n * n:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1
for row in matrix:
    print(" ".join(f"{x:2}" for x in row))
```

</details>

### 69. Print a Character Spiral Matrix
**Problem**: Write a Python program to print a 4x4 character spiral matrix.  
Example:  
```
A B C D  
L M N E  
K P O F  
J I H G
```
<details>
<summary>Solution</summary>

```python
n = 4
matrix = [[" "] * n for _ in range(n)]
num, row, col = 0, 0, 0
top, bottom, left, right = 0, n - 1, 0, n - 1
while num < n * n:
    for i in range(left, right + 1):
        matrix[top][i] = chr(65 + num)
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = chr(65 + num)
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = chr(65 + num)
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = chr(65 + num)
        num += 1
    left += 1
for row in matrix:
    print(" ".join(row))
```

</details>

### 70. Print a Star Christmas Tree
**Problem**: Write a Python program to print a star Christmas tree with 5 rows and a trunk.  
Example:  
```
    *  
   ***  
  *****  
 *******  
*********  
   |||  
   |||
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(2):
    print(" " * (n - 2) + "|||")
```

</details>

### 71. Print a Number Pascal’s Triangle
**Problem**: Write a Python program to print a number Pascal’s triangle with 5 rows, right-aligned.  
Example:  
```
         1  
       1   1  
     1   2   1  
   1   3   3   1  
 1   4   6   4   1
```
<details>
<summary>Solution</summary>

```python
n = 5
def binomial_coeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res
for i in range(n):
    print("  " * (n - i - 1), end="")
    for j in range(i + 1):
        print(f"{binomial_coeff(i, j):2}", end="  ")
    print()
```

</details>

### 72. Print a Hollow Star Heart
**Problem**: Write a Python program to print a hollow star heart with 7 rows.  
Example:  
```
  *   *  
 * * * *  
*   *   *  
 *     *  
  *   *  
   * *  
    *
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    if i == 0:
        print("  *   *  ")
    elif i == 1:
        print(" * * * * ")
    else:
        print(" " * (i - 1) + "*" + " " * (2 * (n - i) - 1) + "*" if i < n - 1 else "")
for i in range(n - 1, -1, -1):
    if i == 0:
        print("    *    ")
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
```

</details>

### 73. Print a Star Swirl
**Problem**: Write a Python program to print a star swirl pattern with 5 rows.  
Example:  
```
*    
 *   
  ***  
   *   
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == n // 2:
        print("  ***")
    else:
        print(" " * (i % 4) + "*")
```

</details>

### 74. Print a Number Matrix Border
**Problem**: Write a Python program to print a 5x5 number matrix border.  
Example:  
```
12345  
1   2  
1   3  
1   4  
12345
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("".join(str(j) for j in range(1, n + 1)))
    else:
        print(f"1{' ' * (n - 2)}{i + 1}")
```

</details>

### 75. Print a Character Matrix Border
**Problem**: Write a Python program to print a 5x5 character matrix border.  
Example:  
```
ABCDE  
A   B  
A   C  
A   D  
ABCDE
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("".join(chr(65 + j) for j in range(n)))
    else:
        print(f"A{' ' * (n - 2)}{chr(65 + i)}")
```

</details>

### 76. Print a Star Arrow
**Problem**: Write a Python program to print a star arrow pattern with 7 rows.  
Example:  
```
   *   
  ***  
 *****  
*******  
 *****  
  ***  
   *
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 77. Print a Number Arrow
**Problem**: Write a Python program to print a number arrow pattern with 7 rows.  
Example:  
```
   1   
  123  
 12345  
1234567  
 12345  
  123  
   1
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
```

</details>

### 78. Print a Character Arrow
**Problem**: Write a Python program to print a character arrow pattern with 7 rows.  
Example:  
```
   A   
  ABC  
 ABCDE  
ABCDEFG  
 ABCDE  
  ABC  
   A
```
<details>
<summary>Solution</summary>

```python
n = 4
for i in range(n):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
```

</details>

### 79. Print a Star Crown
**Problem**: Write a Python program to print a star crown pattern with 5 rows.  
Example:  
```
*   *   *  
 * * * *   
  *   *    
   * *     
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print("*   *   *")
    elif i == 1:
        print(" * * * * ")
    else:
        print(" " * (i) + "*" + " " * (n - i - 2) + ("*" if i < n - 1 else ""))
```

</details>

### 80. Print a Number Crown
**Problem**: Write a Python program to print a number crown pattern with 5 rows.  
Example:  
```
1   2   3  
 4 5 6 7   
  8   9    
   10 11    
    12
```
<details>
<summary>Solution</summary>

```python
n = 5
num = 1
for i in range(n):
    if i == 0:
        print(f"{num}   {num+1}   {num+2}")
        num += 3
    elif i == 1:
        print(f" {num} {num+1} {num+2} {num+3}")
        num += 4
    else:
        print(" " * (i) + str(num) + (" " * (n - i - 2) + str(num + 1) if i < n - 1 else ""))
        num += 2
```

</details>

### 81. Print a Character Crown
**Problem**: Write a Python program to print a character crown pattern with 5 rows.  
Example:  
```
A   B   C  
 D E F G   
  H   I    
   J K     
    L
```
<details>
<summary>Solution</summary>

```python
n = 5
ch = 65
for i in range(n):
    if i == 0:
        print(f"{chr(ch)}   {chr(ch+1)}   {chr(ch+2)}")
        ch += 3
    elif i == 1:
        print(f" {chr(ch)} {chr(ch+1)} {chr(ch+2)} {chr(ch+3)}")
        ch += 4
    else:
        print(" " * (i) + chr(ch) + (" " * (n - i - 2) + chr(ch + 1) if i < n - 1 else ""))
        ch += 2
```

</details>

### 82. Print a Star Wave Pyramid
**Problem**: Write a Python program to print a star wave pyramid with 5 rows.  
Example:  
```
    *  
   ***  
  *****  
 *******  
*********
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 83. Print a Number Wave Pyramid
**Problem**: Write a Python program to print a number wave pyramid with 5 rows.  
Example:  
```
    1  
   123  
  12345  
 1234567  
123456789
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
```

</details>

### 84. Print a Character Wave Pyramid
**Problem**: Write a Python program to print a character wave pyramid with 5 rows.  
Example:  
```
    A  
   ABC  
  ABCDE  
 ABCDEFG  
ABCDEFGHI
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
```

</details>

### 85. Print a Star Double Diamond
**Problem**: Write a Python program to print a star double diamond with 5 rows on each half.  
Example:  
```
    *  
   ***  
  *****  
 *******  
*********  
 *******  
  *****  
   ***  
    *  
   ***  
  *****  
 *******  
*********
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 86. Print a Number Double Diamond
**Problem**: Write a Python program to print a number double diamond with 5 rows on each half.  
Example:  
```
    1  
   123  
  12345  
 1234567  
123456789  
 1234567  
  12345  
   123  
    1  
   123  
  12345  
 1234567  
123456789
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
for i in range(1, n):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
```

</details>

### 87. Print a Character Double Diamond
**Problem**: Write a Python program to print a character double diamond with 5 rows on each half.  
Example:  
```
    A  
   ABC  
  ABCDE  
 ABCDEFG  
ABCDEFGHI  
 ABCDEFG  
  ABCDE  
   ABC  
    A  
   ABC  
  ABCDE  
 ABCDEFG  
ABCDEFGHI
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
for i in range(1, n):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
```

</details>

### 88. Print a Star Helix
**Problem**: Write a Python program to print a star helix pattern with 5 rows.  
Example:  
```
*    
 **   
  ***  
   **  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i <= n // 2:
        print(" " * i + "*" * (i + 1))
    else:
        print(" " * i + "*" * (n - i))
```

</details>

### 89. Print a Number Helix
**Problem**: Write a Python program to print a number helix pattern with 5 rows.  
Example:  
```
1    
 12   
 123  
 12   
 1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i <= n // 2:
        print(" " * i + "".join(str(j) for j in range(1, i + 2)))
    else:
        print(" " * i + "".join(str(j) for j in range(1, n - i + 1)))
```

</details>

### 90. Print a Character Helix
**Problem**: Write a Python program to print a character helix pattern with 5 rows.  
Example:  
```
A    
 AB   
 ABC  
 AB   
 A
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i <= n // 2:
        print(" " * i + "".join(chr(65 + j) for j in range(i + 1)))
    else:
        print(" " * i + "".join(chr(65 + j) for j in range(n - i)))
```

</details>

### 91. Print a Star Infinity
**Problem**: Write a Python program to print a star infinity pattern with 5 rows.  
Example:  
```
  ***  
 *   *  
*     *  
 *   *  
  ***
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("  ***  ")
    elif i == n // 2:
        print("*     *")
    else:
        print(" *   * ")
```

</details>

### 92. Print a Number Infinity
**Problem**: Write a Python program to print a number infinity pattern with 5 rows.  
Example:  
```
  123  
 1   2  
1     3  
 1   4  
  123
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("  123  ")
    elif i == n // 2:
        print(f"1     {i+1}")
    else:
        print(f" 1   {i+1} ")
```

</details>

### 93. Print a Character Infinity
**Problem**: Write a Python program to print a character infinity pattern with 5 rows.  
Example:  
```
  ABC  
 A   B  
A     C  
 A   D  
  ABC
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("  ABC  ")
    elif i == n // 2:
        print(f"A     {chr(65 + i)}")
    else:
        print(f" A   {chr(65 + i)} ")
```

</details>

### 94. Print a Star Wave Diamond
**Problem**: Write a Python program to print a star wave diamond with 5 rows on each half.  
Example:  
```
    *  
   ***  
  *****  
 *******  
*********  
 *******  
  *****  
   ***  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

</details>

### 95. Print a Number Wave Diamond
**Problem**: Write a Python program to print a number wave diamond with 5 rows on each half.  
Example:  
```
    1  
   123  
  12345  
 1234567  
123456789  
 1234567  
  12345  
   123  
    1
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(str(j) for j in range(1, 2 * i + 2)))
```

</details>

### 96. Print a Character Wave Diamond
**Problem**: Write a Python program to print a character wave diamond with 5 rows on each half.  
Example:  
```
    A  
   ABC  
  ABCDE  
 ABCDEFG  
ABCDEFGHI  
 ABCDEFG  
  ABCDE  
   ABC  
    A
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "".join(chr(65 + j) for j in range(2 * i + 1)))
```

</details>

### 97. Print a Star Twisted Pyramid
**Problem**: Write a Python program to print a star twisted pyramid with 5 rows.  
Example:  
```
    *  
   **  
  ***  
 ****  
*****
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
```

</details>

### 98. Print a Number Twisted Pyramid
**Problem**: Write a Python program to print a number twisted pyramid with 5 rows.  
Example:  
```
    1  
   12  
  123  
 1234  
12345
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))
```

</details>

### 99. Print a Character Twisted Pyramid
**Problem**: Write a Python program to print a character twisted pyramid with 5 rows.  
Example:  
```
    A  
   AB  
  ABC  
 ABCD  
ABCDE
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(chr(65 + j) for j in range(i)))
```

</details>

### 100. Print a Star Complex Diamond
**Problem**: Write a Python program to print a star complex diamond with 5 rows on each half.  
Example:  
```
    *  
   * *  
  *   *  
 *     *  
* * * * *  
 *     *  
  *   *  
   * *  
    *
```
<details>
<summary>Solution</summary>

```python
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "*")
    elif i == n - 1:
        print("* " * n)
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
for i in range(n - 2, -1, -1):
    if i == 0:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
```

</details>