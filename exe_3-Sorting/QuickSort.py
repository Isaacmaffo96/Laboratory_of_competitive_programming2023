# Quick Sort
import random as rd


def partition(sequence, left, right):
    pivot = sequence[right]  # right does not equal n
    j = left
    for i in range(left, right):
        if sequence[i] <= pivot:
            sequence[i], sequence[j] = sequence[j], sequence[i]
            j += 1
    sequence[j], sequence[right] = sequence[right], sequence[j]
    return j  # return pivot position


def quick_sort(sequence, left, right):
    if left < right:
        idx = partition(sequence, left, right)
        quick_sort(sequence, left, idx-1)
        quick_sort(sequence, idx+1, right)


"""
Worst case complexity: • time O(n2) • space O(n)
Average case complexity: • time O(n log n) • space O(log n)
Best case complexity: • time O(n log n) • space O(log n)
"""

size = int(rd.uniform(0, 100)) + 1000
mylist = [int(rd.uniform(0, 1000)) for i in range(size)]
print(mylist)
mylist2 = mylist.copy()
quick_sort(mylist, 0, len(mylist)-1)
print(mylist)
mylist2.sort()
print("Sorted?", mylist2 == mylist)
