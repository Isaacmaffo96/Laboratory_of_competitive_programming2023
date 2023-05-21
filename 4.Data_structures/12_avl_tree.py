if __package__:
    from .avl_tree import insert, delete
else:
    from avl_tree import insert, delete
from random import shuffle, randint

# declare empty tree
tree = None

# random keys (with repetitions)
keys = [randint(-9, 0) for _ in range(16)]
keys.extend([randint(0, 9) for _ in range(16)])

# shuffle keys (random keys in random order)
shuffle(keys)
print(keys)

# insert
for k in keys:
    print(f"{'-'*50}")
    print(f"After inserting {k}")
    tree = insert(tree, k)
    print(tree)

# delete some keys (18 does not exist)
keys = keys[:10]
keys.append(18)
for k in keys:
    print(f"{'-'*50}")
    print(f"After deleting {k}")
    tree = delete(tree, k)
    print(tree)
