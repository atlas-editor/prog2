# Programming 2 &ndash; PHW8

**8.1.** (5 points) Consider the following program:

```python
def is_constant(arr: list, lower: int, upper: int) -> bool:
    for i in range(lower+1, upper+1):
        if arr[lower] != arr[i]:
            return False

    return True
```
Your task is to write a **recursive implementation** of the function `is_constant`.

_Input Format_

The first line contains a positive integer $N$, then $N$ pairs of lines follow. Given an index $i<N$, the first line from the $i$-th pair contains two space separated integers $l_i$ and $u_i$ and the second line contains $n_i$ space separated integers $(x_j)_{j<n_i}$ specifying an array $A_i$ for which you have to decide if it is constant starting at index $l_i$ and ending at index $u_i$ (both included).

_Constraints_

* $1 \le N < 100$
* $1 \le n_i < 10^6$
* $0 \le l_i \le u_i < n_i$
* the implementation of the solution must be recursive

_Output Format_

You have to print $N$ lines. On line $i$ you print `True` if the given array is constant on the specified bound and `False` else.

_Sample Input_

```
2
1 2
1 2 3
0 4
22 22 22 22 22
```

_Sample Output_

```
False
True
```

_Explanation_

The first array is $[1,2,3]$ and we are interested in the subarray $[2,3]$ which is not constant so we print `False`. In the second case the array is obviously constant so we print `True`.

---

**8.2.** (5 point) Atticus is taking Programming 2 and wants to solve every bonus problem on his homework. Unfortunately, statistics is not his strong suit and thus he is struggling with the following problem.

Given an array $X[]$ of size $n$ and a natural number $d$ calculate the number of indices $i$ such that $X[i]$ is at least two times larger than the median of the previous $d$-many numbers: $X[i-d], \ldots, X[i-1]$. Consider only indices $i$ which have at least $d$-many predecessors so you are able to calculate the median.

_Input Format_

The first line contains space separated integers $n$ and $d$. The second line contains the array $X[]$ of $n$ integers each separated by a space.

_Constraints_

* $1 \le n < 10^6$
* $1 \le d < n$
* $0 \le X[i] \le 200$

_Output Format_

Print the number of indices $i \ge d$ such that $X[i] \ge 2 \cdot \mathrm{median}(X[i-d], \ldots, X[i-1])$.

_Sample Input_

```
5 4
1 2 3 4 5
```

_Sample Output_

```
1
```

_Explanation_

As $d=4$ we only check the median condition for the last element of the list. The median of $1,2,3,4$ is $2.5$ and $5 \ge 2 \cdot 2.5$ so the condition is met once and we print $1$.