'''
    Leetcode Daily Question (01-01-2025)
    1422. Maximum Score After Splitting a String
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zero = s.count('0')
        one = n-zero
        res = 0
        cur = 0
        for i in s[:-1]:
            if i == '0':
                cur += 1
            else:
                one -= 1
            res = max(res, one+cur)
        return res