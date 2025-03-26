'''
    GeeksforGeeks Daily Question (26-03-2025)
    Word Break
    Python3 solution
'''

class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        words = set(dictionary)
        n = len(s)
        dp = [0]*(n+1)
        dp[-1] = 1
        for i in range(n-1, -1, -1):
            for word in words:
                if i+len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] |= dp[i+len(word)]
        return dp[0]
