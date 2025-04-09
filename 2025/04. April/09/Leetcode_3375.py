'''
    Leetcode Daily Question (09-04-2025)
    3375. Minimum Operations to Make Array Values Equal to K
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        tmp = min(c)
        if tmp < k:
            return -1
        return len(c) - (tmp == k)