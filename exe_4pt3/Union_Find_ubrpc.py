print("UNION-FIND (UNION BY RANK + PATH COMPRESSION)")

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
print("------------------------------")

n = len(E)
representative = [-1 for _ in range(n)]
rank = [-1 for _ in range(n)]

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
