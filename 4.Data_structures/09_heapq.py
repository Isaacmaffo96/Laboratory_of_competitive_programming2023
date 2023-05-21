import random
import heapq

"""We already have an implementation of Heap in Python

import heapq

This is a Min Heap implementation

Remember that you can invert the sign of the keys when a Max Heap is
required"""


# let's start from a list of keys
l = [0,1,2,3,4,5,6,7,8,9]

# key shuffle
random.shuffle(l)
print(f"keys:\t\t{l}")

# transform the list into a Min Heap
heapq.heapify(l) # in-place, in linear time [O(n)]
print(f"keys - heapify:\t{l}")

# push one key keeping the heap variant [O(logN)]
item = -1
heapq.heappush(l, item)
print(f"keys - push -1:\t{l}")

# access the smallest key without pop
print(f"smallest key:\t{l[0]}")

# pop one key keeping the heap variant [O(logN)]
popped = heapq.heappop(l) # remember that this can raise an `Index Error` when the heap is empty

print("---")

# merge two sorted sequences
sList1 = [1,5,8]
sList2 = [2,4,7]
merged = heapq.merge(sList1, sList2) # remember: merge returns an iterator
print(f"sList1:\t\t{sList1}")
print(f"sList2:\t\t{sList2}")
print(f"merged:\t\t{list(merged)}")

print("---")

# return a list of N=3 largest keys from an unordered iterable
N = 3
l = [1,2,3,4,5,6,7,8,9]
random.shuffle(l)
print(f"l:\t\t{l}")
print(f"{N}-largest:\t{heapq.nlargest(N, l)}")

print("---")

# return a list of N=3 smallest elements from an unordered iterable
N = 3
l = [1,2,3,4,5,6,7,8,9]
random.shuffle(l)
print(f"l:\t\t{l}")
print(f"{N}-smallest:\t{heapq.nsmallest(N, l)}")

print("---")
