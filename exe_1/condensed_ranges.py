"""You are given a list of tuples representing ranges. Condense the ranges

E.g.:

Input: [(3, 5), (2, 3), (7, 9), (8, 10)]
Output: [(2, 5), (7, 10)]

Hint:

You can sort a list with list.sort() [complexity: time O(n*log(n)), space O(1)]

Complexity:
    -time: O(n*log(n)) [sorting, then linear scan]
    -space: O(n) [worst case, no overlaps]
"""


def condense_ranges(ranges):

    if ranges is None:
        raise TypeError("Input sequence is None")
    if len(ranges) <= 1:
        return ranges

    ranges.sort()  # sort by left end
    c_ranges = [ranges[0]]  # start with the first range (i.e., the leftmost)

    for r in ranges[1:]:
        # take the boundaries of the last range
        s_prev, e_prev = c_ranges[-1]
        # ...do the same for the current range
        s_curr, e_curr = r

        if e_prev < s_curr:  # no overlap
            c_ranges.append(r)
        else:  # overlap, condense s and r
            c_ranges[-1] = (s_prev, max(e_prev, e_curr))  # replace item (tuple immutability)

    return c_ranges


ranges = [(3, 5), (2, 3), (7, 9), (8, 10)]
print("ranges: {}".format(ranges))
print("condensed ranges: {}".format(condense_ranges(ranges)))
