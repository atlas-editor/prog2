# Programming 2 &ndash; THW4

**4.1.** (3 points) Consider the algorithm:

```python
def tribonacci(n):
    if n < 3:
        return 0
    if n == 3:
        return 1
    return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
```

Given a positive integer $n$ consider the call of this function:

```python
tribonacci(n)
```

Determine the maximal height of the call tree during the execution and  also the number of times the function is called with argument: `2`.

---

**4.2.** (4 points) Describe a recursive approach to the following problem: given a string $s$ find every substring of $s$ which is a palindrome.

---

**4.3.** (3 points) Design a _split_ algorithm for binary search trees. Given a value $v$ and a tree $T$ the algorithm outputs two binary search trees $T_1$ and $T_2$ such that the value of every node in $T_1$ is less than $v$ and the value of every node in $T_2$ is greater than $v$.

---

***4.4.** (2 points) Describe an algorithm which can reconstruct any binary tree given its _preorder_ and _inorder_ traversals.