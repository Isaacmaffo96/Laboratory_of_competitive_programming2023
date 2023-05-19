"""You are given a list of items. Each item has a weight and a value.
You are also given a knapsack with a maximum capacity (i.e., the
maximum weight it can carry). Determine which of the items to pack in
the knapsack so that the value is maximum.
"""


def knapsack(values, weights, capacity):
    """Returns the maximum value for a knapsack with limited capacity

    Complexity:
        -T: O(N*Capacity) [N is the number of items]
        -S: O(Capacity) 
    """

    kns = [[0 for _ in range(capacity + 1)] for _ in range(2)]
    items = len(values)

    # debug: capacities
    print("c:", end="")
    for c in range(capacity + 1):
        print(f"{c:2d} ", end="")
    print("")

    for i in range(items + 1):
        for c in range(capacity + 1):

            # base case: no capacity or no items, empty knapsack
            if i == 0 or c == 0:
                kns[i % 2][c] = 0
            # case 1: enough capacity to pack the current item, we
            # can pack or discard the item
            elif c >= weights[i - 1]:
                kns[i % 2][c] = max(
                    values[i - 1] + kns[(i - 1) % 2][c - weights[i - 1]],
                    kns[(i - 1) % 2][c],
                )
            # case 2: no more capacity, no increase of value
            else:
                kns[i % 2][c] = kns[(i - 1) % 2][c]

        # debug: solution with the first [0; i] items
        print("[ ", end="")
        for v in kns[i % 2]:
            print(f"{v:2d} ", end="")
        print("]")

    return kns[len(weights) % 2][-1]


def run(values, weights, capacity):

    print(f"values: {values}")
    print(f"weights: {weights}")
    print(f"knapsack capacity: {capacity}")
    print(f"knapsack value: {knapsack(values, weights, capacity)}")
    print("-----")


values = [
    [6, 10, 12],
    [6, 6, 6, 6, 6, 10, 12],
    [6, 6, 6, 6, 9, 10, 12],
]

weights = [
    [10, 20, 30],
    [10, 10, 10, 10, 10, 20, 30],
    [5, 5, 5, 5, 2, 8, 15],
]

capacities = [
    50,
    50,
    25,
]

for v, w, c in zip(values, weights, capacities):
    run(v, w, c)
