'''
    GeeksforGeeks Daily Question (02-01-2025)
    Subarrays with sum K
    Python3 solution
'''

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        res = 0
        cur = 0
        d = {0:1}
        for i in arr:
            cur += i
            if cur-k in d:
                res += d[cur-k]
            d[cur] = d.get(cur, 0)+1
        return res
