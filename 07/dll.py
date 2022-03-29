from __future__ import annotations


class Node:
    def __init__(self, data: int, previous: Node = None, next: Node = None) -> None:
        self.data = data
        self.previous = previous
        self.next = next


class LinkedList:
    def __init__(self, node: Node) -> None:
        self.head = node
        self.tail = node

    def addleft(self, node: Node):
        node.next = self.head
        self.head.previous = node
        self.head = node

    def addright(self, node: Node) -> None:
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def __str__(self):
        curr = self.head
        result = ''
        while curr is not None:
            result += f'{curr.data} <-> '
            curr = curr.next

        return result

    def add(self, node, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        node.next = current.next
        current.next = node
        if node.next is not None:
            node.next.previous = node
        node.previous = current

    def f(self, node):
        if node is None:
            return

        self.f(node.next)

        print(node.data, end=" ")

    def sum(self):
        res = 0

        curr = self.head

        while curr is not None:
            res += curr.data
            curr = curr.next

        return res

    def recursive_sum_helper(self, node, temp_sum):
        if node is None:
            return temp_sum
        temp_sum += node.data
        return self.recursive_sum_helper(node.next, temp_sum)

    def recursive_sum(self):
        return self.recursive_sum_helper(self.head, 0)

    def print2(self, node, tp=0):
        tp += 1
        if node is None:
            return
        if tp % 2 == 0:
            print(f"{node.data} ")

        return self.print2(node.next, tp)

    def print2v2(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        if node.next is None:
            return
        self.print2v2(node.next.next)

    def contains(self, node, val):
        if node is None:
            return False
        if node.data == val:
            return True
        return self.contains(node.next, val)


# a = Node(1)

# ll = LinkedList(a)

# for i in range(10):
#     ll.addleft(Node(i))

# print(ll)

# ll.add(Node(37), 10)
# print(ll)

# print()

# print(ll.sum())

# print(ll.recursive_sum(ll.head, 0))


# ll.print2(ll.head)
# ll.print2v2(ll.head)
# print(ll.contains(ll.head, 37))
# print(ll.contains(ll.head, -5))
