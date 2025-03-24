'''
    GeeksforGeeks Daily Question (24-03-2025)
    Matrix Chain Multiplication
    Python3 solution
'''

from functools import lru_cache

class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        @lru_cache(None)
        def solve(i, j):
            if i == j:
                return 0
            maxi = 1e16
            for k in range(i, j):
                maxi = min(maxi, 
                        arr[i-1]*arr[k]*arr[j] 
                        + solve(i, k) 
                        + solve(k+1, j)
                    )
            return maxi
        return solve(1, len(arr)-1)