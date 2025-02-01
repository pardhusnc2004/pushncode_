'''
    Leetcode Daily Question (05-12-2024)
    2337. Move Pieces to Obtain a String
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s = start .replace("_", "")
        t = target.replace("_", "")

        if s != t:
            return False

        left  = 0
        right = 0
        
        for a, b in zip(start, target):
            if a == "L":
                left  -= 1
            elif a == "R":
                right += 1

            if b == "L":
                left  += 1
            elif b == "R":
                right -= 1

            if left < 0 or right < 0:
                return False

        return True