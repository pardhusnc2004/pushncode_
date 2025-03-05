'''
    GeeksforGeeks Daily Question (05-03-2025)
    Longest String Chain
    Python3 solution
'''

from functools import lru_cache

class Solution:
    def longestStringChain(self, words):
        # Code here
        words = set(words)
        dp = {}
        
        def solve(word):
            res = 0
            if word in dp:
                return dp[word]
            for i in range(len(word)):
                newWord = word[:i]+word[i+1:]
                if newWord in words:
                    res = max(res, solve(newWord))
            dp[word] = res+1
            return res+1
            
        res = 0
        for word in words:
            res = max(res, solve(word))
            
        return res