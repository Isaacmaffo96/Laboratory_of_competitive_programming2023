def selectionsort(sequence):

    if len(sequence) <= 1:
        return

    # for each element in the unsorted subsequence
    for i in range(len(sequence) - 1):

        # get the smallest element position
        smallest_ep = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[smallest_ep]:
                smallest_ep = j

        # swap elements at current position and at smallest element position
        if smallest_ep != i:
            sequence[i], sequence[smallest_ep] = sequence[smallest_ep], sequence[i]


"""
Time: • worst O(n2) • best O(n2) • average O(n2)
Space: O(1)
"""
