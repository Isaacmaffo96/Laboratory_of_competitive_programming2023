"""Coding strategy: sliding windows

Problem:
========

You are given a string s. Find the longest substring without repeating
characters.

Example:
========

s = "abbbbbcdee"
result = "bcde"
"""


"""Complexity:
    -time: O(n^2) [worst case: "abcde...zz"]
    -space: O(n) [worst case: "abcde...zz"]
"""


def naive_solution(s):

    if len(s) <= 1:
        return s

    # start and end of the longest substring
    start = end = 0
    # start and end of the current substring
    left = right = 0
    
    while left < len(s):
        # start a new substring
        letters = set(s[left])
        right = left + 1        
        while right < len(s):
            # check next letter
            if s[right] not in letters:
                # add letter to the substring
                letters.add(s[right])
                # update longest substring
                if right - left > end - start:
                    start = left
                    end = right
                # move right forward
                right += 1
            else:
                # end of substring
                break
        # move left forward
        left += 1

    return s[start:end+1]


"""Complexity:
    -time: O(n) [worst case: "abababab...ab"]
    -space: O(n) [worst case: "abcdefghilmno..."]
"""


def sw_solution(s):

    if len(s) <= 1:
        return s

    start = left = 0
    end = right = 0
    indexes = dict() # {letter: index}

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
            rep_ni = indexes[s[right]] + 1
            # remove indexes of letters that are not in the substring anymore
            while left < rep_ni:
                del indexes[s[left]]
                left += 1
            # set the new index properly
            indexes[rep_l] = right
        # move right forward
        right += 1

    return s[start:end+1]


def solve(s):
    
    print("---")    
    print(f"s:\t\t\t{s}")
    print("naive:\t\t\t{}".format(naive_solution(s)))
    print("sliding windows:\t{}".format(sw_solution(s)))
    

print("Find the longest substring in s")    
solve("")
solve("a")
solve("aaaaa")
solve("abbbbbcd")
solve("abbbbbcdee")
solve("abcdefg")
solve("abcdefgghilmno")
