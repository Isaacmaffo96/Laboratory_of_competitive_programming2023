"""Linked list implementation
"""

from io import StringIO
"""
An element in the linked list
"""


class Node:

    def __init__(self, key=None):
        self.key = key
        self.nextNode = None

    def __str__(self):
        return str(self.key)


class mLinkedList():

    def __init__(self):

        self.head = None
        self.length = 0

    def __len__(self):
        """Returns the length of the list"""

        return self.length

    def __str__(self):
        """Returns the linked list str representation"""

        if self.head is None:
            return str(None)

        s = StringIO()

        currNode = self.head
        while currNode:
            s.write(str(currNode))
            s.write(" -> ")
            currNode = currNode.nextNode

        s.write(str(None))

        return s.getvalue()

    def prepend(self, key):
        """Adds a new key at the beginning of the list"""

        newHead = Node(key)
        newHead.nextNode = self.head
        self.head = newHead
        self.length += 1

    def append(self, key):
        """Appends a key to the end of the list"""

        if self.head is None:
            self.head = Node(key)
            self.length += 1
            return

        currNode = self.head
        while currNode:
            if currNode.nextNode is None:
                currNode.nextNode = Node(key)
                self.length += 1
                return
            currNode = currNode.nextNode

    def set(self, key, idx):
        """Adds key to the list at position idx. Raises runtime
       exception if idx falls outside of the list"""

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

    def get(self, idx: int):
        """Returns the node at a given index. Indexes start from
           0. None is returned if index is not found """

        ctr = 0
        currNode = self.head

        while ctr != idx:
            if currNode:
                currNode = currNode.nextNode
            else:
                return None
            ctr += 1

        return currNode

    def deleteAt(self, idx):
        """Deletes element at position idx. No error message if idx
       falls outside of the list"""

        if idx > self.length - 1:
            return

        if idx == 0:
            toDelete = self.head
            self.head = self.head.nextNode
            self.length -= 1
            del toDelete
            return

        pos = 0
        currNode = self.head
        while pos < idx - 1:
            currNode = currNode.nextNode
            pos += 1

        toDelete = currNode.nextNode
        currNode.nextNode = currNode.nextNode.nextNode
        del toDelete
        self.length -= 1

    def reverse(self):
        """Reverses the list (in-place, no new Node allocations)"""

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

    def detectCycle(self):
        """Returns True if there is a cycle in the list"""
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


"""
Run a test and format output

:obj: object instance
:methodName: name of the method to be run
:printList: turn on/off linked list print
:params: optional name parameters for the method
"""


def test(obj, methodName, printList=True, **params):

    # print test params
    print("Method:\t{}".format(methodName), end="")
    if params:
        print(", Params: [", end="")
        for p, v in params.items():
            print(" {}:{} ".format(p, v), end="")
        print("]", end="")
    print()

    # get method
    m = getattr(obj, methodName)

    # run the test
    result = None
    try:
        # equivalent to l.methodName(p1, p2, p3, ...)
        result = m(*params.values())
    except RuntimeError as e:
        print("Runtime error: " + str(e))

    # print test result
    print("Result:\t{}".format(result))
    if printList:
        print("List:\t{}".format(obj))
    print("---")


"""
Some tests
"""
l = mLinkedList()

# str
print("List:\t{}".format(l))
print("---")

# len
print("Length:\t{}".format(len(l)))
print("---")

# append
print("Perform 10 append operations")
for i in range(1, 11):
    l.append(i * 10)
print("List:\t{}".format(l))
print("---")

# get
test(l, "get", idx=0)
test(l, "get", idx=3)
test(l, "get", idx=10)

# prepend
test(l, "prepend", key=111)

# len
test(l, "__len__")  # equivalent to len(l)

# set
test(l, "set", key=77, idx=20)
test(l, "set", key=77, idx=0)
test(l, "set", key=78, idx=7)
test(l, "set", key=79, idx=13)

# delete
test(l, "deleteAt", idx=20)
test(l, "__len__")
test(l, "deleteAt", idx=0)
test(l, "__len__")
test(l, "deleteAt", idx=6)
test(l, "__len__")
test(l, "deleteAt", idx=len(l) - 2)
test(l, "__len__")
test(l, "deleteAt", idx=len(l) - 1)
test(l, "__len__")

# reverse
test(l, "reverse")

# detectCycle
test(l, "detectCycle")

# let's create a cycle in the list
last_idx = len(l) - 1
last_node = l.get(last_idx)
second_to_last_node = l.get(last_idx - 1)
last_node.nextNode = second_to_last_node
# repeat the test
test(l, "detectCycle", printList=False)
# just to confirm detectCycle works as intended
test(l, "detectCycle")
