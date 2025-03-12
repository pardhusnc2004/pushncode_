'''
    GeeksforGeeks Daily Question (12-03-2025)
    Min Cost Climbing Stairs
    Python3 solution
'''

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n = len(cost)
        cost += [0]
        dp = [0]*(n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n+1):
            dp[i] = cost[i]+min(dp[i-1], dp[i-2])
        return dp[-1]