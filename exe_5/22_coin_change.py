"""You are given an array of coins having different denominations and
an integer amount representing the total money, you have to return the
fewest number of coins that you will need to make up that sum (return
+Inf if it is impossible). Assume there is an infinite number of coins
for each denomination."""

INF = float("inf")


def coinChangeNaive(coins, amount):
    """Returns the minimum number of coins to total the amount. This
    approach is unfeasible even for small amounts, can you guess why?
    Try to compute the complexity"""

    if amount < 0:
        return INF
    elif amount == 0:
        return 0

    minCoins = INF

    for coin in coins:
        # try to use this coin
        numCoins = 1 + coinChangeNaive(coins, amount - coin)
        # check the total number of coins used to total the amount
        minCoins = min(minCoins, numCoins)

    return minCoins


def coinChangeDynamic(coins, amount):
    """Returns the minimum number of coins to total the amount. Also
    returns which coins are used.

    Complexity:
        -T: O(Amount*N) [N is the number of coin denominations]
        -S: O(Amount)
    """

    # for each subroblem
    #[
    #  total number of coins used,
    #  reference to the previous sub-problem,
    #  additional coin denomination used,
    #]
    amounts = [[0, None, None] for _ in range(amount + 1)]

    # let's compute the coins to total each amount (bottom-up)
    for amount in range(1, amount + 1):
        # initially you don't know how many coins are needed
        amounts[amount] = [INF, None, None]
        # try to use all the coins to total the current (i-th) amount
        for c in range(len(coins)):
            # check coins[c] doesn't exceed amount
            if amount - coins[c] >= 0:
                subAmountCoins = amounts[amount - coins[c]][0]
                # if subAmountCoins is a finite number
                if subAmountCoins != INF:
                    # check whether coins[c] allows to reduce the
                    # current number of coins to total amount
                    # (initially this number is INF)
                    if subAmountCoins + 1 <= amounts[amount][0]:
                        amounts[amount][0] = subAmountCoins + 1
                        amounts[amount][1] = amounts[amount - coins[c]]
                        amounts[amount][2] = coins[c]

    # debug
    for a, line in enumerate(amounts):
        print(
            f"{a:3d} - {hex(id(line))[7:]}: ",
            f"[nofCoins: {line[0]},\t",
            f"new coin:\t{line[2]},\t",
            f"sub-problem: {hex(id(line[1]))[7:]}]",
        )

    # extract the coins
    usedCoins = []
    ptr = amounts[amount]
    while ptr[1]:
        usedCoins.append(ptr[2])
        ptr = ptr[1]

    return (amounts[amount][0], usedCoins)


def run(amount, coins):

    print(f"Amount: {amount}")
    print(f"Coins available: {coins}")
    if amount < 40:
        print(f"Number of coins (naive): {coinChangeNaive(coins, amount)}")
    print("number of coins (dynamic): {}, coins {}".format(
        *coinChangeDynamic(coins, amount)))
    print("-----")


# run some tests
coins = [2, 3, 4, 5, 10, 25]
amounts = [1, 7, 8, 17, 19, 28, 34, 39, 101, 103]

for amount in amounts:
    run(amount, coins)
