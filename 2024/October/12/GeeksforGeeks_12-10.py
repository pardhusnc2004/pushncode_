'''
    GeeksforGeeks Daily Question (12-10-2024)
    Two Smallests in Every Subarray
    Python3 solution
'''

class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        if len(arr) < 2:
            return -1
        res = 0
        for i in range(len(arr)-1):
            res = max(res, arr[i]+arr[i+1])
        return res