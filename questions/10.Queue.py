# 10. Implementazione dei metodi push e pop per una coda (sequenza di nodi)

# ----------------------------------------------------- #

class Node:

    def __init__(self, key, prev_e=None, next_e=None):

        self.prev_e = prev_e
        self.key = key
        self.next_e = next_e


class MyQueue:

    def __init__(self):

        # init empty queue
        self.head = None
        self.tail = None
        self.length = 0

# ----------------------------------------------------- #

    def isEmpty(self):
        return self.length == 0

    def push(self, key):

        elem = Node(key)

        # empty queue -> head and tail point to the same node
        if self.isEmpty():
            self.head = elem
            self.tail = elem
        else:
            # else extend the queue
            self.tail.next_e = elem
            elem.prev_e = self.tail
            # update the value of the tail
            self.tail = elem

        self.length += 1

    def pop(self):

        if self.isEmpty():
            return None

        # get the current head
        elem = self.head
        # extract the key
        key = elem.key
        # shorten head
        self.head = self.head.next_e
        # update length
        self.length -= 1
        # possibly update tail
        if self.length <= 1:
            self.tail = self.head
        # detach elem
        elem.prev_e = None
        elem.next_e = None
        return key


"""Complexity:
    - time: O(1)
    - space: O(1)
"""
