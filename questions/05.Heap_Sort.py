# 5. Heap Sort

def heapify(sequence, n, i):
    # sift (move large keys upward)
    while True:

        largest = i  # current root
        left = 2 * i + 1  # left child of the tree rooted in i
        right = 2 * i + 2  # right child of the tree rooted in i

        if left < n:  # 1st out-of-bound check
            if sequence[left] > sequence[i]:
                largest = left
        if right < n:  # 2nd out-of-bound check
            if sequence[right] > sequence[largest]:
                largest = right

        if largest != i:
            # move the largest key upward
            sequence[i], sequence[largest] = sequence[largest], sequence[i]
            # keep sifting one child
            i = largest
        else:
            # stop sifting
            break


""" Transforms a given sequence into a max heap, then extracts all the
(sorted) keys"""


def heapsort(sequence):
    n = len(sequence)

    # build the max heap
    for i in range(n, -1, -1):
        heapify(sequence, n, i)

    # sort the sequence, until the max heap is empty:
    # 1. extract the largest key (at position 0)
    # 2. prepend it to the sorted sequence
    # 3. shorten and rebuild the max heap
    for i in range(n - 1, 0, -1):
        # steps 1 and 2
        sequence[0], sequence[i] = sequence[i], sequence[0]
        # step 3
        heapify(sequence, i, 0)


"""
Time: 
    • worst O(n log n) 
    • average O(n log n) 
    • best O(n log n)
Space: O(1)
"""
