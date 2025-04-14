'''
    Leetcode Daily Question (13-04-2025)
    1922. Count Good Numbers
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import cache

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        @cache
        def pow(x, n):
            if not n:
                return 1
            if n%2:
                return x*pow(x, n-1)%(10**9 + 7)
            else:
                return (pow(x, n//2)**2)%(10**9 + 7)
        return pow(5,(n+1)//2)*pow(4, n//2)%(10**9 + 7)