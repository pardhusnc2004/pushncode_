'''
    Leetcode Daily Question (11-03-2025)
    1358. Number of Substrings Containing All Three Characters
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, res, d, n = 0, 0, {}, len(s)
        for right in range(n):
            d[s[right]] = d.get(s[right], 0)+1
            while len(d) == 3:
                res += (n-right)
                d[s[left]] -= 1
                if not d[s[left]]:
                    del d[s[left]]
                left += 1
        return res