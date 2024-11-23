'''
    Leetcode Daily Question (20-11-2024)
    2516. Take K of Each Character From Left and Right
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Total counts
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1

        if min(count) < k:
            return -1

        # Sliding Window
        res = float("inf")
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            res = min(res, len(s) - (r - l + 1))
        return res