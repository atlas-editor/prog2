import math


def permutations(arr, perm=[]):
    if len(arr) == 0:
        print(perm)
    else:
        for i in range(len(arr)):
            permutations(arr[:i] + arr[i+1:], perm + arr[i:i+1])

# permutations([4,5,6])


def brackets(n, S='', left=0, right=0):
    if len(S) == 2 * n:
        print(S)
        return
    if left < n:
        S += '('
        brackets(n, S, left+1, right)
        S = S[:-1]
    if right < left:
        S += ')'
        brackets(n, S, left, right+1)
        S = S[:-1]

# brackets(3)


def subarrays(arr, start=0, end=0):
    if len(arr) == end:
        return

    if start > end:
        subarrays(arr, 0, end+1)
    else:
        print(arr[start:end+1])
        subarrays(arr, start+1, end)

# subarrays([1, 2, 3])


n = 7
a = [n+1] * (n+1)
k = 3
def partition(z, p):
    if k > n:
        print('not possible')
    if z == 0:
        print(a[1:p])
    else:
        for i in range(math.ceil(z/(k-p+1)), min(z-k+p, a[p-1])+1):
            a[p] = i
            partition(z-i, p+1)

# partition(n, 1)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

# preorder(...)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

# inorder(...)


def index_of_root(s):
    if s[0] != '(':
        return 0
    counter = 0
    for i in range(len(s)):
        if s[i] == '(':
            counter += 1
        if s[i] == ')':
            counter -= 1
        if counter == 0:
            return i+1


def from_string(s):
    root_idx = index_of_root(s)

    bracket_after_root_or_end_of_string = s.index(
        '(', root_idx) if '(' in s[root_idx:] else len(s)

    root = Node(int(s[root_idx:bracket_after_root_or_end_of_string]))

    # TODO


s = "((2)7((5)6(11)))2(5((4)9))"
# r = from_string(s)
# preorder(r)