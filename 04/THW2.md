# Programming 2 &ndash; THW2

**2.1.** (5 points) Consider the following program, where `A` is an array of integers:

```python
def fsort(A):
    for i in range(len(A)-1):
        for j in range(i, len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

```
Given a natural number $n$ decide whether the previous algorithm correctly sorts any array of size $n$. Try to sketch a general counterexample for those $n$ for which there is a counterexample.

---

**2.2.** (3 points) Propose an effective algorithm to find the prime decomposition of a given natural number and prove its correctness.

---

**2.3.** (2 points) A sorting algorithm is stable if elements with the same value appear in the same order in the sorted list as they do in the original list.

Say we want to sort cards by their rank, so while sorting their suit is being ignored. This allows the possibility of multiple different correctly sorted versions of the original list. Stable sorting algorithms choose one of these, according to the following rule: if two items compare as equal (like the two 5 cards), then their relative order will be preserved, i.e. if one comes before the other in the input, it will come before the other in the output.

The following depicts a stable sort:
```
[[5, 'hearts'],
[2, 'diamonds],
[7, 'spades'],
[5, 'clubs']]
-->
[[2, 'diamonds],
[5, 'hearts'],
[5, 'clubs'],
[7, 'spades']]
```
while this is not stable:
```
[[5, 'hearts'],
[2, 'diamonds],
[7, 'spades'],
[5, 'clubs']]
-->
[[2, 'diamonds],
[5, 'clubs'],
[5, 'hearts'],
[7, 'spades']]
```

Decide whether Merge sort (as introduced in the lecture) is stable. If not, how to change the algorithm so that it becomes stable. In both cases prove your claim.