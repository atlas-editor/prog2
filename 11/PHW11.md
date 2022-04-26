# Programming 2 &ndash; PHW11

**11.2.** (5 points) Using BFS one can find shortest paths from a given vertex to any other vertex.

Given an undirected graph `G`, your task is to implement an algorithm for finding all vertices `v` which are at distance `k` from a given source vertex.

_Input Format_

The first line contains an integer `m` specifying the number of edges in the graph. Next, `m` lines follow specifying each edge, each line consists of space separated strings. Then one last line follows with a name of the source vertex and a given distance `k` (these values are also space separated).

_Constraints_

* $1 \le m < 10^6$
* $1 \le k < 1000$

_Output Format_

Print the name of each vertex `v` which is at distance `k` from the given source vertex. Each vertex has to be printed on a new line but the order in which you print the vertices can be arbitrary.

_Sample Input_

```
3
A B
A C
A D
A 1
```

_Sample Output_

```
B
C
D
```

_Explanation_

The graph which is created from the input is a star graph with center `A` and leaves `B`, `C`, `D`. Hence the vertices at distance 1 from `A` are exactly the leaves.

---

**11.2.** (5 points) Using BFS (or DFS) one can also decide whether a graph contains a cycle or not.

Given an undirected graph `G`, your task is to implement an algorithm for deciding whether `G` contains a cycle or not. Note that `G` need not be connected.

_Input Format_

The first line contains an integer `m` specifying the number of edges in the graph. Next, `m` lines follow specifying each edge, each line consists of space separated strings.

_Constraints_

* $1 \le m < 10^6$

_Output Format_

Print `YES` if the specified graph contains a cycle. In case the graph is acyclic print `NO`.

_Sample Input_

```
2
A B
C D
```

_Sample Output_

```
NO
```

_Explanation_

The graph which is created from the input is a disjoint union of two edges hence a forest, so acyclic.