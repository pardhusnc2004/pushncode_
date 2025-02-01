'''
    GeeksforGeeks Daily Question (15-01-2025)
    Longest Subarray with Sum K
    Python3 solution
'''

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n = len(arr)
        d, left, cur = {0:-1}, 0, 0
        res = 0
        
        for i in range(n):
            cur += arr[i]
            if cur == k:
                res = i+1
            if cur-k in d:
                res = max(res, i-d[cur-k])
            if cur not in d:
                d[cur] = i
        
        return res