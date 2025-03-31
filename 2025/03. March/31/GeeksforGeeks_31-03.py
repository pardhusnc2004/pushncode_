'''
    GeeksforGeeks Daily Question (31-03-2025)
    Maximize partitions in a String
    Python3 solution
'''

from functools import lru_cache

class Solution:
    def maxPartitions(self , s):
        # code here
        n = len(s)
        alphaMap = {chr(i+ord('a')):[-1, -1] for i in range(26)}

        for i in range(n):
            if alphaMap[s[i]][0] == -1:
                alphaMap[s[i]] = [i, i]
            else:
                alphaMap[s[i]][1] = i

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return n
            maxi = i
            for f, l in alphaMap.values():
                if f <= i < l:
                    maxi = max(maxi, solve(l))
            return maxi
        
        res = 0
        tmp = 0
        prv = 0
        while tmp < n:
            prv = tmp
            tmp = solve(tmp)+1
            res += 1
            
        return res