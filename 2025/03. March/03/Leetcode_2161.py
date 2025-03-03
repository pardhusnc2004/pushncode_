'''
    Leetcode Daily Question (03-03-2025)
    2161. Partition Array According to Given Pivot
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, r = [], []
        pivotCnt = 0
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i > pivot:
                r.append(i)
            else:
                pivotCnt += 1
        res = []
        res += l
        res += [pivot]*pivotCnt
        res += r
        return res