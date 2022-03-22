# Programming 2 &ndash; PHW6


**6.1.** (10 points) Create a class `LinkedList` which implements a linked list and several methods: `appendleft`, `duplicate_elements`, `make_increasing` and `merge`.

Below is the structure of the class and your task is to implement the given methods as described in their docstrings.

```python
from __future__ import annotations


class Node:
    """
    Class representing a node which holds some specified data and is pointing to another Node object (or None).
    """

    def __init__(self, data: int, next: Node = None) -> None:
        """
        The constructor: initializes a node with given data.

        :param data: the data the node will hold
        :param next: the node the current node is pointing to
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Class implementing a linked list.
    """

    def __init__(self, head: Node = None) -> None:
        """
        The constructor: initializes a linked list with a given node.

        :param head: the only node (and hence head) of the created linked list
        """
        self.head = head

    def appendleft(self, node: Node) -> None:
        """
        Add a new element to the linked list from the left, i.e. replace the head  with the new element and alter the pointers accordingly.

        :param node: the node we are adding
        """
        pass

    def duplicate_elements(self, lower: int, upper: int) -> None:
        """
        Duplicate every node in the linked list whose `data` variable holds a value in the inclusive range [lower, upper].

        :param lower: the integer specifying the lower bound of the range (it is included in the range)
        :param upper: the integer specifying the upper bound of the range (it is included in the range)
        """
        pass

    def make_increasing(self) -> None:
        """
        A method to make the linked list increasing in the following sense: if it's empty do nothing, else leave the head in the list and for every node, x, you leave in the list it holds that it's value is larger than the value of the previous node, y, and no node between y and x has this property.

        :example: (5 -> 1 -> 3 -> 6 -> 5 -> 9) is transformed into (5 -> 6 -> 9)
        """
        pass

    def merge(self, other: LinkedList) -> LinkedList:
        """
        A method to merge two sorted linked lists together.

        :param other: the other linked lists to be merged with self
        :return: return a new linked lists whose head references the first node in the merged list
        """
        pass

    def __str__(self) -> str:
        """
        Return a nice string representation of the linked list.

        :return: string representing the linked list
        """
        current = self.head

        if current is None:
            return '(empty)'

        result = ''

        while current is not None:
            result += f'{current.data} -> '
            current = current.next

        return result[:-4]


```

_Task_

Your task to implement the methods in the class `LinkedList` and upload it as `linked_list.py`. Do not print anything into the console and do not rename the class name or any of the method names. You can, however, add helper methods into your implementation.

_Sample Usage_

```python
>>> ll = LinkedList()
>>> ll.appendleft(Node(7))
>>> ll.appendleft(Node(1))
>>> ll.appendleft(Node(3))
>>> print(ll)
3 -> 1 -> 7
>>> ll.duplicate_elements(3,6)
>>> print(ll)
3 -> 3 -> 1 -> 7
>>> ll.make_increasing()
3 -> 7
>>> ll2 = LinkedList()
>>> ll2.appendleft(Node(5))
>>> ll2.appendleft(Node(1))
>>> print(ll.merge(ll2))
1 -> 3 -> 5 -> 7
```

_Explanation_

First we add three elements into the linked list `ll` and as we are adding them from left we get the linked list `3 -> 1 -> 7`. Then we duplicate each element whose value is in the closed range $[3,6]$ and after that apply the `make_increasing` method (this makes the list strictly increasing) to arrive at `3 -> 7`. Finally we merge it with the list `1 -> 5` and get `1 -> 3 -> 5 -> 7`.

_Note_

You can assume correct inputs in the `merge` method, i.e. you do not have to handle the situation if the input lists are not sorted. Also note the typing annotation, e.g. the input for the `appendleft` method is not an integer but an actual `Node` object.