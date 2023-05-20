# 12. Visite bfs e dfs (non ricorsive) in grafo diretto

from collections import deque


def bfs(adl, source):
    """Explores graph adl with BFS"""

    visited = [False for _ in range(len(adl))]
    visited[source] = True
    queue = deque([source])

    while queue:
        vertex = queue.popleft()
        for dst in adl[vertex]:
            if not visited[dst]:
                visited[dst] = True
                queue.append(dst)


def dfs(adl, source):
    """Explores graph adl with DFS"""

    visited = [False for _ in range(len(adl))]
    stack = deque([source])

    while stack:

        vertex = stack.pop()
        visited[vertex] = True

        for dst in adl[vertex]:
            if not visited[dst]:
                stack.append(dst)


"""Complexity (bfs & dfs):
    - Time: O(V+E)
    - Space: O(V)
"""
