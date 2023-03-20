import unittest
import random

if __package__ is None:
    from .bubblesort import bubblesort
    from .selectionsort import selectionsort
    from .insertionsort import insertionsort
    from .mergesort import mergesort
    from .quicksort import quicksort
    from .heapsort import heapsort
    from .radixsort import radixsort
    from .hybrid_approach import hybrid_approach
else:
    from bubblesort import bubblesort
    from selectionsort import selectionsort
    from insertionsort import insertionsort
    from mergesort import mergesort
    from quicksort import quicksort
    from heapsort import heapsort
    from radixsort import radixsort
    from hybrid_approach import hybrid_approach
    

class SortingTest(unittest.TestCase):

    def setUp(self):
        # input
        self.size = 1022
        self.s = [int(random.uniform(0, 100)) for _ in range(0, self.size)]
        # correct test result
        self.sorted_s = self.s.copy()
        self.sorted_s.sort()

    def _test_wrapper(self, algorithm, *params):
        sc = self.s.copy()
        result = algorithm(sc, *params)
        # some algorithms perform in-place sorting, others return a result
        self.assertEqual(self.sorted_s, result if result else sc)

    def test_bubblesort(self):
        self._test_wrapper(bubblesort)

    def test_selectionsort(self):
        self._test_wrapper(selectionsort)

    def test_insertionsort(self):
        self._test_wrapper(insertionsort)

    def test_mergesort(self):
        self._test_wrapper(mergesort)

    def test_quicksort(self):
        self._test_wrapper(quicksort, 0, self.size - 1)

    def test_heapsort(self):
        self._test_wrapper(heapsort)

    def test_radixsort(self):
        self._test_wrapper(radixsort)
        
    def test_hybrid_approach(self):
        self._test_wrapper(hybrid_approach, 0, self.size - 1)
