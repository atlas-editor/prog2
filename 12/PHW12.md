# Programming 2 &ndash; PHW12

**12.1.** (3 points) The problem of finding complete subgraphs, the so called _clique problem_, is known to be NP-complete, which is to say that there is no known effective algorithm for solving it.

Given an undirected graph `G`, your task is to find the size of the largest complete subgraph of `G`, i.e. the number of vertices in some maximum clique of `G`.

_Input Format_

The first line contains an integer `m` specifying the number of edges in the graph. Next, `m` lines follow specifying each edge, each line consists of space separated strings.

_Constraints_

* $1 \le m < 5000$

_Output Format_

Print an integer which is the size of some largest maximal clique in `G`.

_Sample Input_

```
4
A B
A C
B D
B E
```

_Sample Output_

```
2
```

_Explanation_

The graph which is created from the input is a tree, hence without cycles (in particular without triangles), with at least one edge. Thus the largest maximal cliques are edges, i.e. $K_2$.

---

**12.2.** (4 points) Artemis is interested in specific paths in her garden. Her garden is square shaped and at every point in the grid there is a peach tree and she knows how many peaches there are or any given tree. She wants to find a path via her garden starting in the bottom left corner and ending in the top right corner with the property that the sum of peaches on the path is maximal possible.

Given a 2D array `O[][]` of size `n` (the first coordinate specifies the row and the second coordinate the column) describing the number of peaches on any tree in the grid find the optimal route maximizing the number of peaches and the sum of the peaches on this route.

A path `P` in the array `O` is a sequence of coordinates starting at `(n-1, 0)` and ending at `(0, n-1)` such that if `P(k) = (i,j)`, then `P(k+1) = (i-1,j)` or `P(k+1) = (i,j+1)`.

_Input Format_

The first line contains an integer `n` specifying the size of the square array `O[][]`, then `n` lines follow describing each row in the array.

_Constraints_

* $1 \le n < 1000$

_Output Format_

On the first line print the sum of the peaches on the optimal route and then print `2n-1` lines specifying the optimal route from `(n-1, 0)` to `(0, n-1)`. Each line is a space separated pair of integers giving the coordinates of the route. The optimal route is maximizing the expression:

$$
\sum_{(i,j) \in P} O[i][j]
$$

_Note_

Each problem has a unique solution.

_Sample Input_

```
3
1 5 5
1 5 1
5 5 1
```

_Sample Output_

```
25
2 0
2 1
1 1
0 1
0 2
```

_Explanation_

From the picture it's obvious that the optimal path is via all the nodes with value `5`, hence the output.

---

**12.3.** (3 points) "Cave problem" in ReCodEx; must be solved using DFU.