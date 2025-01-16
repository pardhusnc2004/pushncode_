'''
    Leetcode Daily Question (16-01-2025)
    2425. Bitwise XOR of All Pairings
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        if n1&1 and n2&1:
            for i in nums1:
                res ^= i
            for i in nums2:
                res ^= i
            return res
        elif not n1&1 and not n2&1:
            return 0
        else:
            if n1&1:
                for i in nums2:
                    res ^= i
                return res
            else:
                for i in nums1:
                    res ^= i
                return res