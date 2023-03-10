"""Gray code (1953) is a binary numeral system where two successive values
differ only in one bit.

Example for a 3-bit sequence: 000, 001, 011, 010, 110, 111, 101, 100.
From the example: G(4)=6=110.

"""

"""There is a simple way to solve the problem.

Conversion table

Decimal	Binary	Gray
0	    0000	0000
1	    0001	0001
2	    0010	0011
3	    0011	0010
4	    0100	0110
5	    0101	0111
6	    0110	0101
7	    0111	0100
8	    1000	1100
9	    1001	1101
10	    1010	1111
11	    1011	1110
12	    1100	1010
13	    1101	1011
14	    1110	1001
15	    1111	1000   

Take 4 as an example:

G(4) -> 110
B(4) -> 100

G(3) -> 010
B(3) -> 011

G(7) -> 100
B(7) -> 111

The i-th bit of g(n) equals 1 only when the i-th bit of b(n) equals 1
and i+1-th equals 0 (or the opposite, i-th bit equals 0 and i+1-th equals 1)

Complexity:
    - time: O(1)
    - space: O(1)

"""
def gray(n):
    return n ^ (n>>1)


n = 4
print("n = {}, gray code = {}, gray code (bin.) = {}".format(n,
                                                             gray(n),
                                                             format(gray(n), "b")))

"""
# Build the previous sequence with the following
for n in range(7):
    print("n = {}, gray code = {}, gray code (bin.) = {}".format(n,
                                                             gray(n),
                                                             format(gray(n), "03b")))
"""


"""
Additional practice: from a gray code, find the original number
"""
