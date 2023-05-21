"""Trie example. You are given a vocabulary and a prefix string. Find
all the words in the vocabulary that start with the given prefix."""

from collections import deque


class Node:

    def __init__(self, children: dict, isTerm: bool):

        self.children = children
        self.isTerm = isTerm


class Trie():

    def __init__(self):

        self._trie = None

    def index(self, words: list):
        """
        Creates a Trie (or prefix tree) given a set of words

        Complexity:
        
            -S: O(NL) [where N is the number of words, and L is the length of the longest word]
            -T: O(NL)
        """

        # start from an empty Trie
        self._trie = Node({}, False)
        for word in words:
            # perform a visit to the Trie to insert each word
            cn = self._trie
            for char in word:
                if not char in cn.children:
                    cn.children[char] = Node({}, False)
                cn = cn.children[char]
            # memorize word
            cn.isTerm = True

    def autocompletePrefix(self, prefix):
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
        return self._getCompletions(cn, prefix)

    def _getCompletions(self, cn, prefix):

        words = set()
        s = deque([(cn, prefix)])
        while len(s) > 0:
            cn, prefix = s.pop()
            if cn.isTerm:
                words.add(prefix)
            for char in cn.children:
                s.append((cn.children[char], prefix + char))

        return words


def run(trie: Trie, prefix):

    print("---")
    print("Prefix:\t\t", prefix)
    print(
        "Completions:\t",
        trie.autocompletePrefix(prefix),
    )


# a collection of flowers
flowers = [
    "aconitum",
    "african daisy",
    "agapanthus",
    "alchemilla",
    "alstroemeria",
    "alyssum",
    "amaranthus",
    "amaryllis",
    "anemone",
    "angelonia",
    "anthurium",
    "antirrhinum majus",
    "dahlia",
    "iris",
    "orchyd",
]
print("Flowers:", end="")
for p, f in enumerate(flowers):
    if p % 3 == 0:
        print("\n", end="\t")
    print(f, end=", ")
print()

trie = Trie()
trie.index(flowers)

prefixes = ("ac", "an", "orchyd a", "z")
for p in prefixes:
    run(trie, p)
