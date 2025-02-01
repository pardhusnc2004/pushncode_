'''
    Leetcode Daily Question (03-12-2024)
    2109. Adding Spaces to a String
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces)

        res = []
        start = 0
        for i in range(n):
            end = spaces[i]
            res.append(s[start:end])
            start = end
        if start < len(s):
            res.append(s[start:])
            
        return " ".join(res)