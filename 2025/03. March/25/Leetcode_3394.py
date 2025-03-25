'''
    Leetcode Daily Question (25-03-2025)
    3394. Check if Grid can be Cut into Sections
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontalCuts, verticalCuts = [], []
        for i1, j1, i2, j2 in rectangles:
            horizontalCuts.append((j1, 1))
            horizontalCuts.append((j2, -1))
            verticalCuts.append((i1, 1))
            verticalCuts.append((i2, -1))

        horizontalCuts.sort()
        verticalCuts.sort()

        # print(horizontalCuts, verticalCuts)

        horiz, verti = 0, 0
        curX, curY = 0, 0
        for i in range(len(horizontalCuts)):
            curX += horizontalCuts[i][-1]
            curY += verticalCuts[i][-1]
            if curX == 0:
                horiz += 1
            if curY == 0:
                verti += 1
            # print(i, curX, curY, horiz, verti)
        
        return horiz > 2 or verti > 2