# 13. Rilevamento di cicli in grafo diretto (funzione non ricorsiva)

from collections import deque


def detect_cycles(adl):
    """Detects the presence of a cycle in a directed graph."""

    if len(adl) < 2:
        return False

    visited = [False for _ in range(len(adl))]
    onStack = [False for _ in range(len(adl))]
    stack = deque([])

    for src in adl:

        if visited[src]:
            continue
        else:
            stack.append(src)

        while stack:

            v = stack[-1]
            if not visited[v]:
                visited[v] = True
                onStack[v] = True
            else:
                onStack[v] = False
                stack.pop()

            for dst in adl[v]:
                if not visited[dst]:
                    stack.append(dst)
                elif onStack[dst]:
                    return True

        return False


"""Complexity:
    - Time: O(V+E)
    - Space: O(V)
"""
