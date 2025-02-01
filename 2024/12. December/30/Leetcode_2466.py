'''
    Leetcode Daily Question (30-12-2024)
    2466. Count Ways To Build Good Strings
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import *

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        @cache
        def solve(l):
            if l > high:
                return 0
            res = 0
            if low <= l <= high:
                res += 1 
            res += solve(l+zero)+solve(l+one)
            return res%MOD
        return solve(0)