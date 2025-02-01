'''
    Leetcode Daily Question (14-11-2024)
    2064. Minimized Maximum of Products Distributed to Any Store
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *

class Solution:
    def minimizedMaximum(self, n: int, arr: List[int]) -> int:
        def poss(m):
            cur = 0
            x = 0
            for i in arr:
                x += (i+(m-1))//m
            return x <= n
        res = None
        l, r = 1, max(arr)
        while l <= r:
            m = (l+r) >> 1
            if poss(m):
                res = m
                r = m-1
                # case
            else:
                l = m+1
                # opposite case
        return res