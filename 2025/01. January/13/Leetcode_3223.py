'''
    Leetcode Daily Question (13-01-2025)
    3223. Minimum Length of String After Operations
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        res = 0

        for i in c:
            res += 1 if c[i]&1 else 2

        return res