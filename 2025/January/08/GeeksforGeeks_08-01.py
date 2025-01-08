'''
    GeeksforGeeks Daily Question (08-01-2025)
    Count the number of possible triangles
    Python3 solution
'''

from bisect import *

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        # print(arr)
        res = 0
        
        for i in range(n):
            for j in range(i+1, n):
                idx = bisect_left(arr, arr[i]+arr[j], j+1)
                res += idx-j-1
                # print(arr[i], arr[j], j, idx, idx-j)
        
        return res