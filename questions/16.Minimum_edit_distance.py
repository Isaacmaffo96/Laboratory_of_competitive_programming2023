# 16. Calcolo della minima distanza di edit date due stringhe (con operazioni di cancellazione, inserimento, sostituzione)

"""The minimum edit distance (Levenshtein) between two strings is the
minimum number of editing operations needed to change the first string
into the other. Valid edit operations consist of insertions, deletions
and substitutions.


Example:
    s1 = "rose"
    s2 = "frost"
    result = 2
"""


def minimum_edit_distance(s1, s2, debug=False):
    """Returns the minimum number of operations (insert, delete,
    replace) to transform s1 into s2

    Complexity:
        -T: O(N*M) [N is the length of s1, M is the length of s2]
        -S: O(N*M) [actually, the problem can be solved in O(M), see
         home exercise]
    """

    print(f"s1: {s1}, s2: {s2}")

    n = len(s1)
    m = len(s2)

    subProblem = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        subProblem[i][0] = i

    for j in range(m + 1):
        subProblem[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            difference = 1 if s1[i - 1] != s2[j - 1] else 0
            subProblem[i][j] = min(
                subProblem[i - 1][j] + 1,
                subProblem[i][j - 1] + 1,
                subProblem[i - 1][j - 1] + difference,
            )

    return subProblem[-1][-1]


"""
Complexity:
    - Time: O(N*M) 
    - Space: O(N*M)
"""
