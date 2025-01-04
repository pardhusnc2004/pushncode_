'''
    Leetcode Daily Question (04-01-2025)
    1930. Unique Length-3 Palindromic Subsequences
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        vis = set()
        def get(mid):
            res = 0
            for i in left:
                if i+mid not in vis and right[i] > 0:
                    vis.add(i+mid)
                    res += 1
                    
            return res
        left, right = {}, Counter(s)
        res = 0
        for i in s:
            right[i] -= 1
            res += get(i)
            left[i] = left.get(i, 0)+1
        # print(vis)
        return res