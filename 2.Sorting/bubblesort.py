def bubblesort(sequence):

    if len(sequence) <= 1:
        return  # already sorted

    for i in range(len(sequence) - 1):
        for j in range(len(sequence) - 1 - i):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

"""
Time: • worst O(n^2) • best O(n^2) • average O(n^2) 
# Gauss Summation: sum( (n(n-1)) / 2 ) = O(n^2)
Space: O(1)
"""
