class Solution:
    def coinChange(self, coins, amount: int) -> int:
        change = [-1]*(amount+1)
        change[0]=0
        for coin in coins:
            for i in range(coin,len(change)):
                change[i] = 1 + change[i-coin] if change[i-coin] > -1 else -1
        return change[amount]
