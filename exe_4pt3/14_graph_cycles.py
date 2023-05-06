"""Write a program to detect cycles in a directed graph (V vertices, E
edges). When a cycle is detected, print to output all its
vertices. There could be multiple cycles, it's ok to print only one.

P.S. in this lesson we also start talking about properties!"""

from collections import deque


class CycleDetector:

    def _setAdl(self, adl):

        self._adl: list = adl
        self._n = len(adl)

    def _getAdl(self):

        return self._adl

    def _delAdl(self):

        self._adl = list()
        self._n = 0

    """This is the typical use, but you can express the same with
    annotations; type `help(property)` in ipython and read about
    @property"""
    adl = property(
        fget=_getAdl,
        fset=_setAdl,
        fdel=_delAdl,
        doc="The graph adjancency list",
    )

    def detect(self):
        """Detects the presence of a cycle in a directed graph. Prints
        to stdout the cycle found

        Complexity:
            -S: O(V)
            -T: O(V+E)
        """

        if len(self._adl) < 2:
            print("no cycle detected")
            return False  # no cycles with 0 or 1 vertices

        # sequence of DFS visits
        stack = deque([])
        isVisited = [False for _ in range(self._n)]
        onStack = [False for _ in range(self._n)]
        for src in range(self._n):

            if isVisited[src]:
                continue
            else:
                stack.append(src)

            while len(stack) > 0:
                v = stack[-1]  # peek (when the visit to v starts)
                if not isVisited[v]:
                    isVisited[v] = True
                    onStack[v] = True
                else:
                    onStack[v] = False
                    stack.pop()  # pop (when the visit to v is finished)

                for dst in self._adl[v]:
                    if not isVisited[dst]:
                        stack.append(dst)
                    elif onStack[dst]:
                        self._printCycle(stack, dst)
                        return True

        print("no cycle detected")
        return False

    # HOME PRACTICE: try to write a recursive version of `detect()`
    #
    # HINT: you can use colors (e.g., white, gray, black) to keep
    # track of visited vertices

    def _printCycle(self, stack, dst):

        idx = stack.index(dst)
        path = []
        while idx < len(stack):
            path.append(stack[idx])
            idx += 1
        print("cycle detected, vertices", path)

    def printAdl(self):

        print("Adjacency list")
        for v, e in enumerate(self._adl):
            print(f"{v}: {e}")


def run(cycleDetector, adl):

    cycleDetector.adl = adl  # update via property
    cycleDetector.printAdl()
    cycleDetector.detect()
    print("---")


# some graph
adl0 = [[1, 2, 3], [4], [], [2], [2]]
adl1 = [[1, 2, 3], [4], [], [2], [1]]
adl2 = [[], [2], [1]]
adl3 = [[], [2], [2]]
adl4 = [[], [2], [0]]
adl5 = [[1, 3], [4], [1], [2], [3]]
adl6 = [[2], [4], [1, 3], [], [0]]

# instantiates a cycle detector object
cycleDetector = CycleDetector()
# run tests
for i in range(7):
    run(
        cycleDetector,
        locals()["adl" + str(i)],
    )
