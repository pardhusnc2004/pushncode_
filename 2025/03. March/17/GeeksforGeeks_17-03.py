'''
    GeeksforGeeks Daily Question (17-03-2025)
    Subset Sum Problem
    Python3 solution
'''

class Solution:
    def isSubsetSum (self, arr, s):
        N = len(arr)
        # code here 
        dp = [[0]*(s+1) for _ in range(N)]
        for i in range(N):
            dp[i][0] = 1
        for i in range(N):
            for j in range(s+1):
                nottake = dp[i-1][j]
                take = 0
                if j >= arr[i]:
                    take = dp[i-1][j-arr[i]]
                dp[i][j] = take or nottake
        return dp[-1][-1]
        
