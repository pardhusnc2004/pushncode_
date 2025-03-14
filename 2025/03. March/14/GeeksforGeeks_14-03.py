'''
    GeeksforGeeks Daily Question (14-03-2025)
    Coin Change (Count Ways)
    Python3 solution
'''

from functools import lru_cache

class Solution:
    def count(self, coins, rem):
        # code here 
        n = len(coins)
        dp = [0]*(rem+1)
        dp[0] = 1
        
        for i in range(n):
            for j in range(1, rem+1):
                if j >= coins[i]:
                    dp[j] += dp[j-coins[i]]
        
        return dp[-1] 
