'''
    Leetcode Daily Question (05-04-2025)
    1863. Sum of All Subset XOR Totals
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        N = 1<<n
        res = 0
        for i in range(N):
            xor = 0
            for j in range(n):
                if (i>>j)&1:
                    xor ^= nums[j]
            res += xor
        return res