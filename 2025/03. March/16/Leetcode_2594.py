'''
    Leetcode Daily Question (16-03-2025)
    2594. Minimum Time to Repair Cars
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        ranks.sort()
        
        def good(m):
            res = 0
            for i in ranks:
                res += int(sqrt(m//i))
            # print(m, res)
            return res >= cars
        
        l, r = 1, cars*cars*ranks[-1]
        res = r

        while l <= r:
            m = (l+r) >> 1
            if good(m):
                res = min(res, m)
                r = m-1
            else:
                l = m+1

        return res