'''
    Leetcode Daily Question (11-01-2025)
    1400. Construct K Palindrome Strings
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        if k == n:
            return True
        c = Counter(s)
        odd = 0
        for i in c:
            if c[i]&1:
                odd += 1
        return odd <= k