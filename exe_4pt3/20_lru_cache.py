"""LRU cache implementation."""

from io import StringIO


class Pair:

    def __init__(self, k, r):

        self.key = k
        self.resource = r


class Node:

    def __init__(self, data: Pair):

        self.data = data
        self.nxt = None
        self.prv = None

    def __str__(self):

        return f"{self.data.key, self.data.resource}"


class DList:

    def __init__(self):

        # init empty doubly linked list
        self.size = 0
        self.head = Node(None)
        self.head.nxt = self.head

    def setHead(self, data: Pair):
        """Inserts new DList head increasing the size"""

        head = Node(data)
        self.moveToHead(head)
        self.size += 1

        return head

    def moveToHead(self, node):
        """Unlinks 'node' and use it as self.head"""

        # no node
        if node is None:
            return None
        # node within dl
        elif node.prv and node.nxt:
            self.unlink(node)

        # move it to the front
        node.prv = self.head
        node.nxt = self.head.nxt
        self.head.nxt.prv = node
        self.head.nxt = node

        return node

    def removeTail(self):
        """Removes the tail"""

        if self.size == 0:
            return None

        # NB: stop and think (pointers)
        removed = self.unlink(self.head.prv)
        self.size -= 1

        return removed

    def unlink(self, node):
        """Unlinks 'node'"""

        node.nxt.prv = node.prv
        node.prv.nxt = node.nxt
        node.nxt = None
        node.prv = None

        return node

    def printDL(self):

        s = StringIO()

        s.write("DL: [")
        if self.head is None:
            s.write("]")
            return s.getvalue()

        # NB: stop and think ("real" head)
        n = self.head.nxt
        while n != self.head:
            s.write(f"{n},")
            n = n.nxt
        s.write("]")

        return s.getvalue()


class LRUCache:

    def __init__(self, maxSize):

        if maxSize <= 0:
            raise Exception("Invalid cache maxSize")

        self.maxSize = maxSize
        self.dl = DList()
        self.nodes = {}

    def get(self, key):
        """Gets the resource associated with 'key' and sets it as the
        most recently used

        Complexity:
            -S: O(1)
            -T: O(1)
        """

        n = self.nodes.get(key, None)

        # not found
        if not n:
            return None
        else:
            self.dl.moveToHead(n)
            return n.data.resource

    def put(self, key, resource):
        """Puts (or updates) a new pair into the cache

        Complexity:
            -S: O(1) [but remember that in memory the DL will take up
                      to O(N) space, where N is the maxSize of the cache]
            -T: O(1)
        """

        n = self.nodes.get(key, None)

        # update DL
        if n:
            n.data.resource = resource
            self.dl.moveToHead(n)
            return

        # evict from cache
        if self.dl.size == self.maxSize:
            evicted = self.dl.removeTail()
            del self.nodes[evicted.data.key]

        # set new DL head and update lookup dict
        self.nodes[key] = self.dl.setHead(Pair(key, resource))

    def __str__(self):

        return self.dl.printDL()


def run(cache: LRUCache, pair: tuple):

    print(f"put{pair}")
    cache.put(pair[0], pair[1])
    print(cache)
    print("-----")


print("--------------------")
################# LRU CACHE #################
print("LRU CACHE implementation")
print("--------------------")

# init
size = 5
cache = LRUCache(size)
# populate cache
pairs = [
    (1, "a"),
    (1, "b"),
    (2, "c"),
    (3, "d"),
    (4, "e"),
    (5, "f"),
    (6, "g"),
]
for p in pairs:
    run(cache, p)
# cache lookup
print(f"get({4})")
cache.get(4)
print(cache)

print("--------------------")
################# PYTHON @lru_cache #################
print("PYTHON'S @lru_cache")
print("--------------------")

import time
import functools


@functools.lru_cache(maxsize=2)
def do_some(n):

    j = 0
    for _ in range(2**n):
        j += 1
    return j


ns = [20, 21, 22, 21, 20]
for n in ns:
    res = -1
    start = time.time_ns()
    res = do_some(n)
    end = time.time_ns()
    print(f"do_some({n}):\t{res}")
    print(f"time [ns]:\t{end-start}")
    print("---")
