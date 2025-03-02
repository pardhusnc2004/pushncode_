'''
    GeeksforGeeks Daily Question (02-03-2025)
    K Sized Subarray Maximum
    Python3 solution
'''

from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        res = []
        n = len(arr)
        
        d = deque()
        for i in range(n):
            while d and i-d[0] >= k:
                d.popleft()
            while d and arr[i] >= arr[d[-1]]:
                d.pop()
            d.append(i)
            if i >= k-1:
                res.append(arr[d[0]])
        
        return res
