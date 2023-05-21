"""Ex.1 bits_to_flip.

You are given two positive integer numbers a and b. Find the number of
bits to flip to convert int a to int b

"""

"""
Complexity:
   -a and b are guaranteed to have same size
   -space O(log_2(a))
   -time O(log_2(a))
"""


def naive(a, b):
    bts = 0
    str_a = format(a, "010b")  # 010 size formats the output to fit in 10 characters width, with 0 padding;
    str_b = format(b, "010b")  # 2 characters for the 0b prefix, the other 8 for the binary digits.
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            bts += 1
    return bts


"""
Complexity:
   -space O(1)
   -time O(Log_2(a))
"""


def bits_to_flip(a, b):
    bts = 0
    # determine which bits need to be flipped
    c = a ^ b  # ^ --> XOR
    # compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0
    # count them without converting to str representation
    # c: 0b00010010
    while c != 0:  # Comparison operator: check the value of c
        bts += c & 1  # least significant bit # Bitwise Operator & check the binary numbers
        c = c >> 1  # div by 2 , Bitwise Operator >> : Signed right shift
        # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
    return bts


"""
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""


a = int('11101', base=2)  # a = 29
b = int('01111', base=2)  # b = 15

print("a: {}\nb: {}".format(
    format(a, "#010b"), 
    format(b, "#010b")
))

print("bits to flip, naive solution: ", naive(a, b))
print("bits to flip, optimized solution: ", bits_to_flip(a, b))
