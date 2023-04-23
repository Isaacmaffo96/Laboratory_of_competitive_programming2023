"""This lesson gives an introduction to binary trees. We are going to
learn how to insert and search keys, visit the tree in different ways
(in-order, pre-order, post-order), compute the height of the tree,
test whether the tree is full, how to "reverse" the tree, and finally
how to look up the lowest common ancestor for two nodes.

However, some of the following methods have TWO major PROBLEMS:

1) insert leaves the tree unbalanced, hence it may collapse into a
list

2) several functions use recursion, this isn't a safe approach

In the next lesson we are going to implement a better version of the
binary tree. In the meanwhile, why don't you try to improve the
implementation as home practice?

There are also a couple of additional exercises in the comments.

===

P.S. in this lesson we also start talking about decorators!

"""

from io import StringIO
from collections import deque

if __package__:
    from .TestHelper import test
else:
    from TestHelper import test


class mBinaryTree:

    def __init__(self) -> None:

        self.key = None
        self.occurences = 0
        self.left = None
        self.right = None

    def insert(self, key):
        """Inserts a key in the tree (no balancement)

           Complexity:
               -T: O(N) where N is the number of keys for unbalanced
                tree, O(log2(N)) for balanced tree
               -S: O(1)
        """

        curr = self

        if curr.key is None:
            curr.key = key
            curr.occurences += 1
            return

        while True:
            if curr.key == key:
                curr.occurences += 1
                return
            elif curr.key < key:
                if curr.right is None:
                    curr.right = mBinaryTree.createBranch(key)
                    return
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = mBinaryTree.createBranch(key)
                    return
                curr = curr.left

    @staticmethod
    def createBranch(key):

        c = mBinaryTree()
        c.key = key
        c.occurences += 1
        return c

    def search(self, key):
        """Tests the presence of a key

           Complexity:
               -T: O(N) where N is the number of keys for unbalanced
                tree, O(log2(N)) for balanced tree
               -S: O(1)
        """

        curr = self

        while curr:
            if curr.key == key:
                return True
            else:
                if curr.key < key:
                    curr = curr.right
                else:
                    curr = curr.left

        return False

    """
             A
            / \
           B   C
      In Order : [B,A,C]
      Pre Order: [A,B,C]
      Post Order: [B,C,A]
    """


    def inOrder(self, sio=None):

        sio = StringIO()
        self._inOrder(self, sio)
        return sio.getvalue()

    def _inOrder(self, curr, sio):

        if curr.left:
            self._inOrder(curr.left, sio)
        sio.write(str(curr.key) + ", ")
        if curr.right:
            self._inOrder(curr.right, sio)

    def preOrder(self, sio=None):

        sio = StringIO()
        self._preOrder(self, sio)
        return sio.getvalue()

    def _preOrder(self, curr, sio):

        sio.write(str(curr.key) + ", ")
        if curr.left:
            self._preOrder(curr.left, sio)
        if curr.right:
            self._preOrder(curr.right, sio)

    def postOrder(self, sio=None):

        sio = StringIO()
        self._postOrder(self, sio)
        return sio.getvalue()

    def _postOrder(self, curr, sio):

        if curr.left:
            self._postOrder(curr.left, sio)
        if curr.right:
            self._postOrder(curr.right, sio)
        sio.write(str(curr.key) + ", ")

    def write(self, curr=None, l=None, d=None):

        if curr is None:
            curr = self
            l = 0

        if curr.right:
            curr.write(curr.right, l + 1, d='r')
        arrow = ""
        if d == "l":
            arrow = "\\"
        elif d == "r":
            arrow = "/"
        print("{}{}{}({})".format("\t" * l, arrow, curr.key, curr.occurences))
        if curr.left:
            curr.write(curr.left, l + 1, d='l')

    def height(self):
        """Returns the height of the tree (height starts from 0)

        Complexity:
           -T: O(N) where N is the number of keys
           -S: O(N) unbalanced tree, O(log2(N)) for balanced tree
        """

        h_max = 0
        toVisit = deque([(self, 0)])

        while len(toVisit) > 0:
            curr, h = toVisit.pop()
            h_max = max(h_max, h)
            if curr.left:
                toVisit.append((curr.left, h + 1))
            if curr.right:
                toVisit.append((curr.right, h + 1))

        return h_max

    def isFull(self):
        """Returns True if the tree is Full. Full tree: each node has either no
        child or 2 children

        Complexity:
           -T: O(N) where N is the number of keys
           -S: O(N) unbalanced tree, O(log2(N)) for balanced tree
        """

        toVisit = deque([self])
        while len(toVisit) > 0:
            n = toVisit.pop()
            if (n.right and n.left is None) or (n.left and n.right is None):
                return False
            if n.left:
                toVisit.append(n.left)
            if n.right:
                toVisit.append(n.right)

        return True

    def reverseTree(self):
        """Reverses key ordering

        Complexity:
           -T: O(N) where N is the number of keys
           -S: O(N) unbalanced tree, O(log2(N)) for balanced tree
        """

        toReverse = deque([self])
        while len(toReverse) > 0:
            curr = toReverse.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                toReverse.append(curr.left)
            if curr.right:
                toReverse.append(curr.right)

    def lca(self, ka, kb):
        """Given two keys ka and kb, returns the lowest node in the
        tree that is a common ancestor of the nodes storing ka and
        k3. Assumes that ka and kb are always stored in the tree.

        Complexity (for a balanced tree):
            -T: O(log2(N))
            -S: O(1)
        """

        # perform two searches with na and nb
        na = nb = ancestor = self

        while na.key == nb.key:

            ancestor = na

            if na.key < ka:
                na = na.right
            elif na.key > ka:
                na = na.left

            if nb.key < kb:
                nb = nb.right
            elif nb.key > kb:
                nb = nb.left

        return ancestor, ancestor.key

    # HOME PRACTICE

    # def isBalanced(self):
    #     """Returns True if the tree is balanced. Balanced tree: for
    #     each node: 1) the left and right subtrees are balanced, and
    #     2) the height of the left and right subtrees differ at most
    #     by 1."""
    #     # write your code here
    #     pass

    # def isComplete(self):
    #     """Returns True if the tree is Complete. Complete tree: each
    #     level in the tree (except the last) has the maximum number
    #     of nodes"""
    #     # write your code here
    #     pass


# create
t = mBinaryTree()

# insert keys
keys = [50, 25, 75, 15, 35, 40, 80, 15, 25]
for k in keys:
    test(t, "insert", key=k, printObj=False)
test(t, "write")

# search
test(t, "search", key=40, printObj=False)

# visits
test(t, "inOrder")
test(t, "preOrder")
test(t, "postOrder")

# height
test(t, "height")

# fullness
test(t, "isFull")

# lca
test(t, "lca", kan=15, kbn=35)

# reverse
test(t, "reverseTree")
test(t, "write")
