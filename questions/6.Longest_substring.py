# 6. Data una stringa, ricerca della più lunga sotto-stringa (sliding windows)

def longest_substring(s):

    if len(s) <= 1:
        return s

    start = left = 0
    end = right = 0
    indexes = dict()  # {letter: index}

    while right < len(s):
        if indexes.get(s[right], -1) == -1:
            # save the index of this letter
            indexes[s[right]] = right
            # update longest substring
            if right - left > end - start:
                start = left
                end = right
        else:
            # repeated letter
            rep_l = s[right]
            # repeated letter next index
            rep_ni = indexes[rep_l] + 1
            # remove indexes of letters that are not in the substring anymore
            while left < rep_ni:
                del indexes[s[left]]
                left += 1
            # set the new index properly
            indexes[rep_l] = right
        # move right forward
        right += 1

    return s[start:end + 1]


"""Complexity:
    -time: O(n) [worst case: "abababab...ab"]
    -space: O(n) [worst case: "abcdefghilmno..."]
"""


def solve(s):
    print("-------------------------------------")
    print(f"s:\t\t\t\t\t{s}")
    print("sliding windows:\t{}".format(longest_substring(s)))


print("Find the longest substring in s")
solve("")
solve("a")
solve("aaaaa")
solve("abbbbbcd")
solve("abbbbbcdee")
solve("abcdefg")
solve("abcdefgghilmno")
