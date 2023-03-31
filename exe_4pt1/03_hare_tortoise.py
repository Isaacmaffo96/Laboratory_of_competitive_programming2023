"""Coding strategy: fast and slow pointers

Problem:
========

You are given a sequence l of integer numbers. Each number in the
sequence stores the next position you can jump to. Position `None`
terminates the sequence. Write a program to detect cycles in the
sequence. There is a cycle if you can jump to the same position twice
or more. Sequences are built so that you will not trigger an out of
bound exception.

Example 1:
==========

l = [1,2,None]

You traverse the sequence l starting from position 0. From there you
jump to position 1. From position 1 you jump to position 2. You find
None, so you reached the final position. No cycles are detected, so
you return False.

Example 2:
==========

l = [1,2,1,None]

You start from position 0. From there you jump to position 1. Then you
jump to position 2. From position 2 you jump to position 1, wait, you
detected a cycle. You can return the True as result.
"""

"""Complexity:
    - time: O(n)
    - space: O(n) [need to store all the positions in the worst case]
"""


def naive_solution(l):

    # no cycles in an empty sequence
    if len(l) == 0:
        return False

    p = 0
    positions = set([p])

    while p is not None:
        p = l[p]
        if p in positions:
            return True
        positions.add(p)

    return False


"""Complexity:
    - time: O(n)
    - space: O(1)
"""


def fs_solution(l):

    # no cycles in an empty sequence
    if len(l) == 0:
        return False

    fast = 0
    slow = 0

    # FAST and SLOW keep jumping, FAST jumps twice faster than SLOW
    # FAST will reach the end of the sequence before SLOW
    # fast jumps -> pos check -> slow jumps -> fast jumps -> pos check
    while fast is not None:
        fast = l[fast]
        if fast == slow:
            return True
        slow = l[slow]
        if fast is None: # l over
            break
        fast = l[fast]
        if fast == slow:
            return True

    return False


def solve(l):
    
    print("---")    
    print("l:\t\t\t{}".format(l))
    print("naive:\t\t\t{}".format(naive_solution(l)))
    print("fast and slow ptrs:\t{}".format(fs_solution(l)))

    
print("Cycle detection")
solve([])
solve([None])
solve([0])
solve([1,None])
solve([1,2,None])
solve([1,2,1,None])
solve([1,2,3,4,5,6,7,8,None])
solve([1,2,3,4,5,6,7,1,None])
solve([1,2,3,4,5,6,7,8,7,None])
solve([1,2,3,4,5,6,7,7,None])
