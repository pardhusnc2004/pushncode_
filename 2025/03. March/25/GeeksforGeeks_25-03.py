'''
    GeeksforGeeks Daily Question (25-03-2025)
    Boolean Parenthesization
    Python3 solution
'''

from functools import lru_cache
class Solution:
    def countWays(self, s):
        @lru_cache(None)
        def solve(i, j):
            if i == j: 
                if s[i] == 'T':
                    return (1, 0) 
                return (0, 1)
    
            true_count, false_count = 0, 0
    
            for k in range(i + 1, j, 2): 
                left_true, left_false = solve(i, k - 1)
                right_true, right_false = solve(k + 1, j)
    
                if s[k] == '&':
                    true_count += left_true * right_true
                    false_count += (left_true * right_false) + (left_false * right_true) + (left_false * right_false)
                elif s[k] == '|':
                    true_count += (left_true * right_true) + (left_true * right_false) + (left_false * right_true)
                    false_count += left_false * right_false
                elif s[k] == '^':
                    true_count += (left_true * right_false) + (left_false * right_true)
                    false_count += (left_true * right_true) + (left_false * right_false)
    
            return (true_count, false_count)
    
        true_ways, _ = solve(0, len(s) - 1)
        return true_ways
