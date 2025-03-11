'''
    GeeksforGeeks Daily Question (11-03-2025)
    Ways to Reach the n'th Stair
    Python3 solution
'''

from functools import lru_cache
class Solution:
    def countWays(self, n):
        # code here
        @lru_cache
        def solve(n):
            if n <= 1:
                return 1
            res = solve(n-1)
            if n > 1:
                res += solve(n-2)
            return res
        return solve(n)