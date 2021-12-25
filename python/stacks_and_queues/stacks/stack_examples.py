
from typing import Collection


class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self) -> None:
        self._data = []

    def empty(self) -> bool:
        return len(self._data) == 0

    def max(self) -> int:
        return self._data[-1][1]

    def push(self, x: int) -> None:
        self._data.append(
            (x, x if self.empty() else max(self.max(), x)))

    def pop(self) -> int:
        return self._data.pop()[0]


def print_link_list_in_reverse(head: ListNode) -> None:
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next

    while nodes:
        print(nodes.pop())


def driver():
    # nodeA = ListNode(1)
    # nodeA.next = ListNode(2)
    # nodeA.next.next = ListNode(3)
    # print_link_list_in_reverse(nodeA)

    stack = Stack()
    stack.push(1)
    stack.push(9)
    stack.push(3)
    stack.push(2)
    stack.push(13)
    stack.push(94)
    stack.push(14)

    print(stack.max())
    stack.pop()
    print(stack.max())
    stack.pop()
    print(stack.max())
    stack.pop()
    print(stack.max())


if __name__ == "__main__":
    driver()
