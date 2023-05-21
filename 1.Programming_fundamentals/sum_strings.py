"""You are given two non-negative integers, a and b represented as
string. Return the sum a + b as string.

Do not use numbers to handle large integers, also, do not convert
strings to integers directly.

Test the code with different inputs.

E.g.:
a = "168797263998"
b = "28"
r = "168797264026"
"""

"""Complexity:
    - space: O(n) [where n is the length of the longest between a and b]
    - time: O(n)
"""
def sum_strings(a, b):
    
    r = []

    diff = len(a) - len(b)
    carry = 0

    # set a to the longest string
    if diff < 0:
        a, b = b, a

    # sum
    i = 0
    while i < len(a):
        
        tmp = int(a[len(a)-1-i]) + carry # *
        if i < len(b): # *
            tmp += int(b[len(b)-1-i]) 
            
        carry = 0
        
        if tmp < 10:
            r.append(str(tmp))
        else:
            carry = 1
            r.append(str(tmp)[1]) # the char on the right is the unit
        i += 1

    if carry == 1:
        r.append("1")

    return "".join(reversed(r))


def solve(a, b):

    print("a: {}".format(a))
    print("b: {}".format(b))
    print("r: {}".format(sum_strings(a, b)))

    print("---")

solve(a="168797263998", b="28")

solve(a="1", b="9999999")

solve(a="1000001", b="9999999")
