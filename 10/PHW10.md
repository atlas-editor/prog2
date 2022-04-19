# Programming 2 &ndash; PHW10

**10.1.** (10 points) Luna wants to count the number of her offsprings who have at least $k$ older siblings.


Given a description of a family tree in the following recursive format:

`PERSON(CHILD_0(family_tree(CHILD_0))CHILD_1(family_tree(CHILD_1))...CHILD_N-1(family_tree(CHILD_N-1)))`

where the enumeration `(CHILD_i)_i<N` of the children of `PERSON` is in ascending order by age in the description.

If a descendant in the description does not have any children her name is followed by parentheses enclosing the empty string, e.g. the description of a family tree of a person named Melina who has no children is: `Melina()`.

Your task is to calculate the number of people in the family tree who have at least $k$ older siblings.

_Input Format_

The first line contains an integer $k$ and the second line contains a description of a family tree as defined above.

_Note_



_Constraints_

* $1 \le k \le 10$
* $1 \le \text{height of family tree} \le 9$
* $0 \le \text{number of siblings of a person} \le 11$

_Output Format_

Print the number of people in the family tree who have at least $k$ older siblings.

_Sample Input_

```
1
Luna(Ophelia(Mabel()Ruby())Eloise(Nova())Freya())
```

_Sample Output_

```
3
```

_Explanation_

The family tree that is built from the given description looks like this:

```
Luna
├── Ophelia
│   ├── Mabel
│   └── Ruby
├── Eloise
│   └── Nova
└── Freya
```

Since the siblings are enumerated by age we have that Ophelia is the youngest, Eloise the middle child and Freya the oldest daughter of Luna so 2 of her children (Ophelia and Eloise) have at least 1 older sibling (Freya). Now looking deeper into the family tree Ophelia has two children, Mabel and Ruby, and only Mabel has an older sibling (Ruby). Lastly, Eloise has only one daughter, Nova, and so she does not have an older sibling. To sum up, the offsprings of Luna who have at least one older sibling are Ophelia, Eloise and Mabel.