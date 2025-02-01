'''
    GeeksforGeeks Daily Question (25-11-2024)
    Maximum Product Subarray
    Python3 solution
'''

from math import inf

class Solution:
    
    def maxProduct(self, arr):
        res = -inf
        cur = 1
        for i in arr:
            cur *= i
            res = max(res, cur)
            if cur == 0:
                cur = 1
        cur = 1
        for i in reversed(arr):
            cur *= i
            res = max(res, cur)
            if cur == 0:
                cur = 1
        return res
