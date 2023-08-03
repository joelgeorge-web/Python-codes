#you are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#You may assume that you have an infinite number of each kind of coin.


def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] > amount else dp[amount]


testcases = int(input("Enter no of testcases: "))
while testcases:
    coins = list(map(int, input("Enter coins: ").split()))
    amount = int(input("Enter amount: "))
    print(coinChange(coins, amount))
    testcases -= 1