'''
    Leetcode Daily Question (29-12-2024)
    1639. Number of Ways to Form a Target String Given a Dictionary
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import *

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        
        n, m = len(words[0]), len(target)
        d = [defaultdict(int) for _ in range(n)]
        for w in words:
            for i in range(n):
                d[i][w[i]] += 1
        
        @cache
        def solve(i, index):
            if index == m: return 1
            if i == n: return 0

            ans = solve(i+1, index)
            ans += d[i][target[index]] * solve(i+1, index+1)
            return ans % MOD
        return solve(0, 0)