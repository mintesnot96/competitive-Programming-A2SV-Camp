class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        new_node = Node(value)
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.head else -1

    def getRear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
# https://leetcode.com/problems/design-circular-deque/description/
