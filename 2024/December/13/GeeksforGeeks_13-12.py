'''
    GeeksforGeeks Daily Question (13-12-2024)
    Sorted and Rotated Minimum
    Python3 solution
'''

from math import inf

class Solution:
    def findMin(self, arr):
        n = len(arr)
        l, r = 0, n-1
        res = inf
        while l <= r:
            mid = (l+r) >> 1
            res = min(res, arr[mid], arr[l], arr[r])
            if arr[mid] > arr[l]:
                res = min(res, arr[l])
                l = mid+1
            else:
                r = mid-1
        return res
