'''
    Leetcode Daily Question (09-03-2025)
    3208. Alternating Groups II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k-1]
        n = len(colors)
        # print(colors)

        res = 0
        dq = deque()

        for i in range(n):
            if dq and colors[i] == dq[-1]:
                dq.clear()
            dq.append(colors[i])
            if len(dq) == k:
                res += 1
                dq.popleft()
            
        return res