from io import StringIO
"""Adelson-Velsky Landis Tree (AVL)"""


class TreeNode:

    def __init__(self, key) -> None:

        self.key = key
        self.occurences = 1
        self.left = None
        self.right = None
        self.h = 1

    def __str__(self, l=None, d=None, sio=None):

        if self is None:
            return

        if l is None:
            l = 0
        if sio is None:
            sio = StringIO()

        if self.right:
            self.right.__str__(l + 1, d='r', sio=sio)

        arrow = ""
        if d == "l":
            arrow = "\\"
        elif d == "r":
            arrow = "/"
        sio.write("{}{}{}({})\n".format("\t" * l, arrow, self.key,
                                        self.occurences))
        if self.left:
            self.left.__str__(l + 1, d='l', sio=sio)

        # get the str representation for the root of the tree
        if l == 0:
            return sio.getvalue()


def insert(tree: TreeNode | None, key) -> TreeNode:
    """Inserts a new key, it also guarantees that tree will be
    balanced after insertion
    
    Complexity:
        -S: O(log2(N))
        -T: O(log2(N))
    """

    # insertion
    if tree is None:
        return TreeNode(key)
    elif key == tree.key:
        tree.occurences += 1
        return tree
    elif key < tree.key:
        tree.left = insert(tree.left, key)
    else:
        tree.right = insert(tree.right, key)

    # get the new balance factor
    bf = balanceFactor(tree)

    # apply rotations so that bf in {-1; 0; +1}
    if bf in set((-1, 0, +1)):
        # the tree is balanced, just update the height
        tree.h = 1 + max(height(tree.left), height(tree.right))
    elif bf > 1:
        # left subtree is 'taller'
        if key > tree.left.key:
            tree.left = rotateLeft(tree.left)
        tree = rotateRight(tree)
    else:
        # right subtree is 'taller'
        if key < tree.right.key:
            tree.right = rotateRight(tree.right)
        tree = rotateLeft(tree)

    # remember that rotations modify the structure of the tree
    return tree


def delete(tree: TreeNode | None, key, ignoreOccurences=False):
    """Deletes a key, it also guarantees that tree will be balanced
    after deletion. No errors are raised in case the key is not
    found
    
    Complexity:
        -S: O(log2(N))
        -T: O(log2(N))
    """

    # deletion
    if tree is None:
        return tree
    elif tree.key == key:
        if tree.occurences > 1 and (not ignoreOccurences):
            tree.occurences -= 1
            return tree
        else:
            if tree.left is None:
                tmp = tree.right
                tree = None
                return tmp
            elif tree.right is None:
                tmp = tree.left
                tree = None
                return tmp
            else:
                tmp = minKeyNode(tree.right)
                tree.key = tmp.key
                tree.occurences = tmp.occurences
                tree.right = delete(tree.right, tmp.key, ignoreOccurences=True)
    elif tree.key < key:
        tree.right = delete(tree.right, key, ignoreOccurences=ignoreOccurences)
    else:
        tree.left = delete(tree.left, key, ignoreOccurences=ignoreOccurences)

    # get the new balance factor
    bf = balanceFactor(tree)

    # apply rotations so that balance in {-1; 0; +1}
    if bf in set((-1, 0, +1)):
        # the tree is balanced, just update the height
        tree.h = 1 + max(height(tree.left), height(tree.right))
    elif bf > 1:
        if balanceFactor(tree.left) < 0:
            tree.left = rotateLeft(tree.left)
        tree = rotateRight(tree)
    else:
        if balanceFactor(tree.right) > 0:
            tree.right = rotateRight(tree.right)
        tree = rotateLeft(tree)

    return tree


def height(tree: TreeNode):
    """Returns the height of the tree

    Complexity:
        -S: O(1)
        -T: O(1)
    """

    if not tree:
        return 0
    return tree.h


def balanceFactor(tree: TreeNode) -> int:
    """Returns the balance factor of the tree

    Complexity:
        -S: O(1)
        -T: O(1)
    """

    if tree is None:
        return 0
    return height(tree.left) - height(tree.right)


def minKeyNode(tree: TreeNode):
    """Returns the node that stores the minimun key

    Complexity:
        -S: O(1)
        -T: O(log2(N))
    """

    parent = tree
    while tree:
        parent = tree
        tree = tree.left
    return parent


def rotateLeft(tree: TreeNode):
    """Modifies tree promoting tree.right to root

    Complexity:
        -S: O(1)
        -T: O(1)
    """

    right = tree.right
    tmp = right.left
    right.left = tree
    tree.right = tmp

    # adjust the height of tree and right
    tree.h = 1 + max(height(tree.left), height(tree.right))
    right.h = 1 + max(height(right.left), height(right.right))

    return right


def rotateRight(tree):
    """Modifies tree promoting tree.left to root

    Complexity:
        -S: O(1)
        -T: O(1)
    """

    left = tree.left
    tmp = left.right
    left.right = tree
    tree.left = tmp

    # adjust the height of tree and left
    tree.h = 1 + max(height(tree.left), height(tree.right))
    left.h = 1 + max(height(left.left), height(left.right))

    return left


def search(tree: TreeNode | None, key):
    """Tests whether the tree stores key. No error is raised if key is
    not found or tree is None

    Complexity:
        -S: O(1)
        -T: O(log2(N))
    """

    while tree:
        if key == tree.key:
            return True
        elif key < tree.key:
            tree = tree.left
        else:
            tree = tree.right

    return False
