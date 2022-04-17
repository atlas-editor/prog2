# Programming 2 &ndash; PHW9

**9.1.** (5 points) Lile is feeling powerless and thought she would feel better if she calculated some powersets.

Given a string $S$ consisting of unique characters (no character occurs twice in $S$) print all subsets (unique substrings) $s$ of $S$, where $s$ must be in alphabetical order.

_Input Format_

The first line contains the string $S$ and the characters in $S$ are in alphabetical order.

_Constraints_

* $1 \le \mathrm{len}(S) \le 15$
* the implementation of the solution must be recursive

_Output Format_

Print every subset of $S$ on a new line, where the individual subsets must be in alphabetical order but the order in which you print the subsets can be arbitrary.

_Note_

The empty set is a subset of every set, i.e. the empty string is a substring of every string.

_Sample Input_

```
ab
```

_Sample Output_

```

a
b
ab
```

_Explanation_

The powerset of the set $\{a,b\}$ is $\{\emptyset, \{ a \}, \{ b \}, \{ a,b \} \}$ so we print each unique substring of `ab`, i.e. `''` (the empty string), `a`, `b` and `ab`.

---

**8.2.** (5 point) Consider the following algorithm:

**Procedure** `BinaryTreeInsert` (inserting a string into a binary tree)

*Input:* root of a binary tree $v$; string $x$ to insert

1. If $v$ is undefined, return a new node with value $x$ and end the procedure.
2. Else if $x$ is lexicographically smaller or equal to the value of the node $v$ let the left successor of $v$ be `BinaryTreeInsert`(left successor of $v$, $x$).
3. Else if $x$ is lexicographically larger than the value of the node $v$ let the right successor of $v$ be `BinaryTreeInsert`(right successor of $v$, $x$).
4. Return the node $v$.


Your task is to implement this procedure. On your input you will be given a space separated sequence of strings and your task is to build a binary tree from them in such a way so that every new string is added into the tree using the procedure `BinaryTreeInsert` in order they appear in the input sequence. Your output will then be the concatenation of all strings in the *preorder* of the binary tree you built, i.e. no spaces between values of different nodes.

_Input Format_

The first line contains a space separated array of strings $S[]$.

_Constraints_

* $1 \le len(S) < 10^5$
* $1 \le len(S[i]) < 10$

_Output Format_

Print the concatenation of all strings in the preorder of the binary tree you built from the sequence $S[]$ using `BinaryTreeInsert`.

_Sample Input_

```
c d ab a
```

_Sample Output_

```
cabad
```

_Explanation_

The binary tree that is built from the given sequence looks like this:

```
    c
   / \
  ab  d
 /  
a 
```

Now using the definition of the preorder we get the sequence: `c`, `ab`, `a`, `d`, hence the output.