'''
    Leetcode Daily Question (11-02-2025)
    1910. Remove All Occurrences of a Substring
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m, n = len(s), len(part)
        stack = []
        for i in range(m):
            stack.append(s[i])
            if len(stack) >= n:
                if "".join(stack[-n:]) == part:
                    k = 0
                    while k != n:
                        stack.pop()
                        k += 1
        return "".join(stack)
