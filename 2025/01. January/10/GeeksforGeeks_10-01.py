'''
    GeeksforGeeks Daily Question (10-01-2025)
    Count distinct elements in every window
    Python3 solution
'''

class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        d = {}
        res = []
        
        for i in range(n):
            d[arr[i]] = d.get(arr[i], 0)+1
            if i >= k:
                d[arr[i-k]] -= 1
                if not d[arr[i-k]]:
                    del d[arr[i-k]]
            if i >= k-1:
                res.append(len(d))
        
        return res