# Programming 2 &ndash; PHW4


**4.1.** (5 points) Lev is given a list of values of certain elements. He has to share the elements with his friend but Lev wants the most value. Help him find the least number of elements whose values sum up to a larger number than the values of the rest of the elements.

Given an array $E[]$ of positive integers find the smallest number $k$ such that the sum of some $k$ elements from $E[]$ is larger than the sum of the rest.

_Input Format_

The first line contains an integer $n$. The second line contains the array $E[]$ of $n$ integers each separated by a space.

_Constraints_

* $1 \le n < 1000$
* $1 \le E[i] < 1000$

_Output Format_

Print the least number $k$ such that there is a sequence $i_0 < i_1 < \cdots < i_{k-1}$ of indices such that $\sum_{j=0}^{k-1} E[i_j] > \sum_{j=0}^{n-1} E[j] - \sum_{j=0}^{k-1} E[i_j]$.

_Sample Input_

```
2
8 8
```

_Sample Output_

```
2
```

_Explanation_

 Lev has to take both elements because if he only took one the values would be equal.

**Note:** In this exercise it is  forbidden to use any built-in method which sorts a given array, e.g. the methods `sort` or `sorted`. You can (and should), however, implement any sorting algorithm of your choosing.

---

**4.2.** (5 points) Lilith is interested in numbers ending with lots of zeroes, particularly numbers which are factorials.

Given a positive integer $k$ find the smallest number $x$ such that $x!$ ends with at least $k$ zeroes.

_Input Format_

The input is just one positive integer $k$.

_Constraints_

* $1 \le k < 10^7$

_Output Format_

Print the least number $x$ such that $x!$ ends with at least $k$ zeroes.

_Sample Input_

```
1
```

_Sample Output_

```
5
```

_Explanation_

 It is easy to calculate that $5!=120$ while $n!$ does not end with a zero for any $n<5$.