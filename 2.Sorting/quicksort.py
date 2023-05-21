"""The method partition selects a pivot, puts the pivot in the correct
position, and moves to its left all the elements lower than it

"""


def partition(sequence, left, right):
    
    # take the rightmost element as pivot
    pivot = sequence[right]
    # save the virtual position of the pivot
    i = left    

    # move to the left of the pivot all the elements that are lower
    # than it
    for j in range(left, right):
        if sequence[j] <= pivot:
            # element j preceeds the pivot, move it to the left of it (virtually)
            sequence[i], sequence[j] = sequence[j], sequence[i]
            # update the virtual position of the pivot
            i = i + 1

    # put the pivot in the correct position
    sequence[i], sequence[right] = sequence[right], sequence[i]

    # return the position of the pivot that was used
    return i


def quicksort(sequence, left, right):

    if left < right:

        # split the sequence into two partitions using a pivot
        idx = partition(sequence, left, right)

        # apply quicksort to both partitions
        quicksort(sequence, left, idx-1)
        quicksort(sequence, idx+1, right)        


"""
Worst case complexity: • time O(n2) • space O(n)
Average case complexity: • time O(n log n) • space O(log n)
Best case complexity: • time O(n log n) • space O(log n)
"""

"""Can you spot the problem associated with this implementation?

The problem is that partition always selects the righmost element as
the pivot. This could lead to two partitions with 1 and N-1 elements,
respectively. If this problem keeps repeating every time we call
partition, then we will consume up to O(N) space (think about the
number of function calls we perform).

To solve the problem we can:
1) select a random pivot
2) use the median as pivot
"""
