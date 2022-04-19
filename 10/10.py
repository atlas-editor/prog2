def partition(arr, low, high):
    pivot = arr[high]
    less_than_pivot = []
    greater_than_pivot = []

    for i in range(low, high):
        if arr[i] <= pivot:
            less_than_pivot.append(arr[i])
        else:
            greater_than_pivot.append(arr[i])

    arr[low:high+1] = less_than_pivot + [pivot] + greater_than_pivot

    pivot_idx = low + len(less_than_pivot)

    return pivot_idx


def quicksort(arr, low, high):
    if low >= high:
        return

    pivot_idx = partition(arr, low, high)

    quicksort(arr, low, pivot_idx-1)
    quicksort(arr, pivot_idx+1, high)


arr = [4, 1, 5, 2, 6, 3, -1, 11, 2, 22]
quicksort(arr, 0, len(arr)-1)
# print(arr)

# # in-place partition

# def partition_in_place(arr, low, high):
# 	i = (low-1)		 # index of smaller element
# 	pivot = arr[high]	 # pivot

# 	for j in range(low, high):

# 		# if current element is smaller than or equal to pivot
# 		if arr[j] <= pivot:

# 			# increment index of smaller element
# 			i = i+1
# 			arr[i], arr[j] = arr[j], arr[i]

# 	arr[i+1], arr[high] = arr[high], arr[i+1]
# 	return i+1


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def balanced_tree(arr):
	"""
	construct a balanced binary tree from a given sorted array
	"""

	if not arr:
		return None

	mid = (len(arr)) // 2

	root = Node(arr[mid])
	root.left = balanced_tree(arr[:mid])
	root.right = balanced_tree(arr[mid+1:])

	return root


a = [3, 7, 9, 12, 14, 16, 24]
root = balanced_tree(a)


def preorder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder(node.left)

    preorder(node.right)

# preorder(root)


def tree_min(node):
	"""
	return the smallest element in a binary search tree
	"""

	if node.left is None:
		return node
	return tree_min(node.left)

# print(tree_min(root))


def tree_delete(node, val):
    """
    delete a node from a binary search tree with value `val`
    """
    if node is None:
        return

    if val < node.data:
        node.left = tree_delete(node.left, val)
    if val > node.data:
        node.right = tree_delete(node.right, val)
    if val == node.data:
        if node.left is None and node.right is None:
            return
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        _min = tree_min(node.right)

        node.data = _min.data
        node.right = tree_delete(node.right, _min.data)
    return node

# tree_delete(root, 24)
# tree_show(root)


def preorder_with_tabs(node, gen=0):
    if node is None:
        return
    tmp = (gen*" ") + str(node.data)
    print(tmp)
    preorder_with_tabs(node.left, gen+1)
    preorder_with_tabs(node.right, gen+1)

# preorder_with_tabs(root)


def contains(node, val):
	if node is None:
		return False
	if node.data == val:
		return True
	if node.data < val:
		return contains(node.right, val)
	else:
		return contains(node.left, val)

# print(contains(root, 3))
# print(contains(root, 99))


def contains_iterative(node, val):
	current = node

	while current is not None:
		if current.data == val:
			return True
		if current.data < val:
			current = current.right
		else:
			current = current.left

	return False

# print(contains_iterative(root, 3))
# print(contains_iterative(root, 99))


def height(node):
	if node is None:
		return 0
	return max(height(node.left), height(node.right)) + 1

# print(height(root))


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
    """
    construct a tree from a string representation
	"""
    root_idx = index_of_root(s)

    bracket_after_root = s.index(
        '(', root_idx) if '(' in s[root_idx:] else len(s)

    root = Node(int(s[root_idx:bracket_after_root]))

    if s[0] == '(':
        root.left = from_string(s[1:root_idx-1])
    if s[-1] == ')':
        root.right = from_string(s[bracket_after_root+1:-1])

    return root

s = "((2)7((5)6(11)))2(5((4)9))"
r = from_string(s)
# preorder_with_tabs(r)