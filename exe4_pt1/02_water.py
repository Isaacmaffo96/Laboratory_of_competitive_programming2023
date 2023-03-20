"""Coding strategy: two pointers

Problem:
========

You are given an integer sequence of length n. Each i-th element in
the sequence represents the vertical height of a wall. Find the
maximum quantity of water that can be stored between two walls (the
two walls can be at any distance). Assume that walls have no volume
(i.e., they are just vertical lines).

Example:
========

heights = [1,2,3,2]

    |
  | | |
| | | |

Water can be poured in the container in 6 ways:

    |
  | | |
|w| | |

    |
  |w| |
| |w| |

    |
  | |w|
| | |w|

    |
  | | |
|w|w| |

    |
  |w|w| MAX water: Water = min(2,2) * (3-1) = 4
| |w|w|

    |
  | | |
|w|w|w|

"""

"""Complexity:
    - time: O(n^2)
    - space: O(1)
"""


def naive_solution(heights):

    max_water = 0

    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            h = min(heights[i], heights[j])
            max_water = max(max_water, h*(j-i))            

    return max_water


"""Complexity:
    - time: O(n)
    - space: O(1)
"""


def tp_solution(heights):

    l = 0
    r = len(heights) - 1
    max_water = 0

    while l < r:
        h = min(heights[l], heights[r])
        max_water = max(max_water, h*(r-l))
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_water


def solve(heights):
    
    print("---")    
    print("heigth:\t\t\t{}".format(heights))
    print("naive:\t\t\t{}".format(naive_solution(heights)))
    print("two pointers:\t\t{}".format(tp_solution(heights)))


solve([1])
solve([1,1])
solve([1,2])
solve([1,2,1])
solve([1,7,6,2,5,4,8])    
solve([1,5,6,2,5,12,8])
solve([18,5,6,2,5,12,13])
solve([4,5,38,58,5,6,2])
