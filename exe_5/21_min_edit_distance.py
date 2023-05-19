"""The minimum edit distance (Levenshtein) between two strings is the
minimum number of editing operations needed to change the first string
into the other. Valid edit operations consist of insertions, deletions
and substitutions.


Example:
	s1 = "rose"
	s2 = "frost"
	result = 2

"""


def printSubProblems(s1, s2, subProblem):
    """Prints s1, s2 and subProblem(s) to stdout"""

    n = len(s1)
    m = len(s2)

    print(" " * 5 + "\"" + " " * 3, end="")
    for j in range(1, m + 1):
        print(f"{s2[j-1]:4}", end="")
    print()
    for i in range(n + 1):
        beg = "\"["
        if i != 0:
            beg = f"{s1[i-1]}["
        print(beg, end="")
        for j in range(m + 1):
            print(f"{subProblem[i][j]:>4}", end="")
        print("]")


def med(s1, s2, debug=False):
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

    for i in range(m + 1):
        subProblem[0][i] = i
    for i in range(n + 1):
        subProblem[i][0] = i

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            difference = 1 if s1[i - 1] != s2[j - 1] else 0
            subProblem[i][j] = min(
                subProblem[i - 1][j] + 1,
                subProblem[i][j - 1] + 1,
                subProblem[i - 1][j - 1] + difference,
            )

    if debug:
        printSubProblems(s1, s2, subProblem)

    print(f"distance: {subProblem[-1][-1]}")
    print("---")

    # HOME EXERCISE: modify the minimum edit distance function to
    # solve the problem in O(M) space (looking at the code, you only
    # need subProblem[i-1] to solve subProblem[i])


strings = (
    ("rose", "frost"),
    ("home", "dome"),
    ("abce", "babce"),
    ("execution", "intention"),
    ("craftsmanship", "partnership"),
)

for s1, s2 in strings:
    med(s1, s2, True)
