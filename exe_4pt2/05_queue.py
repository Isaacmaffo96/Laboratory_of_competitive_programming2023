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


class MyQueue:

    def __init__(self):

        # init empty queue
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):

        return self.length == 0

    def __len__(self):

        return self.length

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
queue = MyQueue()
print("Init queue: {}".format(queue))
print("---")

print("Length: {}".format(len(queue)))
print("---")

# push
keys = ["Bob", "Alice", "Eve", "Sarah"]
for key in keys:
    test(queue, "push", key=key)
test(queue, "__len__")

# pop
for _ in range(5):
    test(queue, "pop")
test(queue, "__len__")    
