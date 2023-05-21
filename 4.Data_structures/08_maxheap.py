import math
from io import StringIO
import random
if __package__:
    from .TestHelper import test
else:
    from TestHelper import test


"""Max heap implementation"""    
class myHeap:


    def __init__(self, sequence):

        self.heap = sequence
        self.n = len(sequence)
        self._buildHeap()


    def __len__(self):

        return self.n

    
    """Helper to visualize elements and indexes"""
    def __str__(self):

        s1 = StringIO()
        s2 = StringIO()        

        s1.write("heap\t[")
        s2.write("\tidx\t[")        
        for idx, e in enumerate(self.heap):
            s1.write("{:4}".format(e))            
            s2.write("{:4}".format(idx))

        s1.write("  ]\n")
        s2.write("  ]")                
        s1.write(s2.getvalue())

        return s1.getvalue()

        
    """Private method to build the max heap"""
    def _buildHeap(self):

        # no need to sift half of the leaves
        start = self.n - math.floor(self.n / 2)
        # build the max heap
        for i in range(start, -1, -1):
            self._heapify(i)

            
    """Private method to set the heap property on a particular path"""
    def _heapify(self, i):

        # siftDown
        while True:

            largest = i # root
            left = 2 * i + 1 # left child
            right = 2 * i + 2 # right child

            if left < self.n: # 1st out-of-bound check
                if self.heap[left] > self.heap[i]:
                    largest = left
            if right < self.n: # 2nd out-of-bound check
                if self.heap[right] > self.heap[largest]:
                    largest = right
        
            if largest != i:
                # move the largest key upward
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                # keep sifting
                i = largest
            else:
                # stop sifting
                break

            
    """Returns `True` for a valid Max Heap"""
    def validate(self):

        for i in range(self.n):
            left = 2 * i + 1
            if left < self.n:
                if self.heap[left] > self.heap[i]:
                    return False
            right = 2 * i + 2
            if right < self.n:
                if self.heap[right] > self.heap[i]:
                    return False

        return True

    
    """Push a new element to the Max Heap"""
    def push(self, key):

        self.heap.append(key)
        self.n += 1

        # sift up
        child = self.n - 1
        while child > 0:
            parent = math.floor( (child - 1) / 2)
            if self.heap[child] > self.heap[parent]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                child = parent
            else:
                break

            
    """Pop the greatest element from the Max Heap"""
    def pop(self):

        if self.n < 1:
            return None

        # put the greatest key at the end of the backing array
        self.heap[0], self.heap[self.n-1] = self.heap[self.n-1], self.heap[0]
        self.n -= 1

        # restore the heap property
        parent = 0
        while parent < self.n:
            largest = parent
            left = 2 * parent + 1
            right = 2 * parent + 2

            if left < self.n:
                if self.heap[left] > self.heap[parent]:
                    largest = left
            if right < self.n:
                if self.heap[right] > self.heap[largest]:
                    largest = right

            if largest != parent:
                # sift down
                self.heap[largest], self.heap[parent] = self.heap[parent], self.heap[largest]
                parent = largest
            else:
                break

        # pop the greatest key from the backing array
        return self.heap.pop()
        

# random sequence construction (with odd or even nof keys)   
keys = [i * 10 for i in range(10 + random.randint(0, 3))]
# shuffle keys
random.shuffle(keys)
print("keys:\t{}".format(keys))
print("---")

# build a max heap from the collection of keys
maxHeap = myHeap(keys)
test(maxHeap, "__str__", printObj=False)

# test the heap property
test(maxHeap, "validate")

# perform some push operations
new_keys = [-1, 150, 18, 55]
for k in new_keys:
    test(maxHeap, "push", key=k)

# test again the heap property
test(maxHeap, "validate")

# test some pop operations
for i in range(3):
    test(maxHeap, "pop")

# test again the heap property
test(maxHeap, "validate")
