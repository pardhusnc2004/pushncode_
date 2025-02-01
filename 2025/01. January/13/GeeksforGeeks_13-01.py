'''
    GeeksforGeeks Daily Question (13-01-2025)
    Container With Most Water
    Python3 solution
'''

class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        l, r = 0, n-1
        res = 0
        
        while l < r:
            width = r-l
            height = min(arr[l], arr[r])
            res = max(res, width*height)
            if arr[l] >= arr[r]:
                r -= 1
            else:
                l += 1
        
        return res