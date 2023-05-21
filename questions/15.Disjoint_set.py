# 15. Implementazione di disjoint-set forest con union by rank e path compression (funzioni makeSet, find, union)

# ------------------------------------- #

# we are given a set of elements
E = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print(f"Elements:\t{E}")

# a set of links is also given
L = set([
    (0, 1),
    (2, 4),
    (5, 7),
    (1, 5),
    (6, 7),
    (7, 8),
    (8, 2),
    (10, 11),
    (12, 13),
    (11, 14),
])

# ------------------------------------- #


def make_set(e):

    representative[e] = e
    rank[e] = 0


def find(e):

    toCompress = []
    while e != representative[e]:
        toCompress.append(e)
        e = representative[e]
    for el in toCompress:
        representative[el] = e
    return e


def union(e1, e2):
    """Amortized analysis is used to determine the complexity (see
    slides). After M union and find operations on a disjoint-set
    forest with N nodes, the runtime is O(M*inv_ack(N))."""

    e1 = find(e1)
    e2 = find(e2)
    if e1 == e2:
        return
    if rank[e1] == rank[e2]:
        rank[e1] += 1
        representative[e2] = e1
    elif rank[e1] > rank[e2]:
        representative[e2] = e1
    else:
        representative[e1] = e2


representative = [-1 for _ in range(len(E))]
rank = [-1 for _ in range(len(E))]

for e in E:
    make_set(e)

for l in L:
    e1, e2 = l
    union(e1, e2)

"""Complexity:
    - Time: O(M*inv_ack(N))
    - Space: O(N)
"""
