# Heap Sort
import random as rd


def heapify(sequence, n, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            if sequence[left] > sequence[largest]:
                largest = left

        if right < n:
            if sequence[right] > sequence[largest]:
                largest = right

        if largest != i:
            sequence[i], sequence[largest] = sequence[largest], sequence[i]
            i = largest
        else:
            break


def heap_sort(sequence):
    n = len(sequence)
    for i in range(n, -1, -1):
        heapify(sequence, n, i)

    for i in range(n-1, 0, -1):
        sequence[0], sequence[i] = sequence[i], sequence[0]
        heapify(sequence, i, 0)


"""
Time: 
    • worst O(n log n) 
    • average O(n log n) 
    • best O(n log n)
Space: O(1)
"""

size = int(rd.uniform(0, 100)) + 1000
mylist = [int(rd.uniform(0, 1000)) for i in range(size)]
print(mylist)
mylist2 = mylist.copy()
heap_sort(mylist)
print(mylist)
mylist2.sort()
print("Sorted?", mylist2 == mylist)
