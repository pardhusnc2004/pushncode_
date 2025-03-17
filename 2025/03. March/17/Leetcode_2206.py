'''
    Leetcode Daily Question (17-03-2025)
    2206. Divide Array Into Equal Pairs
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in c:
            if c[i]&1:
                return False
        return True