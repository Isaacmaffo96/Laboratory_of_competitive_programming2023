# 4. Quick Sort

def partition(sequence, left, right):
    """
    The method partition selects a pivot, puts the pivot in the correct
    position, and moves to its left all the elements lower than it
    """
    # take the rightmost element as pivot
    pivot = sequence[right]
    # save the virtual position of the pivot
    i = left

    # move to the left of the pivot all the elements that are lower
    # than it
    for j in range(left, right):
        if sequence[j] <= pivot:
            # element j precedes the pivot, move it to the left of it (virtually)
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
        quicksort(sequence, left, idx - 1)
        quicksort(sequence, idx + 1, right)


"""
Worst case complexity: • time O(n2) • space O(n)
Average case complexity: • time O(n log n) • space O(log n)
Best case complexity: • time O(n log n) • space O(log n)
"""
