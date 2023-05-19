# 8. Data una lista di nodi, rilevare la presenza di cicli (fast and slow pointers)

# Definition for singly-linked list.
# class Node:
#     def __init__(self, key=None):
#         self.key = key
#         self.nextNode = None


"""Returns True if there is a cycle in the list"""
def detect_cycle(head):

    if not head or not head.nextNode:
        return False

    slow = fast = head

    while fast:
        fast = fast.nextNode
        if not fast:
            break
        if fast == slow:
            return True
        fast = fast.nextNode
        slow = slow.nextNode
        if fast == slow:
            return True

    return False


"""Complexity:
    - time: O(n)
    - space: O(1)
"""


# def detect_cycle(head):
#
#     fast = slow = head
#
#     while fast and fast.nextNode:
#         fast = fast.nextNode.nextNode
#         slow = slow.nextNode
#         if fast == slow:
#             return True
#
#     return False

# -------------------------------------- #

class mLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    """Returns True if there is a cycle in the list"""
    def detectCycle(self):
        if self.length == 0:
            return False

        fast = self.head
        slow = self.head

        while fast:
            fast = fast.nextNode
            if fast == slow:
                return True
            slow = slow.nextNode
            if fast is None:
                break
            fast = fast.nextNode
            if fast == slow:
                return True

        return False


"""Complexity:
    - time: O(n)
    - space: O(1)
"""
