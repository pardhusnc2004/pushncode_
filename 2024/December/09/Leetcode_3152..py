'''
    Leetcode Daily Question (09-12-2024)
    3152. Special Array II
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        
        def good(start, end, check):
            l = 0
            r = len(check) - 1
            while l <= r:
                m = (l+r) >> 1
                flag = check[m]
                if flag < start:
                    l = m + 1
                elif flag > end:
                    r = m - 1
                else:
                    return True
            return False

        res = [False] * len(queries)
        check = []

        for i in range(1, len(nums)):
            if nums[i]&1 == nums[i - 1]&1:
                check.append(i)

        for i, query in enumerate(queries):
            start, end = query
            flag = good(start + 1, end, check)
            if not flag:
                res[i] = True
        return res
