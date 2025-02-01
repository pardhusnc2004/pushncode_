'''
    Leetcode Daily Question (12-01-2025)
    2116. Check if a Parentheses String Can Be Valid
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n&1:
            return False
        braces, X = [], []
        for idx, i in enumerate(s):
            if locked[idx] == '0':
                X.append(idx)
            else:
                if i == ')':
                    if braces:
                        braces.pop()
                    elif X:
                        X.pop()
                    else:
                        return False
                else:
                    braces.append(idx)
        while braces and X and braces[-1] < X[-1]:
            X.pop()
            braces.pop()
        return not braces