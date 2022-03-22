# Programming 2 &ndash; PHW5


**5.1.** (5 points) NumPy problem, see ReCodEx for description.

**5.2.** (5 points) The local ice cream shop is offering a huge discount. Needless to say they are overwhelmed by customers. The shop recorded the times when each customer came and also the time it took to serve them.

Given a positive integer $N$, the number of customers, and for every $i<N$ a pair $(x_i, y_i)$ of integers, where $x_i$ is the time when customer $i$ stood in line (the number of minutes after the shop opened) and $y_i$ is the number of minutes it took to serve him. What was the longest queue throughout the day?

_Input Format_

The first line contains a positive integer $N$, then $N$ lines follow and the $i$-th line contains contains two integers $x_i, y_i$.

_Constraints_

* $1 \le N < 10^6$
* $1 \le x_i < 10^6$
* $1 \le y_i < 10^3$
* $i \neq j \to x_i \neq x_j$

_Note_

The enumeration of the pairs need not be in the order the customers came, i.e. if $i<j$ we do not necessarily have $x_i < x_j$. Also, in a situation when a customer comes at time $T$ and another customer is being served exactly until $T$ consider the arriving customer as being in line.

_Output Format_

Print the the longest queue that occurred.

_Sample Input_

```
3
1 1
9 1
2 2
```

_Sample Output_

```
1
```

_Explanation_

For easier explanation assume the ice cream shop opened at 1pm. The first customer came at 1:01pm and stayed there until 1:02pm, during that time the second customer came, specifically at 1:02pm, he waited until the first customer is served (technically he had to stand in line) and left at 1:06pm, then when the third and last customer came at 1:09pm no one was there so they did not have to stand in line. Hence the only time a queue was formed was when the second customer came and he was alone in the queue.