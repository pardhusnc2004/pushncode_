'''
    Leetcode Daily Question (15-12-2024)
    1792. Maximum Average Pass Ratio
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], toppers: int) -> float:
        def gain(i, j):
            return (i + 1) / (j + 1) - i / j
        hp = []
        for i, j in classes:
            heappush(hp, (-gain(i, j), i, j))
        for _ in range(toppers):
            __, i, j = heappop(hp)
            i += 1
            j += 1
            heappush(hp, (-gain(i, j), i, j))
        ll = len(classes)
        res = 0
        for _, i, j in hp:
            res += i/j
        return res/ll