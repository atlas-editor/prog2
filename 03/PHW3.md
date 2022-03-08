# Programming 2 &ndash; PHW3

**3.1.** (5 points) Godrick is grafting his trees in the garden. As he is admiring their flowers he is looking for a special tree, a tree such that the sum of all flowers on the trees to its left is equal to the sum of all flowers to the trees to its right. 

Given an array $F[]$ of size $n$, where $F[i]$ is the number of flowers on the $i$-th tree, decide whether there  is an index $j$ such that the number of flowers on trees to its left is equal to the number of flowers on trees to its right.

_Input Format_

The first line contains $T$, the number of test cases. The next $T$ pairs of lines each represent a test case.
* The first line contains $n$, the number of elements in the array.
* The second line contains $n$ space separated integers specifyng the array $F[]$. 

_Constraints_

* $1 \le T \le 10$
* $1 \le n < 10^5$
* $0 \le F[i] < 10^5$

_Output Format_

Print `YES` if there is an index $j$ as specified above, `NO` else.

_Sample Input_

```
2
3
1 2 3
4
2 0 0 0
```

_Sample Output_

```
NO
YES
```

_Explanation_

In the first case it is easy to check that no index satisfies our condition and in the second the index $j=0$ is a witness as the sum to its left is $0$ (there are no trees to its left) and the sum to the right is also $0$ (no flowers on either tree to its right).

---

**3.2.** (5 points) Margit loves primes and is interested in prime factors of very large numbers.

Given a natural number $n$, find the largest number of distinct prime factors of any natural number less than or equal to $n$.

_Input Format_

The first line contains $T$, the number of test cases. The next $T$ lines each represent one natural number.

_Constraints_

* $1 \le T \le 10^5$
* $1 \le n \le 10^{18}$

_Output Format_

Print the maximum number of distinct prime factors of any number $i$ such that $0 \le i \le n$.

_Sample Input_

```
2
1
15
```

_Sample Output_

```
0
2
```

_Explanation_

In the first case, as   $1$ is less than the smallest prime there are no prime factors. In the second case the maximum, $2$, is attained several times, e.g. $10 = 2 \cdot 5$ and no number in this range has $3$ distinct prime factors.