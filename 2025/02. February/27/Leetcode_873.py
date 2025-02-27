'''
    Leetcode Daily Question (27-02-2025)
    873. Length of Longest Fibonacci Subsequence
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import cache

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        numMap = {arr[i]:i for i in range(n)}
        
        @cache
        def solve(cur, prev):
            diff = arr[cur] - arr[prev]
            res = 2
            if diff in numMap and diff < arr[prev]:
                res = 1+solve(numMap[diff], cur)
            return res
        
        for i in range(2, n):
            for j in range(i):
                res = max(res, solve(j, i))
        
        return res if res >= 3 else 0