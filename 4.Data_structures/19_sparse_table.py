"""Answering range minimum queries with a sparse table."""
import math


class SparseTable:

    def __init__(self):

        self._data: list = list()
        self._st: list = list()
        self._n: int = 0
        self._log: int = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: list):

        self._data = data
        if data is None or len(data) == 0:
            raise Exception("No data provided")
        self._precompute()
        self._visualize()

    def _precompute(self):
        """
        Precomputes the sparse table

        Complexity:
            -T: O(N*log(N))
            -S: O(N*log(N))
        """

        self._n = len(self._data)
        # question: what happens when self._n is a power of 2?
        self._log = math.floor(math.log2(self._n)) + 1

        self._st = [[float("inf") for _ in range(self._log)]
                    for _ in range(self._n)]

        # 1-element ranges
        for i in range(self._n):
            self._st[i][0] = self.data[i]

        # power-of-two ranges (NB: loop ordering matters)
        for k in range(1, self._log):
            i = 0
            while i + 2**k - 1 < self._n:
                self._st[i][k] = min(
                    self._st[i][k - 1],
                    self._st[i + 2**(k - 1)][k - 1],
                )
                i += 1

    def _visualize(self):

        print(f"data:\n\t{self._data}")

        print("st:")
        # length of the ranges
        print(
            "\t   ",
            "".join(f"{2**p:5}" for p in range(self._log)),
        )
        # sparse table content
        for i, line in enumerate(self._st):
            print(
                f"\t{i:2}[",
                "".join(f"{line[c]:5}" for c in range(self._log)),
                "]",
            )

    def query(self, L, R):
        """Returns the minimum element within the range [L;R]

        Complexity:
            -T: O(log(R-L)) [to determine k based on the span, lookups take O(1)]
            -S: O(1)
        """

        if L > R:
            L, R = R, L
        if L < 0 or R > self._n - 1:
            raise Exception("Invalid range input")

        span = R - L + 1
        k = 0
        while 2**(k + 1) <= span:
            k += 1
        # table lookup takes O(1)
        return min(
            self._st[L][k],
            self._st[R + 1 - 2**k][k],
        )


# init sparse table
st = SparseTable()
# precomputation
st.data = [2, 3, 7, 5, 9, 11, 1, 3, -1, 10, 4, 2, 18, 7, 9, 11]
# query
ranges = [
    (0, 1),
    (1, 4),
    (1, 5),
    (0, 7),
    (4, 6),
    (3, 8),
    (1, 14),
    (14, 15),
    (15, 15),
]
for L, R in ranges:
    print(f"query({L},{R}): {st.query(L, R)}")
