'''
    GeeksforGeeks Daily Question (30-10-2024)
    Pairs with difference k
    Python3 solution
'''
from collections import Counter
class Solution:
    def countPairsWithDiffK(self,arr, k):
        # code here
        res = 0
        d = Counter(arr)
        if not k:
            for i in d.values():
                if i > 1:
                    res += (i*(i-1))//2
            return res
        for i in sorted(d.keys()):
            if i+k in d:
                res += d[i]*(d[i+k])
        
        return res