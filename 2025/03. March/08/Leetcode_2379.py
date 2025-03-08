'''
    Leetcode Daily Question (08-03-2025)
    2379. Minimum Recolors to Get K Consecutive Black Blocks
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black, white, left = 0, 0, 0
        n = len(blocks)
        res = inf
        for i in range(n):
            if blocks[i] == 'W':
                white += 1
            else:
                black += 1
            while white + black > k:
                if blocks[left] == 'W':
                    white -= 1
                else:
                    black -= 1
                left += 1
            if i-left+1 >= k:
                res = min(res, white)
        while white:
            if blocks[left] == 'W':
                white -= 1
            else:
                black -= 1
            if black+white >= k:
                res = min(res, white)
            left += 1
        return res