# Merge Sort
import random as rd


def merge_sort(sequence):

    if len(sequence) == 1:
        return sequence

    middle = len(sequence) // 2
    left_s = merge_sort(sequence[:middle])
    right_s = merge_sort(sequence[middle:])

    i = j = k = 0
    while i < len(left_s) and j < len(right_s):
        if left_s[i] < right_s[j]:
            sequence[k] = left_s[i]
            i += 1
        else:
            sequence[k] = right_s[j]
            j += 1
        k += 1

    while i < len(left_s):
        sequence[k] = left_s[i]
        i += 1
        k += 1

    while j < len(right_s):
        sequence[k] = right_s[j]
        j += 1
        k += 1

    return sequence


"""
Time: 
    • worst O(n log n) 
    • best O(n log n) 
    • average O(n log n)
Space: O(n)
"""

size = int(rd.uniform(0, 100)) + 1000
mylist = [int(rd.uniform(0, 1000)) for i in range(size)]
print(mylist)
mylist2 = mylist.copy()
print(merge_sort(mylist))
mylist2.sort()
print("Sorted?", mylist2 == mylist)
