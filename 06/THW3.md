# Programming 2 &ndash; THW3

**3.1.** (3 points) Let `D` be a data structure working on integers which implements two operations `insert` and `extract_min`, where `insert` inserts a given integer into `D` and the method `extract_min` returns the least element from `D`. Prove that if $n$ is the number of elements stored in `D` then the asymptotic complexity of `insert` or `extract_min` must be $\Omega(\log(n))$.

---

**3.2.** (4 points) Given a linked list, propose an algorithm which decides whether there is a cycle in the list, i.e. either there is a node which points to itself, a pair of nodes pointing to each other, or there are nodes $x, y, z$, such that $x \neq y$ and $x$ points to $z$ as well as $y$ points to $z$. What is the time and space complexity of your algorithm?

---

**3.3.** (3 points) Suppose we represent sets using linked lists. Propose an algorithm which returns the intersection of two sets using this representation and calculate its time and space complexity.

_Note:_ The resulting intersection must use the objects in the two sets, i.e. do not create new nodes.

---

***3.4.** (2 points) Solve problem **3.2.** in linear time and using constant memory.