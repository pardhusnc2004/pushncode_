'''
    GeeksforGeeks Daily Question (14-12-2024)
    Search in Rotated Sorted Array
    Python3 solution
'''

from math import inf

class Solution:
    def search(self,arr,x):
        n = len(arr)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) >> 1
            # print(l, r, mid)
            if (arr[mid] == x):
                return mid
            if arr[mid] >= arr[l]:
                if arr[l] <= x <= arr[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if arr[mid] <= x <= arr[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
