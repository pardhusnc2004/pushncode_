'''
    GeeksforGeeks Daily Question (09-01-2025)
    Indexes of Subarray Sum
    Python3 solution
'''

class Solution:
    def subarraySum(self, arr, target):
        # code here
        res = []
        n = len(arr)
        
        cur = 0
        d = {0:-1}
        for i in range(n):
            cur += arr[i]
            if cur-target in d:
                res += [d[cur-target]+2, i+1]
                return res
            if cur not in d:
                d[cur] = i
        
        return [-1]