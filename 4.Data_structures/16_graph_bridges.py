"""A bridge is defined as an edge which, when removed, makes the graph
disconnected (i.e., it increases the number of connected
components). Implement a program to find all the bridges in an
undirected graph with V vertices and E edges.

"""

from collections import deque
from random import shuffle


class BridgeFinder:
    """Find bridges in an undirected graph. The graph is represented
    by the adjacency map `adm`. The object automatically transforms
    `adm` from directed to undirected format (so to minimize human
    errors when creating the adjacency map)."""

    def __init__(self, adm):

        self.adm = adm

    @property
    def adm(self):

        return self._adm

    @adm.setter
    def adm(self, adm):

        if len(adm) == 0:
            return

        self._adm = adm
        self._n = len(self._adm)
        self._makeUndirected()
        print("Adjacency map:")
        for v, e in self._adm.items():
            print("{} -> {}".format(v, e))

    def _makeUndirected(self):

        # revert edges
        radm = {v: [] for v in range(self._n)}
        for v in range(self._n):
            for to in self._adm[v]:
                radm[to].append(v)

        # ensure the graph is undirected
        for v in range(self._n):
            edges = set()
            edges.update(self._adm[v])
            edges.update(radm[v])
            self._adm[v] = list(edges)
            shuffle(self._adm[v])  # just for testing

    def _dfs(self, vertex, previous):

        self._visited[vertex] = True
        self._discovery[vertex] = self._low[vertex] = self._time
        self._time += 1
        for dst in self._adm[vertex]:
            if dst == previous:
                continue
            if self._visited[dst]:
                self._low[vertex] = min(self._low[vertex],
                                        self._discovery[dst])
            else:
                self._dfs(dst, vertex)
                self._low[vertex] = min(self._low[vertex], self._low[dst])
                if self._low[dst] > self._discovery[vertex]:
                    print(f"   - {vertex}--{dst}")

    def find(self):
        """Prints to stdout all the bridges found in the graph.

        Complexity:
            -T: O(V+E)
            -S: O(V)
        """

        if len(self._adm) == 0:
            return

        print("Bridges:")

        self._time = 0
        # discovery time for each vertex
        self._discovery = [-1 for _ in range(self._n)]
        # vertex low time
        self._low = [float("inf") for _ in range(self._n)]
        # visited vertices
        self._visited = [False for _ in range(self._n)]

        # let's perform a sequence of DFS visits on the graph
        for origin in self._adm:
            self._time += 1
            if self._visited[origin]:
                continue
            self._dfs(origin, -1)

    def findI(self):
        """
        Iterative solution to find bridges
        """

        print("Bridges iterative version:")

        time = 0
        discovery = [-1 for _ in range(self._n)]
        low = [float("inf") for _ in range(self._n)]
        visited = [False for _ in range(self._n)]

        for o in self._adm:

            if visited[o]:
                continue

            # stack
            s = deque([])
            # (previous, current, edge, return)
            s.append((-1, o, 0, False))
            while len(s) > 0:
                p, c, e, ret = s[-1]
                if ret:
                    # return from vertex dst
                    dst = self._adm[c][e]
                    low[c] = min(low[c], low[dst])
                    if low[dst] > discovery[c]:
                        print(f"   - {c}--{dst}")
                    s[-1] = (p, c, e + 1, False)
                dst = -1
                if e <= len(self._adm[c]) - 1:
                    dst = self._adm[c][e]
                else:
                    s.pop()
                    continue
                if dst == p:
                    s[-1] = (p, c, e + 1, False)
                    continue
                if visited[dst]:
                    low[c] = min(low[c], discovery[dst])
                    s[-1] = (p, c, e + 1, False)
                    continue
                else:
                    time += 1
                    discovery[dst] = time
                    low[dst] = time
                    visited[dst] = True
                    s[-1] = (p, c, e, True)
                    s.append((c, dst, 0, False))


def run(bridgeFinder, adm, i=None):

    i = 0 if i is None else i

    print(f"EXAMPLE {i}")
    bridgeFinder.adm = adm
    bridgeFinder.find()
    bridgeFinder.findI()
    print(f"{'-'*30}")


adm0 = {
    0: [1],
    1: [2, 3],
    2: [0],
    3: [4],
    4: [5],
    5: [3],
    6: [5, 7],
    7: [8],
    8: [9],
    9: [6, 10],
    10: []
}

adm1 = {
    0: [1],
    1: [2],
    2: [0],
}

adm2 = {
    0: [1],
    1: [2],
    2: [3],
    3: [4],
    4: [0],
}

adm3 = {
    0: [1],
    1: [2],
    2: [3],
    3: [],
    4: [],
}

adm4 = {
    0: [1],
    1: [0],
    2: [],
    3: [4, 6],
    4: [5],
    5: [3],
    6: [],
}

adm5 = {
    0: [1],
    1: [],
    2: [3],
    3: [],
}

adm6 = {
    0: [],
    1: [2],
    2: [],
    3: [4],
    4: [],
}

adm7 = {
    0: [1, 2, 7],
    1: [2, 3, 6],
    2: [4],
    3: [4, 5],
    4: [6],
    5: [6, 7],
    6: [8, 7],
    7: [],
    8: [],
}

adm8 = {
    0: [1, 2, 7],
    1: [2, 3, 6],
    2: [4, 5],
    3: [4, 5],
    4: [6, 7],
    5: [6, 7],
    6: [7],
    7: [],
}

adm9 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2],
}

# build resolver
bridgeFinder = BridgeFinder({})

# run examples
for i in range(10):
    run(
        bridgeFinder,
        locals()["adm" + str(i)],
        i,
    )
