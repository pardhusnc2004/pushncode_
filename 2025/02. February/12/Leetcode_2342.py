'''
    Leetcode Daily Question (12-02-2025)
    2342. Max Sum of a Pair With Equal Sum of Digits
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)

        def sumOfDigits(n):
            res = 0
            while n:
                res += n%10
                n //= 10
            return res
        
        for i in nums:
            tmp = sumOfDigits(i)
            if tmp not in d:
                d[tmp] = []
            d[tmp].append(i)
        
        res = -1
        for i in d:
            if len(d[i]) >= 2:
                d[i].sort()
                res = max(res, d[i][-1]+d[i][-2])
        return res