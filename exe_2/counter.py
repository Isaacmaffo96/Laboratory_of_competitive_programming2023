"""Implement a Counter, or rather count the occurrences of each
    character in a string. Note the ordering in the following example.

from collections import Counter
s = "hollywood"
Counter(s)
# Counter({'o': 3, 'l': 2, 'h': 1, 'y': 1, 'w': 1, 'd': 1})
"""

"""Complexity:
    - time: O(n*log(n)) where n is the length of s
    - space: O(d) where d in the number of unique letters in s
"""
def Counter(s):
    
    lc = dict()

    # count occurences
    for c in s:
        f = lc.get(c, -1)
        if f == -1:
            lc[c] = 1
        else:
            lc[c] += 1

    # sort occurences and return
    return dict(sorted(lc.items(), key=lambda x: x[1], reverse=True))


s = "hollywood"
print("String: {}".format(s))
print("Counter: {}".format(Counter(s)))
