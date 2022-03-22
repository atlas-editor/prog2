from __future__ import annotations


class Node:

    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node

    def appendleft(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def pop(self) -> Node:
        current = self.head

        while current is not None:
            if current.next is not None and current.next.next is None:
                last_element = current.next
                current.next = None
                return last_element
            current = current.next

    def popleft(self) -> Node:
        if self.head is None:
            return

        head = self.head
        self.head = self.head.next
        return head

    def reverse(self) -> None:
        predecessor = None
        current = self.head
        while current is not None:
            successor = current.next
            current.next = predecessor
            predecessor = current
            current = successor
        self.head = predecessor

    def __str__(self) -> str:
        current = self.head

        if current is None:
            return '(empty)'

        result = ''

        while current is not None:
            result += f'{current.data} -> '
            current = current.next

        return result[:-4]
