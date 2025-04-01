'''
    Leetcode Daily Question (01-04-2025)
    2140. Solving Questions With Brainpower
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import *

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def solve(i):
            if i >= n:
                return 0
            return max(
                questions[i][0]+solve(i+questions[i][1]+1),
                solve(i+1)
            )
        
        return solve(0)