'''
    Leetcode Daily Question (30-03-2025)
    763. Partition Labels
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import *

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        alphaMap = {chr(i+ord('a')):[-1, -1] for i in range(26)}

        for i in range(n):
            if alphaMap[s[i]][0] == -1:
                alphaMap[s[i]] = [i, i]
            else:
                alphaMap[s[i]][1] = i

        @cache
        def solve(i):
            if i >= n:
                return n
            maxi = i
            for f, l in alphaMap.values():
                if f <= i < l:
                    maxi = max(maxi, solve(l))
            return maxi
        
        res = []
        tmp = 0
        prv = 0
        while tmp < n:
            prv = tmp
            tmp = solve(tmp)+1
            res.append(tmp-prv)
            
        return res