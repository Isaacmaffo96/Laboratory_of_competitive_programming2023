"""You are given a list of integer numbers l1. Return a new list l2
    containing the base 2 logarithm only for even numbers in l1.
"""

"""
Complexity:
    - time: O(n)
    - space: O(n)
"""

import math


def solve(l1):
    return [math.log2(item) for item in l1 if item % 2 == 0]

l1 = [i for i in range(1, 20)]
print("l1: {}".format(l1))

l2 = solve(l1)
print("l2: {}".format(l2))
