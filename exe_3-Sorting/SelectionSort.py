# Selection Sort
import random as rd


def selection_sort(sequence):

    if len(sequence) <= 1:
        return sequence

    smallest = 0

    for i in range(len(sequence)-1):
        smallest = i
        for curr in range(i, len(sequence)):
            if sequence[curr] < sequence[smallest]:
                smallest = curr
        sequence[i], sequence[smallest] = sequence[smallest], sequence[i]

    return sequence


"""
Time: • worst O(n2) • best O(n2) • average O(n2)
Space: O(1)
"""

size = int(rd.uniform(0, 100)) + 1000
mylist = [int(rd.uniform(0, 1000)) for i in range(size)]
print(mylist)
mylist2 = mylist.copy()
print(selection_sort(mylist))
mylist2.sort()
print("Sorted?", mylist2 == mylist)
