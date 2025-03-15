'''
    GeeksforGeeks Daily Question (15-03-2025)
    Coin Change (Minimum Coins)
    Python3 solution
'''

from functools import cache

class Solution:
    def minCoins(self, coins, S):
        n = len(coins)
        @cache
        def solve(i, rem):
            if i == 0:
                if rem%coins[i] == 0:
                    return rem//coins[i]
                return 10**9
            notTake = solve(i-1, rem)
            take = 10**9
            if rem >= coins[i]:
                take = 1+solve(i, rem-coins[i])
            return min(take, notTake)
        res = solve(n-1, S)
        return res if res != 10**9 else -1