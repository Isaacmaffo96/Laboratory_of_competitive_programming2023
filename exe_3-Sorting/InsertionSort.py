# Insertion Sort
import random as rd


def insertion_sort(sequence):

    if len(sequence) <= 1:
        return sequence

    for i in range(1, len(sequence)):
        j = i
        curr = sequence[i]
        while j > 0 and sequence[j-1] > curr:
            sequence[j] = sequence[j-1]
            j -= 1
        else:
            sequence[j] = curr
    return sequence


"""
Time: 
    • worst O(n2), when the sequence is sorted decreasingly, it requires to swap all the elements, at each iteration
    • best O(n), no swaps performed if the sequence is already ordered
    • average O(n2) 
Space: O(1)
"""

size = int(rd.uniform(0, 100)) + 1000
mylist = [int(rd.uniform(0, 1000)) for i in range(size)]
print(mylist)
mylist2 = mylist.copy()
print(insertion_sort(mylist))
mylist2.sort()
print("Sorted?", mylist2 == mylist)
