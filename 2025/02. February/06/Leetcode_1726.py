'''
    Leetcode Daily Question (06-02-2025)
    1726. Tuple with Same Product
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for i in range(n):
            for j in range(i+1, n):
                tmp = nums[i]*nums[j]
                d[tmp] = d.get(tmp, 0)+1
        res = 0
        for i in d:
            tmp = d[i]
            res += ((tmp-1)*tmp) // 2
        # print(d)
        return res*8