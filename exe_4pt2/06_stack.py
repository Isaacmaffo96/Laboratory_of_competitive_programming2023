if __package__:
    from .TestHelper import test
else:
    from TestHelper import test
    
from io import StringIO

class Node:

    def __init__(self, key, prev_e=None, next_e=None):

        self.prev_e = prev_e
        self.key = key
        self.next_e = next_e

    def __str__(self):

        return self.key + " -> "


class MyStack:

    def __init__(self):

        # init empty stack
        self.head = None
        self.length = 0

    def isEmpty(self):

        return self.length == 0

    def __len__(self):

        return self.length

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

    def __str__(self) -> str:

        objstr = StringIO()

        curr = self.head
        while curr:
            objstr.write(str(curr))
            curr = curr.next_e

        objstr.write("None")

        return objstr.getvalue()


# init
stack = MyStack()
print("Init stack: {}".format(stack))
print("---")

print("Length: {}".format(len(stack)))
print("---")

# push
keys = ["Bob", "Alice", "Eve", "Sarah"]
for key in keys:
    test(stack, "push", key=key)
test(stack, "__len__")

# pop
for _ in range(5):
    test(stack, "pop")
test(stack, "__len__")    
