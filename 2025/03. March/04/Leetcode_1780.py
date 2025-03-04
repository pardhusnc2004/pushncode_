'''
    Leetcode Daily Question (04-03-2025)
    1780. Check if Number is a Sum of Powers of Three
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        @cache
        def solve(i, rem):
            if rem == 0:
                return True
            if 3**i > rem:
                return False
            return solve(i+1, rem) or solve(i+1, rem-3**i)
        return solve(0, n)