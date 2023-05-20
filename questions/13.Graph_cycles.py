# 13. Rilevamento di cicli in grafo diretto (funzione non ricorsiva)

from collections import deque


def detect_cycles(adl):
    """Detects the presence of a cycle in a directed graph."""

    n = len(adl)

    if n < 2:
        print("no cycle detected")
        return False  # no cycles with 0 or 1 vertices

    # sequence of DFS visits
    stack = deque([])
    isVisited = [False for _ in range(n)]
    onStack = [False for _ in range(n)]
    for src in range(n):

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

            for dst in adl[v]:
                if not isVisited[dst]:
                    stack.append(dst)
                elif onStack[dst]:
                    return True

    return False


"""Complexity:
    - Time: O(V+E)
    - Space: O(V)
"""
