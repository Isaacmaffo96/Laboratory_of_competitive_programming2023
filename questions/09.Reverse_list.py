# 9. Inversione di una lista evitando l’allocazione di nuovi nodi

# Definition for singly-linked list.
# class Node:
#     def __init__(self, key=None):
#         self.key = key
#         self.nextNode = None


"""Reverse the list (in-place, no new Node allocations)"""
def reverse(head):

    if not head or not head.nextNode:
        return head

    leftNode = None
    centerNode = head
    rightNode = head.nextNode

    while rightNode:
        centerNode.nextNode = leftNode
        leftNode = centerNode
        centerNode = rightNode
        rightNode = rightNode.nextNode

    centerNode.nextNode = leftNode
    head = centerNode

    return head


"""Complexity:
    - time: O(n)
    - space: O(1)
"""

# -------------------------------------- #

class mLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    """Reverse the list (in-place, no new Node allocations)"""
    def reverse(self):

        if self.length <= 1:
            return

        leftNode = None
        centerNode = self.head
        rightNode = self.head.nextNode

        while rightNode:
            centerNode.nextNode = leftNode
            leftNode = centerNode
            centerNode = rightNode
            rightNode = rightNode.nextNode

        centerNode.nextNode = leftNode
        self.head = centerNode


"""Complexity:
    - time: O(n)
    - space: O(1)
"""
