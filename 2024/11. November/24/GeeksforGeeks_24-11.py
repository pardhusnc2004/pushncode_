'''
    GeeksforGeeks Daily Question (24-11-2024)
    Kadane's Algorithm
    Python3 solution
'''

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        res = -1e9
        cur = 0
        for i in arr:
            cur += i
            res = max(res, cur)
            if cur < 0:
                cur = 0
        return res