# 7. Implementazione di una lista utilizzando una sequenza di nodi (funzioni set, append, deleteAt)

# ----------------------------------------------------- #

class Node:
    def __init__(self, key=None):
        self.key = key
        self.nextNode = None


class mLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

# ----------------------------------------------------- #

    """Insert a new element at the beginning of the list.
        Complexity:
            -time: O(1)
            -space: O(1)"""
    def prepend(self, key):

        newHead = Node(key)
        newHead.nextNode = self.head
        self.head = newHead
        self.length += 1

    """Add key to the list at position idx. 
        Raises runtime exception if idx falls outside of the list
        Complexity:
            -time: O(n)
            -space: O(1)"""
    def set(self, key, idx):

        if self.length < idx:
            raise RuntimeError(f"idx {idx} outside of the list")

        newNode = Node(key)

        if idx == 0:
            self.prepend(key)
            return

        pos = 0
        currNode = self.head
        while pos < idx - 1:
            currNode = currNode.nextNode
            pos += 1

        newNode.nextNode = currNode.nextNode
        currNode.nextNode = newNode
        self.length += 1

    """Append a key to the end of the list
        Complexity:
            -time: O(n)
            -space: O(1)"""
    def append(self, key):

        newNode = Node(key)

        if not self.head:
            self.head = newNode
            self.length += 1
            return

        currNode = self.head
        while currNode.nextNode:
            currNode = currNode.nextNode

        currNode.nextNode = newNode
        self.length += 1

    """Delete element at position idx. No error message if idx falls
        outside of the list
        Complexity:
            -time: O(n)
            -space: O(1)"""
    def deleteAt(self, idx):

        if idx > self.length - 1:
            return

        if idx == 0:
            self.head = self.head.nextNode
            self.length -= 1
            return

        pos = 0
        currNode = self.head
        while pos < idx - 1:
            currNode = currNode.nextNode
            pos += 1

        if pos + 2 == self.length:
            currNode.nextNode = None
        else:
            currNode.nextNode = currNode.nextNode.nextNode
        self.length -= 1


"""Complexity (set, append, deleteAt):
    -time: O(n)
    -space: O(1)
"""
