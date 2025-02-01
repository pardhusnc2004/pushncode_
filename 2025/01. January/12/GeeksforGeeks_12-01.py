'''
    GeeksforGeeks Daily Question (12-01-2025)
    Trapping Rain Water
    Python3 solution
'''

class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        rMax, lMax = [-1]*n, [-1]*n
        lMax[0] = arr[0]
        rMax[-1] = arr[-1]
        for i in range(1, n):
            lMax[i] = max(arr[i], lMax[i-1])
        for i in range(n-2, -1, -1):
            rMax[i] = max(rMax[i+1], arr[i])
        res = 0
        
        for i in range(n):
            res += min(rMax[i], lMax[i])-arr[i]
        
        return res