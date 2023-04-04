"""
execute the following code interactively
"""
from collections import deque

# create a deque
d = deque()
d

# deque creation (iterable)
d = deque(("a", "b", "c", "d", "e", "f"))
d

# deque creation (iterable)
d = deque("abcdef")
d

# deque creation (iterable)
d = deque([1, 2, 3, 4, 5, 6])
d

# deque creation (generator)
d = deque(range(6))
d

# popleft and appendleft
d.popleft()
d
d.appendleft(0)
d

# pop and append
d.pop()
d
d.append(5)
d

# sequence of pops
while len(d) > 0:
    d.pop()
d.pop()  # IndexError: pop from an empty deque

# length
len(d)

# indexing
d = deque(range(6))
d[5]
d[6] # IndexError: deque index out of range

# remove an item by value
d = deque("abcdef")
d.remove("e") # performs a linear scan
d

# deque with fixed len
d = deque([1,2,3], maxlen=5)
d
for i in range(4, 8):
    d.append(i) # items 1 and 2 are discarded when 6 and 7 are appended
d

# rotation
d = deque([1,2,3,4,5,6])
d.rotate(3) # items are shifted to the left
d
d.rotate(-3) # items are shifted to the right
d

# list extraction
d = deque([1,2,3,4,5,6])
list(d)

# sorting
d = deque([1,2,3,4,5,6])
d = sorted(d, reverse=True)
d
type(d) # notice that type(d) is 'list'
