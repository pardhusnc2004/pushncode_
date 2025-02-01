'''
    GeeksforGeeks Daily Question (03-01-2025)
    Count Subarrays with given XOR
    Python3 solution
'''

class Solution:
    def subarrayXor(self, arr, k):
        # code here
        res = 0
        
        d = {0:1}
        curXor = 0
        for i in arr:
            curXor ^= i
            if curXor ^ k in d:
                res += d[curXor^k]
            d[curXor] = d.get(curXor, 0)+1
        return res
