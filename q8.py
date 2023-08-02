#you are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#You may assume that you have an infinite number of each kind of coin.


def coinChange(coins, amount):
    coins.sort(reverse=True)
    count = 0
    a = 0
    if amount<coins[0]:
        while amount>=count:
            coins[0]+=coins[0]
            a+=1
            if(amount-count<coins[0]):
                coins.pop(0)
                a-=1
        
    else:
        return -1

    return a

testcases = int(input("Enter no of testcases: "))
while testcases:
    coins = list(map(int, input("Enter coins: ").split()))
    amount = int(input("Enter amount: "))
    print(coinChange(coins, amount))
    testcases -= 1