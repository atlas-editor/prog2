# Programming 2 &ndash; THW5

**5.1.** (4 points) Suppose an arithmetic expression is given as a tree. Each leaf is an integer and each internal node is one of the standard arithmetical operations (`+`, `-`, `∗`, `/`). For example, the expression `(1*(3-4))+7` is represented by the following tree.

```
    +
   / \
  *   7
 / \ 
1   -
   / \
  3   4  
```

Give an `O(n)` algorithm for evaluating such an expression, where there are `n` nodes in the tree.

---

**5.2.** (4 points) Use the partitioning idea of quicksort to give an algorithm that ﬁnds the median element of an array of `n` integers. Analyze the time complexity of your algorithm.

---

**5.3.** (2 points) Describe a recursive algorithm to solve the following problem: given an even positive integer `n=2k`, find all binary numbers with equal sum in left and right halves, i.e. the sum of the first `k` digits is equal to the sum of the last `k` digits.

_Note:_ Your algorithm should not generate every possible binary sequence and then check for equality between halves, this should be taken care of during the generation.

---

***5.4.** (1 point) How would the time complexity of your algorithm from **5.2.** change if in each partitioning step we managed to find a pivot which lies in the two middle quarters of the given array?