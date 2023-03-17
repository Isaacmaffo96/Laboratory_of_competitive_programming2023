# Bubble Sort
import random as rd


def bubble_sort(sequence):

    if len(sequence) <= 1:
        return sequence

    for i in range(len(sequence)-1):
        for j in range(len(sequence)-1-i):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence


"""
Time: • worst O(n^2) • best O(n^2) • average O(n^2) 
# sommatioria di Gauss: sum( (n(n-1)) / 2 ) = O(n^2)
Space: O(1) 
# non allochiamo nulla in memoria
"""

size = int(rd.uniform(0, 100)) + 1000
mylist = [int(rd.uniform(0, 1000)) for i in range(size)]
print(mylist)
mylist2 = mylist.copy()
print(bubble_sort(mylist))
mylist2.sort()
print("Sorted?", mylist2 == mylist)
