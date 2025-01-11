'''
    GeeksforGeeks Daily Question (11-01-2025)
    Longest substring with distinct characters
    Python3 solution
'''

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        res = 0
        d, left = {}, 0
        n = len(s)
        
        for i in range(n):
            d[s[i]] = d.get(s[i], 0)+1
            while d[s[i]] > 1:
                d[s[left]] -= 1
                if not d[s[left]]:
                    del d[s[left]]
                left += 1
            res = max(res, i-left+1)
        
        return res