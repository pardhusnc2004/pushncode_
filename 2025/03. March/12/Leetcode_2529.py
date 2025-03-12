'''
    Leetcode Daily Question (12-03-2025)
    2529. Maximum Count of Positive Integer and Negative Integer
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(1 if i<0 else 0 for i in nums), sum(1 if i>0 else 0 for i in nums))