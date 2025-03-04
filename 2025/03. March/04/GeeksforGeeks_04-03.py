'''
    GeeksforGeeks Daily Question (04-03-2025)
    Longest Increasing Subsequence
    Python3 solution
'''

class Solution:
    def lis(self, arr):
        # code here
        
        n = len(arr)
        dp = [1]*n
        
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
