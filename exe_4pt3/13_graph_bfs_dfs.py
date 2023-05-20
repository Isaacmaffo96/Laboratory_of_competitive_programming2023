"""Directed graph with V vertices and E edges"""

from collections import deque


def bfs(adl, source, destination=None):
    """Explores graph adl with BPS

    adl: adjacency list
    source: source node
    destination: an optional destination node

    BFS
    
    - the path found by breadth first search to any node is the
      shortest path to that node, i.e. the path that contains the
      smallest number of edges
    - O(V+E) time
    - O(V) space
    """

    n = len(adl)
    # exploration queue
    q = deque([source])
    # queued vertices
    queued = [False for _ in range(n)]
    queued[source] = True
    # distances (from the source)
    distances = [0 for _ in range(n)]

    print("expl. order -> ", end="")
    while len(q) != 0:
        v = q.popleft()
        print(v, " ", end="")
        for dst in adl[v]:
            if not queued[dst]:
                q.append(dst)
                queued[dst] = True
                distances[dst] = distances[v] + 1
    print()

    print("source:\t\t", source)
    print("nodes:\t\t", list(range(n)))
    print("distances:\t", distances)

    if destination:
        if not queued[destination]:
            print(f"{destination} is unreachable ")
        else:
            print(f"{destination} is reachable ")


def dfs(adl, source, destination=None):
    """Explores graph adl with DFS

    adl: adjacency list
    source: source node
    destination: an optional destination node

    DFS

    - finds the lexicographical first path in the graph from a source
      to each vertex (it will also find the shortest paths in a tree,
      because only one path exists for each vertex in that case)
    - T: O(V+E)
    - S: O(V)
    """

    n = len(adl)
    s = deque([(source, 0)])
    visited = [False for _ in range(n)]

    print("expl. order -> ", end="")
    while len(s) != 0:
        v, e = s[-1]
        if not visited[v]:
            print(v, " ", end="")
            visited[v] = True
        if e <= len(adl[v]) - 1:
            dst = adl[v][e]
            s[-1] = (v, e + 1)
            if not visited[dst]:
                s.append((dst, 0))
        else:
            s.pop()

    print()
    if destination:
        if not visited[destination]:
            print(f"{destination} is unreachable")
        else:
            print(f"{destination} is reachable")


# -------------------------------------------- #

def dfs_v2(adl, source, destination=None):

    visited = [False for _ in range(len(adl))]
    stack = deque([source])
    print("expl. order -> ", end="")

    while stack:
        """
        v = stack[-1]
        if not visited[v]:
            visited[v] = True
            print(v, " ", end="")
        else:
            stack.pop(
        """
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, " ", end="")
        for dst in adl[v]:
            if not visited[dst]:
                stack.append(dst)
    print()
    if destination:
        if not visited[destination]:
            print(f"{destination} is unreachable")
        else:
            print(f"{destination} is reachable")


adl = [
    [1, 2, 3, 5],
    [4, 5],
    [7],
    [2],
    [5],
    [0, 1, 6],
    [7],
    [],
    [],
]
n = len(adl)
print("Adjacenty list:")
for i in range(n):
    print(i, adl[i])
print("---")

# breadth-first search
print("BFS")
bfs(adl, 0, 7)
print("---")

# depth-first search
print("DFS")
dfs(adl, 0, 7)

# depth-first search v2
print("---")
print("DFS v2.0")
dfs_v2(adl, 0, 7)
