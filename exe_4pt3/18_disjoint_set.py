from typing import Dict

print("INCREMENTAL CONNECTIVITY")


def findPartition(P: Dict[int, set], elem: int) -> int:
    """Finds the partition that stores 'elem'"""

    for pid in P:
        if elem in P[pid]:
            return pid

    # something went wrong
    return -1


def mergePartitions(P: Dict[int, set], pid1, pid2):
    """Merges two partitions given the identifiers"""

    # pid1 is the bigger partition
    if len(P[pid1]) < len(P[pid2]):
        pid1, pid2 = pid2, pid1
    # merge pid2 into pid1
    P[pid1] = P[pid1].union(P[pid2])
    # delete pid2
    del P[pid2]


def samePartition(P: Dict[int, set], e1, e2):
    """Given two elements and a set of partitions, returns True if the
    two elements belong to the same partition"""

    return findPartition(P, e1) == findPartition(P, e2)


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
print(f"Links:\t\t{L}")

# we need to compute the partitions
P = {}

# initially all elements in E are partitions (of 1 element)
for pid, e in enumerate(E):
    P[pid] = set([e])

# we now need to process links to compute the final set of partitions
for link in L:
    # get the elements
    e1, e2 = link
    pid1 = findPartition(P, e1)
    pid2 = findPartition(P, e2)
    mergePartitions(P, pid1, pid2)
print(f"Partitions:\t{P}")

# test the functionality
e1, e2 = 0, 1
print(f"Same partition {e1}-{e2}?", samePartition(P, e1, e2))
e1, e2 = 12, 3
print(f"Same partition {e1}-{e2}?", samePartition(P, e1, e2))

#Partitions: { {0, 1, 2, 4, 5, 6, 7, 8}, {3}, {9}, {10, 11, 14}, 12: {12, 13} }

print("------------------------------")

print("UNION-FIND (WITHOUT OPTIMIZATIONS)")

n = len(E)
representative = [-1 for _ in range(n)]


def makeSet_wo(e):

    representative[e] = e


def find_wo(e):
    while e != representative[e]:
        e = representative[e]
    return e


def union_wo(e1, e2):
    """Without optimizations the find function can take up to O(N)
    time, the reason is that the tree may degenerate to a list (i.e.,
    we always set e1<-e2)"""

    e1 = find_wo(e1)  # reassign to representatives only
    e2 = find_wo(e2)
    if e1 == e2:
        return
    representative[e2] = e1


# init partitions
for e in E:
    makeSet_wo(e)
# update partitions
for link in L:
    e1, e2 = link
    union_wo(e1, e2)

print("Representative:\t[", end="")
for i in range(n):
    print(format(representative[i], "3d"), end="")
print("]")

print("Elements:\t[", end="")
for i in range(n):
    print(format(i, "3d"), end="")
print("]")

print("------------------------------")

print("UNION-FIND (UNION BY RANK)")

n = len(E)
representative = [-1 for _ in range(n)]
rank = [-1 for _ in range(n)]


def makeSet_ubr(e):

    representative[e] = e
    rank[e] = 0


def find_ubr(e):
    while e != representative[e]:
        e = representative[e]
    return e


def union_ubr(e1, e2):
    """When union by rank is performed, and this is the sole
    optimization introduced (see the slides), the rank matches the
    height of the tree. Hence, for a tree with N nodes, a call to find
    takes up to O(log(N)) time."""

    e1 = find_ubr(e1)
    e2 = find_ubr(e2)
    if e1 == e2:
        return
    if rank[e1] == rank[e2]:
        rank[e1] += 1
        representative[e2] = e1
    elif rank[e1] > rank[e2]:
        representative[e2] = e1
    else:
        representative[e1] = e2


# init partitions
for e in E:
    makeSet_ubr(e)
# update partitions
for link in L:
    e1, e2 = link
    union_ubr(e1, e2)

print("Representative:\t[", end="")
for i in range(n):
    print(format(representative[i], "3d"), end="")
print("]")

print("Elements:\t[", end="")
for i in range(n):
    print(format(i, "3d"), end="")
print("]")

print("Rank:\t\t[", end="")
for i in range(n):
    print(format(rank[i], "3d"), end="")
print("]")

print("------------------------------")

print("UNION-FIND (UNION BY RANK + PATH COMPRESSION)")

n = len(E)
representative = [-1 for _ in range(n)]
rank = [-1 for _ in range(n)]


def makeSet_ubrpc(e):

    representative[e] = e
    rank[e] = 0


def find_ubrpc(e):

    toCompress = []
    while e != representative[e]:
        toCompress.append(e)
        e = representative[e]
    for el in toCompress:
        representative[el] = e
    return e


def union_ubrpc(e1, e2):
    """Amortized analysis is used to determine the complexity (see
    slides). After M union and find operations on a disjoint-set
    forest with N nodes, the runtime is O(M*inv_ack(N))."""

    e1 = find_ubrpc(e1)
    e2 = find_ubrpc(e2)
    if e1 == e2:
        return
    if rank[e1] == rank[e2]:
        rank[e1] += 1
        representative[e2] = e1
    elif rank[e1] > rank[e2]:
        representative[e2] = e1
    else:
        representative[e1] = e2


# init partitions
for e in E:
    makeSet_ubrpc(e)
# update partitions
for link in L:
    e1, e2 = link
    union_ubrpc(e1, e2)

print("Representative:\t[", end="")
for i in range(n):
    print(format(representative[i], "3d"), end="")
print("]")

print("Elements:\t[", end="")
for i in range(n):
    print(format(i, "3d"), end="")
print("]")

print("Rank:\t\t[", end="")
for i in range(n):
    print(format(rank[i], "3d"), end="")
print("]")

print("------------------------------")
