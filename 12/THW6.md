# Programming 2 &ndash; THW6

**6.1.** (3 points) An independent set of an undirected graph `G = (V, E)` is a set of vertices `U`
such that no edge in `E` is incident to two vertices of `U`.

Give an `O(|V|)` algorithm for ﬁnding a maximum-size independent set if G is a tree.

_Hint:_ If `G` is a tree and `v` is a leaf in `G`, then there exists a maximal cardinality independent set containing `v`. Prove this.

---

**6.2.** (2 points) Suppose that you are given a sorted sequence of distinct integers. Give an `O(log(n))` algorithm to determine whether there is a fixed point in the sequence, i.e. an element whose index is equal to its value.

---

**6.3.** (3 points) Suppose you are given a set of coin denominations and a number `S`. Using dynamic programming to devise an efficient algorithm for ﬁnding the minimum number of coins whose values sum up to exactly `S`, if possible.

---

**6.4.** (2 points) Find an algrithm for generating all possible topological orderings of a given directed acyclic graph.

---

***6.5.** (2 points) Consider the following problem: given a set of positive integers $S = \{s_0 , \ldots, s_{n-1} \}$ find a subset $I \subseteq S$ such that
$$\sum_{i \in I} s_i = \sum_{i \in S \setminus I} s_i$$
Let $M = \sum_{i \in S} s_i$. Give an $O(n \cdot M)$ dynamic programming algorithm to find $I$.