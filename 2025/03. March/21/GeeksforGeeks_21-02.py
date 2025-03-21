'''
    GeeksforGeeks Daily Question (21-03-2025)
    Stickler Thief
    Python3 solution
'''

class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr)
        dp = [0]*n
        res = 0
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+arr[i], dp[i-1])
        return max(dp)
