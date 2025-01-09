'''
    Leetcode Daily Question (09-01-2025)
    2185. Counting Words With a Given Prefix
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        for word in words:
            if len(word) >= len(pref) and word[:len(pref)] == pref:
                res += 1

        return res