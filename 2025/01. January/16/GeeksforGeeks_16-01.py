'''
    GeeksforGeeks Daily Question (16-01-2025)
    Largest subarray of 0's and 1's
    Python3 solution
'''

class Solution:
    def maxLen(self, arr):
        # code here
        n = len(arr)
        res = 0
        d = {0:-1}
        cur = 0
        for i in range(n):
            cur += 1 if arr[i] == 1 else -1
            if not cur:
                res = i+1
            elif cur in d:
                res = max(res, i-d[cur])
            if cur not in d:
                d[cur] = i
        return res