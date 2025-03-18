'''
    GeeksforGeeks Daily Question (18-03-2025)
    Partition Equal Subset Sum
    Python3 solution
'''

from math import dist
from heapq import *
from typing import List

class Solution:
    def equalPartition(self, arr):
        N = len(arr)
        # code here
        _sum = sum(arr)
        if _sum&1:
            return False
        req = _sum//2
        dp = [0]*(req+1)
        dp[0] = 1
        
        for i in range(N):
            for j in range(req, -1, -1):
                if arr[i] <= j:
                    dp[j] |= dp[j-arr[i]]
                
        return dp[-1]