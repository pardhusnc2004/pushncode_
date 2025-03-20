'''
    GeeksforGeeks Daily Question (20-03-2025)
    Stock Buy and Sell – Max 2 Transactions Allowed
    Python3 solution
'''

from functools import lru_cache
class Solution:
    def maxProfit(self, prices, k=2):
        # code here
        n=len(prices)
        dp=[[0] * n for _ in range(k+1)]
        if n<=1 or k ==0:
            return 0
        for i in range(1,k+1):
            dif=-prices[0]
            for j in range(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j]+dif)
                dif=max(dif,dp[i-1][j]-prices[j])
        return dp[k][n-1]