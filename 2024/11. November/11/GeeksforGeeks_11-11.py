'''
    GeeksforGeeks Daily Question (11-11-2024)
    Make array elements unique
    Python3 solution
'''

from collections import *
class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        res = 0
        for i in range(1, len(arr)):
            print(arr[i] <= arr[i-1], arr[i], arr[i-1])
        # print(arr)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                # print(i, i-1, arr[i], arr[i-1])
                res += arr[i-1] - arr[i] + 1
                arr[i] = arr[i-1] + 1
        return res 
