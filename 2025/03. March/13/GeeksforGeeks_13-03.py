'''
    GeeksforGeeks Daily Question (13-03-2025)
    0 - 1 Knapsack Problem
    Python3 solution
'''

class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapsack(self, W, val, wt):
        # code here
        N = len(wt)
        
        dp = [[0]*(W+1) for _ in range(N)]
        for i in range(wt[0], W+1):
            dp[0][i] = val[0]
        
        for i in range(1, N):
            for j in range(1, W+1):
                dp[i][j] = dp[i-1][j]
                if j >= wt[i]:
                    dp[i][j] = max(dp[i][j], val[i]+dp[i-1][j-wt[i]])
        # for i in dp:
        #     print(*i)
        return dp[-1][-1]