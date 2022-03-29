Create a class `DoublyLinkedList` which implements a doubly linked list and several methods: `appendleft`, `append`, `reverse`, `string_reverse` and `special_sum`.

Below is the structure of the class and your task is to implement the given methods as described in their docstrings.

_Constraints_

The methods: `print_reverse` and `special_sum` must be implemented **recursively**.

```python
from __future__ import annotations


class Node:
    """
    Class representing a node which holds some specified data and is pointing to two other Node objects (or None), usually thought of as nodes preceding and succeeding the given node.
    """

    def __init__(self, data: int, prev: Node = None, next: Node = None) -> None:
        """
        The constructor: initializes a node with given data.

        :param data: the data the node will hold
        :param prev: the node preceding the current node
        :param next: the node succeeding the current node
        """
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """
    Class implementing a doubly linked list.
    """

    def __init__(self, node: Node) -> None:
        """
        The constructor: initializes a linked list with a given node.

        :param node: the only node (and hence head and also tail) of the created linked list
        """
        self.head = node
        self.tail = node

    def appendleft(self, node: Node) -> None:
        """
        Add a new element to the linked list from the left, i.e. replace the head with the new element and alter the pointers accordingly.

        :param node: the node we are adding
        """
        pass

    def append(self, node: Node) -> None:
        """
        Add a new element to the linked list from the right, i.e. replace the tail with the new element and alter the pointers accordingly.

        :param node: the node we are adding
        """
        pass

    def reverse(self) -> None:
        """
        Reverse self in the sense that the head becomes the tail and vice versa and alter the pointers accordingly.

        :example: HEAD = 5 <-> 3 <-> 7 <-> 11 <-> 2 = TAIL is transformed into HEAD = 2 <-> 11 <-> 7 <-> 3 <-> 5 = TAIL
        """
        pass

    def string_reverse(self) -> str:
        """
        Return a string containing the values of the nodes in the linked list in reverse. The format should be the following:

        "{node0.data} {node1.data} {node2.data} ... {nodek.data}"

        :example: the linked list 5 <-> 2 <-> 2 <-> 99 <-> 2 should return the string "2 99 2 2 5"
        :note: this method must be implemented recursively
        """
        pass

    def special_sum(self, limit) -> int:
        """
        Return the sum of all values in the nodes of the list where the value is greater than `limit`.

        :note: this method must be implemented recursively
        """
        pass

    def __str__(self) -> str:
        """
        Return a nice string representation of the doubly linked list.

        :return: string representing the doubly linked list
        """
        current = self.head

        if current is None:
            return '(empty)'

        result = ''

        while current is not None:
            result += f'{current.data} <-> '
            current = current.next

        return result[:-5]

```

_Task_

Your task to implement the methods in the class `DoublyLinkedList` and upload it as `doubly_linked_list.py`. Do not print anything into the console and do not rename the class name or any of the method names or their signatures. You can, however, add helper methods into your implementation.

_Sample Usage_

```python
>>> dll = DoublyLinkedList()
>>> dll.appendleft(Node(7))
>>> dll.appendleft(Node(1))
>>> dll.appendleft(Node(3))
>>> dll.append(Node(9))
>>> print(dll)
3 <-> 1 <-> 7 <-> 9
>>> dll.reverse()
>>> print(dll)
9 <-> 7 <-> 1 <-> 3
>>> print(dll.string_reverse())
3 <-> 1 <-> 7 <-> 9
>>> dll.special_sum(3)
17
```

_Explanation_

First we add three elements into the list `dll` from left and one from the right and hence we get: `3 <-> 1 <-> 7 <-> 9`. Then we reverse the doubly linked list and get `9 <-> 7 <-> 1 <-> 3` so now printing out the values in reverse gets us the list we started with. Lastly, we sum over the values greater than 3, i.e. `1+7+9=17`.