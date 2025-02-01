'''
    Leetcode Daily Question (10-12-2024)
    2981. Find Longest Special Substring That Occurs Thrice I
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def maximumLength(self, s: str) -> int:
        c = Counter(s)
        res = max([1 if c[i] >= 3 else 0 for i in c])
        n = len(s)
        left, d = 0, {}
        for right in range(n):
            d[s[right]] = d.get(s[right], 0)+1
            while d and len(d) > 1:
                d[s[left]] -= 1
                if not d[s[left]]:
                    del d[s[left]]
                left += 1
            if self.occurAtLeastThrice(s, s[left:right+1]):
                res = max(res, right-left+1)

        return res if res > 0 else -1
    
    def occurAtLeastThrice(self, s, sub):
        m, n = len(s), len(sub)
        cur = 0
        for i in range(m-n+1):
            if s[i:i+n] == sub:
                cur += 1
                if cur == 3:
                    return True
        return False