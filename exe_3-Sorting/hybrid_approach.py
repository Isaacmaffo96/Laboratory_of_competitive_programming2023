if __package__ is None:
    from .insertionsort import insertionsort
    from .quicksort import partition
else:
    from insertionsort import insertionsort
    from quicksort import partition


def hybrid_approach(sequence, start, end):

    while start < end:
        # short sequences
        if end - start + 1 < 15:
            # with insertion sort end needs a +1
            insertionsort(sequence, start, end + 1)
            break
        # long sequences
        else:
            pivot = partition(sequence, start, end)
            # sort the shorter subsequence first to reduce memory consumption
            if pivot - start < end - pivot:
                hybrid_approach(sequence, start, pivot - 1)
                start = pivot + 1
            else:
                hybrid_approach(sequence, pivot + 1, end)
                end = pivot-1
