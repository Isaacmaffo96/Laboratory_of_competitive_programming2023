# 2. Insertion Sort

def insertion_sort(sequence):

    if len(sequence) <= 1:
        return

    for i in range(1, len(sequence)):

        curr = sequence[i]
        j = i
        # find the location j where curr should be placed, move all
        # the elements greater than curr to the right of curr
        while j > 0 and sequence[j - 1] > curr:  # note the precedence relation
            sequence[j] = sequence[j - 1]  # move forward the element in position j-1
            j -= 1
        else:  # insert curr in the correct position
            sequence[j] = curr


"""
Time: 
    • best O(n), no swaps performed if the sequence is already ordered
    • average O(n2)
    • worst O(n2), when the sequence is sorted decreasingly, it requires to swap all the elements, at each iteration
Space: O(1)
"""
