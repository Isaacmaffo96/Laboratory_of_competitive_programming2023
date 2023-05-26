# 14. Funzione di auto-completamento prefissi dato un trie (già costruito)

# ------------------------------------------- #

from collections import deque


class Node:

    def __init__(self, children: dict, isTerm: bool):

        self.children = children
        self.isTerm = isTerm


class Trie():

    def __init__(self):

        self._trie = None

# ------------------------------------------- #

    def autocomplete_prefix(self, prefix):
        """Given a prefix, returns all the completion candidates in
        the Trie

        Complexity:

            -T: O(P + N*((L-P)^2)) [where P is the length of the
             prefix, L is the length of the longest word, N is the
             number of words. The square root is due to str
             concat. Consider that in a typical scenario N >> L > P]
            -S: O(N*L)
        """

        cn = self._trie
        for char in prefix:
            if cn is None or not (char in cn.children):
                return []
            cn = cn.children[char]
        # prefix exists; return all the completions
        return self._get_completions(cn, prefix)

    def _get_completions(self, cn, prefix):

        words = set()
        s = deque([(cn, prefix)])
        while len(s) > 0:
            cn, prefix = s.pop()
            if cn.isTerm:
                words.add(prefix)
            for char in cn.children:
                s.append((cn.children[char], prefix + char))

        return words


"""
Complexity:
    - Time : O(P + N*((L-P)^2))
    - Space: O(N*L)
"""
