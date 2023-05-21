"""You are given a list of integer numbers. Find the sub-list with
    the largest sum and return the sum

E.g.:

input = [1,2,-3,1,-2,3,-1,4,5,-7,4,-3]
output = 11 (from [3,-1,4,5])
"""

"""
Complexity:
    - time: O(n)
    - space: O(1)
"""


def m_sum(numbers):

    if len(numbers) == 0:
        raise ValueError("No numbers provided")

    currSum = numbers[0]
    maxSum = numbers[0]

    for i in range(1, len(numbers)):

        # try to cumulate
        currSum = max(currSum + numbers[i], numbers[i])
        # update the maximum value
        maxSum = max(maxSum, currSum)

    return maxSum


numbers = [1,2,-3,1,-2,3,-1,4,5,-7,4,-3]
print("numbers: {}".format(numbers))
print("max sum: {}".format(m_sum(numbers)))
