# Programming 2 &ndash; PHW1

**1.1.** (3 points) Given the students' score sheet for the 'Charles University Codes' competition, you are required to find the third highest score. You are given $n$ scores. Store them in a list and find the third highest score.

_Input Format_

The first line contains $n$. The second line contains an array $A[]$ of $n$ integers each separated by a space.

You can assume that there is always a third highest score, i.e. it does not happen that everyone's score is only one of two values.

_Constraints_

* $2 \le n < 10^4$
* $-100 \le A[i] \le 100$

_Output Format_

Print the third highest score.

_Sample Input_

```
5
2 3 6 6 5
```

_Sample Output_

```
3
```

_Explanation_

The given list is $[2,3,6,6,5]$. The maximum score is $6$, second maximum is $5$ and the third highest score is $3$. Hence, we print $3$ as the output.

---

**1.2.** (3 points) It is opposite day and your boss tasked you with an unusual assignment. He needs you to 'opposite capitalize' the first and last names of people in the database, i.e. the first character of both the first and last name should be lowercase otherwise the characters need to be uppercase. For example, `paul atreides` should be capitalized "correctly" as `pAUL aTREIDES`.

Given a full name, your task is to capitalize the name appropriately.

_Input Format_

A single line of input containing the full name. $S$.

_Constraints_

* $3 \le \mathtt{len}(S) < 1000$
* The string consists of alphanumeric characters and spaces.

_Note:_ in a word only the first character is lowercase. For example `42DOUG` when 'opposite capitalized' remains `42DOUG`.

_Output Format_

Print the 'opposite capitalized' string, $S$.

_Sample Input_

```
XAEA12 Musk
```

_Sample Output_

```
xAEA12 mUSK
```

---

**1.3.** (4 points) Given a natural number $n$ your task is to compute the sum of all _odd_ terms in the Fibonacci sequence divisible by $7$, $F(i)$, not exceeding $n$. The Fibonacci sequence is defined recursively as:

$F(0)=0, F(1)=1$

$F(i+2)=F(i) + F(i+1)$

_Input Format_

A single line of input  containing the natural number $n$.

_Constraints_

* $0 \le n < 4 \cdot 10^6$

_Output Format_

Print the sum of all odd terms of the Fibonacci sequence divisible by $7$ that are less than or equal to $n$.

_Sample Input_

```
8
```

_Sample Output_

```
0
```

_Explanation_

The first few terms of the Fibonacci sequence are: $0,1,1,2,3,5,8,13, \ldots$ The odd terms less than or equal to $8$ are $1,1,3,5$, none of these is divisible by $7$ so we print out $0$.

---

***1.4.** (3 points) Cupid is convinced that two people are destined for each other if and only if the sum of their heights is equal to a magical constant $L$. You are given a list $H[]$ of heights of several beings (including but not limited to humans) of length $n$ and your task is to help Cupid to find out if there is a couple that is destined to each other.

_Input Format_

The first line contains the integer $L$. The second line contains $n$ and the third line contains the array $H[]$ of $n$ integers each separated by a space.

_Constraints_

* $2 \le L < 2*10^6$
* $2 \le n < 10^6$
* $1 \le H[i] < 10^6$

_Output Format_

Print `LOVE` if there are indices $i<j<n$ such that $H[i]+H[j]=L$, else print `NOT TODAY`.

_Sample Input_

```
7
5
1 2 1 3 4
```

_Sample Output_

```
LOVE
```

_Explanation_

The sum of the last two entries is $7$, so $H[3]+H[4]=7$