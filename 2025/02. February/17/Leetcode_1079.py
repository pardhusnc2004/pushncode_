'''
    Leetcode Daily Question (17-02-2025)
    1079. Letter Tile Possibilities
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c = Counter(tiles)

        def solve():
            res = 0
            for ch in c:
                if c[ch] > 0:
                    c[ch] -= 1
                    res += 1 + solve()
                    c[ch] += 1
            return res

        return solve()