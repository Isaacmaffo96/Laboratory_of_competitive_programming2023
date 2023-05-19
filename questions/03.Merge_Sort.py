# 3. Merge Sort

def mergesort(sequence):
    if len(sequence) > 1:

        # split the sequence and apply mergesort to the subsequences
        middle = len(sequence) // 2  # integer division
        left_s = mergesort(sequence[0: middle])
        right_s = mergesort(sequence[middle: len(sequence)])

        # merge the two ordered subsequences
        i = j = k = 0
        while i < len(left_s) and j < len(right_s):
            if left_s[i] < right_s[j]:
                sequence[k] = left_s[i]
                i += 1
            else:
                sequence[k] = right_s[j]
                j += 1
            k += 1

        # copy the remaining tail
        while i < len(left_s):
            sequence[k] = left_s[i]
            i += 1
            k += 1
        while j < len(right_s):
            sequence[k] = right_s[j]
            j += 1
            k += 1

        # return the sorted subsequence
        return sequence

    # base case
    return [sequence[0]]


"""
Time: 
    • worst O(n log n) 
    • best O(n log n) 
    • average O(n log n)
Space: O(n)
"""