'''
    GeeksforGeeks Daily Question (06-03-2025)
    Longest Common Subsequence
    Python3 solution
'''

from functools import lru_cache

class Solution:
    def lcs(self, s1, s2):
        # code here
        
        n1, n2 = len(s1), len(s2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]