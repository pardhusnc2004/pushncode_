'''
    GeeksforGeeks Daily Question (15-10-2024)
    Subarray range with given sum
    Python3 solution
'''

class Solution:
    def subArraySum(self,arr, tar):
        #Your code here
        d = {0:1}
        res = 0
        cur = 0
        for i in arr:
            cur += i
            res += d.get(cur-tar, 0)
            d[cur] = d.get(cur,0)+1
        return res