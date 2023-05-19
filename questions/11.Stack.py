# 11. Implementazione dei metodi push e pop per una pila (sequenza di nodi)

# ----------------------------------------------------- #

class Node:

    def __init__(self, key, prev_e=None, next_e=None):

        self.prev_e = prev_e
        self.key = key
        self.next_e = next_e


class MyStack:

    def __init__(self):

        # init empty stack
        self.head = None
        self.length = 0

# ----------------------------------------------------- #

    def isEmpty(self):
        return self.length == 0

    def push(self, key):

        elem = Node(key)

        # empty stack -> head point to the same node
        if self.isEmpty():
            self.head = elem
        else:
            # else extend the stack
            self.head.prev_e = elem
            elem.next_e = self.head
            self.head = elem

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

        return key


"""Complexity:
    - time: O(1)
    - space: O(1)
"""
