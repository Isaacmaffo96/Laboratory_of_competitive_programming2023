"""You are given an undirected weighted graph with V vertices and E
edges. Weights are non-negative and represent the distance between two
vertices. You are also given a starting vertex src. Find the shortest
path from src to all other vertices"""

from collections import deque


class Dijkstra:

    def __init__(self):

        # adjacency matrix
        # src: [[dest1, distance1], [dest2, distance2], ...]
        self.adm = {
            0: [[1, 3], [2, 1], [3, 2]],
            1: [[4, 4]],
            2: [],
            3: [[2, 7], [4, 1]],
            4: [[5, 8]],
            5: [[0, 5], [6, 4]],
            6: [[7, 12]],
            7: [],
            8: [],
        }
        self.n = len(self.adm)
        # distances
        self.tot_distance = [float("inf") for _ in range(self.n)]
        # precedent vertices
        self.precedent = [-1 for _ in range(self.n)]
        # used vertices
        self.used = [False for _ in range(self.n)]

    def computeShortestPaths(self, src):
        """Computes the shortest path between src and all other
        vertices in the graph

        Complexity:
            -S: O(V)
            -T: O(V^2+E)
        """

        # we start from src, which of course is at distance 0
        self.tot_distance[src] = 0
        # until there are unused (and reachable) vertices
        for _ in range(self.n):
            v = -1
            # find the unused vertex v (that is) nearest to src
            for j in range(self.n):
                if not self.used[j] and (v == -1 or self.tot_distance[j] <
                                         self.tot_distance[v]):
                    v = j
            # v is unreachable, stop
            if self.tot_distance[v] == float("inf"):
                break
            # mark v as used
            self.used[v] = True
            # update the tot_distance based on v's edges
            for edge in self.adm[v]:
                dst, distance = edge[0], edge[1]
                if self.tot_distance[v] + distance < self.tot_distance[dst]:
                    self.tot_distance[dst] = self.tot_distance[v] + distance
                    self.precedent[dst] = v

        print("nodes:\t\t", list(range(len(self.adm))))
        print("distances:\t", self.tot_distance)
        print("parents:\t", self.precedent)

    def extractPath(self, src, dst):
        """Extracts the path between src and dst"""

        if self.precedent[dst] == -1:
            return "no path found"

        path = deque([])
        v = dst
        while v != src:
            path.appendleft(v)
            v = self.precedent[v]
        path.appendleft(v)
        return path

    def printAdm(self):

        print("Adjacency map:")
        for k, v in self.adm.items():
            print(k, v)

    # HOME PRACTICE:
    #
    # 1) try to use `property` to reorganize the code
    #
    # 2) you can improve the efficiency using a heap (i.e., avoiding
    # the linear search); try to implement this version of the
    # algorithm as an exercise


pathFinder = Dijkstra()
pathFinder.printAdm()
print("---")

print("Compute shortest paths:")
src = 0
pathFinder.computeShortestPaths(src)
print("---")

print("Path extraction:")
print("path from 0 to 5,", "->".join(map(str, pathFinder.extractPath(0, 5))))
print("path from 0 to 8,", pathFinder.extractPath(0, 8))
