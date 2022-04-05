def increasing_seq(n, k, start=0, seq=[]):
    """
    print all increasing sequences of length n with values 0, ..., k-1
    """
    for i in range(start, n):
        seq.append(i)
        if len(seq) < k:
            increasing_seq(n, k, i+1, seq)
        else:
            print(seq)
        seq.pop()


def permutations(arr, perm=[]):
    """
    print all permutations of arr
    """
    if len(arr) == 0:
        print(perm)
    else:
        for i in range(len(arr)):
            permutations(arr[:i] + arr[i+1:], perm + arr[i:i+1])


def sum(a, b):
    """
    return the sum of a and b
    """
    if b == 0:
        return a
    return sum(a+1, b-1)


def contains(arr, val):
    """
    return True if val is in arr, False else
    """
    if len(arr) == 0:
        return False
    return arr[0] == val or contains(arr[1:], val)


def contains_v2(arr, val):
    """
    return True if val is in arr, False else

    * better than the previous implementation because the call tree has only height log(len(arr)) BUT STILL WORSE THAN THE ITERATIVE IMPLEMENTATION; even though the theoretical time complexity of both contains and contains_v2 is O(n)
    """
    if len(arr) == 0:
        return False

    mid = len(arr)//2
    return arr[mid] == val or contains_v2(arr[:mid], val) or contains_v2(arr[mid+1:], val)

# from turtle import *

# speed(0)
# left(90)

# angle = 30


# def fractal_tree(size, level):

#     if level > 0:

#         forward(size)

#         right(angle)

#         fractal_tree(0.8 * size, level-1)

#         left(2 * angle)

#         fractal_tree(0.8 * size, level-1)

#         right(angle)

#         forward(-size)


# fractal_tree(80, 7)
